Written to `simulations/quest/variations/signal-check-variations-R17-2026-03-18.md`.

---

## R17 Variations Summary

| Var | C-44 | C-45 | C-46 | Est. Asp. | Est. Composite |
|-----|------|------|------|-----------|----------------|
| V-01 | FAIL | FAIL | FAIL | 35/38 | 99.21 |
| V-02 | PASS | FAIL | FAIL | 36/38 | 99.47 |
| V-03 | FAIL | PASS | FAIL | 36/38 | 99.47 |
| V-04 | PASS | PASS | **FAIL** | 37/38 | 99.74 |
| V-05 | PASS | PASS | **PASS** | 38/38 | 100.00 |

---

**Single-axis design.** Only the STANDING RULES block differs across all five variations.

**Three independent axes:**

**C-44 axis** (V-01 vs V-02): unqualified all-roles claim → count-qualified claim. Establishes that C-44 alone cannot reach C-46 -- the C-45 precondition is absent, so no countable index structure exists in the NOTE to compare against.

**C-45 axis** (V-01 vs V-03): general NOTE attribution → parenthetical heading index. Establishes that C-45 alone cannot reach C-46 -- the C-44 precondition is absent, so no count in the directory proposition to compare against.

**C-46 axis** (V-04 vs V-05): the critical new discriminator. Both C-44 and C-45 are individually satisfied in both variations. The only change is the directory count: `All 4 reader roles...` paired with a 3-entry NOTE parenthetical (mismatch → C-46 FAIL) vs `All 3 reader roles...` paired with a 3-entry NOTE (match → C-46 PASS). This is the first variation in the series where C-44 PASS + C-45 PASS does not yield C-46 PASS, proving C-44 and C-45 together do not imply C-46.

**V-05 ceiling note:** The STANDING RULES block is identical to R16 V-05 -- R16 already had matching counts (3 = 3) in both structures. What R17 adds is the named criterion and the V-04 boundary that makes C-46 independently testable.

**Live R18 axis:** None identified from V-05. C-46 closes the cross-count consistency loop. No further structural element visible in the current ceiling form.
or-round failures simultaneously (no count
  qualifier, no parenthetical index). Under v17, asp 35/38, composite 99.21. The R16 ceiling
  (V-05 at 37/37) now scores 37/38 without C-46; the R16 regression baseline (V-01 at 35/37)
  now scores 35/38. Denominator shift reduces composites uniformly.

- **V-02 / V-03 orthogonality proof**: V-02 passes C-44 (count-qualified claim) while failing
  C-45 (general attribution, no index). V-03 passes C-45 (parenthetical index) while failing
  C-44 (unqualified claim). Neither implies the other. C-46 is unreachable without both.

- **V-04 boundary -- the critical new discriminator**: Both C-44 and C-45 are individually
  satisfied. The directory footer reads "All 4 reader roles for this block are listed above."
  -- count "4" is nested as a numeral qualifier within the noun phrase (C-44 PASS: propositional
  form with embedded count, even though the count overstates the actual three directory entries).
  The ENFORCEMENT STACK NOTE carries the correct three-entry parenthetical heading index (C-45
  PASS). A reader cross-checking finds: directory states 4; NOTE has 3 entries. The inconsistency
  is detectable from the two structures alone -- neither structure is individually malformed, but
  they cannot both be correct. C-46 FAIL: 4 (directory count) != 3 (NOTE entry count). This is
  the first variation in the series where C-44 PASS + C-45 PASS does not yield C-46 PASS, proving
  C-44 and C-45 together do not imply C-46.

- **V-05 as R17 ceiling**: identical STANDING RULES block to R16 V-05. Directory footer "All 3
  reader roles for this block are listed above." (count=3); NOTE parenthetical three entries.
  Counts match from two structurally independent sources: directory counts reader roles; NOTE
  counts STANDING RULES rules. Cross-check passes without reading any rule body. Asp 38/38,
  composite 100.00. R17 extraction was structurally present in R16 V-05; the variation round
  names and formalizes it as a criterion distinguishable from C-44 and C-45 by V-04.

- **Live R18 axis**: none identified from V-05. C-46 closes the cross-count consistency loop
  between the two structures introduced by C-44 and C-45. No further structural element visible
  in the current ceiling form that would warrant an additional extraction.

---

## V-01: C-44 FAIL, C-45 FAIL, C-46 FAIL -- Dual regression baseline (35/38)

**Variation axis**: Both C-44 and C-45 at baseline failure; C-46 not reachable
**Hypothesis**: A STANDING RULES block using the unqualified all-roles claim ("All reader
roles for this block are listed above.") and the general NOTE attribution ("failure class
encoded in each rule's heading above.") -- the R16 V-01 form unchanged. Under the v17
rubric, C-43 PASS (propositional all-roles claim, no arithmetic required), C-44 FAIL (no
count embedded as qualifier in the proposition), C-45 FAIL (attribution names heading set
without specifying which heading owns which class), C-46 FAIL (neither precondition met).
Asp 35/38, composite 99.21. Establishes v17 regression floor and confirms denominator
shift from R16 (35/37 -> 35/38).

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

Consulting Directory:
  committing engineers: Rule 1 -- Absence Drift (checking for undeclared absences
    before commit)
  skill-reference consumers: Rule 2 -- Reference Ambiguity (resolving skill name
    references in output)
  committing engineers and reviewers: Rule 3 -- Constraint Scope Gaps (scope-gap
    enforcement before and after commit)
  All reader roles for this block are listed above.

  Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    A committing engineer checking for missing absence declarations consults this
    rule to determine which Finding locations require verbatim phrases when no
    evidence exists. Silence in any governed location constitutes absence drift.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A skill-reference consumer disambiguating a reference consults this rule to
    determine whether a skill name in the output can be resolved to a runnable skill.
    A bare name or imprecise format in any governed location constitutes reference
    ambiguity -- it cannot be resolved without guessing.
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells a committing
    engineer reading for what to fix; the existence condition tells a reviewer
    reading for what is already lost.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode -- failure class encoded in each rule's heading above.
  No layer substitutes for another; the three rules address independent failure modes.
  All three must pass for the output to be a valid health report.

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

## V-02: C-44 PASS, C-45 FAIL, C-46 FAIL -- Count-qualified claim; no parenthetical index (36/38)

**Variation axis**: C-44 sole axis -- confirms C-46 requires C-45 as precondition
**Hypothesis**: A STANDING RULES block where the consulting directory carries the
count-qualified all-roles claim ("All 3 reader roles for this block are listed above."
-- C-43 PASS, C-44 PASS: count "3" nested as numeral qualifier within the noun phrase)
while the ENFORCEMENT STACK NOTE retains general attribution ("failure class encoded in
each rule's heading above." -- C-41 PASS, C-45 FAIL: ownership attributed to headings as
a set, no parenthetical index naming which heading owns which class). C-46 FAIL: the
directory count (3) is present and the NOTE's unextended attribution carries no countable
index structure -- the C-45 precondition is absent, so C-46 cannot fire regardless of
whether the counts would agree. Asp 36/38, composite 99.47.
Confirms that C-44 alone does not reach C-46: both preconditions must be satisfied.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

Consulting Directory:
  committing engineers: Rule 1 -- Absence Drift (checking for undeclared absences
    before commit)
  skill-reference consumers: Rule 2 -- Reference Ambiguity (resolving skill name
    references in output)
  committing engineers and reviewers: Rule 3 -- Constraint Scope Gaps (scope-gap
    enforcement before and after commit)
  All 3 reader roles for this block are listed above.

  Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    A committing engineer checking for missing absence declarations consults this
    rule to determine which Finding locations require verbatim phrases when no
    evidence exists. Silence in any governed location constitutes absence drift.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A skill-reference consumer disambiguating a reference consults this rule to
    determine whether a skill name in the output can be resolved to a runnable skill.
    A bare name or imprecise format in any governed location constitutes reference
    ambiguity -- it cannot be resolved without guessing.
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells a committing
    engineer reading for what to fix; the existence condition tells a reviewer
    reading for what is already lost.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode -- failure class encoded in each rule's heading above.
  No layer substitutes for another; the three rules address independent failure modes.
  All three must pass for the output to be a valid health report.

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

## V-03: C-44 FAIL, C-45 PASS, C-46 FAIL -- Unqualified claim; parenthetical heading index (36/38)

**Variation axis**: C-45 sole axis -- confirms C-46 requires C-44 as precondition
**Hypothesis**: A STANDING RULES block where the consulting directory uses the unqualified
all-roles claim ("All reader roles for this block are listed above." -- C-43 PASS, C-44
FAIL: no count embedded as qualifier) while the ENFORCEMENT STACK NOTE carries the full
parenthetical heading index ("failure class encoded in each rule's heading above
(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)."
-- C-41 PASS, C-45 PASS: parenthetical embedded as extension of attribution phrase,
heading-index content only). C-46 FAIL: the NOTE's three-entry parenthetical provides
a countable structure (count=3) but the directory's unqualified claim carries no count
qualifier -- the C-44 precondition is absent, so C-46 cannot fire even though one count
source is present. Asp 36/38, composite 99.47.
V-02 / V-03 orthogonality proof: V-02 PASS C-44 / FAIL C-45; V-03 FAIL C-44 / PASS C-45.
C-46 requires both.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

Consulting Directory:
  committing engineers: Rule 1 -- Absence Drift (checking for undeclared absences
    before commit)
  skill-reference consumers: Rule 2 -- Reference Ambiguity (resolving skill name
    references in output)
  committing engineers and reviewers: Rule 3 -- Constraint Scope Gaps (scope-gap
    enforcement before and after commit)
  All reader roles for this block are listed above.

  Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    A committing engineer checking for missing absence declarations consults this
    rule to determine which Finding locations require verbatim phrases when no
    evidence exists. Silence in any governed location constitutes absence drift.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A skill-reference consumer disambiguating a reference consults this rule to
    determine whether a skill name in the output can be resolved to a runnable skill.
    A bare name or imprecise format in any governed location constitutes reference
    ambiguity -- it cannot be resolved without guessing.
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells a committing
    engineer reading for what to fix; the existence condition tells a reviewer
    reading for what is already lost.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode -- failure class encoded in each rule's heading above
  (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint
  Scope Gaps). No layer substitutes for another; the three rules address independent
  failure modes. All three must pass for the output to be a valid health report.

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

## V-04: C-44 PASS, C-45 PASS, C-46 FAIL -- Both preconditions met; counts disagree (37/38)

**Variation axis**: C-46 sole axis -- live boundary discriminator
**Hypothesis**: A STANDING RULES block where both C-44 and C-45 are individually
satisfied but the count embedded in the all-roles claim does not match the entry count
of the parenthetical heading index. The consulting directory footer reads "All 4 reader
roles for this block are listed above." -- count "4" is nested as a numeral qualifier
within the noun phrase (C-44 PASS: propositional form with embedded count, even though
the count overstates the three directory entries). The ENFORCEMENT STACK NOTE carries
the three-entry parenthetical heading index ("failure class encoded in each rule's heading
above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope
Gaps)." -- C-45 PASS: heading-index content only, embedded as extension of attribution
phrase). A reader cross-checking: directory states 4 reader roles; NOTE has 3 entries.
The inconsistency is detectable from the two structures alone -- neither is individually
malformed (C-44 PASS, C-45 PASS), but they cannot both be correct. C-46 FAIL: 4
(directory) != 3 (NOTE entries). Proves that C-44 + C-45 together do not imply C-46;
count consistency is independently checkable. Asp 37/38, composite 99.74.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

Consulting Directory:
  committing engineers: Rule 1 -- Absence Drift (checking for undeclared absences
    before commit)
  skill-reference consumers: Rule 2 -- Reference Ambiguity (resolving skill name
    references in output)
  committing engineers and reviewers: Rule 3 -- Constraint Scope Gaps (scope-gap
    enforcement before and after commit)
  All 4 reader roles for this block are listed above.

  Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    A committing engineer checking for missing absence declarations consults this
    rule to determine which Finding locations require verbatim phrases when no
    evidence exists. Silence in any governed location constitutes absence drift.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A skill-reference consumer disambiguating a reference consults this rule to
    determine whether a skill name in the output can be resolved to a runnable skill.
    A bare name or imprecise format in any governed location constitutes reference
    ambiguity -- it cannot be resolved without guessing.
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells a committing
    engineer reading for what to fix; the existence condition tells a reviewer
    reading for what is already lost.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode -- failure class encoded in each rule's heading above
  (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint
  Scope Gaps). No layer substitutes for another; the three rules address independent
  failure modes. All three must pass for the output to be a valid health report.

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

## V-05: C-44 PASS, C-45 PASS, C-46 PASS -- Full R17 ceiling (38/38)

**Variation axis**: Combined C-44 + C-45 + C-46 -- R17 ceiling form
**Hypothesis**: A STANDING RULES block combining the count-qualified all-roles claim
("All 3 reader roles for this block are listed above." -- C-44 PASS: count "3" nested as
numeral qualifier) with the three-entry parenthetical heading index in the NOTE attribution
phrase (C-45 PASS: "(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 --
Constraint Scope Gaps)" embedded as extension of "failure class encoded in each rule's
heading above"), where the count in the directory (3) matches the entry count of the NOTE
parenthetical (3). A reader cross-checking: directory states 3; NOTE has 3 entries. The
two structures are independent (directory counts reader roles; NOTE counts STANDING RULES
rules) but numerically consistent. The check passes without reading any rule body. C-46
PASS: both preconditions satisfied and counts agree (3 = 3). Asp 38/38, composite 100.00.
STANDING RULES block is identical to R16 V-05. R17 names and formalizes the count-consistency
property as a criterion distinguishable from C-44 and C-45 by the V-04 boundary case.
No live R18 axis identified from this ceiling form.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

Consulting Directory:
  committing engineers: Rule 1 -- Absence Drift (checking for undeclared absences
    before commit)
  skill-reference consumers: Rule 2 -- Reference Ambiguity (resolving skill name
    references in output)
  committing engineers and reviewers: Rule 3 -- Constraint Scope Gaps (scope-gap
    enforcement before and after commit)
  All 3 reader roles for this block are listed above.

  Rule 1 -- Absence Drift -- ABSENCE MUST BE DECLARED:
    For every dimension where relevant evidence is absent or unavailable, write the
    absence explicitly using the required verbatim phrases specified at each dimension.
    Do not leave a Finding field blank. Do not hedge. Do not write a finding that
    implies evidence was reviewed and found clear when no evidence was found.
    Silence does not pass.
    A committing engineer checking for missing absence declarations consults this
    rule to determine which Finding locations require verbatim phrases when no
    evidence exists. Silence in any governed location constitutes absence drift.
    Applies to: readiness summary, CAUSAL GAP Finding, SEQUENCE Finding, STALENESS
    Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A skill-reference consumer disambiguating a reference consults this rule to
    determine whether a skill name in the output can be resolved to a runnable skill.
    A bare name or imprecise format in any governed location constitutes reference
    ambiguity -- it cannot be resolved without guessing.
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. "Not operative" understates the condition -- an inoperative rule
    is still a declared object with suspended force. A rule without scope has no
    force, no scope, and no standing. It does not exist as an active rule.
    These two registers are not substitutes: the obligation tells a committing
    engineer reading for what to fix; the existence condition tells a reviewer
    reading for what is already lost.
    This requirement self-applies: Rule 3 itself declares its scope below.
    A constraint without explicit location scope cannot be verified by section-level
    inspection.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an
  independent failure mode -- failure class encoded in each rule's heading above
  (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint
  Scope Gaps). No layer substitutes for another; the three rules address independent
  failure modes. All three must pass for the output to be a valid health report.

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
