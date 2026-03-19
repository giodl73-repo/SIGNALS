Written to `simulations/quest/variations/signal-check-variations-R15-2026-03-18.md`.

---

## R15 Variations Summary

| Var | C-42 | C-43 | Est. Asp. | Est. Composite |
|-----|------|------|-----------|----------------|
| V-01 | PASS | **FAIL** | 34/35 | 99.71 |
| V-02 | PASS (boundary) | **FAIL** (boundary) | 34/35 | 99.71 |
| V-03 | PASS | PASS | 35/35 | 100.00 |
| V-04 | PASS | PASS | 35/35 | 100.00 |
| V-05 | PASS | PASS | 35/35 | 100.00 |

---

**Single-axis design.** The five variations differ only in the STANDING RULES block. Sections 3–8 (GATHER, READINESS, PREFLIGHT, CROSS-ITEM, MISSING SIGNAL GUIDE, ARTIFACT) are identical across all variations.

**C-43 axis (three single-axis, two combined):**

| Var | Consulting Directory footer | NOTE change | Hypothesis |
|-----|----------------------------|-------------|------------|
| V-01 | `(3 reader roles governed by this block):` in header, no footer | none | Count-annotation form: C-42 PASS, C-43 FAIL |
| V-02 | `All applicable roles are listed.` | none | Generic claim lacking "reader roles for this block": C-42 PASS boundary, C-43 FAIL |
| V-03 | `All reader roles for this block are listed above.` | none | Canonical form: R14 V-05 verbatim, 35/35 regression |
| V-04 | `All 3 reader roles for this block are listed above.` | none | Count-qualified claim: C-43 PASS; live R16 axis |
| V-05 | `All reader roles for this block are listed above.` | inline heading index appended to attribution phrase | NOTE taxonomy pointer: C-43 PASS + C-39 boundary; live R16 axis |

**Key boundary notes:**
- **V-01 vs V-03**: The distinction that fails C-43 is purely about verification mechanism -- count-annotation requires arithmetic; all-roles claim does not. Both satisfy C-42.
- **V-02 boundary**: "All applicable roles are listed." fails on two specificity gaps: role category ("applicable" vs "reader") and scope anchor (absent "for this block"). Without both, the reader cannot determine the claim's scope from the directory alone.
- **V-03 as regression**: R14 V-05 already satisfies C-43 -- the criterion was extracted from V-05's form. R15's ceiling is 35/35 and R14 V-05 already reached it.
- **V-04 live R16 axis**: Does `"All 3 reader roles..."` warrant its own criterion distinguishing count-qualified from plain all-roles claim? R15 scores both as C-43 PASS; R16 scorecard decides.
- **V-05 live R16 axis**: Does the inline heading index `"(Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint Scope Gaps)"` in the NOTE upgrade the NOTE to a self-contained taxonomy pointer (extractable as C-44), or does it expand NOTE content in a way that conflicts with C-39's purity constraint?
serts coverage as a direct proposition. V-01 holds C-41 PASS (NOTE retains ownership attribution) to isolate C-43 as the sole failing axis.

**Note on V-02 boundary:**
"All applicable roles are listed." attempts a completeness claim but fails C-43 on specificity: "applicable" is undefined (applicable to what?), and no block-scoping phrase ("for this block") anchors the claim to the consulting directory's scope. C-43 requires the claim to identify "reader roles" (the role category) and "for this block" (the scope). A reader cannot determine from "All applicable roles are listed." whether this covers all roles in the output, all roles for the block, or all roles the author considered at writing time.

**Note on V-04 (count-qualified all-roles claim):**
"All 3 reader roles for this block are listed above." carries both a count and the all-roles proposition. C-43 PASS because the proposition is primary -- a reader accepts or challenges the claim as stated without arithmetic. The count is supplementary. The R16 question: does embedding a count alongside the claim introduce a redundant verification path that warrants its own criterion distinguishing claim-with-count from claim-alone? R15 scores both V-04 and V-03 equivalently at C-43 PASS.

**Note on V-05 (NOTE taxonomy index):**
V-05 tests whether the pure interdependency NOTE (C-39) can carry an inline heading index without violating C-39's constraint that the NOTE's content be limited to the interdependency relationship. The index is embedded parenthetically inside the ownership attribution phrase rather than as separate prose. The NOTE still says nothing about what each rule prevents; it only names which headings carry that information and then lists the headings inline. C-39 PASS argument: the parenthetical is an extension of the attribution pointer, not independent explanatory prose. The live R16 question is whether this extension is acceptable under C-39 or whether it introduces a new obligation (that the NOTE names headings inline) that should be independently testable.

**Potential R16 signals from V-04 and V-05:**
(1) Count-qualified all-roles claim: should a C-44 distinguish "All 3 reader roles..." from "All reader roles..." -- the former providing a checkable cross-reference alongside the direct proposition, the latter requiring only propositional acceptance? (2) NOTE inline taxonomy index: should a C-44 require the NOTE to carry an inline heading index once C-41 has attributed ownership to headings, making the NOTE independently scannable for the taxonomy without requiring a reader to scroll up? (3) Could both properties together constitute an explicit "Transfer of Authority" block -- a named design pattern declaring that content ownership has been delegated to specific headings -- making the pattern an architectural choice rather than two separate structural properties?

---

## V-01: C-43 FAIL -- Count-annotation completeness; no all-roles claim

**Variation axis**: Consulting directory completeness form (C-43) -- clear failure
**Hypothesis**: A STANDING RULES block where the consulting directory uses count-annotation
form as its completeness assertion: the header reads "Consulting Directory (3 reader roles
governed by this block):" -- the count is stated, it matches the three entries in the body,
so C-42 is satisfied (role coverage is verifiable via arithmetic). No all-roles claim is
present. A reader verifying coverage must count the three directory entries and confirm they
match the stated 3 to conclude the directory is complete; the verification mechanism is
arithmetic. C-43 requires a direct proposition that the reader accepts or challenges without
counting. Count-annotation form requires counting. C-42 PASS (count present, count matches
entry count), C-43 FAIL (count-annotation form, not all-roles claim form). The ENFORCEMENT
STACK NOTE retains the ownership attribution phrase ("failure class encoded in each rule's
heading above") so C-41 PASS. Scores 34/35.
Confirms C-43 is not discharged by C-42: a count annotation satisfying C-42 with an accurate
count does not satisfy C-43 because the verification mechanism is still arithmetic.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES

The following rules apply to every section of this output, without exception.
Violations in any section fail the output, not just the section.

Consulting Directory (3 reader roles governed by this block):
  committing engineers: Rule 1 -- Absence Drift (checking for undeclared absences
    before commit)
  skill-reference consumers: Rule 2 -- Reference Ambiguity (resolving skill name
    references in output)
  committing engineers and reviewers: Rule 3 -- Constraint Scope Gaps (scope-gap
    enforcement before and after commit)

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

## V-02: C-43 FAIL (boundary) -- Generic completeness claim; no block-scoping

**Variation axis**: Consulting directory completeness form (C-43) -- boundary failure
**Hypothesis**: A STANDING RULES block where the consulting directory carries a footer-line
completeness claim -- "All applicable roles are listed." -- that is generic rather than
explicit: "applicable" is undefined (applicable to what context, what output, what
decisions?), and no block-scoping phrase ("for this block") anchors the claim to the
consulting directory's specific scope. A reader relying on this claim cannot determine
whether it covers all roles for the STANDING RULES block, all roles in the entire output,
or all roles the author considered at writing time. The claim exists (C-42 boundary PASS --
some completeness assertion is present) but is not the specific "all reader roles for this
block" form required by C-43: "reader roles" names the role category and "for this block"
anchors the scope. C-42 PASS (boundary -- a claim is present), C-43 FAIL (not the explicit
all-roles-for-this-block form; scope ambiguity prevents the reader from verifying block
coverage from the claim text alone). The ENFORCEMENT STACK NOTE retains the ownership
attribution phrase. Scores 34/35.
Confirms that a generic completeness statement does not satisfy C-43: the specificity gap
("reader roles for this block" vs. "applicable roles") is the operative distinction.

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
  All applicable roles are listed.

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

## V-03: C-43 PASS -- R14 V-05 regression baseline (35/35)

**Variation axis**: Regression baseline -- R14 V-05 verbatim
**Hypothesis**: R14 V-05 satisfies all 34 criteria from the R14 rubric, including C-42
(all-roles claim "All reader roles for this block are listed above.") and C-41 (NOTE
ownership attribution "failure class encoded in each rule's heading above"). Under the
R15 rubric, R14 V-05's completeness assertion is already in the canonical all-roles claim
form required by C-43: it asserts coverage as a direct proposition; "reader roles" names
the role category; "for this block" anchors the scope; "listed above" locates the entries;
no arithmetic is required to accept or challenge the proposition. C-42 PASS, C-43 PASS.
The regression confirms that R14's ceiling was 35/35 under the v15 rubric: R14 V-05
already satisfies C-43 because the all-roles claim form was the excellence axis extracted
from V-05 as R14's signal. Scores 35/35.

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

## V-04: C-43 PASS -- Count-qualified all-roles claim (potential R16 axis)

**Variation axis**: Consulting directory completeness form -- count-qualified all-roles claim
**Hypothesis**: A STANDING RULES block where the consulting directory carries a count-qualified
all-roles claim -- "All 3 reader roles for this block are listed above." -- embedding the
count (3) within the all-roles assertion itself. The claim is still a direct proposition:
a reader accepts or challenges "All 3 reader roles for this block are listed above" as a
whole without requiring arithmetic to do so. The embedded count (3) is supplementary -- it
provides a quick internal cross-check for a reader who wants to verify, but the primary
verification mechanism is propositional acceptance, not arithmetic. Unlike count-annotation
form (V-01: "Consulting Directory (3 reader roles governed by this block):"), where the count
is the assertion and arithmetic is required to verify it, here the count is a qualifier inside
an all-roles claim and the claim itself is the assertion. C-42 PASS, C-43 PASS. Scores 35/35.
Live R16 axis: does the embedded count distinguish this form as a higher or different form
from the pure all-roles claim (V-03: "All reader roles for this block are listed above.")?
A potential C-44 would test whether "All 3 reader roles..." provides a checkable cross-reference
absent from the plain form, making the claim both a proposition and a count-verifiable assertion.
R15 scores both V-04 and V-03 equivalently at C-43 PASS; the distinction is a candidate for
R16 extraction if the scorecard identifies the count-qualified form as independently testable.

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

## V-05: C-43 PASS + NOTE taxonomy index (potential R16 axis)

**Variation axis**: NOTE inline taxonomy index alongside ownership attribution
**Hypothesis**: A STANDING RULES block where (a) the consulting directory carries the
canonical all-roles claim -- "All reader roles for this block are listed above." (C-42
PASS, C-43 PASS) -- and (b) the ENFORCEMENT STACK NOTE's ownership attribution phrase
is extended with an inline heading index: "failure class encoded in each rule's heading
above (Rule 1 -- Absence Drift; Rule 2 -- Reference Ambiguity; Rule 3 -- Constraint
Scope Gaps)." The index is embedded parenthetically as part of the attribution phrase,
not as independent prose about what each rule prevents. The NOTE still says nothing about
what any rule prevents, achieves, or blocks; it attributes failure-mode ownership to the
headings (C-41 PASS) and then names the headings inline, making the NOTE independently
scannable for the taxonomy without requiring a reader to scroll up to the rule headings.
C-39 PASS argument: the parenthetical content is an extension of the attribution pointer
("encoded in... above -- here are the headings: ..."), not a restatement of rule function;
the NOTE retains no "prevents..." or "blocks..." prose. C-41 PASS, C-43 PASS. Scores 35/35.
Live R16 axis: once C-41 attributes failure-mode ownership to headings, does carrying an
inline heading index in the NOTE additionally satisfy an independently testable property --
that the NOTE is a self-contained taxonomy pointer requiring no upward scan? Or does the
parenthetical index constitute content expansion that violates C-39's purity constraint
(NOTE content limited exclusively to the interdependency relationship)? If the scorecard
finds V-05's NOTE taxonomy index independently testable from C-41 and C-39, it is an R16
extraction candidate.

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
