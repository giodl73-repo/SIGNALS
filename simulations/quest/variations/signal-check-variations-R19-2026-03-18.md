Written to `simulations/quest/variations/signal-check-variations-R19-2026-03-18.md`.

---

## R19 Variations Summary

| Var | C-49 | New axis | Est. Asp. | Est. Composite |
|-----|------|----------|-----------|----------------|
| V-01 | PASS | Axis D -- structured cross-item pattern block (single-axis) | 41/41 | 100.00 |
| V-02 | PASS | Axis E -- severity-ordered missing signal guide (single-axis) | 41/41 | 100.00 |
| V-03 | PASS | Axis F -- evidence-weight STATUS qualifier (single-axis) | 41/41 | 100.00 |
| V-04 | PASS | Combined D+E -- structured patterns + priority ordering; no coverage column | 41/41 | 100.00 |
| V-05 | PASS | Combined D+E+F + **live R19 axis** -- inventory dimension-coverage column | 41/41 | 100.00 |

---

**Design rationale:** All five share the R18 V-05 baseline (STANDING RULES at C-46 ceiling, section-function annotations, coaching vocabulary, scan table, dimensional-status preamble in READINESS SUMMARY, triple-vector saturation). R19 moves to three untouched sections.

**Three single-axis designs:**

- **Axis D (V-01):** CROSS-ITEM PATTERNS replaces free prose with a labeled block (`Pattern: | Items implicated: | Root cause: | Single action:`). Null-pattern form is also a labeled block. Pattern components are recoverable from format scan without reading prose.

- **Axis E (V-02):** MISSING SIGNAL GUIDE opens with an explicit ordering declaration and orders OPEN before FLAG, CAUSAL GAP before SEQUENCE before STALENESS before COHERENCE within each tier. Most-blocking gap is always first.

- **Axis F (V-03):** STATUS uses 5-state vocabulary (`OK-STRONG | OK-WEAK | FLAG | OPEN`). Epistemic confidence visible from status line alone without reading Basis.

**Combined designs:**

- **V-04 (D+E):** Structured patterns + priority ordering. 3-state STATUS. Standard 5-column inventory. Confirms D+E together do not yield the live R19 axis.

- **V-05 (D+E+F + live axis):** All three axes plus a 6th `Dims` column in the inventory table (C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE). Makes per-dimension coverage visible before analysis begins.

**C-50 candidate (live R19 axis in V-05):** Inventory dimension-coverage column. Independently testable from C-47/C-48/C-49 and from all three R19 axes. Boundary confirmed clean across V-01 through V-04 (all 5-column tables, all C-50 FAIL).
| OPEN`) rather than 3-state (`OK | FLAG |
  OPEN`). OK-STRONG means 2+ independent artifacts cover this dimension, all within
  staleness threshold. OK-WEAK means 1 artifact only, or an artifact at threshold
  boundary. Makes epistemic confidence visible from the status line alone without
  reading the Basis field.

**Combined designs:**

- **V-04 (D+E):** Structured pattern block + severity-ordered guide. No evidence-weight
  qualifier. Standard 5-column inventory table. Establishes that D+E together do not
  reach the live R19 axis: the inventory dimension-coverage column is absent.

- **V-05 (D+E+F + live axis):** All three axes PLUS the **inventory dimension-coverage
  column** -- a 6th column (`Dims`) in the artifact inventory table listing which of the
  four check dimensions each artifact addresses (C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS,
  Co=COHERENCE). Makes per-dimension coverage visible from the inventory before analysis.

**C-50 candidate (live R19 axis in V-05):** Inventory dimension-coverage column.
V-01 through V-04 all use the standard 5-column table and fail C-50. Boundary confirmed
clean across four variations. C-50 requires no precondition from the established chain;
independently testable from C-47, C-48, and C-49.

---

## V-01: Structured cross-item pattern block (single-axis D)

**Variation axis**: Axis D only
**Hypothesis**: Replacing the free-prose cross-item pattern analysis with a named labeled
block (`Pattern: | Items implicated: | Root cause: | Single action:`) makes the pattern's
components structurally recoverable without reading unstructured text. The null-pattern
form is a labeled block with explicit null values. All R18 axes (A/B/C + C-47/C-48/C-49)
retained. Standard 5-column inventory table. C-50 FAIL. Est. asp. 41/41, composite 100.00.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES [STANDING RULES -- Constraints that persist across all evaluations]

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
[FUNCTION: Build the artifact inventory that all four preflight dimensions operate on.
 Discovering what exists is separate from interpreting what it means. If no artifacts
 exist, the run stops here -- health cannot be assessed without a ground truth.]

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing -- the 2-4 sentence view the team reads before any detail.
 Written last, placed first. Does not decide; frames what the team is walking into.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK / FLAG / OPEN]
  SEQUENCE: [OK / FLAG / OPEN]
  STALENESS: [OK / FLAG / OPEN]
  COHERENCE: [OK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Each dimension is an independent question about
 signal quality, ordered by difficulty of recovery. STATUS values computed here feed
 the readiness summary above.]

Scan index (reference before analysis; absence phrases listed here are also embedded
at point of use in each item below per Rule 1 -- both locations required):

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item below uses this structure:

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

The order is intentional: start with the causal question, because it is the signal
teams gather last and find missing most often.

--- Item 1: CAUSAL GAP ---

Why this matters:
  The team may have a full discovery stack and still have no evidence for how the
  feature causes the claimed outcome -- just that it might. Mechanism is the hardest
  gap to name and the one most commonly assumed away. Start here.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What the inventory shows:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated: "The claimed outcome is not named in any artifact -- this is itself
    a gap."

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

What the team can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

Why this matters:
  Commitment tends to foreclose investigation. A spec written before any discovery
  signal existed reflects a direction chosen before the team knew what they were
  committing to. Ordering is a fact -- check it before interpreting it.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What the inventory shows:
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

What the team can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy. Fast-moving
  markets make 30-day-old competitive signals unreliable. Stable enterprise cycles
  may hold at 90 days. The team's threshold should match the domain, not a default.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What the inventory shows:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What the team can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Hidden contradictions surface after commitment. Two signals addressing the same
  question should roughly agree -- or the disagreement should be named and deliberate.
  The team should see the contradiction before it sees the consequences.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What the inventory shows:
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

What the team can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis. Two or more FLAG/OPEN items sharing a root can be
 closed with a single action. This section expresses that root and action as a labeled
 block -- not prose -- making pattern components recoverable from structure alone. If
 all items are OK, the null-pattern block is written; this section never silently passes.]

Step back from the four items. Do two or more share a common root cause?

Write a pattern block. If a pattern exists:

  Pattern: [descriptive name -- e.g., "Premature Commitment", "Stale Signal Cascade"]
  Items implicated: [list dimensions by name -- e.g., CAUSAL GAP, SEQUENCE]
  Root cause: [single sentence -- the one condition explaining all implicated items]
  Single action: [/namespace:skill -- Rule 2; the one action addressing the root]

Common patterns to look for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: root = missing discovery phase;
    single action = /discover:causal
  - SEQUENCE FLAG + CAUSAL GAP OPEN: root = premature commitment; mechanism gap
    is downstream; single action = /discover:causal
  - STALENESS FLAG + COHERENCE FLAG: root = stale signal is source of contradiction;
    single action = refresh the stale artifact

If no pattern exists:

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1 applies: do not leave the block blank or omit it. The null-pattern form is
required when no pattern exists. Do not write "No cross-item pattern found." as a prose
sentence -- use the labeled null-pattern block.
Rule 2 applies: the Single action field uses /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Actionable gap map. Every FLAG or OPEN dimension maps to a runnable skill.
 A reviewer reading this section should be able to assign the next action without
 reading the preflight items. Rule 1 and Rule 2 both apply to every line.]

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
[FUNCTION: Persist the health report. Frontmatter fields are machine-readable;
 the artifact is the ground truth for any future /signal:check run on this topic.]

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

## V-02: Severity-ordered missing signal guide (single-axis E)

**Variation axis**: Axis E only
**Hypothesis**: MISSING SIGNAL GUIDE opens with an explicit ordering declaration and
orders items by severity: OPEN before FLAG, with CAUSAL GAP before SEQUENCE before
STALENESS before COHERENCE within the same severity tier. An output with the guide
but without the ordering declaration and severity sort satisfies guide-presence
requirements but not the priority-ordering requirement. All R18 axes (A/B/C +
C-47/C-48/C-49) retained. Prose CROSS-ITEM PATTERNS. Standard 5-column inventory
table. C-50 FAIL. Est. asp. 41/41, composite 100.00.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES [STANDING RULES -- Constraints that persist across all evaluations]

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
[FUNCTION: Build the artifact inventory that all four preflight dimensions operate on.
 Discovering what exists is separate from interpreting what it means. If no artifacts
 exist, the run stops here -- health cannot be assessed without a ground truth.]

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing -- the 2-4 sentence view the team reads before any detail.
 Written last, placed first. Does not decide; frames what the team is walking into.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK / FLAG / OPEN]
  SEQUENCE: [OK / FLAG / OPEN]
  STALENESS: [OK / FLAG / OPEN]
  COHERENCE: [OK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Each dimension is an independent question about
 signal quality, ordered by difficulty of recovery. STATUS values computed here feed
 the readiness summary above.]

Scan index (reference before analysis; absence phrases listed here are also embedded
at point of use in each item below per Rule 1 -- both locations required):

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item below uses this structure:

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

The order is intentional: start with the causal question, because it is the signal
teams gather last and find missing most often.

--- Item 1: CAUSAL GAP ---

Why this matters:
  The team may have a full discovery stack and still have no evidence for how the
  feature causes the claimed outcome -- just that it might. Mechanism is the hardest
  gap to name and the one most commonly assumed away. Start here.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What the inventory shows:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated: "The claimed outcome is not named in any artifact -- this is itself
    a gap."

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

What the team can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

Why this matters:
  Commitment tends to foreclose investigation. A spec written before any discovery
  signal existed reflects a direction chosen before the team knew what they were
  committing to. Ordering is a fact -- check it before interpreting it.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What the inventory shows:
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

What the team can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy. Fast-moving
  markets make 30-day-old competitive signals unreliable. Stable enterprise cycles
  may hold at 90 days. The team's threshold should match the domain, not a default.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What the inventory shows:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What the team can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Hidden contradictions surface after commitment. Two signals addressing the same
  question should roughly agree -- or the disagreement should be named and deliberate.
  The team should see the contradiction before it sees the consequences.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What the inventory shows:
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

What the team can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis. Two or more FLAG/OPEN items sharing a root can be
 closed with a single action. This section names that root and that action. If all
 items are OK, this section confirms no pattern exists -- it does not silently pass.]

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
[FUNCTION: Actionable gap map, ordered by severity so the most blocking gap appears
 first. A reviewer reading this section can assign the highest-priority action from
 the first line without reading the preflight items. Rule 1 and Rule 2 both apply
 to every line.]

Items ordered by severity: OPEN before FLAG.
Within same severity tier: CAUSAL GAP, then SEQUENCE, then STALENESS, then COHERENCE.
This ordering is invariant -- do not reorder by preference or discovery order.

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Examples (OPEN items listed before FLAG items):
  CAUSAL GAP OPEN: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE OPEN: run /discover:competitors -- produces dated discovery artifact to establish order
  COHERENCE OPEN: run /scout:feasibility -- produces second feasibility signal for comparison
  STALENESS FLAG: run /discover:competitors -- refreshes competitive landscape signal

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

=== ARTIFACT ===
[FUNCTION: Persist the health report. Frontmatter fields are machine-readable;
 the artifact is the ground truth for any future /signal:check run on this topic.]

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

## V-03: Evidence-weight STATUS qualifier (single-axis F)

**Variation axis**: Axis F only
**Hypothesis**: STATUS fields use a 5-state vocabulary (`OK-STRONG | OK-WEAK | FLAG |
OPEN`) rather than 3-state (`OK | FLAG | OPEN`). OK-STRONG = 2+ independent artifacts,
all within staleness threshold. OK-WEAK = 1 artifact only, or at threshold boundary.
Makes epistemic confidence visible from the status line alone without reading Basis.
All R18 axes (A/B/C + C-47/C-48/C-49) retained. Prose CROSS-ITEM PATTERNS. Unordered
MISSING SIGNAL GUIDE. Standard 5-column inventory table. C-50 FAIL. Est. asp. 41/41,
composite 100.00.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES [STANDING RULES -- Constraints that persist across all evaluations]

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
[FUNCTION: Build the artifact inventory that all four preflight dimensions operate on.
 Discovering what exists is separate from interpreting what it means. If no artifacts
 exist, the run stops here -- health cannot be assessed without a ground truth.]

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing -- the 2-4 sentence view the team reads before any detail.
 Written last, placed first. Does not decide; frames what the team is walking into.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  SEQUENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  STALENESS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  COHERENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Each dimension is an independent question about
 signal quality, ordered by difficulty of recovery. STATUS values computed here feed
 the readiness summary above. The OK-STRONG / OK-WEAK distinction makes evidence
 depth visible from the status line: a scan of STATUS fields alone reveals where
 coverage is well-supported vs. marginal.]

STATUS scale used throughout this check:
  OK-STRONG = 2+ independent artifacts cover this dimension, all within staleness threshold
  OK-WEAK   = 1 artifact only, or an artifact at the threshold boundary; covered but thin
  FLAG      = issue found -- evidence exists but raises a concern worth reviewing
  OPEN      = no artifact covers this dimension at all

Scan index (reference before analysis; absence phrases listed here are also embedded
at point of use in each item below per Rule 1 -- both locations required):

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item below uses this structure:

  STATUS: OK-STRONG | OK-WEAK | FLAG | OPEN
  Basis: [name the specific artifacts examined -- with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1
    applies: use the exact required phrase, do not leave blank, do not hedge]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK-STRONG or OK-WEAK]

The order is intentional: start with the causal question, because it is the signal
teams gather last and find missing most often.

--- Item 1: CAUSAL GAP ---

Why this matters:
  The team may have a full discovery stack and still have no evidence for how the
  feature causes the claimed outcome -- just that it might. Mechanism is the hardest
  gap to name and the one most commonly assumed away. Start here.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What the inventory shows:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated: "The claimed outcome is not named in any artifact -- this is itself
    a gap."

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

  OK-STRONG: 2+ artifacts each independently trace the mechanism chain.
  OK-WEAK: 1 artifact traces the mechanism; single-source coverage.
  FLAG: artifact exists but traces correlation rather than mechanism (see Step 2).
  OPEN: no artifact addresses mechanism at all.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {artifact names}"]
  Finding: [(a) or required absence phrase (b) -- required]

What the team can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

Why this matters:
  Commitment tends to foreclose investigation. A spec written before any discovery
  signal existed reflects a direction chosen before the team knew what they were
  committing to. Ordering is a fact -- check it before interpreting it.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK-STRONG or OK-WEAK when no discovery artifacts were checked.

What the inventory shows:
  Classify each artifact as discovery (discover, scout, prove, research, listen) or
  commitment (draft, topic, program). Note the date of each.

  OK-STRONG: 2+ discovery artifacts, all predating commitment by a clear margin.
  OK-WEAK: 1 discovery artifact predating commitment, or a narrow margin between dates.
  FLAG: commitment precedes discovery -- inversion detected.
  OPEN: no discovery artifacts -- ordering cannot be established.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required verbatim absence phrase: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or required absence phrase (c) -- required]

What the team can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy. Fast-moving
  markets make 30-day-old competitive signals unreliable. Stable enterprise cycles
  may hold at 90 days. The team's threshold should match the domain, not a default.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What the inventory shows:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  OK-STRONG: all artifacts within threshold; most at less than half the threshold age.
  OK-WEAK: all artifacts within threshold but one or more are near the boundary.
  FLAG: one or more artifacts exceed the named threshold.
  OPEN: no dated artifacts found.

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What the team can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Hidden contradictions surface after commitment. Two signals addressing the same
  question should roughly agree -- or the disagreement should be named and deliberate.
  The team should see the contradiction before it sees the consequences.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK-STRONG or OK-WEAK when there was nothing to compare.

What the inventory shows:
  Find at least one pair of artifacts addressing the same question. State what each says.

  OK-STRONG: 2+ pairs examined; all agree; no latent contradictions surfaced.
  OK-WEAK: 1 pair examined; they agree; limited comparison scope.
  FLAG: at least one pair disagrees on a named question.
  OPEN: single artifact only -- no comparable pair available.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]

What the team can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis. Two or more FLAG/OPEN items sharing a root can be
 closed with a single action. This section names that root and that action. If all
 items are OK-STRONG or OK-WEAK, this section confirms no pattern exists -- it does
 not silently pass.]

Step back from the four items. Do two or more share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action.
Look especially for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: one missing discovery phase -- one root,
    two symptoms. Action: /discover:causal addresses both.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: spec preceded discovery; mechanism gap is
    downstream of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signal is source of contradiction.
  - Multiple OK-WEAK: thin coverage across dimensions; single action = run the
    discovery skill for the thinnest dimension.

Rule 2 applies here: all skill references use /namespace:skill format.
Rule 1 applies here: if no pattern exists, write "No cross-item pattern found."
Do not leave this section blank.

If a pattern exists: name it, name which items it explains, name the single action
addressing the root -- using /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Actionable gap map. Every FLAG or OPEN dimension maps to a runnable skill.
 A reviewer reading this section should be able to assign the next action without
 reading the preflight items. Rule 1 and Rule 2 both apply to every line.]

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
[FUNCTION: Persist the health report. Frontmatter fields are machine-readable;
 the artifact is the ground truth for any future /signal:check run on this topic.]

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: ok-strong | ok-weak | flag | open
  sequence_status: ok-strong | ok-weak | flag | open
  staleness_status: ok-strong | ok-weak | flag | open
  coherence_status: ok-strong | ok-weak | flag | open
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

## V-04: Combined D+E -- structured pattern block + severity-ordered guide

**Variation axis**: Combined D+E; axis F absent; no inventory coverage column
**Hypothesis**: Structured pattern block (D) and severity-ordered guide (E) combined.
STATUS uses 3-state vocabulary (OK / FLAG / OPEN) -- evidence-weight qualifier absent.
Standard 5-column inventory table -- no dimension-coverage column. Establishes that D+E
together do not reach the live R19 axis. C-50 FAIL. All R18 axes retained.
Est. asp. 41/41, composite 100.00.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES [STANDING RULES -- Constraints that persist across all evaluations]

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
[FUNCTION: Build the artifact inventory that all four preflight dimensions operate on.
 Discovering what exists is separate from interpreting what it means. If no artifacts
 exist, the run stops here -- health cannot be assessed without a ground truth.]

Use Glob: simulations/**/*{topic}*.md

Build the inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing -- the 2-4 sentence view the team reads before any detail.
 Written last, placed first. Does not decide; frames what the team is walking into.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK / FLAG / OPEN]
  SEQUENCE: [OK / FLAG / OPEN]
  STALENESS: [OK / FLAG / OPEN]
  COHERENCE: [OK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Each dimension is an independent question about
 signal quality, ordered by difficulty of recovery. STATUS values computed here feed
 the readiness summary above.]

Scan index (reference before analysis; absence phrases listed here are also embedded
at point of use in each item below per Rule 1 -- both locations required):

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item below uses this structure:

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

The order is intentional: start with the causal question, because it is the signal
teams gather last and find missing most often.

--- Item 1: CAUSAL GAP ---

Why this matters:
  The team may have a full discovery stack and still have no evidence for how the
  feature causes the claimed outcome -- just that it might. Mechanism is the hardest
  gap to name and the one most commonly assumed away. Start here.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What the inventory shows:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated: "The claimed outcome is not named in any artifact -- this is itself
    a gap."

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

What the team can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

Why this matters:
  Commitment tends to foreclose investigation. A spec written before any discovery
  signal existed reflects a direction chosen before the team knew what they were
  committing to. Ordering is a fact -- check it before interpreting it.

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK when no discovery artifacts were checked.

What the inventory shows:
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

What the team can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy. Fast-moving
  markets make 30-day-old competitive signals unreliable. Stable enterprise cycles
  may hold at 90 days. The team's threshold should match the domain, not a default.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What the inventory shows:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What the team can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Hidden contradictions surface after commitment. Two signals addressing the same
  question should roughly agree -- or the disagreement should be named and deliberate.
  The team should see the contradiction before it sees the consequences.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK when there was nothing to compare.

What the inventory shows:
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

What the team can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis. Two or more FLAG/OPEN items sharing a root can be
 closed with a single action. This section expresses that root and action as a labeled
 block. If all items are OK, the null-pattern block is written -- this section never
 silently passes.]

Step back from the four items. Do two or more share a common root cause?

Write a pattern block. If a pattern exists:

  Pattern: [descriptive name -- e.g., "Premature Commitment", "Stale Signal Cascade"]
  Items implicated: [list dimensions by name -- e.g., CAUSAL GAP, SEQUENCE]
  Root cause: [single sentence -- the one condition explaining all implicated items]
  Single action: [/namespace:skill -- Rule 2; the one action addressing the root]

Common patterns to look for:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: root = missing discovery phase;
    single action = /discover:causal
  - SEQUENCE FLAG + CAUSAL GAP OPEN: root = premature commitment; mechanism gap
    is downstream; single action = /discover:causal
  - STALENESS FLAG + COHERENCE FLAG: root = stale signal is source of contradiction;
    single action = refresh the stale artifact

If no pattern exists:

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1 applies: do not leave the block blank or omit it. The null-pattern form is
required when no pattern exists.
Rule 2 applies: the Single action field uses /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Actionable gap map, ordered by severity so the most blocking gap appears
 first. A reviewer reading this section can assign the highest-priority action from
 the first line without reading the preflight items. Rule 1 and Rule 2 both apply
 to every line.]

Items ordered by severity: OPEN before FLAG.
Within same severity tier: CAUSAL GAP, then SEQUENCE, then STALENESS, then COHERENCE.
This ordering is invariant -- do not reorder by preference or discovery order.

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Examples (OPEN items listed before FLAG items):
  CAUSAL GAP OPEN: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE OPEN: run /discover:competitors -- produces dated discovery artifact to establish order
  COHERENCE OPEN: run /scout:feasibility -- produces second feasibility signal for comparison
  STALENESS FLAG: run /discover:competitors -- refreshes competitive landscape signal

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

=== ARTIFACT ===
[FUNCTION: Persist the health report. Frontmatter fields are machine-readable;
 the artifact is the ground truth for any future /signal:check run on this topic.]

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

## V-05: Combined D+E+F + live R19 axis -- inventory dimension-coverage column

**Variation axis**: Combined D+E+F + live R19 axis
**Hypothesis**: All three new R19 axes (D: structured pattern block, E: severity-ordered
guide, F: evidence-weight STATUS) PLUS the **inventory dimension-coverage column** -- a
6th column (`Dims`) in the artifact inventory table listing which of the four check
dimensions each artifact addresses (C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS,
Co=COHERENCE). An artifact addressing multiple dimensions lists all separated by commas.
An artifact with unclear coverage lists `?`. Makes per-dimension artifact coverage
visible from the inventory table before any preflight analysis begins: a reader scanning
the Dims column sees which dimensions have artifact coverage without entering any analysis
section.

C-50 candidate boundary: V-01 through V-04 all carry 5-column tables and fail C-50.
V-05 adds the 6th column. Boundary confirmed clean across four variations. C-50
independently testable from C-47, C-48, C-49, and axes D/E/F.

Est. asp. 41/41 (all R18 criteria pass) + C-50 candidate. Composite 100.00.

---

```
You are running /signal:check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly --
it makes sure the pilot sees everything before they decide. Nothing here blocks you
from proceeding. It exists so you know what you know before you commit.

STANDING RULES [STANDING RULES -- Constraints that persist across all evaluations]

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
[FUNCTION: Build the artifact inventory that all four preflight dimensions operate on.
 The Dims column annotates per-dimension coverage directly in the table, making coverage
 gaps visible before analysis begins. A dimension absent from all Dims cells predicts
 OPEN status in the preflight check without requiring any section to be read.]

Use Glob: simulations/**/*{topic}*.md

Build the inventory. The Dims column lists which check dimensions this artifact addresses.
Use: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE.
Multiple dimensions: list all separated by commas (e.g., "Sq, St").
Unknown coverage: use ?.

  | # | Artifact path | Namespace | Signal type | Date | Dims |
  |---|--------------|-----------|-------------|------|------|

Artifact count: {N}
Dims legend: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE, ?=unclear

Pre-analysis coverage scan: before entering any preflight item, note which dimension
abbreviations appear in the Dims column and which do not. A missing abbreviation
predicts OPEN; a single-row abbreviation predicts OK-WEAK at best.

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing -- the 2-4 sentence view the team reads before any detail.
 Written last, placed first. Does not decide; frames what the team is walking into.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  SEQUENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  STALENESS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  COHERENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. If recommending an action, name the skill using
/namespace:skill format (Rule 2). Frame as pilot briefing -- not a verdict. The team
decides.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Each dimension is an independent question about
 signal quality, ordered by difficulty of recovery. The Dims column in the inventory
 provides coverage prediction before each item. STATUS values computed here feed the
 readiness summary above.]

STATUS scale used throughout this check:
  OK-STRONG = 2+ independent artifacts cover this dimension, all within staleness threshold
  OK-WEAK   = 1 artifact only, or an artifact at the threshold boundary; covered but thin
  FLAG      = issue found -- evidence exists but raises a concern worth reviewing
  OPEN      = no artifact covers this dimension at all

Scan index (reference before analysis; absence phrases listed here are also embedded
at point of use in each item below per Rule 1 -- both locations required):

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item below uses this structure:

  STATUS: OK-STRONG | OK-WEAK | FLAG | OPEN
  Basis: [name the specific artifacts examined -- with dates; "see above" does not pass;
    if no artifacts cover the area, write "no artifact covers [question]"]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1
    applies: use the exact required phrase, do not leave blank, do not hedge]
  Action: [required if STATUS is FLAG or OPEN; must use /namespace:skill format --
    Rule 2; omit only when STATUS is OK-STRONG or OK-WEAK]

The order is intentional: start with the causal question, because it is the signal
teams gather last and find missing most often.

--- Item 1: CAUSAL GAP ---

Why this matters:
  The team may have a full discovery stack and still have no evidence for how the
  feature causes the claimed outcome -- just that it might. Mechanism is the hardest
  gap to name and the one most commonly assumed away. Start here.

Dims prediction: count rows with C in the Dims column. 0 rows predicts OPEN;
1 row predicts OK-WEAK at best; 2+ rows may support OK-STRONG if mechanism is traced.

Required verbatim absence phrase for this item:
  When no mechanism evidence is found, write this exactly:
    "No mechanism evidence found -- the causal gap is open."
  Do not substitute, hedge, or leave the Finding blank. This exact wording is required.

What the inventory shows:

  Step 1: Name the claimed outcome for {topic}:
    "The claimed outcome is: [outcome]."
    If not stated: "The claimed outcome is not named in any artifact -- this is itself
    a gap."

  Step 2: Define mechanism evidence -- a causal chain of observable intermediate steps
  from feature to outcome. Not:
    - A correlation ("users who use X have better Y scores")
    - An outcome claim ("users will benefit")
    - A proxy metric ("adoption rate will increase")
  Is: "Feature causes outcome because [step 1] -> [step 2] -> [step 3]."

  Step 3: Scan artifacts with C in Dims. State one of:
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism] by tracing
        [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase: "No mechanism evidence found -- the causal
        gap is open."
  Rule 1: form (b) is required when no mechanism evidence exists. Do not leave blank.

  OK-STRONG: 2+ C-annotated artifacts each independently trace the mechanism chain.
  OK-WEAK: 1 C-annotated artifact traces the mechanism; single-source coverage.
  FLAG: C-annotated artifact exists but traces correlation rather than mechanism.
  OPEN: no C in any Dims cell, or no C-annotated artifact passes the mechanism test.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content; if none: "no artifact addresses
    mechanism -- inventory checked: {artifact names}"]
  Finding: [(a) or required absence phrase (b) -- required]

What the team can do:
  Action: [if FLAG or OPEN: "Run /discover:causal to establish mechanism evidence
    before committing." Rule 2: /discover:causal, not "discover-causal".]

--- Item 2: SEQUENCE ---

Why this matters:
  Commitment tends to foreclose investigation. A spec written before any discovery
  signal existed reflects a direction chosen before the team knew what they were
  committing to. Ordering is a fact -- check it before interpreting it.

Dims prediction: count rows with Sq in the Dims column. 0 rows predicts OPEN;
presence of Sq with no commitment artifact predicts OPEN (no comparison possible).

Required verbatim absence phrase for this item:
  When no discovery artifacts exist, write this exactly:
    "No discovery artifacts found -- ordering cannot be established."
  Do not write SEQUENCE OK-STRONG or OK-WEAK when no discovery artifacts were checked.

What the inventory shows:
  Classify each artifact using Namespace and Signal type. Discovery: namespaces
  discover, scout, prove, research, listen. Commitment: namespaces draft, topic, program.

  OK-STRONG: 2+ discovery artifacts, all predating commitment by a clear margin.
  OK-WEAK: 1 discovery artifact predating commitment, or a narrow margin between dates.
  FLAG: commitment precedes discovery -- inversion detected.
  OPEN: no discovery artifacts found.

  Compare dates. State one of:
    (a) "Discovery precedes commitment: [discovery artifact, date] predates [commitment
        artifact, date]."
    (b) "Commitment precedes discovery: [commitment artifact, date] predates [discovery
        artifact, date]. Inversion flagged."
    (c) Required verbatim absence phrase: "No discovery artifacts found -- ordering
        cannot be established."
  Rule 1: form (c) is required when no discovery artifacts exist.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifact names and dates compared; if no discovery artifacts: "no discovery
    artifacts in inventory"]
  Finding: [(a), (b), or required absence phrase (c) -- required]

What the team can do:
  Action: [if FLAG or OPEN: name the missing discovery signal and skill using
    /namespace:skill format -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy. Fast-moving
  markets make 30-day-old competitive signals unreliable. Stable enterprise cycles
  may hold at 90 days. The team's threshold should match the domain, not a default.

Dims prediction: all dated artifacts are candidates; the St annotation identifies
artifacts gathered specifically for staleness-sensitive signals.

Required verbatim absence phrase for this item:
  When no dated artifacts exist, write this exactly:
    "No dated artifacts found -- staleness cannot be assessed."
  Do not apply a threshold to an empty inventory without noting the absence.

What the inventory shows:
  First, name the threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  OK-STRONG: all artifacts within threshold; most at less than half the threshold age.
  OK-WEAK: all within threshold but one or more are near the boundary.
  FLAG: one or more artifacts exceed the named threshold.
  OPEN: no dated artifacts found.

  Apply to each artifact. State which are within threshold and which are past it.
  Rule 1: if no dated artifacts, write the required absence phrase above.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [each artifact with date; or "no dated artifacts in inventory"]
  Finding: [fresh/stale breakdown by name; OR required absence phrase:
    "No dated artifacts found -- staleness cannot be assessed."]

What the team can do:
  Action: [if FLAG or OPEN: name the stale artifact, its age vs. threshold, and the
    skill to refresh it -- /namespace:skill format required -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Hidden contradictions surface after commitment. Two signals addressing the same
  question should roughly agree -- or the disagreement should be named and deliberate.
  The team should see the contradiction before it sees the consequences.

Dims prediction: count rows with Co in the Dims column. 0-1 rows predicts OPEN
(no comparable pair). 2+ Co rows may support OK-WEAK or OK-STRONG.

Required verbatim absence phrase for this item:
  When only one artifact exists, write this exactly:
    "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."
  Do not write COHERENCE OK-STRONG or OK-WEAK when there was nothing to compare.

What the inventory shows:
  Find at least one pair of Co-annotated artifacts addressing the same question.

  OK-STRONG: 2+ pairs examined; all agree; no latent contradictions surfaced.
  OK-WEAK: 1 pair examined; they agree; limited comparison scope.
  FLAG: at least one pair disagrees on a named question.
  OPEN: single artifact only -- no comparable pair available.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y].
      These disagree on [question]."
    Required absence phrase when no pair: "Only one artifact exists for {topic} --
      no comparable pair available to assess coherence."
  Rule 1: absence phrase is required when no pair exists.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact -- no comparable pair"]
  Finding: [named agreement, contradiction, or required absence phrase -- Rule 1 applies]

What the team can do:
  Action: [if FLAG or OPEN: what resolves the contradiction or provides a second
    artifact -- /namespace:skill format required -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis. Two or more FLAG/OPEN items sharing a root can be
 closed with a single action. The labeled block structure makes pattern components
 recoverable without reading prose. The Dims column may also reveal a thin-coverage
 pattern: multiple dimensions with only one artifact each. If all items are OK-STRONG
 or OK-WEAK, the null-pattern block is written -- this section never silently passes.]

Step back from the four items. Do two or more share a common root cause?
Also scan the Dims column: if 3+ dimensions have only one artifact each, that is
a "Thin Coverage" pattern distinct from individual dimension gaps.

Write a pattern block. If a pattern exists:

  Pattern: [descriptive name -- e.g., "Premature Commitment", "Stale Signal Cascade",
    "Thin Coverage"]
  Items implicated: [list dimensions by name -- e.g., CAUSAL GAP, SEQUENCE]
  Root cause: [single sentence -- the one condition explaining all implicated items]
  Single action: [/namespace:skill -- Rule 2; the one action addressing the root]

Common patterns:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: root = missing discovery phase;
    single action = /discover:causal
  - SEQUENCE FLAG + CAUSAL GAP OPEN: root = premature commitment;
    single action = /discover:causal
  - STALENESS FLAG + COHERENCE FLAG: root = stale signal is source of contradiction;
    single action = refresh the stale artifact
  - Multiple OK-WEAK (Dims scan: 3+ dimensions with 1 artifact each):
    root = thin coverage; single action = run the discovery skill for the weakest dim

If no pattern exists:

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1 applies: do not leave the block blank or omit it. The null-pattern form is
required when no pattern exists.
Rule 2 applies: the Single action field uses /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Actionable gap map, ordered by severity so the most blocking gap appears
 first. A reviewer reading this section can assign the highest-priority action from
 the first line without reading the preflight items. Rule 1 and Rule 2 both apply
 to every line.]

Items ordered by severity: OPEN before FLAG.
Within same severity tier: CAUSAL GAP, then SEQUENCE, then STALENESS, then COHERENCE.
This ordering is invariant -- do not reorder by preference or discovery order.

For every item with STATUS FLAG or OPEN, one line per gap. All skill references use
/namespace:skill format (Rule 2 -- applies to every line in this section):

  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Examples (OPEN items listed before FLAG items):
  CAUSAL GAP OPEN: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE OPEN: run /discover:competitors -- produces dated discovery artifact to establish order
  COHERENCE OPEN: run /scout:feasibility -- produces second feasibility signal for comparison
  STALENESS FLAG: run /discover:competitors -- refreshes competitive landscape signal

Rule 1 applies to this section: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required." Do not leave
a gap line blank.

If no items are FLAG or OPEN: "No missing signals -- signal health is clear."

=== ARTIFACT ===
[FUNCTION: Persist the health report. Frontmatter fields are machine-readable;
 the artifact is the ground truth for any future /signal:check run on this topic.
 The dims_coverage field records the per-dimension artifact counts from the Dims column.]

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  causal_gap_status: ok-strong | ok-weak | flag | open
  sequence_status: ok-strong | ok-weak | flag | open
  staleness_status: ok-strong | ok-weak | flag | open
  coherence_status: ok-strong | ok-weak | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  explicit_absences_declared: true | false
  skill_format_enforced: true
  cross_dimension_pattern: true | false
  missing_signals_by_skill: true | false
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
  dims_coverage:
    causal_gap: {count of artifacts with C in Dims column}
    sequence: {count of artifacts with Sq in Dims column}
    staleness: {count of artifacts with St in Dims column}
    coherence: {count of artifacts with Co in Dims column}
```

---

## Live R19 axis identification

**C-50 candidate**: The artifact inventory table includes a dimension-coverage column
("Dims") mapping each artifact to the specific check dimensions (CAUSAL GAP / SEQUENCE /
STALENESS / COHERENCE -- abbreviated C/Sq/St/Co) it provides signal for, making
per-dimension artifact coverage visible from the inventory scan before any preflight
analysis; an output using the standard 5-column inventory table satisfies the inventory
gathering requirements but not C-50: the reader must enter each dimension's analysis
section to determine which artifacts were examined for that dimension; C-50 is
independently testable from C-47, C-48, and C-49; C-50 is independently testable from
axes D, E, and F; C-50 requires no precondition from the established criterion chain;
boundary confirmed clean: V-01 through V-04 all use 5-column tables and fail C-50;
V-05 carries the 6-column table with Dims column and passes.

**Boundary confirmation by variation:**

| Var | Axes present | Dims column | C-50 |
|-----|-------------|-------------|------|
| V-01 | D | Absent (5-column) | FAIL |
| V-02 | E | Absent (5-column) | FAIL |
| V-03 | F | Absent (5-column) | FAIL |
| V-04 | D+E | Absent (5-column) | FAIL |
| V-05 | D+E+F + live axis | Present (6-column, Dims annotated) | PASS |

The Dims column is independently testable from all three R19 single axes and from
all R18 criteria (C-47/C-48/C-49). No combination of D, E, and F independently
yields C-50.
