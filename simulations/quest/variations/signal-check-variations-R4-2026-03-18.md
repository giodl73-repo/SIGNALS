Written to `simulations/quest/variations/signal-check-variations-R4-2026-03-18.md`.

---

**R4 summary:**

| V | Axis | New v4 criteria targeted | Est. composite |
|---|------|--------------------------|----------------|
| V-01 | C-17 alone | Inline verbatim phrases; technical register (no structural framing) | 98.18 |
| V-02 | C-18 alone | Structural framing vocabulary; phrases in reference table | 98.18 |
| V-03 | C-19 alone | Triple-stack declaration as unit; technical register; table phrases | 98.18 |
| V-04 | C-17 + C-18 | Inline phrases + structural framing; no triple-stack declaration | 99.09 |
| **V-05** | **C-17 + C-18 + C-19** | **Full v4 canonical; R3 V-05 + explicit triple-stack declaration** | **100.0** |

**Three research questions the isolations answer:**

1. **C-17 vs. reference table (V-01 vs. V-02)**: Does embedding verbatim absence phrases inline at point of use reduce drift beyond a pre-analysis reference table — independently of structural framing?
2. **C-18 structural framing (V-02 vs. V-01)**: Does preflight/pilot vocabulary in section headings and STATUS labels prevent register drift better than a top-of-file disclaimer alone — independently of phrase placement?
3. **C-19 stack declaration (V-03 alone vs. V-05)**: Does explicitly naming the three rules as a coordinated stack with independent failure modes add robustness beyond listing them independently — even when C-17 and C-18 are absent?

**V-04 = R3 V-05 verbatim.** It's carried forward as R4's baseline to confirm its score under the v4 denominator (11 aspirational vs. v3's 8). Expected: 10/11 (C-19 the only miss).

**V-05 adds only the ENFORCEMENT STACK NOTE** inserted after the rules in STANDING RULES — zero structural overhead over R3 V-05. The declaration names each rule's failure mode (absence drift / reference ambiguity / constraint scope gaps) and states that no layer substitutes for another.
nstruction block. C-18 deliberately absent (technical register, top-of-file disclaimer only — no preflight/pilot structural vocabulary). C-19 deliberately absent (rules listed independently, no triple-stack declaration).

**Hypothesis:** Inline verbatim phrases improve absence declaration compliance compared to a reference table, independently of whether the advisory register is carried structurally. C-17 passes; C-18 fails (register is declared at top but not expressed through dimension headings or STATUS framing vocabulary); C-19 fails. Tests whether phrase placement alone (at point of use vs. lookup table) is the mechanism, or whether structural framing context amplifies the effect.

**Expected Score:** 98.18 (5/5 essential, 3/3 recommended, 9/11 aspirational — C-18 and C-19 fail)

```
You are running /signal:check for topic: {topic}.

ADVISORY NOTE: This is a health check, not a verdict. Everything surfaced here is
for your awareness. Nothing here prevents you from proceeding. Use it to decide
whether you have enough signal to commit with confidence.

STANDING RULES

The following rules apply to every section of this output, without exception.
A violation in any section fails the output.

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
/namespace:skill format (Rule 2). Frame as an advisory briefing -- not a verdict.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== HEALTH CHECK DIMENSIONS ===

Each dimension uses this structure:

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

--- Dimension 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? This is the signal teams gather last, if ever. A full
  discovery stack can exist while the mechanism remains uninvestigated.

Required verbatim absence phrase for this dimension:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

Analysis:

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
  Rule 1: form (b) is required when no mechanism evidence exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content]
  Finding: [(a) or required absence phrase (b) -- required]
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing."]

--- Dimension 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off
  investigation. Specs written before discovery signals existed may reflect direction
  chosen before the team knew what they were committing to.

Required verbatim absence phrase for this dimension:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

Analysis:
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
  Basis: [artifact names and dates compared]
  Finding: [(a), (b), or required absence phrase (c) -- required]
  Action: [if FLAG or OPEN: name the missing discovery signal and skill --
    /namespace:skill format required]

--- Dimension 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.
  Fast-moving market: a 30-day-old competitive signal may be unreliable. Stable
  enterprise cycle: a 90-day-old signal may hold. This checks whether artifact
  dates fall within a defensible window for the decisions being made.

Required verbatim absence phrase for this dimension:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

Analysis:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required]

--- Dimension 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question,
  they should roughly agree -- or the disagreement should be visible and deliberate.
  Hidden contradictions surface after commitment.

Required verbatim absence phrase for this dimension:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

Analysis:
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
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required]

=== CROSS-ITEM PATTERNS ===

Step back from the four dimensions. Do two or more share a common root cause?

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

If a pattern exists: name it, name which dimensions it explains, name the single
action addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every dimension with STATUS FLAG or OPEN, one line per gap. All skill references
use /namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces dated discovery artifact to establish order
  STALENESS flag: run /discover:competitors -- refreshes competitive landscape signal
  COHERENCE open: run /scout:feasibility -- produces second feasibility signal for comparison

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required."

If no dimensions are FLAG or OPEN: "No missing signals -- signal health is clear."

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

## V-02: C-18 Axis — Structural Framing Vocabulary, Reference Table for Phrases

**Axis:** C-18 — advisory register carried structurally through framing vocabulary (preflight/pilot labels, advisory STATUS framing, clearance-oriented headers). C-17 deliberately absent (verbatim phrases collected in a REQUIRED ABSENCE PHRASES table before dimension analysis -- satisfies C-15 but not C-17). C-19 deliberately absent (no triple-stack declaration).

**Hypothesis:** Structural framing vocabulary (preflight/pilot/clearance/advisory embedded in section headings and STATUS labels) prevents register drift more reliably than a top-of-file disclaimer, independently of whether verbatim phrases are at point of use or in a reference table. C-18 passes; C-17 fails (phrases are in table, not inline per dimension); C-19 fails. Tests whether structural vocabulary alone carries the advisory register, or whether inline phrases at point of use (C-17) are also needed to maintain register coherence throughout.

**Expected Score:** 98.18 (5/5 essential, 3/3 recommended, 9/11 aspirational -- C-17 and C-19 fail)

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
A violation in any section fails the output.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly. Required absence phrases are collected in the REQUIRED ABSENCE
    PHRASES table below. Do not leave a Finding field blank. Do not hedge. Silence
    does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP advisory, SEQUENCE advisory, STALENESS
    advisory, COHERENCE advisory, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

REQUIRED ABSENCE PHRASES

When no relevant evidence exists for a dimension, use the required phrase verbatim:

  | Dimension   | Required phrase when absent |
  |-------------|----------------------------|
  | CAUSAL GAP  | "No mechanism evidence found -- the causal gap is open." |
  | SEQUENCE    | "No discovery artifacts found -- ordering cannot be established." |
  | STALENESS   | "No dated artifacts found -- staleness cannot be assessed." |
  | COHERENCE   | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence." |

Do not substitute, hedge, or paraphrase these phrases. Rule 1: use exactly as written.

=== GATHER YOUR SIGNALS ===

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== PILOT BRIEFING ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have flags worth the pilot's attention. Name any skill using /namespace:skill format
(Rule 2). This is the pilot briefing -- not a clearance. The team decides whether to fly.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made."

=== PREFLIGHT CHECK ===

Each item uses this structure:

  ADVISORY STATUS: CLEAR | REVIEW | OPEN
    CLEAR = no issue found
    REVIEW = issue found -- worth the pilot's attention before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts examined -- with dates; if no artifacts cover
    the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase from the
    table above -- Rule 1 applies: use the exact required phrase, do not leave blank]
  Advisory: [required if ADVISORY STATUS is REVIEW or OPEN; must use /namespace:skill
    format -- Rule 2; omit only when ADVISORY STATUS is CLEAR]

Work through all four items in order.

--- Preflight Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? A full discovery stack can exist while the mechanism
  remains uninvestigated.

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated in any artifact: "The claimed outcome is not named in any artifact --
    this is itself a gap."

  Step 2: Mechanism evidence means a causal chain of observable intermediate steps
  from feature to outcome -- not a correlation, outcome claim, or proxy metric.
  Form: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan every artifact. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required absence phrase from table: "No mechanism evidence found -- the causal
        gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists.

  ADVISORY STATUS: [CLEAR / REVIEW / OPEN]
  Basis: [artifacts checked for mechanism content]
  Finding: [(a) or required absence phrase (b) -- required]
  Advisory: [if REVIEW or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing."]

--- Preflight Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Specs written before discovery signals
  existed may reflect direction chosen before the team knew what they were committing to.

  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion noted."
    (c) Required absence phrase from table: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  ADVISORY STATUS: [CLEAR / REVIEW / OPEN]
  Basis: [artifact names and dates compared]
  Finding: [(a), (b), or required absence phrase (c) -- required]
  Advisory: [if REVIEW or OPEN: name the missing discovery signal and skill --
    /namespace:skill format required]

--- Preflight Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.
  This checks whether artifact dates fall within a defensible window for the
  decisions being made.

  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, use required absence phrase from table.

  ADVISORY STATUS: [CLEAR / REVIEW / OPEN]
  Basis: [each artifact with date]
  Finding: [fresh/stale breakdown by name; OR required absence phrase from table:
    "No dated artifacts found -- staleness cannot be assessed."]
  Advisory: [if REVIEW or OPEN: name the stale artifact, its age vs. threshold, and
    the skill to refresh it -- /namespace:skill format required]

--- Preflight Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? Hidden contradictions surface after
  commitment. This checks whether signals addressing the same question agree.

  Find at least one pair of artifacts addressing the same question. State what each says.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase from table when no pair: "Only one artifact exists for
      {topic} -- no comparable pair available to assess coherence."
  Rule 1: absence phrase from table is required when no pair exists.

  ADVISORY STATUS: [CLEAR / REVIEW / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]
  Advisory: [if REVIEW or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more share a common root cause?

Addressing a shared root closes multiple gaps with one advisory action. Look for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/REVIEW: one missing discovery phase -- one root.
  - SEQUENCE REVIEW + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap downstream.
  - STALENESS REVIEW + COHERENCE REVIEW: stale signal is source of contradiction.

Rule 2 applies here: all skill references use /namespace:skill format.
Rule 1 applies here: if no pattern exists, write "No cross-item pattern found."

If a pattern exists: name it, name which items it explains, name the single advisory
action addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===

For every item with ADVISORY STATUS REVIEW or OPEN, one line per gap. All skill
references use /namespace:skill format (Rule 2 -- applies to every line):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces dated discovery artifact to establish order
  STALENESS flag: run /discover:competitors -- refreshes competitive landscape signal
  COHERENCE open: run /scout:feasibility -- produces second feasibility signal for comparison

Rule 1: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required."

If no items are REVIEW or OPEN: "No missing signals -- signal health is clear."

=== ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: clear | review | open
  sequence_status: clear | review | open
  staleness_status: clear | review | open
  coherence_status: clear | review | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  explicit_absences_declared: true | false
  skill_format_enforced: true
  cross_dimension_pattern: true | false
  missing_signals_by_skill: true | false
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of REVIEW or OPEN dimension names}]
```

---

## V-03: C-19 Axis — Triple Enforcement Stack Declared as Unit

**Axis:** C-19 -- the STANDING RULES block explicitly names the three enforcement mechanisms as a coordinated stack with independent failure modes, stating that no layer substitutes for another. C-17 deliberately absent (phrases in reference table before dimensions, not inline -- C-15 passes, C-17 fails). C-18 deliberately absent (technical register; no preflight/pilot structural vocabulary; advisory disclaimer at top only).

**Hypothesis:** Declaring the three enforcement rules as a coordinated stack with named interdependency (C-19) improves constraint robustness beyond listing the three rules independently, even when C-17 and C-18 are absent. The declaration signals that each rule addresses a distinct failure mode -- absence drift (Rule 1), reference ambiguity (Rule 2), constraint scope gaps (Rule 3) -- and that all three are required. C-19 passes; C-17 and C-18 fail. Tests whether naming the stack relationship adds robustness independently of structural framing and inline phrase placement.

**Expected Score:** 98.18 (5/5 essential, 3/3 recommended, 9/11 aspirational -- C-17 and C-18 fail)

```
You are running /signal:check for topic: {topic}.

ADVISORY NOTE: This is a health check, not a verdict. Everything surfaced here is
for your awareness. Nothing here prevents you from proceeding. Use it to decide
whether you have enough signal to commit with confidence.

STANDING RULES

The following rules apply to every section of this output, without exception.
A violation in any section fails the output.

  Rule 1 -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly. Required absence phrases are collected in the REQUIRED ABSENCE
    PHRASES table below. Do not leave a Finding field blank. Do not hedge. Silence
    does not pass.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.

  Rule 2 -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.

  Rule 3 -- CONSTRAINTS ARE LOCATION-COMPLETE:
    Every Rule in this STANDING RULES block explicitly names all output locations
    it governs. Rules not scoped to specific locations apply to the full output.
    Applies to: all constraints in this block and any per-section constraint declarations.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode:
    Rule 1 (absence declaration) -- prevents silent omissions; absence drift produces
      outputs that appear complete but contain no evidence for missing dimensions.
    Rule 2 (skill format) -- prevents reference ambiguity; bare names or imprecise
      references block automated and human consumers from resolving skills.
    Rule 3 (location enumeration) -- prevents constraint scope gaps; a rule without
      explicit location scope cannot be verified without full-output scan.
  No rule substitutes for another. All three must pass for the output to be a valid
  health report. Passing two of three does not constitute a passing output.

REQUIRED ABSENCE PHRASES

When no relevant evidence exists for a dimension, use the required phrase verbatim:

  | Dimension   | Required phrase when absent |
  |-------------|----------------------------|
  | CAUSAL GAP  | "No mechanism evidence found -- the causal gap is open." |
  | SEQUENCE    | "No discovery artifacts found -- ordering cannot be established." |
  | STALENESS   | "No dated artifacts found -- staleness cannot be assessed." |
  | COHERENCE   | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence." |

Do not substitute, hedge, or paraphrase these phrases.

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
/namespace:skill format (Rule 2). This is an advisory briefing -- not a verdict.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made."

=== HEALTH CHECK DIMENSIONS ===

Each dimension uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts examined -- with dates; if no artifacts cover
    the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase from the
    table above -- Rule 1 applies]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK]

--- Dimension 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just
  that it might, but how? A full discovery stack can exist while the mechanism
  remains uninvestigated.

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated in any artifact: "The claimed outcome is not named in any artifact --
    this is itself a gap."

  Step 2: Mechanism evidence means a causal chain of observable intermediate steps.
  Not: correlation, outcome claim, or proxy metric.
  Is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan every artifact. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required absence phrase: "No mechanism evidence found -- the causal gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content]
  Finding: [(a) or required absence phrase (b) -- required]
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence."]

--- Dimension 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? Commitment tends to close off
  investigation.

  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required absence phrase: "No discovery artifacts found -- ordering cannot be
        established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared]
  Finding: [(a), (b), or required absence phrase (c) -- required]
  Action: [if FLAG or OPEN: name the missing discovery signal and skill --
    /namespace:skill format required]

--- Dimension 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines freshness.

  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact.
  Rule 1: if no dated artifacts, write required absence phrase from table.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]
  Action: [if FLAG or OPEN: name the stale artifact, age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required]

--- Dimension 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? Hidden contradictions surface after
  commitment.

  Find at least one pair of artifacts addressing the same question.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- required]
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required]

=== CROSS-ITEM PATTERNS ===

Step back from the four dimensions. Do two or more share a common root cause?

Look for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing discovery phase -- one root.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap downstream.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is source of contradiction.

Rule 2 applies: all skill references use /namespace:skill format.
Rule 1 applies: if no pattern exists, write "No cross-item pattern found."

=== MISSING SIGNAL GUIDE ===

For every dimension with STATUS FLAG or OPEN, one line per gap. All skill references
use /namespace:skill format (Rule 2):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Rule 1: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required."

If no dimensions are FLAG or OPEN: "No missing signals -- signal health is clear."

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

## V-04: C-17 + C-18 Axes — Inline Phrases + Structural Framing (R3 V-05 Canonical)

**Axes combined:** C-17 (verbatim phrases embedded inline at point of use within each dimension) + C-18 (advisory register carried structurally through preflight/pilot vocabulary in section headings, STATUS labels, and framing headers). C-19 deliberately absent (STANDING RULES lists rules independently; no explicit triple-stack declaration). This is R3 V-05 carried forward as R4's V-04 to confirm its score under the v4 denominator (11 aspirational criteria vs. v3's 8).

**Hypothesis:** R3 V-05 already satisfies C-17 and C-18. Under v4, it scores 10/11 aspirational (all C-09 through C-18 pass; only C-19 fails). V-04 confirms this and establishes the R4 starting floor. V-05 adds C-19 on top to reach v4 ceiling.

**Expected Score:** 99.09 (5/5 essential, 3/3 recommended, 10/11 aspirational -- only C-19 fails)

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

## V-05: C-17 + C-18 + C-19 — Full v4 Canonical

**Axes combined:** C-17 (verbatim phrases embedded inline at point of use) + C-18 (advisory register carried structurally through preflight/pilot vocabulary) + C-19 (triple enforcement stack declared as a coordinated unit with interdependency named). R3 V-05 is the base; the single addition is the ENFORCEMENT STACK NOTE in STANDING RULES declaring Rules 1, 2, and 3 as addressing independent failure modes and that no layer substitutes for another. This is the v4 rubric-ceiling reference.

**Hypothesis:** All 19 criteria can be satisfied by adding the triple-stack interdependency declaration (C-19) to the R3 V-05 base, which already satisfies C-17 and C-18. The ENFORCEMENT STACK NOTE requires only inserting after the rules in the STANDING RULES block -- zero structural overhead relative to R3 V-05. The declaration makes explicit what was previously only implicit: that the three rules address distinct failure modes and form a complete rather than redundant enforcement stack.

**Expected Score:** 100.0 (5/5 essential, 3/3 recommended, 11/11 aspirational)

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

  Rule 3 -- CONSTRAINTS ARE LOCATION-COMPLETE:
    Every Rule in this STANDING RULES block explicitly names all output locations
    it governs (see "Applies to:" lines above). A constraint without explicit location
    scope cannot be verified by section-level inspection.
    Applies to: all Rule declarations in this STANDING RULES block.

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

## Design Notes

**Why V-01 fails C-18:** The top-of-file ADVISORY NOTE declares the advisory register once, but section headings use neutral technical vocabulary ("HEALTH CHECK DIMENSIONS", "Dimension 1: CAUSAL GAP", "Analysis:", "Finding:", "Action:"). C-18 requires the advisory register to be expressed through the structural vocabulary itself -- preflight/pilot/clearance/advisory embedded in dimension labels and status fields -- so that the register is enforced at each section, not declared once and then at risk of drifting.

**Why V-02 fails C-17:** The REQUIRED ABSENCE PHRASES table appears before dimension analysis and collects all four required phrases in one location. C-17 requires the phrases to appear inline at each dimension's point of use -- within the dimension's instruction block. The reference-table form satisfies C-15 (phrases exist and are specified per dimension) but not C-17, because the model must look up the phrase from the table rather than encountering it at the moment of drafting the Finding. Point-of-use embedding prevents the table-lookup dependency and reduces drift risk.

**Why V-03 fails C-18:** Same as V-01 -- top-of-file ADVISORY NOTE without structural vocabulary in section headings or STATUS labels. The technical register ("HEALTH CHECK DIMENSIONS", "STATUS: OK | FLAG | OPEN", "Finding:", "Action:") does not carry the advisory frame structurally.

**Why V-04 fails C-19:** The STANDING RULES block lists Rule 1 and Rule 2 independently with no declaration of their relationship or combined purpose. C-19 requires the prompt to explicitly state that the rules address independent failure modes and that no rule substitutes for another. Listing two rules does not constitute a coordinated-stack declaration.

**What V-05 adds over V-04:** The ENFORCEMENT STACK NOTE inserted after the rules in STANDING RULES. It names the three rules as a coordinated stack, enumerates each rule's specific failure mode (absence drift, reference ambiguity, constraint scope gaps), and declares that satisfying two of three does not constitute a passing output. This is the minimum addition to reach C-19: the declaration must name the interdependency explicitly and state that the layers are non-substitutable.

**V-04 = R3 V-05 verbatim:** V-04 is carried forward without change from R3 to confirm the score under the v4 denominator. R3 V-05 scored 8/8 aspirational under v3. Under v4's 11 aspirational criteria, R3 V-05 scores 10/11 (C-09 through C-18 pass; C-19 fails). V-04 confirms this floor; V-05 adds the single ENFORCEMENT STACK NOTE to close the gap.
