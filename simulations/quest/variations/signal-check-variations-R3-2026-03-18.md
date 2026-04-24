Written to `simulations/quest/variations/signal-check-variations-R3-2026-03-18.md`.

---

**R3 summary:**

| V | Axis | New v3 criteria targeted | Est. composite |
|---|------|--------------------------|---------------|
| V-01 | C-14 alone | Named STANDING RULES block; structural rules only | 97.5 |
| V-02 | C-15 alone | Verbatim phrase table; no named block | 97.5 |
| V-03 | C-16 alone | Per-constraint location enumeration, distributed | 97.5 |
| V-04 | C-14 + C-16 | Named block with full location enumeration; no verbatim forms | 98.75 |
| V-05 | C-14 + C-15 + C-16 | Full v3 canonical; R2 V-05 base retained | 100 |

All five are gold. The isolations let you answer four specific questions:
1. Does C-14 alone improve absence compliance over per-section reminders?
2. Does C-15 alone (verbatim table, no named block) close absence drift?
3. Does distributed C-16 (V-03) propagate as well as preamble C-16 (V-04)?
4. What does C-15 add to V-04 when C-14 + C-16 are already present?
 V-04/V-05 from R2 scored 100 under both v2 and v3 because they happened to satisfy C-14/C-15/C-16. R3 tests those three criteria in isolation — R2 never isolated them independently. V-01 asks: does a named preamble block alone improve compliance without verbatim forms or location enumeration? V-02 asks: do verbatim phrase tables close absence drift without a named block? V-03 asks: does distributed location enumeration propagate constraints as well as a global preamble? V-04 pairs C-14 + C-16. V-05 is the v3 ceiling reference.

**Research questions:**
1. Does C-14 (named preamble block) alone improve absence declaration compliance over per-section reminders, even without verbatim forms?
2. Does C-15 (verbatim forms) close absence drift even without a named preamble block — or does the absence of C-14 create enough structural drift to negate it?
3. Does C-16 distributed per-section (V-03) propagate constraints as effectively as C-16 in a named preamble block (V-04)?
4. What does C-15 add over structural absence guidance when C-14 + C-16 are already present (V-04 vs. V-05)?

**Expected scoring under v3:**

| V | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Gold? |
|---|----------------|------------------|-------------------|-----------|-------|
| V-01 | 60 (5/5) | 30 (3/3) | 7.5 (C-09 thru C-14, 6/8) | 97.5 | YES |
| V-02 | 60 (5/5) | 30 (3/3) | 7.5 (C-09 thru C-13 + C-15, 6/8) | 97.5 | YES |
| V-03 | 60 (5/5) | 30 (3/3) | 7.5 (C-09 thru C-13 + C-16, 6/8) | 97.5 | YES |
| V-04 | 60 (5/5) | 30 (3/3) | 8.75 (C-09 thru C-14 + C-16, 7/8) | 98.75 | YES |
| V-05 | 60 (5/5) | 30 (3/3) | 10 (all 8, 8/8) | 100 | YES |

Aspirational base assumed for all variations: C-09, C-10, C-11, C-12, C-13.
V-01 adds C-14. V-02 adds C-15. V-03 adds C-16. V-04 adds C-14+C-16. V-05 adds all three.

---

## V-01: Named Preamble Block (C-14 axis)

**Axis:** C-14 — a named STANDING RULES block precedes all inventory and analysis. Rules are structural (no verbatim absence phrases, no explicit location enumeration) to isolate C-14 from C-15 and C-16.

**Hypothesis:** A named preamble block with structural absence and format rules is sufficient to improve constraint compliance over per-section reminders alone. C-14 passes; C-15 and C-16 fail because Rule 1 lacks verbatim forms and neither rule enumerates all governed locations. The block establishes an enforcement frame before the model encounters any evidence, which should reduce absence drift compared to reminders embedded mid-analysis.

```
You are running /signal-check for topic: {topic}.

This is a coaching check, not a gate. It surfaces what looks inconsistent so you
can decide what to address before committing. Nothing here produces a verdict that
blocks you from proceeding.

STANDING RULES

These rules apply throughout this output. No section is exempt.

  Rule 1 -- Absence must be declared:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly. Do not leave a Finding field blank. Do not hedge ("may exist
    elsewhere"). A blank finding reads as "checked and clear" -- not as "no evidence
    found." Silence does not pass.

  Rule 2 -- Skill reference format:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility
    Wrong: "discover-causal", "run the relevant discover skill", "/discover skill"
    Bare skill names anywhere in this output do not pass.

=== ARTIFACT INVENTORY ===

Use Glob: simulations/**/*{topic}*.md

Inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts found for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps. Name any gap-closing skill using /namespace:skill format (Rule 2). Frame
as advisory briefing -- not a verdict. Rule 1 applies: if no evidence supports a
positive finding, state the absence rather than implying health.

=== DIMENSION ANALYSIS ===

Structure per dimension:

  STATUS: OK | FLAG | OPEN
    OK = no issue identified
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [artifact names and dates -- "see above" does not pass; name them here;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation -- OR -- explicit absence declaration when
    evidence is absent; Rule 1 applies: state the absence, do not leave blank]
  Action: [required if STATUS is FLAG or OPEN; use /namespace:skill format (Rule 2);
    omit only if STATUS is OK]

--- CAUSAL GAP ---

Does any artifact establish the mechanism from {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome.
Step 2: Scan the inventory for mechanism evidence -- a causal chain of observable
  intermediate steps from feature to outcome. Not a correlation. Not a summary claim.
  Not a proxy metric. A mechanism traces: "Feature causes outcome because [step 1] ->
  [step 2] -> [step 3]."
Step 3: State one of:
  (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by [steps]."
  (b) "No mechanism evidence found. The causal gap is open."

Rule 1 applies: if no mechanism evidence exists, write option (b). Do not leave blank.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none address mechanism, write:
    "no artifact addresses mechanism -- checked: {list artifacts}"]
  Finding: [(a) or (b) -- required]
  Action: [if FLAG or OPEN: Run /discover:causal (Rule 2)]

--- SEQUENCE ---

Did discovery happen before specification?

Compare dates: discovery-type artifacts (discover, scout, prove, research, listen
namespaces) vs. specification-type artifacts (draft, topic, program namespaces).
Name the artifacts and their dates.

Rule 1 applies: if no discovery artifacts exist, state this -- do not write SEQUENCE OK
when no discovery artifacts were checked.

  STATUS: [OK / FLAG / OPEN]
    OK = discovery dates precede specification dates
    FLAG = mixed or ambiguous order
    OPEN = no discovery artifacts exist
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts found in inventory"]
  Finding: [what the dates show; OR "No discovery artifacts found -- ordering cannot
    be established." Rule 1 required when no discovery exists.]
  Action: [if FLAG or OPEN: name the discovery skill using /namespace:skill format (Rule 2)]

--- STALENESS ---

Are signals recent enough to trust?

Name the threshold before applying it:
  "For {topic}'s domain, signals older than [N] days are stale because [reason]."

Apply to each artifact. Name which are within threshold and which are past it.

Rule 1 applies: if no dated artifacts exist, state this -- do not apply a threshold
to an empty inventory without noting the absence.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date, checked against threshold; or "no dated artifacts
    in inventory"]
  Finding: [which are fresh, which are stale -- by name; OR: "No dated artifacts found --
    staleness cannot be assessed." Rule 1 required when no dated artifacts exist.]
  Action: [if FLAG or OPEN: artifact to refresh + /namespace:skill to run (Rule 2)]

--- COHERENCE ---

Do signals agree with each other?

Find at least one pair of artifacts addressing the same question. State agreement
or contradiction specifically. "Signals seem aligned" without named artifact pairs
does not pass.

Rule 1 applies: if only one artifact exists, state this -- do not write COHERENCE OK
when there was nothing to compare.

  STATUS: [OK / FLAG / OPEN]
    OK = signals agree on shared questions
    FLAG = contradiction identified
    OPEN = single artifact -- no pair to compare
  Basis: [artifact pairs examined; or "single artifact -- no comparable pair available"]
  Finding: [named agreement or contradiction; OR "Only one artifact exists for {topic}
    -- no comparable pair available to assess coherence." Rule 1 required when no pair.]
  Action: [if FLAG or OPEN: what resolves contradiction + /namespace:skill (Rule 2)]

=== CROSS-DIMENSION PATTERNS ===

Review all four STATUS values. If two or more share a common root cause, name it.
Name the single action addressing the shared root -- using /namespace:skill format (Rule 2).

Common patterns:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: missing discovery phase; one root, two symptoms.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: premature commitment; mechanism gap is downstream.
  - STALENESS FLAG + COHERENCE FLAG: stale signal as source of contradiction.

Rule 1 applies: if no pattern exists, write "No cross-dimension pattern identified."
Do not leave this section blank.

=== MISSING SIGNAL GUIDE ===

For every FLAG or OPEN dimension, one line per gap. All skill references use
/namespace:skill format (Rule 2):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

If all clear: "No missing signals -- signal health is clear."

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

## V-02: Verbatim Absence Phrase Table (C-15 axis)

**Axis:** C-15 -- each dimension specifies a required verbatim absence phrase. Phrases are collected in a REQUIRED ABSENCE PHRASES table before dimension analysis. No named STANDING RULES block (C-14 not present). Tests whether a verbatim-form reference table alone produces consistent explicit absence declarations.

**Hypothesis:** C-15 can be satisfied by a pre-analysis reference table collating all four required phrases. This is lighter-weight than embedding phrases per-section (V-05) and tests whether the model refers back to a table or needs the phrase at the point of use. C-14 fails (no named block); C-16 fails (absence constraint not location-enumerated); C-15 passes.

```
You are running /signal-check for topic: {topic}.

Coaching check -- not a gate. Surfaces inconsistencies so you can decide what to
address before committing. Advisory throughout.

SKILL REFERENCE FORMAT (applies to this entire output):
  Every skill reference uses /namespace:skill format.
  Correct: /discover:causal, /discover:competitors, /scout:feasibility
  Wrong: "discover-causal", "run the relevant discover skill", "/discover skill"
  Bare skill names anywhere in this output do not pass.

=== ARTIFACT INVENTORY ===

Use Glob: simulations/**/*{topic}*.md

Inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts found for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. Name any gap-closing skill using /namespace:skill format.
Frame as advisory briefing -- not a verdict.

=== DIMENSION ANALYSIS ===

REQUIRED ABSENCE PHRASES -- when relevant evidence is absent, use this exact wording:

  | Dimension  | Required verbatim phrase when evidence is absent |
  |------------|--------------------------------------------------|
  | CAUSAL GAP | "No mechanism evidence found -- the causal gap is open." |
  | SEQUENCE   | "No discovery artifacts found -- ordering cannot be established." |
  | STALENESS  | "No dated artifacts found -- staleness cannot be assessed." |
  | COHERENCE  | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence." |

These phrases are required. Do not substitute, hedge, or leave a Finding blank.
Use the exact wording from the table above when relevant evidence is absent.

Structure per dimension:

  STATUS: OK | FLAG | OPEN
    OK = no issue identified
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [artifact names and dates -- name them explicitly; if no relevant artifacts,
    state what was checked and found absent]
  Finding: [specific named observation; OR required absence phrase from the table above]
  Action: [required if FLAG or OPEN; must use /namespace:skill format; omit only if OK]

--- CAUSAL GAP ---

Does any artifact establish the mechanism from {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome.
Step 2: Scan for mechanism evidence -- a causal chain of observable intermediate steps.
  Not a correlation. Not an outcome claim. Not a proxy metric.
  A mechanism is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."
Step 3: State one of:
  (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by [steps]."
  (b) Required absence phrase: "No mechanism evidence found -- the causal gap is open."

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses mechanism"]
  Finding: [(a) or required absence phrase (b) -- phrase is required; blank does not pass]
  Action: [if FLAG or OPEN: /discover:causal]

--- SEQUENCE ---

Did discovery happen before specification?

Classify artifacts as discovery (discover, scout, prove, research, listen) or commitment
(draft, topic, program). Compare dates.

  STATUS: [OK / FLAG / OPEN]
    OK = discovery precedes commitment
    FLAG = inverted or mixed order
    OPEN = no discovery artifacts
  Basis: [artifact names and dates compared; or "no discovery artifacts in inventory"]
  Finding: [what the dates show; or required absence phrase:
    "No discovery artifacts found -- ordering cannot be established."]
  Action: [if FLAG or OPEN: name the missing discovery skill using /namespace:skill]

--- STALENESS ---

Are signals recent enough to trust?

Name the threshold first:
  "For {topic}'s domain, signals older than [N] days are stale because [reason]."

Apply to each artifact.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date, checked against threshold; or "no dated artifacts"]
  Finding: [fresh/stale breakdown by name; or required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]
  Action: [if FLAG or OPEN: artifact to refresh + /namespace:skill]

--- COHERENCE ---

Do signals agree? Find at least one pair addressing the same question.
"Signals seem aligned" without named pairs does not pass.

  STATUS: [OK / FLAG / OPEN]
    OK = signals agree on shared questions
    FLAG = contradiction identified
    OPEN = single artifact -- no pair to compare
  Basis: [pairs examined; or "single artifact -- no comparable pair available"]
  Finding: [named agreement or contradiction; or required absence phrase:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."]
  Action: [if FLAG or OPEN: what resolves contradiction + /namespace:skill]

=== CROSS-DIMENSION PATTERNS ===

Review all four STATUS values. If two or more share a common root, name it and name
the single action closing the shared root -- using /namespace:skill format.

If no shared root: "No cross-dimension pattern identified."

=== MISSING SIGNAL GUIDE ===

For every FLAG or OPEN dimension, one line per gap. All skill references use
/namespace:skill format:

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

If all clear: "No missing signals -- signal health is clear."

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

## V-03: Per-Constraint Location Enumeration (C-16 axis)

**Axis:** C-16 -- every constraint declaration explicitly names every output location where it applies. No named STANDING RULES block (C-14 not present). No verbatim forms (C-15 not present). Constraints are declared at their first appearance AND cross-reference all other governed locations.

**Hypothesis:** C-16 can be satisfied without C-14 if each constraint exhaustively names every location it governs at its point of declaration. The model receives identical constraint coverage distributed across sections rather than batched in a preamble. Tests whether location enumeration (the structural mechanism) matters independently of where in the prompt it appears.

```
You are running /signal-check for topic: {topic}.

Coaching check -- not a gate. Nothing here produces a verdict that blocks you.

=== ARTIFACT INVENTORY ===

Use Glob: simulations/**/*{topic}*.md

Inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts found for {topic}." Stop.

=== READINESS SUMMARY ===

[Write last -- position first in the final artifact.]

2-4 sentences: signal health posture for {topic}, which dimensions are clear, which
have gaps. Advisory framing -- not a verdict.

SKILL FORMAT (applies to this section AND to all action fields in DIMENSION ANALYSIS,
to CROSS-DIMENSION PATTERNS, and to MISSING SIGNAL GUIDE): every skill reference in
any of those locations uses /namespace:skill format -- e.g., /discover:causal. Bare
skill names ("discover-causal"), vague references ("run a discover skill"), and
partial format ("/discover skill") do not pass in any of those locations.

ABSENCE (applies to this section AND to all Finding fields in DIMENSION ANALYSIS,
to CROSS-DIMENSION PATTERNS, and to MISSING SIGNAL GUIDE): if no artifact evidence
supports a finding, write the absence explicitly. Blank findings do not pass in any
of those locations.

=== DIMENSION ANALYSIS ===

Structure per dimension:

  STATUS: OK | FLAG | OPEN
    OK = no issue identified
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [artifact names and dates; if no artifacts cover the area, state this explicitly]
  Finding: [specific named observation; if evidence is absent, write the absence --
    ABSENCE CONSTRAINT (applies to this Finding field AND SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, readiness summary, and MISSING SIGNAL GUIDE): blank
    findings do not pass in any of those locations]
  Action: [required if FLAG or OPEN -- SKILL FORMAT CONSTRAINT (applies to this action
    field AND SEQUENCE action, STALENESS action, COHERENCE action, cross-dimension
    patterns, and MISSING SIGNAL GUIDE): /namespace:skill format required in all those
    locations; no bare names in any of them]

--- CAUSAL GAP ---

Does any artifact establish the mechanism from {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome.
Step 2: Scan for mechanism evidence -- a causal chain of observable steps from feature
  to outcome. Not a correlation. Not an outcome claim.
  A mechanism is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."
Step 3: Write one of:
  (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by [steps]."
  (b) "No mechanism evidence found. The causal gap is open."

ABSENCE CONSTRAINT (applies to this Finding field AND SEQUENCE Finding, STALENESS
Finding, COHERENCE Finding, readiness summary, and MISSING SIGNAL GUIDE): if evidence
is absent, state it explicitly -- blank and hedged findings do not pass in any of
those locations.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked; if none address mechanism: "no artifact addresses mechanism"]
  Finding: [(a) or (b) -- required; absence constraint applies]
  Action: [if FLAG or OPEN -- SKILL FORMAT CONSTRAINT (applies here AND to SEQUENCE
    action, STALENESS action, COHERENCE action, cross-dimension patterns, and MISSING
    SIGNAL GUIDE): use /discover:causal -- /namespace:skill format required in all
    those locations]

--- SEQUENCE ---

Did discovery happen before specification?

Classify artifacts as discovery (discover, scout, prove, research, listen) or
commitment (draft, topic, program). Compare dates.

  STATUS: [OK / FLAG / OPEN]
    OK = discovery precedes commitment
    FLAG = inverted or mixed order
    OPEN = no discovery artifacts
  Basis: [artifacts compared with dates; or "no discovery artifacts in inventory"]
  Finding: [what dates show; or "No discovery artifacts found -- ordering cannot be
    established." -- absence constraint same scope as declared at CAUSAL GAP Finding]
  Action: [if FLAG or OPEN: name discovery skill -- skill format constraint same scope
    as declared at CAUSAL GAP action]

--- STALENESS ---

Are signals recent enough to trust?

Name the threshold: "For {topic}'s domain, signals older than [N] days are stale
because [reason]."

Apply to each artifact.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale by name; or "No dated artifacts found -- staleness cannot be
    assessed." -- absence constraint same scope as declared at CAUSAL GAP Finding]
  Action: [if FLAG or OPEN: artifact to refresh + skill to run -- skill format
    constraint same scope as declared at CAUSAL GAP action]

--- COHERENCE ---

Do signals agree? Find at least one pair addressing the same question. Named pairs
required -- "signals seem aligned" without names does not pass.

  STATUS: [OK / FLAG / OPEN]
    OK = signals agree on shared questions
    FLAG = contradiction identified
    OPEN = single artifact -- no pair to compare
  Basis: [pairs examined; or "single artifact -- no comparable pair available"]
  Finding: [named agreement or contradiction; or "Only one artifact exists for {topic}
    -- no comparable pair available to assess coherence." -- absence constraint same scope]
  Action: [if FLAG or OPEN: what resolves contradiction + /namespace:skill --
    skill format constraint same scope as declared at CAUSAL GAP action]

=== CROSS-DIMENSION PATTERNS ===

Review all four STATUS values. If two or more share a common root, name it.

SKILL FORMAT CONSTRAINT (applies to this section -- same constraint declared at CAUSAL
GAP action, SEQUENCE action, STALENESS action, COHERENCE action, and MISSING SIGNAL
GUIDE): all skill references use /namespace:skill format in all those locations.

ABSENCE CONSTRAINT (applies to this section -- same constraint declared at each
Finding field above and in MISSING SIGNAL GUIDE): if no pattern exists, write
"No cross-dimension pattern identified." Do not leave blank.

If a pattern exists: name it, name which dimensions it explains, name the single action
addressing the shared root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every FLAG or OPEN dimension, one line per gap:

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

SKILL FORMAT CONSTRAINT (applies to every line in this section -- same constraint
declared at each action field above and at cross-dimension patterns): /namespace:skill
format required; bare skill names do not pass in this section.

ABSENCE CONSTRAINT (applies to this section -- same constraint declared at each
Finding field above): if a gap exists but no skill is identified, write "no skill
identified for [dimension] -- manual investigation required." Do not leave a gap blank.

If all clear: "No missing signals -- signal health is clear."

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

## V-04: STANDING RULES with Full Location Enumeration (C-14 + C-16 combination)

**Axes combined:** C-14 (named STANDING RULES preamble block) + C-16 (explicit location enumeration in every constraint). C-15 not present -- absence phrases are structural guidance ("write the absence explicitly"), not verbatim forms per dimension.

**Hypothesis:** C-14 and C-16 form a structural pair. The named preamble block establishes the enforcement frame; location enumeration in each rule closes the propagation gap. Should pass 7/8 aspirational (all except C-15). The missing gap -- C-15 -- tests whether structural absence guidance with full location scope is sufficient, or whether exact required wording is also needed (V-05 answers this).

```
You are running /signal-check for topic: {topic}.

Coaching check -- not a gate. Surfaces inconsistencies so you can decide what to
address before committing. Nothing here overrides your judgment.

STANDING RULES

These rules govern every section of this output. No section is exempt.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    When evidence relevant to a dimension is absent or unavailable, write the absence
    explicitly. Do not leave a Finding field blank. Do not hedge ("may exist elsewhere").
    Do not write a finding that implies evidence was reviewed and found clear when no
    evidence was found. Silence does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-dimension patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of these locations do not pass.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover skill"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-dimension patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of these locations do not pass.

=== ARTIFACT INVENTORY ===

Use Glob: simulations/**/*{topic}*.md

Inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts found for {topic}. Consider running
/discover:causal or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===

[Write last -- position first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps. Name any gap-closing skill using /namespace:skill format (Rule 2). Frame
as advisory briefing -- not a verdict. Rule 1 applies: if no evidence supports a
positive finding, state the absence.

=== DIMENSION ANALYSIS ===

Structure per dimension:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [artifact names and dates -- name them explicitly; if no artifacts cover
    the area: state "no artifact covers [question]"]
  Finding: [specific named observation; OR explicit absence declaration -- Rule 1
    applies: state the absence, do not leave blank]
  Action: [required if FLAG or OPEN; use /namespace:skill format (Rule 2);
    omit only if STATUS is OK]

--- CAUSAL GAP ---

Does any artifact establish the mechanism from {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome.
Step 2: Scan for mechanism evidence -- a causal chain of observable intermediate steps.
  Not a correlation. Not an outcome claim.
  A mechanism is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."
Step 3: Produce one of two statements:
  (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by [steps]."
  (b) "No mechanism evidence found. The causal gap is open."

Rule 1 applies: if no mechanism evidence exists, write (b). Do not leave blank.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {list}"]
  Finding: [(a) or (b) -- required; Rule 1 applies]
  Action: [if FLAG or OPEN: Run /discover:causal to establish mechanism evidence.
    Rule 2: /discover:causal, not "discover-causal".]

--- SEQUENCE ---

Did discovery happen before specification?

Classify artifacts as discovery (discover, scout, prove, research, listen) or
commitment (draft, topic, program). Note dates.

  STATUS: [OK / FLAG / OPEN]
    OK = discovery precedes commitment
    FLAG = inverted or mixed order
    OPEN = no discovery artifacts
  Basis: [artifacts compared, with dates; if no discovery artifacts: state this]
  Finding: [what dates show; OR: "No discovery artifacts found -- ordering cannot be
    established." Rule 1 applies: this form required when no discovery exists.]
  Action: [if FLAG or OPEN: name the missing discovery skill using /namespace:skill
    format -- Rule 2]

--- STALENESS ---

Are signals recent enough to trust?

Name the threshold first:
  "For {topic}'s domain, signals older than [N] days are stale because [reason]."

Apply to each artifact.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; if no dated artifacts: "no dated artifacts in inventory"]
  Finding: [which are fresh, which are stale -- by name; OR: "No dated artifacts found --
    staleness cannot be assessed." Rule 1 applies when no dated artifacts exist.]
  Action: [if FLAG or OPEN: artifact to refresh + /namespace:skill to run -- Rule 2]

--- COHERENCE ---

Do signals agree? Find at least one pair addressing the same question.
"Signals seem aligned" without named pairs does not pass.

  STATUS: [OK / FLAG / OPEN]
    OK = signals agree on shared questions
    FLAG = contradiction identified
    OPEN = single artifact -- no pair to compare
  Basis: [pairs examined; or "single artifact -- no comparable pair available"]
  Finding: [named agreement or contradiction; OR: "Only one artifact exists for {topic}
    -- no comparable pair available to assess coherence." Rule 1 required when no pair.]
  Action: [if FLAG or OPEN: what resolves contradiction + /namespace:skill -- Rule 2]

=== CROSS-DIMENSION PATTERNS ===

Review all four STATUS values. If two or more share a common root, name it.
Name the single action addressing the shared root -- using /namespace:skill format (Rule 2).

Common patterns:
  - CAUSAL GAP OPEN + SEQUENCE OPEN: missing discovery phase; one root, two symptoms.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: premature commitment; mechanism gap is downstream.
  - STALENESS FLAG + COHERENCE FLAG: stale signal as source of contradiction.

Rule 1 applies: if no pattern exists, write "No cross-dimension pattern identified."
Do not leave this section blank.

=== MISSING SIGNAL GUIDE ===

For every FLAG or OPEN dimension, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Rule 1 applies: if a gap exists but no skill is identified, write "no skill identified
for [dimension] -- manual investigation required." Do not leave a gap line blank.

If all clear: "No missing signals -- signal health is clear."

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

## V-05: Full v3 Canonical Stack (C-14 + C-15 + C-16 on R2 V-05 base)

**Axes combined:** C-14 (named STANDING RULES preamble) + C-15 (verbatim required absence phrases per dimension) + C-16 (explicit location enumeration in every constraint) on the R2 V-05 structural base (CAUSAL GAP first, preflight framing, item-label scaffold, MISSING SIGNAL GUIDE with examples).

**Hypothesis:** All 16 criteria can be satisfied by combining: (a) STANDING RULES preamble with location-enumerated rules (C-14 + C-16), (b) verbatim required absence phrases at each dimension's point of use (C-15), and (c) the full R2 V-05 structural base. Each new v3 mechanism addresses a distinct failure mode -- structural frame (C-14), exact wording (C-15), propagation scope (C-16). This is the v3 rubric-ceiling reference.

```
You are running /signal-check for topic: {topic}.

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

## Design notes

**Why V-01 fails C-16:** Rule 1 says "applies throughout this output" -- structural scope, not explicit location enumeration. Rule 2 has a basic list ("Bare skill names anywhere in this output") but does not enumerate each governed output location by name. C-16 requires any constraint to explicitly name every governed location. Generic scope ("throughout the output") does not satisfy this. C-14 passes because the named STANDING RULES block is present and precedes all inventory and analysis.

**Why V-02 fails C-14:** The REQUIRED ABSENCE PHRASES table is a reference table, not a named STANDING RULES block. C-14 requires a named block (with a heading declaring system-wide enforcement obligations) that precedes all inventory and dimension analysis. A table of phrases and a standalone format line do not constitute a named governance preamble. The skill format constraint is also not in a named block.

**Why V-03 fails C-14 despite satisfying C-16:** C-14 requires a single named preamble block consolidating system-wide constraints before any inventory. V-03 distributes constraints per section with cross-references. This satisfies C-16 (each constraint names all governed locations) but not C-14 (no named preamble block). These criteria are structurally orthogonal: C-14 is about consolidation and position; C-16 is about scope declaration completeness.

**Why V-04 fails C-15:** Both rules in the STANDING RULES block declare structural absence obligations ("write the absence explicitly") without specifying exact required wording per dimension. C-15 requires the prompt to name at least one required verbatim phrase per dimension. Structural guidance alone does not satisfy C-15 regardless of how well-located or how explicitly scoped the constraint is.

**What V-05 adds over V-04:** Verbatim required phrases at each dimension's point of use. The model receives both the enforcement frame (STANDING RULES with location enumeration) and the exact required output form per dimension. EX-05 showed verbatim forms prevent absence drift more reliably than structural instructions alone -- even with full location enumeration in place. V-04 vs. V-05 is the empirical test of this claim.
