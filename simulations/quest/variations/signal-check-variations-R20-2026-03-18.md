Written to `simulations/quest/variations/signal-check-variations-R20-2026-03-18.md`.

---

**R20 variations summary:**

| Var | Axis | New element |
|-----|------|-------------|
| V-01 | G | VERDICT section (GO / CONDITIONAL / NO-GO + Condition + Blocking dimensions) |
| V-02 | H | Quality column in inventory (STRONG / ADEQUATE / WEAK per artifact) |
| V-03 | I | Prior check field per preflight item (IMPROVING / STABLE / DEGRADING / NEW) |
| V-04 | G+H | VERDICT + Quality; no trajectory; no evidence trace |
| V-05 | G+H+I + live | All three + Evidence trace in VERDICT (row # -> artifact path) |

**Live R20 axis (C-54 candidate):** Evidence trace field in VERDICT — maps each blocking dimension to its specific inventory row number and artifact path (or "not represented in inventory"). Creates a closed loop: verdict → blocking dim → inventory row → source artifact, navigable without entering the preflight items. Independently testable. Requires VERDICT section (Axis G) as precondition; VERDICT alone does not imply it. Boundary confirmed clean: V-01 has VERDICT but no trace (FAIL), V-04 has G+H but no trace (FAIL), V-05 alone passes.
ist, or "None"]`.
  The overall readiness decision is scannable before reading any preflight item. An output
  with READINESS SUMMARY but without a VERDICT section satisfies the pilot-briefing requirement
  but not the verdict requirement: the reader must scan all four STATUS fields and infer the
  overall decision.

- **Axis H (V-02):** A seventh column `Quality` is added to the artifact inventory table.
  Each row is annotated STRONG (recent, specific, direct), ADEQUATE (within threshold but
  limited), or WEAK (borderline or indirect). Makes artifact reliability visible before
  entering any preflight analysis. An output with Dims column but without Quality column
  satisfies C-50 but not the quality-annotation requirement.

- **Axis I (V-03):** A `Prior check:` field is added to each preflight dimension item,
  comparing the current STATUS to the most recent prior check artifact for the same topic.
  States the prior date, prior status, and trajectory (IMPROVING / STABLE / DEGRADING / NEW).
  An output without the Prior check field satisfies all existing STATUS requirements but not
  the trajectory requirement.

**Combined designs:**

- **V-04 (G+H):** VERDICT section + Quality column. No prior check. No evidence trace.
  Establishes that G+H together do not reach the live R20 axis.

- **V-05 (G+H+I + live axis):** All three axes PLUS the **Evidence trace field** in the
  VERDICT section -- a structured mapping from each blocking dimension to the specific
  inventory row(s) responsible for the gap (by row number and artifact path, or "not
  represented in inventory"). Creates a closed loop: VERDICT names the blocking dimension
  -> Evidence trace maps to the exact inventory row(s) -> reader navigates from verdict to
  source without entering the preflight items. Machine-readable: `verdict`, `blocking_dims`,
  `evidence_trace` in frontmatter.

**C-54 candidate (live R20 axis in V-05):** Evidence trace field in VERDICT block.
V-01 through V-04 carry zero, one, or two of G/H/I but none carry the Evidence trace.
Boundary confirmed clean. C-54 requires VERDICT section (Axis G) as precondition; Axis G
alone does not imply C-54. C-54 is independently testable: presence or absence of the
Evidence trace field in the VERDICT block is structurally observable without entering any
preflight item.

---

## V-01: Verdict block (single-axis G)

**Variation axis**: Axis G only
**Hypothesis**: A VERDICT section placed immediately after READINESS SUMMARY -- containing
`Verdict: GO | CONDITIONAL | NO-GO`, `Condition:`, and `Blocking dimensions:` as labeled
fields -- makes the overall readiness decision scannable before reading any preflight item.
An output with READINESS SUMMARY but without a VERDICT section satisfies the pilot-briefing
requirement but not the verdict requirement: the reader must scan all four STATUS fields and
infer the decision. All R19 axes (C-50/C-51/C-52/C-53) retained. Quality column absent.
Prior check absent. Evidence trace absent. Est. asp. 45/45, composite 100.00.

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
    Applies to: readiness summary, VERDICT, CAUSAL GAP Finding, SEQUENCE Finding,
    STALENESS Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A skill-reference consumer disambiguating a reference consults this rule to
    determine whether a skill name in the output can be resolved to a runnable skill.
    A bare name or imprecise format in any governed location constitutes reference
    ambiguity -- it cannot be resolved without guessing.
    Applies to: readiness summary, VERDICT, CAUSAL GAP action, SEQUENCE action, STALENESS
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

=== VERDICT ===
[FUNCTION: Single-line readiness decision derived from the STATUS block. The team can
 read this section and understand what the signals say about commit readiness without
 entering any preflight item. Not punitive -- states what is blocking and what the
 condition is for clearing it. Written between READINESS SUMMARY and THE PREFLIGHT CHECK.]

Verdict: [GO | CONDITIONAL | NO-GO]
  GO = all dimensions are OK-STRONG or OK-WEAK; no FLAGS or OPENs
  CONDITIONAL = one or more dimensions are FLAG; coverage exists but has issues
  NO-GO = one or more dimensions are OPEN; no artifact covers the dimension

Condition: [If GO: "None -- all dimensions pass." If CONDITIONAL or NO-GO: state the
  exact condition that, if met, would upgrade the verdict. One sentence per blocking
  dimension. Example: "CAUSAL GAP OPEN: run /discover:causal to produce mechanism
  evidence before committing." Rule 2: all skill references in /namespace:skill format.]

Blocking dimensions: [list each FLAG or OPEN dimension by name, or "None" if Verdict
  is GO. Example: "CAUSAL GAP (OPEN), COHERENCE (FLAG)"]

Rule 1 applies: if no artifacts exist and the check stopped at GATHER YOUR SIGNALS,
write: "Verdict: NO-GO -- no signal artifacts exist for {topic}."

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Each dimension is an independent question about
 signal quality, ordered by difficulty of recovery. The Dims column in the inventory
 provides coverage prediction before each item. STATUS values computed here feed the
 readiness summary and VERDICT above.]

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
 The dims_coverage field records the per-dimension artifact counts from the Dims column.
 The verdict field encodes the overall readiness decision.]

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  verdict: go | conditional | no-go
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

## V-02: Artifact quality annotation (single-axis H)

**Variation axis**: Axis H only
**Hypothesis**: A seventh column `Quality` in the artifact inventory table -- annotating each
artifact as STRONG (recent, specific, direct), ADEQUATE (within threshold but limited), or
WEAK (borderline or indirect) -- makes artifact reliability visible before entering any
preflight analysis. An output with the Dims column but without the Quality column satisfies
C-50 but not the quality-annotation requirement: the reader must enter the preflight items
to assess artifact reliability. All R19 axes (C-50/C-51/C-52/C-53) retained. Verdict block
absent. Prior check absent. Evidence trace absent. Est. asp. 45/45, composite 100.00.

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
[FUNCTION: Build the artifact inventory with Dims (coverage) and Quality (reliability)
 columns. Both are visible before any preflight analysis begins -- coverage gap AND
 reliability gap are readable from the inventory table alone.]

Use Glob: simulations/**/*{topic}*.md

Build the inventory. Dims column: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE.
Quality column: assess each artifact's reliability before entering preflight items.

Quality annotation rules:
  STRONG: artifact is recent (well within threshold), directly addresses the topic,
    and provides specific evidence for the dimension it covers.
  ADEQUATE: artifact is within threshold but has one limiting factor -- borderline
    recency, indirect topic relevance, or covers the dimension only partially.
  WEAK: artifact is at or beyond threshold boundary, or addresses the topic only
    indirectly, or provides thin evidence insufficient to strengthen a dimension.

  | # | Artifact path | Namespace | Signal type | Date | Dims | Quality |
  |---|--------------|-----------|-------------|------|------|---------|

Artifact count: {N}
Dims legend: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE, ?=unclear
Quality legend: STRONG = reliable anchor; ADEQUATE = usable with caution; WEAK = low weight

Pre-analysis scans (run both before entering any preflight item):
  Coverage scan: note which dimension abbreviations appear in Dims. Missing = predicts OPEN;
    single row = predicts OK-WEAK at best.
  Quality scan: note how many STRONG and ADEQUATE artifacts exist per dimension. A dimension
    covered only by WEAK artifacts is at risk of OK-WEAK or FLAG even if Dims shows coverage.

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
 signal quality, ordered by difficulty of recovery. The Dims and Quality columns in the
 inventory provide coverage and reliability predictions before each item. STATUS values
 computed here feed the readiness summary above.]

STATUS scale used throughout this check:
  OK-STRONG = 2+ independent artifacts cover this dimension, all within staleness threshold
  OK-WEAK   = 1 artifact only, or an artifact at the threshold boundary; covered but thin
  FLAG      = issue found -- evidence exists but raises a concern worth reviewing
  OPEN      = no artifact covers this dimension at all

Quality weight note: a dimension covered only by WEAK-quality artifacts cannot reach
OK-STRONG. A WEAK artifact contributes to coverage count but carries a quality caveat
in the Finding.

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
  Basis: [name the specific artifacts examined -- with dates and Quality rating from
    inventory; "see above" does not pass]
  Finding: [specific named observation; OR required verbatim absence phrase -- Rule 1]
  Action: [required if STATUS is FLAG or OPEN; /namespace:skill format -- Rule 2]

The order is intentional: start with the causal question, because it is the signal
teams gather last and find missing most often.

--- Item 1: CAUSAL GAP ---

Why this matters:
  Mechanism is the hardest gap to name and the one most commonly assumed away. Start here.

Dims prediction: count rows with C in the Dims column. 0 rows predicts OPEN;
1 row predicts OK-WEAK at best; 2+ rows may support OK-STRONG if mechanism is traced.
Quality check: if all C-annotated artifacts are WEAK, cap STATUS at OK-WEAK regardless
of count.

Required verbatim absence phrase:
  "No mechanism evidence found -- the causal gap is open."

What the inventory shows:
  Step 1: "The claimed outcome is: [outcome]." (Or: "not named in any artifact.")
  Step 2: Mechanism evidence = causal chain [step 1] -> [step 2] -> [step 3].
    Not a correlation, outcome claim, or proxy metric.
  Step 3: Scan C-annotated artifacts. State one of:
    (a) "Mechanism evidence found: [artifact, date, Quality] establishes [mechanism]
        by tracing [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase.

  OK-STRONG: 2+ STRONG or ADEQUATE C-annotated artifacts each independently trace mechanism.
  OK-WEAK: 1 artifact traces mechanism; or all C-annotated artifacts are WEAK quality.
  FLAG: artifact traces correlation rather than mechanism.
  OPEN: no C in any Dims cell, or no C-annotated artifact passes the mechanism test.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with Quality rating; if none: "no artifact addresses mechanism"]
  Finding: [(a) or required absence phrase (b) -- required]

What the team can do:
  Action: [if FLAG or OPEN: /discover:causal -- Rule 2]

--- Item 2: SEQUENCE ---

Why this matters:
  Ordering is a fact -- check it before interpreting it.

Dims prediction: count Sq rows. 0 predicts OPEN.
Quality note: WEAK discovery artifact counts for ordering but carries reliability caveat.

Required verbatim absence phrase:
  "No discovery artifacts found -- ordering cannot be established."

What the inventory shows:
  Classify: Discovery (discover, scout, prove, research, listen) vs Commitment (draft,
  topic, program).

  OK-STRONG: 2+ STRONG or ADEQUATE discovery predating commitment by clear margin.
  OK-WEAK: 1 predating; or WEAK quality discovery; or narrow margin.
  FLAG: commitment precedes discovery -- inversion.
  OPEN: no discovery artifacts.

  (a) "Discovery precedes commitment: [discovery, date, Quality] predates [commitment, date]."
  (b) "Commitment precedes discovery: inversion flagged."
  (c) Required verbatim absence phrase.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifact names, dates, and Quality compared]
  Finding: [(a), (b), or required absence phrase (c)]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy.

Dims prediction: St annotation identifies staleness-sensitive artifacts.
Quality note: WEAK artifacts near threshold boundary are especially at risk of FLAG.

Required verbatim absence phrase:
  "No dated artifacts found -- staleness cannot be assessed."

What the inventory shows:
  "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  OK-STRONG: all within threshold; most < half threshold age; STRONG or ADEQUATE quality.
  OK-WEAK: all within threshold but near boundary, or WEAK quality.
  FLAG: one or more exceed threshold.
  OPEN: no dated artifacts.

  Apply to each artifact. Include Quality rating in the assessment.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [each artifact with date and Quality]
  Finding: [fresh/stale breakdown with Quality notes; or required absence phrase]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Contradictions should be named before they surface as consequences.

Dims prediction: 0-1 Co rows predicts OPEN. 2+ may support OK-WEAK or OK-STRONG.
Quality note: contradiction between two WEAK artifacts is less urgent; note Quality
in the Finding to give the team calibration.

Required verbatim absence phrase:
  "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."

What the inventory shows:
  OK-STRONG: 2+ STRONG/ADEQUATE pairs examined; all agree.
  OK-WEAK: 1 pair; they agree; or both are WEAK quality.
  FLAG: at least one pair disagrees on a named question.
  OPEN: single artifact only.

  Agreement: "[A, date, Quality] and [B, date, Quality] both say [X]."
  Contradiction: "[A, date, Quality] says [X]. [B, date, Quality] says [Y]. Disagree on [q]."
  Absence phrase when no pair: required verbatim phrase above.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [pairs with Quality ratings; or "single artifact -- no comparable pair"]
  Finding: [agreement, contradiction, or required absence phrase]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis with labeled blocks. Dims reveals Thin Coverage; Quality
 reveals Weak Foundation. If all items pass, null-pattern block written -- never silent.]

Step back from the four items. Do two or more share a common root?
Scan inventory:
  - Thin Coverage: 3+ dimensions with 1 Dims artifact each.
  - Weak Foundation: 3+ dimensions covered only by WEAK-quality artifacts.

Write a pattern block:

  Pattern: [name -- e.g., "Premature Commitment", "Thin Coverage", "Weak Foundation",
    "Stale Signal Cascade"]
  Items implicated: [list dimensions]
  Root cause: [single sentence]
  Single action: [/namespace:skill -- Rule 2]

If no pattern exists:

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1: null-pattern block required when no pattern exists.
Rule 2: Single action uses /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Actionable gap map, severity-ordered. OPEN before FLAG. Within tier:
 CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE. Rule 1 and Rule 2 apply to every line.]

For every FLAG or OPEN dimension:
  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Examples (OPEN before FLAG):
  CAUSAL GAP OPEN: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE OPEN: run /discover:competitors -- produces dated discovery artifact to establish order
  COHERENCE OPEN: run /scout:feasibility -- produces second feasibility signal for comparison
  STALENESS FLAG: run /discover:competitors -- refreshes competitive landscape signal

Rule 1: blank lines do not pass. If no skill: "no skill identified -- manual investigation."
If all pass: "No missing signals -- signal health is clear."

=== ARTIFACT ===
[FUNCTION: Persist the health report. Includes quality_distribution for machine-readable
 artifact reliability summary.]

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
  quality_distribution:
    strong: {count}
    adequate: {count}
    weak: {count}
```

---

## V-03: Dimension trajectory -- prior check comparison (single-axis I)

**Variation axis**: Axis I only
**Hypothesis**: A `Prior check:` field added to each preflight dimension item -- stating the
prior run's date, prior STATUS, and trajectory label (IMPROVING / STABLE / DEGRADING / NEW)
relative to the most recent prior /signal:check artifact for the same topic -- makes the
temporal trajectory of each dimension visible within the analysis. An output without the
Prior check field satisfies all existing STATUS requirements but not the trajectory requirement:
the reader cannot determine whether a dimension is improving or degrading without opening the
prior artifact manually. All R19 axes (C-50/C-51/C-52/C-53) retained. Verdict block absent.
Quality column absent. Evidence trace absent. Est. asp. 45/45, composite 100.00.

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
    Finding, COHERENCE Finding, Prior check fields, cross-item patterns, and MISSING
    SIGNAL GUIDE. Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule.
    This requirement self-applies: Rule 3 itself declares its scope below.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an independent
  failure mode. All three must pass for the output to be a valid health report.

=== GATHER YOUR SIGNALS ===
[FUNCTION: Build the artifact inventory and look up any prior check run for this topic.
 Prior check lookup feeds the Prior check field in each preflight item below.]

Use Glob: simulations/**/*{topic}*.md
Also Glob: simulations/signal/check/{topic}-check-*.md (prior check lookup)

Prior check lookup:
  If a prior check artifact exists: note its date and the per-dimension STATUS values from
    its frontmatter fields (causal_gap_status, sequence_status, staleness_status,
    coherence_status). Record as: prior_check_date = {date}, prior statuses noted per dim.
  If no prior check exists: record "no prior check found -- this is the first run."

Build the inventory. Dims column: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE.

  | # | Artifact path | Namespace | Signal type | Date | Dims |
  |---|--------------|-----------|-------------|------|------|

Artifact count: {N}
Dims legend: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE, ?=unclear

Pre-analysis coverage scan: which Dims abbreviations appear? Missing = predicts OPEN;
single row = predicts OK-WEAK at best.

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing. Written last, placed first. Does not decide; frames the view.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  SEQUENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  STALENESS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  COHERENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}. Rule 2: /namespace:skill format.
Rule 1: "No signal artifacts found -- health assessment cannot be made." if no artifacts.

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Each item includes a Prior check field that compares
 current STATUS to the most recent prior run, making the trajectory of each dimension
 visible without opening the prior artifact manually.]

STATUS scale:
  OK-STRONG = 2+ independent artifacts cover this dimension, all within staleness threshold
  OK-WEAK   = 1 artifact only, or at threshold boundary; covered but thin
  FLAG      = evidence exists but raises a concern worth reviewing
  OPEN      = no artifact covers this dimension at all

Trajectory vocabulary for Prior check field:
  IMPROVING = prior STATUS was worse than current (e.g., OPEN -> OK-WEAK, FLAG -> OK-STRONG)
  STABLE    = prior STATUS matches current (no change in diagnostic state)
  DEGRADING = prior STATUS was better than current (e.g., OK-STRONG -> OK-WEAK, OK-WEAK -> FLAG)
  NEW       = no prior check artifact found for this topic

Prior check rule (Rule 1 applies): if a prior check exists but its STATUS for this
dimension is not in its frontmatter, write "prior check found ({date}) but dimension
status not recorded -- treating as NEW." Do not leave Prior check blank.

Scan index (absence phrases embedded at point of use per Rule 1):

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item uses this structure:

  Prior check: [{prior date}: {prior status}] -> [{current status}: IMPROVING | STABLE |
    DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: OK-STRONG | OK-WEAK | FLAG | OPEN
  Basis: [artifacts with dates; "see above" does not pass]
  Finding: [observation or required verbatim absence phrase -- Rule 1]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2; omit if OK-STRONG or OK-WEAK]

--- Item 1: CAUSAL GAP ---

Why this matters:
  The team may have a full discovery stack and still have no evidence for how the
  feature causes the claimed outcome. Mechanism is the hardest gap to name. Start here.

Dims prediction: 0 C rows predicts OPEN; 1 predicts OK-WEAK; 2+ may support OK-STRONG.

Required verbatim absence phrase:
  "No mechanism evidence found -- the causal gap is open."

What the inventory shows:
  Step 1: "The claimed outcome is: [outcome]." (Or: not named -- itself a gap.)
  Step 2: Mechanism = causal chain [step 1] -> [step 2] -> [step 3]. Not correlation.
  Step 3: Scan C-annotated artifacts.
    (a) "Mechanism evidence found: [artifact, date] establishes [mechanism]."
    (b) Required verbatim absence phrase.

  OK-STRONG: 2+ C-annotated artifacts trace mechanism independently.
  OK-WEAK: 1 artifact traces mechanism.
  FLAG: artifact traces correlation not mechanism.
  OPEN: no C in Dims.

  Prior check: [{prior date}: {prior causal_gap_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content]
  Finding: [(a) or required absence phrase (b)]

What the team can do:
  Action: [if FLAG or OPEN: /discover:causal -- Rule 2]

--- Item 2: SEQUENCE ---

Why this matters:
  Ordering is a fact. Check it before interpreting it.

Dims prediction: 0 Sq rows predicts OPEN.

Required verbatim absence phrase:
  "No discovery artifacts found -- ordering cannot be established."

What the inventory shows:
  Classify: Discovery (discover, scout, prove, research, listen) vs Commitment (draft,
  topic, program). Compare dates.

  OK-STRONG: 2+ discovery predating commitment by clear margin.
  OK-WEAK: 1 predating; or narrow margin.
  FLAG: commitment precedes discovery -- inversion.
  OPEN: no discovery artifacts.

  (a) "Discovery precedes commitment: [artifact, date] predates [commitment, date]."
  (b) "Commitment precedes discovery: inversion flagged."
  (c) Required verbatim absence phrase.

  Prior check: [{prior date}: {prior sequence_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifact names and dates compared]
  Finding: [(a), (b), or required absence phrase (c)]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy.

Dims prediction: St annotation identifies staleness-sensitive artifacts.

Required verbatim absence phrase:
  "No dated artifacts found -- staleness cannot be assessed."

What the inventory shows:
  "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  OK-STRONG: all within threshold; most < half threshold age.
  OK-WEAK: all within threshold but near boundary.
  FLAG: one or more exceed threshold.
  OPEN: no dated artifacts.

  Prior check: [{prior date}: {prior staleness_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [each artifact with date]
  Finding: [fresh/stale breakdown; or required absence phrase]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Hidden contradictions should surface before commitment, not after.

Dims prediction: 0-1 Co rows predicts OPEN. 2+ may support OK-WEAK or OK-STRONG.

Required verbatim absence phrase:
  "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."

What the inventory shows:
  OK-STRONG: 2+ pairs agree.
  OK-WEAK: 1 pair agrees; limited scope.
  FLAG: pair disagrees.
  OPEN: single artifact.

  Agreement: "[A, date] and [B, date] both say [X]."
  Contradiction: "[A, date] says [X]. [B, date] says [Y]. Disagree on [question]."
  Required absence phrase when no pair.

  Prior check: [{prior date}: {prior coherence_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [pairs examined; or "single artifact"]
  Finding: [agreement, contradiction, or absence phrase]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis with labeled blocks. Trajectory adds a Signal Decay
 pattern: 2+ dimensions showing DEGRADING. If all pass, null-pattern block written.]

Step back from all four items. Do two or more share a common root?
Trajectory scan: if 2+ dimensions show DEGRADING, that is a "Signal Decay" pattern.

  Pattern: [name -- e.g., "Premature Commitment", "Thin Coverage", "Signal Decay",
    "Stale Signal Cascade"]
  Items implicated: [dimensions]
  Root cause: [single sentence]
  Single action: [/namespace:skill -- Rule 2]

If no pattern:

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1: null-pattern block required.
Rule 2: Single action uses /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Severity-ordered gap map. OPEN before FLAG. Rule 1 and Rule 2 every line.]

Ordering: OPEN before FLAG. Within tier: CAUSAL GAP, SEQUENCE, STALENESS, COHERENCE.

  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Rule 1: blank lines do not pass.
If all pass: "No missing signals -- signal health is clear."

=== ARTIFACT ===
[FUNCTION: Persist the health report. Includes trajectory fields for machine-readable
 trend tracking across runs.]

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
    causal_gap: {count}
    sequence: {count}
    staleness: {count}
    coherence: {count}
  prior_check_date: {date or null}
  trajectory:
    causal_gap: improving | stable | degrading | new
    sequence: improving | stable | degrading | new
    staleness: improving | stable | degrading | new
    coherence: improving | stable | degrading | new
```

---

## V-04: Combined G+H -- verdict block + quality annotation

**Variation axis**: Combined G+H; axis I absent; evidence trace absent
**Hypothesis**: VERDICT section (G) and Quality column (H) combined. Prior check absent.
Evidence trace absent. Establishes that G+H together do not reach the live R20 axis.
All R19 axes (C-50/C-51/C-52/C-53) retained. Est. asp. 45/45, composite 100.00.

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
    Applies to: readiness summary, VERDICT, CAUSAL GAP Finding, SEQUENCE Finding,
    STALENESS Finding, COHERENCE Finding, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    Applies to: readiness summary, VERDICT, CAUSAL GAP action, SEQUENCE action, STALENESS
    action, COHERENCE action, cross-item patterns, and MISSING SIGNAL GUIDE.
    Bare skill names in any of those locations do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule.
    This requirement self-applies: Rule 3 itself declares its scope below.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

ENFORCEMENT STACK NOTE:
  Rules 1, 2, and 3 form a coordinated enforcement stack. Each addresses an independent
  failure mode. All three must pass for the output to be a valid health report.

=== GATHER YOUR SIGNALS ===
[FUNCTION: Build the artifact inventory with Dims (coverage) and Quality (reliability)
 columns. Both visible before preflight analysis begins.]

Use Glob: simulations/**/*{topic}*.md

Quality annotation:
  STRONG: recent (well within threshold), directly addresses topic, specific evidence.
  ADEQUATE: within threshold but limited in one dimension (recency, relevance, or depth).
  WEAK: at/beyond boundary, or indirect, or thin evidence.

  | # | Artifact path | Namespace | Signal type | Date | Dims | Quality |
  |---|--------------|-----------|-------------|------|------|---------|

Artifact count: {N}
Dims legend: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE, ?=unclear
Quality legend: STRONG = reliable anchor; ADEQUATE = usable with caution; WEAK = low weight

Pre-analysis scans:
  Coverage scan: which Dims abbreviations appear? Missing = predicts OPEN.
  Quality scan: which dimensions covered only by WEAK? At risk of OK-WEAK even with coverage.

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing. Written last, placed first. Does not decide; frames the view.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  SEQUENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  STALENESS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  COHERENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]

2-4 sentences. Rule 2: /namespace:skill format. Rule 1: absence phrase if no artifacts.

=== VERDICT ===
[FUNCTION: Single-line readiness decision. Scannable before entering any preflight item.
 Derived from the STATUS block. Condition field names exact remediation per blocking dim.]

Verdict: [GO | CONDITIONAL | NO-GO]
  GO = all dimensions OK-STRONG or OK-WEAK
  CONDITIONAL = one or more FLAG; coverage exists but has issues
  NO-GO = one or more OPEN; dimension entirely unrepresented

Condition: [GO: "None -- all dimensions pass." CONDITIONAL/NO-GO: one sentence per
  blocking dimension. Rule 2: /namespace:skill format for any skill reference.]

Blocking dimensions: [each FLAG or OPEN dimension, or "None"]

Rule 1: if check stopped at GATHER YOUR SIGNALS: "Verdict: NO-GO -- no signal artifacts
exist for {topic}."

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Dims and Quality columns provide coverage and
 reliability predictions before each item. STATUS feeds readiness summary and VERDICT.]

STATUS scale:
  OK-STRONG = 2+ independent artifacts, all within staleness threshold
  OK-WEAK   = 1 artifact, or at threshold boundary; covered but thin
  FLAG      = evidence exists but raises a concern
  OPEN      = no artifact covers this dimension

Quality weight: WEAK-only coverage caps STATUS at OK-WEAK.

Scan index:

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item structure:
  STATUS: OK-STRONG | OK-WEAK | FLAG | OPEN
  Basis: [artifacts with dates and Quality; "see above" does not pass]
  Finding: [observation or required verbatim absence phrase -- Rule 1]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 1: CAUSAL GAP ---

Mechanism is the hardest gap to name. Start here.

Dims prediction: 0 C rows = predicts OPEN; 1 = OK-WEAK; 2+ may support OK-STRONG.
Quality check: WEAK-only C-annotated artifacts cap STATUS at OK-WEAK.

Required verbatim absence phrase: "No mechanism evidence found -- the causal gap is open."

  Step 1: "The claimed outcome is: [outcome]."
  Step 2: Mechanism = [step 1] -> [step 2] -> [step 3]. Not correlation.
  Step 3: Scan C-annotated artifacts.
    (a) "Mechanism evidence found: [artifact, date, Quality] establishes [mechanism]."
    (b) Required verbatim absence phrase.

  OK-STRONG: 2+ STRONG/ADEQUATE trace mechanism independently.
  OK-WEAK: 1; or all WEAK. FLAG: correlation not mechanism. OPEN: no C in Dims.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with Quality]
  Finding: [(a) or absence phrase (b)]
  Action: [if FLAG or OPEN: /discover:causal -- Rule 2]

--- Item 2: SEQUENCE ---

Ordering is a fact. Check it before interpreting it.

Dims prediction: 0 Sq rows predicts OPEN.
Quality note: WEAK discovery counts for ordering but carries reliability caveat.

Required verbatim absence phrase: "No discovery artifacts found -- ordering cannot be established."

  Classify: Discovery vs Commitment.
  OK-STRONG: 2+ STRONG/ADEQUATE discovery predating commitment.
  OK-WEAK: 1; or WEAK quality; or narrow margin. FLAG: inversion. OPEN: no discovery.

  (a) "Discovery precedes commitment: [discovery, date, Quality] predates [commitment, date]."
  (b) "Commitment precedes discovery: inversion flagged."
  (c) Required verbatim absence phrase.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with Quality compared]
  Finding: [(a), (b), or (c)]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 3: STALENESS ---

Domain velocity determines how long a signal stays trustworthy.

Dims prediction: St annotation = staleness-sensitive.
Quality: WEAK artifacts near boundary especially at risk.

Required verbatim absence phrase: "No dated artifacts found -- staleness cannot be assessed."

  Threshold: "For {topic}'s domain: signals older than [N] days are stale because [reason]."
  OK-STRONG: all fresh, most < half age, STRONG/ADEQUATE.
  OK-WEAK: within threshold but near boundary or WEAK.
  FLAG: one or more exceed threshold. OPEN: no dated artifacts.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with date and Quality]
  Finding: [fresh/stale with Quality; or absence phrase]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 4: COHERENCE ---

Contradictions surface after commitment. Name them before.

Dims prediction: 0-1 Co rows predicts OPEN.
Quality: contradiction between WEAK artifacts is less urgent -- note in Finding.

Required verbatim absence phrase: "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."

  OK-STRONG: 2+ STRONG/ADEQUATE pairs agree.
  OK-WEAK: 1 pair; or both WEAK. FLAG: disagree. OPEN: single artifact.

  Agreement: "[A, date, Quality] and [B, date, Quality] both say [X]."
  Contradiction: "[A, date, Quality] says [X]. [B, date, Quality] says [Y]."
  Required absence phrase when no pair.

  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [pairs with Quality; or "single artifact"]
  Finding: [agreement, contradiction, or absence phrase]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis with labeled blocks. Thin Coverage from Dims; Weak
 Foundation from Quality. Null-pattern block required when no pattern exists.]

Scan:
  - Thin Coverage: 3+ dimensions with 1 Dims artifact each.
  - Weak Foundation: 3+ dimensions covered only by WEAK artifacts.

  Pattern: [name]
  Items implicated: [dimensions]
  Root cause: [single sentence]
  Single action: [/namespace:skill -- Rule 2]

  -- or --

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1: null-pattern block required. Rule 2: /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Severity-ordered. OPEN before FLAG. Within tier: CAUSAL GAP, SEQUENCE,
 STALENESS, COHERENCE. Rule 1 and Rule 2 every line.]

  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Rule 1: blank lines do not pass.
If all pass: "No missing signals -- signal health is clear."

=== ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  verdict: go | conditional | no-go
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
  open_dimensions: [{list}]
  dims_coverage:
    causal_gap: {count}
    sequence: {count}
    staleness: {count}
    coherence: {count}
  quality_distribution:
    strong: {count}
    adequate: {count}
    weak: {count}
```

---

## V-05: Combined G+H+I + live R20 axis -- evidence trace in verdict block

**Variation axis**: Combined G+H+I + live R20 axis
**Hypothesis**: All three new R20 axes (G: verdict block, H: quality column, I: prior check)
PLUS the **Evidence trace field** in the VERDICT section -- a structured mapping from each
blocking dimension to the specific inventory row(s) responsible for the gap (by row number
and artifact path, or "not represented in inventory"). Creates a closed structural loop:
VERDICT names the blocking dimension -> Evidence trace maps to the exact inventory row(s)
-> reader navigates from verdict to source without entering the preflight items.
Machine-readable: `verdict`, `blocking_dims`, `evidence_trace` in frontmatter.

C-54 candidate boundary: V-01 has Axis G (verdict block) but no Evidence trace -- fails C-54.
V-02 and V-03 lack Axis G -- fail C-54. V-04 has G+H but no Evidence trace -- fails C-54.
V-05 alone carries the Evidence trace. Boundary confirmed clean. C-54 requires VERDICT section
as precondition; VERDICT alone does not imply C-54. Independently testable from C-50/51/52/53.

Est. asp. 45/45 (all R19 criteria pass) + C-54 candidate. Composite 100.00.

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
    Applies to: readiness summary, VERDICT (including Evidence trace), CAUSAL GAP
    Finding, SEQUENCE Finding, STALENESS Finding, COHERENCE Finding, Prior check
    fields, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A skill-reference consumer disambiguating a reference consults this rule to
    determine whether a skill name in the output can be resolved to a runnable skill.
    A bare name or imprecise format in any governed location constitutes reference
    ambiguity -- it cannot be resolved without guessing.
    Applies to: readiness summary, VERDICT (Condition field only), CAUSAL GAP action,
    SEQUENCE action, STALENESS action, COHERENCE action, cross-item patterns, and
    MISSING SIGNAL GUIDE. Evidence trace field does not require skill references.
    Bare skill names in any governed location do not pass.

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
[FUNCTION: Build the artifact inventory with Dims (coverage), Quality (reliability),
 and prior check lookup. Row numbers assigned here are referenced by the Evidence trace
 in VERDICT -- they must be stable and match what appears in the table.]

Use Glob: simulations/**/*{topic}*.md
Also Glob: simulations/signal/check/{topic}-check-*.md (prior check lookup)

Prior check lookup:
  If a prior check artifact exists: note its date and per-dimension STATUS values from
    frontmatter (causal_gap_status, sequence_status, staleness_status, coherence_status).
    Record: prior_check_date = {date}, prior statuses per dimension.
  If no prior check exists: record "no prior check -- this is the first run."

Quality annotation:
  STRONG: recent (well within threshold), directly addresses topic, specific evidence.
  ADEQUATE: within threshold but limited in one dimension.
  WEAK: at/beyond boundary, or indirect, or thin evidence.

Assign row numbers to each artifact in order. These numbers are used in Evidence trace.

  | # | Artifact path | Namespace | Signal type | Date | Dims | Quality |
  |---|--------------|-----------|-------------|------|------|---------|

Artifact count: {N}
Dims legend: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE, ?=unclear
Quality legend: STRONG = reliable anchor; ADEQUATE = usable with caution; WEAK = low weight

Pre-analysis scans (run all before entering any preflight item):
  Coverage scan: which Dims abbreviations appear? Missing = predicts OPEN.
    Single row = predicts OK-WEAK at best.
  Quality scan: which dimensions covered only by WEAK? At risk of OK-WEAK or FLAG.
  dims_coverage counts: C={N}, Sq={N}, St={N}, Co={N}.

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing -- 2-4 sentences framing the team's view before any detail.
 Written last, placed first. Does not decide; the VERDICT section below states the
 decision. This section provides the narrative context.]

[Write this section last -- place it first in the final artifact.]

STATUS:
  CAUSAL GAP: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  SEQUENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  STALENESS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  COHERENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. Rule 2: /namespace:skill format for any skill reference.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made." Do not imply signal health when none was checked.

=== VERDICT ===
[FUNCTION: Single-line readiness decision plus Evidence trace. The Verdict field gives
 the overall readiness signal scannable without reading any preflight item. The Evidence
 trace field maps each blocking dimension to the specific inventory row(s) responsible for
 the gap -- creating a closed loop from verdict to source. This is the live R20 axis:
 V-01 through V-04 carry zero to two of G/H/I but none carry the Evidence trace; V-05
 carries all three axes plus the Evidence trace. The loop is: Verdict states blocking
 dimension -> Evidence trace maps to Row # -> Row # in inventory table names the artifact
 (or confirms absence). Reader navigates from decision to source without preflight items.]

Verdict: [GO | CONDITIONAL | NO-GO]
  GO = all dimensions OK-STRONG or OK-WEAK; no blocking gaps
  CONDITIONAL = one or more FLAG; coverage exists but has an issue
  NO-GO = one or more OPEN; dimension entirely unrepresented in inventory

Condition: [If GO: "None -- all dimensions pass." If CONDITIONAL or NO-GO: one sentence
  per blocking dimension stating exact remediation. Rule 2: /namespace:skill format.]

Blocking dimensions: [each FLAG or OPEN dimension by name, or "None"]

Evidence trace: [For each blocking dimension listed above, map to the inventory source.
  Format per blocking dimension:
    [Dimension] ([STATUS]): Row {N} -- {artifact path} -- {one phrase explaining the gap}
    -- OR --
    [Dimension] ([STATUS]): not represented in inventory -- no artifact carries {abbrev} in Dims
  If Verdict is GO: "None -- all dimensions pass; inventory rows confirm coverage."
  Rule 1 applies: do not leave Evidence trace blank for any blocking dimension. If source
    is ambiguous, write "source ambiguous -- inspect rows {N, M} for {dimension} coverage."
  Note: Evidence trace uses row numbers from the GATHER YOUR SIGNALS table. Rule 2 does
    not apply within Evidence trace (no skill references required in this field).]

Rule 1 applies to entire VERDICT section: if no artifacts exist and check stopped:
  "Verdict: NO-GO -- no signal artifacts exist for {topic}.
   Condition: Run /discover:causal to begin signal gathering. Rule 2 applies.
   Blocking dimensions: CAUSAL GAP (OPEN), SEQUENCE (OPEN), STALENESS (OPEN), COHERENCE (OPEN)
   Evidence trace: all dimensions -- not represented in inventory -- no artifacts found."

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. Dims and Quality columns provide coverage and
 reliability predictions. Prior check field adds trajectory. STATUS values feed the
 readiness summary and VERDICT. Evidence trace in VERDICT references row numbers from
 the inventory -- row numbers computed during GATHER YOUR SIGNALS must match.]

STATUS scale:
  OK-STRONG = 2+ independent artifacts cover this dimension, all within staleness threshold
  OK-WEAK   = 1 artifact only, or at threshold boundary; covered but thin
  FLAG      = evidence exists but raises a concern worth reviewing
  OPEN      = no artifact covers this dimension at all

Quality weight: WEAK-only coverage caps STATUS at OK-WEAK regardless of artifact count.

Trajectory vocabulary for Prior check field:
  IMPROVING = prior STATUS was worse than current
  STABLE    = prior STATUS matches current (no change)
  DEGRADING = prior STATUS was better than current
  NEW       = no prior check artifact found for this topic

Scan index (absence phrases embedded at point of use per Rule 1 -- both locations required):

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item uses this structure:

  Dims prediction: [inference from Dims column count for this dimension]
  Prior check: [{prior date}: {prior status}] -> [{current}: IMPROVING | STABLE | DEGRADING]
    -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: OK-STRONG | OK-WEAK | FLAG | OPEN
  Basis: [artifacts with dates and Quality; "see above" does not pass]
  Finding: [observation or required verbatim absence phrase -- Rule 1]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2; omit if OK-STRONG or OK-WEAK]

--- Item 1: CAUSAL GAP ---

Why this matters:
  The team may have a full discovery stack and still have no evidence for how the
  feature causes the claimed outcome. Mechanism is the hardest gap to name. Start here.

Dims prediction: count rows with C in the Dims column. 0 rows predicts OPEN;
1 row predicts OK-WEAK at best; 2+ rows may support OK-STRONG if mechanism is traced.
Quality check: all WEAK C-annotated artifacts cap STATUS at OK-WEAK.

Required verbatim absence phrase:
  "No mechanism evidence found -- the causal gap is open."

What the inventory shows:
  Step 1: "The claimed outcome is: [outcome]." (Or: not named -- itself a gap.)
  Step 2: Mechanism = causal chain [step 1] -> [step 2] -> [step 3]. Not correlation.
  Step 3: Scan C-annotated artifacts.
    (a) "Mechanism evidence found: [artifact, date, Quality] establishes [mechanism]
        by tracing [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase.

  OK-STRONG: 2+ STRONG/ADEQUATE C-annotated artifacts trace mechanism independently.
  OK-WEAK: 1 artifact; or all WEAK quality.
  FLAG: artifact traces correlation not mechanism.
  OPEN: no C in Dims; or no artifact passes mechanism test.

  Dims prediction: [state count and prediction]
  Prior check: [{prior date}: {prior causal_gap_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with Quality; if none: "no artifact addresses mechanism"]
  Finding: [(a) or required absence phrase (b)]

What the team can do:
  Action: [if FLAG or OPEN: /discover:causal -- Rule 2]

--- Item 2: SEQUENCE ---

Why this matters:
  Commitment forecloses investigation. Ordering is a fact -- check it first.

Dims prediction: count Sq rows. 0 predicts OPEN.
Quality note: WEAK discovery counts for ordering but carries reliability caveat.

Required verbatim absence phrase:
  "No discovery artifacts found -- ordering cannot be established."

What the inventory shows:
  Classify: Discovery (discover, scout, prove, research, listen) vs Commitment (draft,
  topic, program). Compare dates.

  OK-STRONG: 2+ STRONG/ADEQUATE discovery predating commitment by clear margin.
  OK-WEAK: 1 predating; or WEAK quality; or narrow margin.
  FLAG: commitment precedes discovery -- inversion.
  OPEN: no discovery artifacts.

  (a) "Discovery precedes commitment: [discovery, date, Quality] predates [commitment, date]."
  (b) "Commitment precedes discovery: inversion flagged."
  (c) Required verbatim absence phrase.

  Dims prediction: [Sq count and prediction]
  Prior check: [{prior date}: {prior sequence_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with dates and Quality compared]
  Finding: [(a), (b), or required absence phrase (c)]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 3: STALENESS ---

Why this matters:
  Domain velocity determines how long a signal stays trustworthy.

Dims prediction: St annotation identifies staleness-sensitive artifacts.
Quality note: WEAK artifacts near boundary especially at risk.

Required verbatim absence phrase:
  "No dated artifacts found -- staleness cannot be assessed."

What the inventory shows:
  "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  OK-STRONG: all within threshold; most < half age; STRONG/ADEQUATE quality.
  OK-WEAK: within threshold but near boundary; or WEAK quality.
  FLAG: one or more exceed threshold.
  OPEN: no dated artifacts.

  Dims prediction: [St count and prediction]
  Prior check: [{prior date}: {prior staleness_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [each artifact with date and Quality]
  Finding: [fresh/stale with Quality notes; or required absence phrase]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 4: COHERENCE ---

Why this matters:
  Hidden contradictions surface after commitment. Name them before.

Dims prediction: 0-1 Co rows predicts OPEN. 2+ may support OK-WEAK or OK-STRONG.
Quality note: contradiction between WEAK artifacts is noted with lower urgency.

Required verbatim absence phrase:
  "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."

What the inventory shows:
  OK-STRONG: 2+ STRONG/ADEQUATE pairs agree; no latent contradictions.
  OK-WEAK: 1 pair; agree; limited scope; or both WEAK.
  FLAG: at least one pair disagrees.
  OPEN: single artifact only.

  Agreement: "[A, date, Quality] and [B, date, Quality] both say [X]."
  Contradiction: "[A, date, Quality] says [X]. [B, date, Quality] says [Y]."
  Required absence phrase when no pair.

  Dims prediction: [Co count and prediction]
  Prior check: [{prior date}: {prior coherence_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [pairs with Quality; or "single artifact -- no comparable pair"]
  Finding: [agreement, contradiction, or required absence phrase]

What the team can do:
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis with labeled blocks. Dims reveals Thin Coverage; Quality
 reveals Weak Foundation; trajectory reveals Signal Decay. Null-pattern block required
 when no pattern exists -- this section never silently passes.]

Step back from all four items. Do two or more share a common root?
Scan:
  - Thin Coverage: 3+ dimensions with 1 Dims artifact each.
  - Weak Foundation: 3+ dimensions covered only by WEAK artifacts.
  - Signal Decay: 2+ dimensions showing DEGRADING in Prior check field.

  Pattern: [name -- e.g., "Premature Commitment", "Thin Coverage", "Weak Foundation",
    "Signal Decay", "Stale Signal Cascade"]
  Items implicated: [list dimensions]
  Root cause: [single sentence]
  Single action: [/namespace:skill -- Rule 2]

Common patterns:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: root = missing discovery phase;
    action = /discover:causal
  - STALENESS FLAG + COHERENCE FLAG: root = stale signal causing contradiction;
    action = refresh the stale artifact
  - Multiple OK-WEAK (Dims: 3+ dims with 1 artifact each):
    root = thin coverage; action = discovery skill for weakest dim
  - Signal Decay (2+ DEGRADING): root = signal portfolio eroding without refresh;
    action = /discover:causal or /scout:feasibility for the most degraded dim

If no pattern exists:

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1 applies: null-pattern block required when no pattern exists.
Rule 2 applies: Single action uses /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Actionable gap map, severity-ordered. Most blocking gap appears first.
 Rule 1 and Rule 2 both apply to every line.]

Items ordered by severity: OPEN before FLAG.
Within same severity tier: CAUSAL GAP, then SEQUENCE, then STALENESS, then COHERENCE.
Invariant ordering -- do not reorder by preference or discovery order.

For every FLAG or OPEN dimension:
  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Examples (OPEN before FLAG):
  CAUSAL GAP OPEN: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE OPEN: run /discover:competitors -- produces dated discovery artifact to establish order
  COHERENCE OPEN: run /scout:feasibility -- produces second feasibility signal for comparison
  STALENESS FLAG: run /discover:competitors -- refreshes competitive landscape signal

Rule 1: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required."

If all dimensions pass: "No missing signals -- signal health is clear."

=== ARTIFACT ===
[FUNCTION: Persist the health report. Frontmatter includes verdict, blocking_dims,
 evidence_trace, trajectory, quality_distribution, and dims_coverage -- all machine-readable.
 This artifact is the ground truth for any future /signal:check run on this topic,
 and its STATUS fields feed the trajectory computation of the next run's Prior check fields.]

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  verdict: go | conditional | no-go
  blocking_dims: [{list of FLAG or OPEN dimension names, or empty list}]
  evidence_trace:
    causal_gap: "Row {N}: {artifact path}" | "not represented in inventory"
    sequence: "Row {N}: {artifact path}" | "not represented in inventory"
    staleness: "Row {N}: {artifact path}" | "not represented in inventory"
    coherence: "Row {N}: {artifact path}" | "not represented in inventory"
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
  quality_distribution:
    strong: {count}
    adequate: {count}
    weak: {count}
  prior_check_date: {date or null}
  trajectory:
    causal_gap: improving | stable | degrading | new
    sequence: improving | stable | degrading | new
    staleness: improving | stable | degrading | new
    coherence: improving | stable | degrading | new
```

---

## Live R20 axis identification

**C-54 candidate**: The VERDICT section includes an Evidence trace field mapping each
blocking dimension to the specific inventory row(s) responsible for the gap (by row number
and artifact path, or "not represented in inventory"), creating a closed structural loop
from verdict decision to source artifact (or confirmed absence); an output with a VERDICT
section (Axis G) but without an Evidence trace field satisfies the verdict-block requirement
but not C-54: the reader cannot navigate from the blocking dimension to the exact inventory
source without entering the preflight items; C-54 requires the VERDICT section as a
precondition; the VERDICT section alone does not imply C-54; C-54 is independently testable:
presence or absence of the Evidence trace field in the VERDICT block is structurally
observable without entering any preflight item or section body; boundary confirmed clean
across four variations: V-01 carries Axis G without Evidence trace (C-54 FAIL); V-02 and
V-03 lack Axis G (C-54 FAIL); V-04 carries G+H without Evidence trace (C-54 FAIL);
V-05 alone carries the Evidence trace (C-54 PASS).

**Boundary confirmation by variation:**

| Var | Axes present | Verdict block | Quality column | Prior check | Evidence trace | C-54 |
|-----|-------------|---------------|----------------|-------------|----------------|------|
| V-01 | G | Present | Absent | Absent | Absent | FAIL |
| V-02 | H | Absent | Present | Absent | Absent | FAIL |
| V-03 | I | Absent | Absent | Present | Absent | FAIL |
| V-04 | G+H | Present | Present | Absent | Absent | FAIL |
| V-05 | G+H+I + live | Present | Present | Present | Present | PASS |
