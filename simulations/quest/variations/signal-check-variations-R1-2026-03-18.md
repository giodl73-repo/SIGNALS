Written to `simulations/quest/variations/signal-check-variations-R1-2026-03-18.md`.

---

## signal-check Variations — R1

**5 variations across 3 axes:**

| V | Label | Axis | Key move |
|---|-------|------|----------|
| V-01 | Status-tagged sections | Output format | `STATUS / Basis / Finding / Action` per dimension — forces artifact citation structurally |
| V-02 | CAUSAL GAP first | Dimension order | Leads with mechanism before SEQUENCE/COHERENCE/STALENESS — prevents trailing-analysis silence on C-04 |
| V-03 | Coaching scaffold | Phrasing register | Preflight metaphor + "What you can do:" per section — makes coaching register feel structural, not instructed |
| V-04 | Tags + CAUSAL GAP first | Combination | V-01 + V-02 — essentials + recommended without aspirational scaffold |
| V-05 | Full canonical stack | Combination | All three — every criterion (C-01 to C-10) has a dedicated structural slot |

**Three research questions:**
1. Do status tags close C-02/C-03 failures better than prose instruction alone?
2. Does CAUSAL GAP-first order close the C-04 silence pattern regardless of framing?
3. Does the preflight scaffold produce C-05 compliance more reliably than a stated "not punitive" instruction?

V-05 is the rubric-ceiling reference — expected score 100. V-04 should clear gold (estimated 85). V-01 through V-03 are the diagnostic singles.
urth dimension receives only a sentence or
  two after three prior sections have been written. C-04 fails most commonly through silence, not error.
  Leading with the hardest question forces engagement before any other analysis is on record.

- **V-03 (phrasing register):** A "preflight checklist" framing with per-section "What we're checking /
  What we found / What you can do" scaffold consistently activates coaching register because the metaphor
  makes advisory language feel natural. Formal dimension headers may trigger evaluation-register defaults
  that override the coaching intent stated in the skill description.

---

## V-01: Status-tagged sections (output format axis)

**Axis:** Output format — each dimension produces a named STATUS tag, an artifact-grounded Basis, a
specific Finding, and (when flagged) an Action field. Structure forces discrete conclusions over hedged prose.

**Hypothesis:** C-02 and C-03 fail primarily because prose sections allow vague summaries that pass
without citing artifact names or dates. Adding a required `Basis:` field that must list artifact names and
dates makes artifact-grounding a structural requirement — not an implicit expectation. The `Action:` field
makes next-step production mandatory at the section level rather than optional at the end.

```
You are running /signal-check for topic: {topic}.

This is a coaching check — not a gate. The output surfaces what looks inconsistent
so you can decide what to address before committing.

=== STEP 1: ARTIFACT INVENTORY ===

Use Glob to find all signal artifacts for {topic} in simulations/.
Search pattern: simulations/**/*{topic}*.md

List every artifact found. For each row:

  | Artifact | Namespace | Signal type | Date |
  |----------|-----------|-------------|------|

If no artifacts are found, write: "No signal artifacts found for {topic}. Analysis
cannot proceed." and stop.

=== STEP 2: DIMENSION ANALYSIS ===

Analyze all four dimensions below. Each section has a required structure.
Complete all four regardless of findings.

Required structure per dimension:
  STATUS: OK | FLAG | OPEN
    OK = no issue identified
    FLAG = issue identified, team should review before committing
    OPEN = gap present, no artifact covers this area
  Basis: [artifact names and dates cited -- "see above" does not pass; name them]
  Finding: [specific observation -- generic summary does not pass]
  Action: [if STATUS is FLAG or OPEN, name a concrete next step; omit only if OK]

--- SEQUENCE ---

Did discovery happen before specification?

Check the dates of discovery-type artifacts (namespace: discover, scout, prove) against
the dates of specification-type artifacts (namespace: draft, topic). For each comparison,
cite the artifact names and their dates.

  STATUS: [OK / FLAG / OPEN]
  Basis: [list the artifact names and dates you compared]
  Finding: [does the date evidence show discovery before specification, after, or mixed?
    Name the specific artifacts that establish the order. Do not assert order without
    citing dates.]
  Action: [if FLAG or OPEN -- what specific artifact or signal would resolve this?]

--- COHERENCE ---

Do your signals agree with each other?

Look for claims in two or more artifacts that bear on the same question (e.g., market size,
user need, feasibility). Name at least one pair that agrees and at least one pair that
contradicts -- or state explicitly that only one artifact covers each question (no pair
available to compare).

  STATUS: [OK / FLAG / OPEN]
  Basis: [names of artifact pairs examined]
  Finding: [name at least one specific agreement (Artifact A and Artifact B both say X)
    or contradiction (Artifact A says X, Artifact B says Y). Generic "signals seem
    aligned" without named artifacts does not pass.]
  Action: [if FLAG or OPEN -- which pair should be reconciled, and how?]

--- STALENESS ---

Are your signals recent enough to trust?

Name your staleness threshold first, calibrated to the topic's domain velocity
(e.g., "30 days for a competitive market," "90 days for a stable enterprise segment").
Apply it to each artifact in the inventory.

  Threshold: [name it explicitly -- "recent enough" without a number does not pass]
  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked against the threshold]
  Finding: [which artifacts are within threshold, which are past it?]
  Action: [if FLAG or OPEN -- which artifact needs refreshing, and which skill would
    produce the refresh?]

--- CAUSAL GAP ---

Do you have evidence for the mechanism linking the feature to the claimed outcome?

Name the claimed outcome for {topic}. Then check whether any artifact establishes the
mechanism -- the causal chain from the feature to the outcome. A mechanism is not the
outcome itself ("users will adopt it") nor a correlation; it is an account of why the
feature causes the outcome.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact(s) that address mechanism, if any -- or "no artifact addresses
    mechanism"]
  Finding: [does any artifact name the causal chain? If yes, cite it. If no, state
    explicitly: "no mechanism evidence found -- the gap is open."]
  Action: [if FLAG or OPEN -- which discover skill would close this gap?]

=== STEP 3: CROSS-DIMENSION PATTERNS ===

Review the four STATUS values above. If two or more dimensions share a common root cause
(e.g., SEQUENCE FLAG and CAUSAL GAP OPEN both trace to the team specifying before running
any discovery), name the shared root and describe the pattern.

If no cross-dimension link exists, write: "No cross-dimension pattern identified."

=== STEP 4: READINESS SUMMARY ===

Open the report with a 2-4 sentence summary:
  - Overall signal health posture for {topic}
  - Which dimensions are clear, which have open gaps
  - Whether the team can proceed with current signals or should address gaps first

Write this summary BEFORE the dimension breakdown in the final output.
(Draft it last, then move it to the top of the artifact.)

=== STEP 5: ARTIFACT ===

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  sequence_status: ok | flag | open
  coherence_status: ok | flag | open
  staleness_status: ok | flag | open
  causal_gap_status: ok | flag | open
  staleness_threshold_named: true | false
  artifact_count: {count from inventory}
  cross_dimension_pattern: true | false
  open_dimensions: [{list of dimension names with FLAG or OPEN status}]
```

---

## V-02: CAUSAL GAP first (dimension order axis)

**Axis:** Dimension order — CAUSAL GAP is analyzed first, before SEQUENCE, STALENESS, or COHERENCE.
The natural "story" order (SEQUENCE first, mechanism last) is reversed.

**Hypothesis:** C-04 fails primarily through silence — the dimension receives a brief sentence or is
skipped after three prior sections have been written. Leading with CAUSAL GAP forces mechanism engagement
before the model has written anything else. Cross-dimension patterns (C-09) are also more likely to be
named when the causal gap is on record before SEQUENCE is analyzed, because the analyst can see whether
a SEQUENCE gap explains the mechanism gap rather than treating them as independent.

```
You are running /signal-check for topic: {topic}.

This is a coaching check, not a gate. It surfaces what looks inconsistent so you
can decide what to address before committing. Not punitive -- your signals are
yours to act on.

=== ARTIFACT INVENTORY ===

Use Glob to find all signal artifacts for {topic} in simulations/.
Pattern: simulations/**/*{topic}*.md

List each artifact: path, namespace, signal type, date.

If none found: "No signal artifacts found for {topic}." Stop.

=== READINESS SUMMARY ===

After completing the four dimension sections below, return here and write a 2-4 sentence
summary of overall signal health posture. State which dimensions are clear, which have gaps,
and whether the team can proceed or should address something first. This summary appears
at the top of the final report -- draft it last, position it first.

=== DIMENSION ANALYSIS ===

Analyze all four dimensions. The order below is intentional: start with the causal
question, which is the hardest to establish and the most commonly absent.

--- CAUSAL GAP ---

Do you have evidence for the mechanism linking {topic}'s feature to its claimed outcome?

This is the hardest signal to gather because it requires more than correlation or adoption
data -- it requires an account of why the feature causes the outcome.

Step 1: Name the claimed outcome for {topic}.

Step 2: Check whether any artifact names the causal chain from the feature to that outcome.
A causal chain is a sequence of observable intermediate steps, not a summary claim ("users
will benefit"). Check across all namespaces -- mechanism evidence can appear in discover,
prove, scout, or research artifacts.

Step 3: Report one of two things -- and be explicit:
  (a) "Mechanism evidence found: [artifact name] establishes [the chain] by [how]."
  (b) "No mechanism evidence found. The causal gap is open."

Silence on mechanism does not pass this section.

If the gap is open: name the skill that would close it (e.g., /discover-causal).

--- SEQUENCE ---

Did discovery happen before specification?

Check the dates of discovery-type artifacts (discover, scout, prove namespaces) against
specification-type artifacts (draft, topic namespaces). Cite artifact names and dates.

If discovery artifacts predate specification artifacts: note this and state which ones.
If specification predates discovery: flag the inversion and name the specific artifacts.
If no discovery artifacts exist: state this explicitly -- do not assert an order.

--- STALENESS ---

Are your signals recent enough to trust?

Before assessing, name your threshold:
  "For {topic}'s domain, signals older than [N] days are stale because [brief reason]."

Apply the threshold to each artifact. Name which are within threshold and which are past it.
If any artifact is past threshold, name the Signal skill that would refresh it.

--- COHERENCE ---

Do your signals agree with each other?

Find signal pairs that address the same question. Name at least one:
  Agreement: "[Artifact A] and [Artifact B] both say [X]."
  Contradiction: "[Artifact A] says [X]. [Artifact B] says [Y]."

If only one artifact covers each question, state: "No comparable pair available for
[question] -- only one artifact covers it."

Generic "signals seem aligned" without named artifact pairs does not pass this section.

=== CROSS-DIMENSION PATTERNS ===

Look across the four findings above. Do two or more dimensions share a common root cause?

Example: if SEQUENCE shows specification before discovery AND CAUSAL GAP is open, the
root may be the same event: the team committed to a spec before gathering mechanism evidence.
Name the pattern rather than listing four independent issues.

If no shared root exists, state: "No cross-dimension pattern identified."

=== NEXT ACTIONS ===

For every issue flagged across any dimension, state a concrete next step.

Format:
  Issue: [dimension and finding]
  Next action: [specific step -- name the skill if relevant]

If all dimensions are OK, write: "No actions required -- signal health is clear."

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
```

---

## V-03: Coaching scaffold (phrasing register axis)

**Axis:** Phrasing register — the entire prompt uses a preflight-checklist metaphor. Each dimension is
framed as "What we're checking / What we found / What you can do." Coaching language is built into the
section definitions, not just the framing preamble.

**Hypothesis:** C-05 fails not because models ignore the "not punitive" instruction but because the
analytical framing of "flag vs. pass" activates evaluation-register defaults regardless of the stated
intent. A metaphor that is inherently advisory (preflight check before takeoff -- the pilot decides
whether to fly) makes coaching register feel structurally appropriate rather than an override of default
behavior. Embedding "What you can do" as a named output slot in each section makes C-07 compliance
structural rather than instructed.

```
You are running /signal-check for topic: {topic}.

Think of this as a preflight checklist before takeoff. The checklist does not decide whether
to fly -- the pilot does. It surfaces what to look at so the pilot can make an informed
call. Nothing in this report blocks you from proceeding. It exists to make sure you know
what you know before you commit.

=== GATHER YOUR SIGNALS ===

Use Glob to find all signal artifacts for {topic} under simulations/.
Pattern: simulations/**/*{topic}*.md

For each artifact found, note:
  - What it is (namespace and signal type)
  - When it was written (date from filename or frontmatter)
  - What question it answers

No artifacts found? That is itself a signal. Write: "No signal artifacts exist yet for
{topic}. Consider running discovery skills before committing." Then stop.

=== THE CHECKLIST ===

Work through each item below. The format for each item is:

  What we're checking: [the question this item asks]
  What we found: [your observation, grounded in the artifacts above -- name them]
  What you can do: [a concrete next step if there's something to address; or "Nothing
    needed here -- this item is clear" if not]

Complete all four items.

--- Item 1: SEQUENCE ---

What we're checking:
  Did you discover before you specified? Evidence-first development works best when
  discovery signals (competitors, causal evidence, user research) predate commitment
  signals (specs, proposals). This item checks whether your artifact dates support that
  order.

What we found:
  Look at the dates of your discovery-type artifacts (discover, scout, prove namespaces)
  and your specification-type artifacts (draft, topic namespaces). State what you see.

  Name the artifacts and their dates. Do not assert an order without citing dates.
  If no discovery artifacts exist, say so -- that is the finding.

What you can do:
  If discovery artifacts predate specs: nothing needed here.
  If specs predate discovery, or discovery is absent: name what signal you'd want to have
  gathered earlier, and which skill produces it.

--- Item 2: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When multiple signals touch the same question
  (e.g., market size, user urgency, feasibility), they should roughly agree -- or the
  disagreement should be visible and understood. Invisible contradictions are the ones
  that hurt.

What we found:
  Find at least one pair of artifacts that bear on the same question. State what each says.
  Name them specifically. "Signals seem aligned" without naming the artifacts and what they
  say does not count as a finding.

  If only one artifact covers each question: say so. That means there is no pair to compare
  yet -- which is its own kind of gap.

What you can do:
  If signals agree: nothing needed here.
  If signals contradict: name the contradiction and what additional signal would clarify it.
  If no pairs exist: name what second artifact would give you something to compare against.

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Signal age matters differently by domain -- a
  competitive market changes in weeks; an enterprise procurement cycle changes in quarters.
  This item checks whether your artifacts are within a reasonable freshness window for the
  decisions you're making.

What we found:
  First, name your freshness threshold for this topic's domain:
    "For {topic}'s context, I'm using [N] days as the freshness window because [brief reason]."

  Then check each artifact against that threshold. Name which ones are fresh and which ones
  are past it.

What you can do:
  If all artifacts are fresh: nothing needed here.
  If any artifact is stale: name it, state how old it is vs. the threshold, and name the
  skill that would produce a refreshed signal.

--- Item 4: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the outcome -- not just that it might,
  but how? This is often the last signal gathered, or not gathered at all. A team can have
  solid discovery, fresh signals, and internally consistent artifacts while still having
  no account of the causal mechanism. This item surfaces that gap if it exists.

What we found:
  Name the claimed outcome for {topic}.

  Now check: does any artifact establish the causal chain from the feature to that outcome?
  A causal chain is a sequence of observable steps -- it is not "users will adopt it" or
  a correlation metric.

  State clearly either:
    (a) "Mechanism evidence found: [artifact] establishes [chain] by [how]."
    (b) "No mechanism evidence found. The causal gap is open."

  Do not leave this item blank or hedge with "mechanism may be implied."

What you can do:
  If mechanism evidence exists: nothing needed here.
  If the gap is open: name the skill that would close it (e.g., /discover-causal).

=== PATTERNS ===

Step back from the four items above. Do any of them share a common cause?

For example: if SEQUENCE shows late discovery AND CAUSAL GAP is open, the root might be
the same: the team moved to spec before gathering any discovery evidence. When this happens,
it is more useful to name the pattern than to list two separate issues.

Look for it. If you see a shared root, name it in one sentence. If you don't, write:
"No cross-item pattern found."

=== READINESS SUMMARY ===

Two to four sentences at the top of your report. Write this section last, but place it
first in the output. Tell the team:
  - What the overall picture looks like
  - Which items are clear, which need a look before committing
  - Whether signals are strong enough to proceed or whether there's a specific gap worth
    closing first

Remember: this is the pilot briefing, not a go/no-go gate. State what you see and what
you recommend. The team decides.

=== WRITE THE ARTIFACT ===

Save to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  sequence_status: ok | flag | open
  coherence_status: ok | flag | open
  staleness_status: ok | flag | open
  causal_gap_status: ok | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  cross_dimension_pattern: true | false
  artifact_count: {count}
```

---

## V-04: Status tags + CAUSAL GAP first (combination: format + dimension order)

**Axes combined:** V-01 (status-tagged format) + V-02 (CAUSAL GAP first)

**Hypothesis:** The status-tag format enforces grounded findings (C-02, C-03) regardless of dimension
order. CAUSAL GAP-first ensures mechanism engagement before fatigue sets in (C-04). Together they should
close the most common essential-criteria failures. The structural `Action:` field in each section enforces
C-07 across all four dimensions simultaneously. This combination should score well on all 5 essentials
and all 3 recommended criteria. The aspirational criteria (C-09, C-10) require additional instruction
not present here -- testing whether essentials + recommended can be achieved without the aspirational
scaffold.

```
You are running /signal-check for topic: {topic}.

Coaching check -- not a gate. Surfaces inconsistencies so you can decide what to
address before committing. Advisory throughout.

=== ARTIFACT INVENTORY ===

Glob: simulations/**/*{topic}*.md

Build an inventory table:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts found: stop. Write "No signal artifacts found for {topic}."

=== READINESS SUMMARY ===

[Write this section last, but place it first in the artifact.]

2-4 sentences: overall signal health posture, which dimensions are clear, which have gaps,
whether signals support proceeding or recommend addressing a gap first.

=== DIMENSION ANALYSIS ===

Each dimension uses this structure:

  STATUS: OK | FLAG | OPEN
  Basis: [artifact names and dates -- citing "above" is not sufficient; name them here]
  Finding: [specific, named observation]
  Action: [required if STATUS is FLAG or OPEN; omit only if OK]

Analyze in the order below.

--- CAUSAL GAP ---

Does any artifact establish the mechanism linking {topic}'s feature to its claimed outcome?

Step 1: Name the claimed outcome for {topic}.

Step 2: Scan the artifact inventory for anything that names a causal chain -- a sequence
of observable steps from feature to outcome. Check all namespaces.

Step 3: Produce the structured output:

  STATUS: OK | FLAG | OPEN
    OK = artifact found that names the mechanism
    FLAG = artifact touches mechanism but does not trace the chain explicitly
    OPEN = no artifact addresses mechanism
  Basis: [artifact name(s) that were checked for mechanism content; if none, write "none"]
  Finding: [one of two explicit statements:
    (a) "Mechanism evidence found: [artifact] traces [chain] via [steps]."
    (b) "No mechanism evidence found. The causal gap is open."
    Silence does not pass.]
  Action: [if FLAG or OPEN: name the skill to run -- e.g., "Run /discover-causal to
    establish mechanism evidence before committing."]

--- SEQUENCE ---

Did discovery happen before specification?

Compare dates of discovery-type artifacts (discover, scout, prove) to specification-type
artifacts (draft, topic). Cite artifact names and dates in Basis.

  STATUS: OK | FLAG | OPEN
    OK = discovery dates precede specification dates
    FLAG = mixed or ambiguous order
    OPEN = no discovery artifacts exist
  Basis: [artifact names and dates compared -- e.g., "competitors-check-2026-03-10 (discover)
    vs. feature-spec-2026-03-05 (draft)"]
  Finding: [state the order the dates show; name the specific artifacts establishing it;
    do not assert order without dates]
  Action: [if FLAG or OPEN: name the discovery skill and signal that would close the gap]

--- STALENESS ---

Are signals fresh enough to trust?

Name your threshold before applying it:
  "Threshold for {topic}: signals older than [N] days are stale, because [reason]."

Apply threshold to each artifact in the inventory.

  STATUS: OK | FLAG | OPEN
    OK = all artifacts within threshold
    FLAG = one or more artifacts past threshold
    OPEN = all artifacts past threshold, or inventory has no dated artifacts
  Basis: [artifacts checked, with their dates]
  Finding: [which are within threshold, which are past it -- by name]
  Action: [if FLAG or OPEN: name the artifact to refresh and the skill to run]

--- COHERENCE ---

Do your signals agree with each other?

Identify artifact pairs that address the same question. Name at least one agreement or
contradiction, or state why no comparable pair is available.

  STATUS: OK | FLAG | OPEN
    OK = signals agree on the questions they share
    FLAG = contradiction identified
    OPEN = only one artifact per question -- no pair to compare
  Basis: [artifact pairs examined]
  Finding: [name a specific agreement or contradiction:
    "Artifact A [date] says X. Artifact B [date] says Y." Generic summary does not pass.]
  Action: [if FLAG or OPEN: name what would resolve the contradiction or provide
    a comparable second artifact, and which skill produces it]

=== CROSS-DIMENSION PATTERNS ===

Review the four STATUS values. If two or more dimensions share a common root cause, name it.

Examples:
  - SEQUENCE OPEN + CAUSAL GAP OPEN: "The team has not run discovery -- both gaps trace
    to a single missing phase."
  - SEQUENCE FLAG + CAUSAL GAP OPEN: "Specification preceded discovery; the mechanism gap
    is likely a downstream effect of the same decision."

If no shared root: "No cross-dimension pattern identified."
If a pattern exists: name it, name which dimensions it explains, and name the single
action that would close both.

=== MISSING SIGNAL GUIDE ===

For each dimension with STATUS FLAG or OPEN, name the specific skill (by namespace and
skill name) that would close the gap. One line per gap:

  [Dimension] gap: run /[namespace]:[skill] to [what it produces]

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

## V-05: Full canonical stack (combination: format + dimension order + coaching register)

**Axes combined:** V-01 (status-tagged format) + V-02 (CAUSAL GAP first) + V-03 (coaching scaffold)

**Hypothesis:** All 10 criteria can be satisfied in a single output by: (a) CAUSAL GAP-first order
preventing C-04 silence, (b) STATUS/Basis/Finding/Action structure enforcing C-02, C-03, C-06, C-07
structurally, (c) preflight metaphor in the preamble activating coaching register throughout for C-05,
(d) explicit READINESS SUMMARY at the top for C-08, (e) CROSS-DIMENSION PATTERNS section targeting C-09,
and (f) MISSING SIGNAL GUIDE requiring namespace + skill name for C-10. This is the rubric-ceiling
reference for v1 -- every criterion has a dedicated structural slot.

```
You are running /signal-check for topic: {topic}.

Think of this as a preflight check. The checklist does not decide whether to fly -- it
makes sure the pilot sees everything before they decide. Nothing here blocks you from
proceeding. It exists so you know what you know before you commit.

=== GATHER YOUR SIGNALS ===

Use Glob to locate all signal artifacts for {topic}:
  Pattern: simulations/**/*{topic}*.md

Build an inventory:

  | # | Artifact path | Namespace | Signal type | Date |
  |---|--------------|-----------|-------------|------|

Artifact count: {N}

If no artifacts are found: "No signal artifacts exist yet for {topic}. Consider running
discovery skills before committing." Stop.

=== READINESS SUMMARY ===

[Write this section last -- place it first in the final artifact.]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which have
gaps the team may want to address, and what the team can do now vs. what would strengthen
their position before committing. Frame as a briefing, not a verdict.

=== THE PREFLIGHT CHECK ===

Each item uses this structure:

  STATUS: OK | FLAG | OPEN
    OK = no issue
    FLAG = issue found, worth reviewing before committing
    OPEN = gap -- no artifact covers this area
  Basis: [name the specific artifacts you examined -- dates included; "see above" or
    "listed earlier" does not pass; name them here in each section]
  Finding: [specific named observation; generic summaries without artifact names do not pass]
  Action: [required if STATUS is FLAG or OPEN; omit only when OK]

Work through all four items. The order is intentional: start with the causal question.

--- Item 1: CAUSAL GAP ---

What we're checking:
  Do you have evidence for why the feature causes the claimed outcome -- not just that it
  might, but how? This is the signal teams gather last, if ever. A full set of discovery
  artifacts can still leave this gap open. Surfacing it now, before committing, is the
  point of this item.

What we found:
  Step 1: Name the claimed outcome for {topic}.

  Step 2: Scan the artifact inventory for any signal that names a causal chain from the
  feature to that outcome. A causal chain is a sequence of observable steps -- not a
  summary claim ("users will benefit") and not a correlation ("adoption correlates with Y").
  It explains how the feature causes the outcome.

  Step 3: State explicitly:
    (a) "Mechanism evidence found: [artifact name, date] establishes [mechanism] by tracing
        [the steps]."
    (b) "No mechanism evidence found. The causal gap is open."

  Silence is not acceptable here. If you are uncertain, state the uncertainty -- but name
  whether evidence exists or does not.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifacts checked for mechanism content]
  Finding: [(a) or (b) from above]

What you can do:
  Action: [if FLAG or OPEN: "Run /discover-causal to establish mechanism evidence before
    committing." Or name a more specific skill if a partial mechanism already exists.]

--- Item 2: SEQUENCE ---

What we're checking:
  Did discovery happen before specification? The order matters because commitment tends
  to close off investigation. If specs were written before discovery signals existed, the
  team may have committed to a direction before knowing what they were committing to.

What we found:
  Compare the dates of discovery-type artifacts (discover, scout, prove namespaces) to
  specification-type artifacts (draft, topic namespaces). Name the artifacts and their dates.
  State what the dates show.

  If no discovery artifacts exist: state this -- that is the finding, not a reason to skip
  the item.
  If discovery dates precede spec dates: state this and name the specific artifacts.
  If spec dates precede discovery: state this, name the inversion, and name which artifacts
  establish the order.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact names and dates compared]
  Finding: [what the dates show -- no assertion without dates]

What you can do:
  Action: [if FLAG or OPEN: name the discovery signal missing before specification, and
    the skill that produces it]

--- Item 3: STALENESS ---

What we're checking:
  Are your signals fresh enough to act on? Domain velocity determines what "fresh" means.
  A fast-moving market makes a 30-day-old competitive signal unreliable. A stable enterprise
  procurement cycle means a 90-day-old signal may still be sound. This item checks whether
  your artifact dates fall within a defensible freshness window.

What we found:
  First, name your threshold:
    "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  Apply it to each artifact. State which are within threshold and which are past it.

  STATUS: [OK / FLAG / OPEN]
  Basis: [each artifact with its date, checked against threshold]
  Finding: [which are fresh, which are stale -- by name]

What you can do:
  Action: [if FLAG or OPEN: name the stale artifact, how old it is vs. the threshold, and
    the skill that would produce a fresh signal]

--- Item 4: COHERENCE ---

What we're checking:
  Do your signals tell a consistent story? When two signals address the same question
  (market size, user urgency, competitive threat, feasibility), they should roughly agree --
  or the disagreement should be visible and deliberate. Hidden contradictions are the ones
  that surface after commitment.

What we found:
  Find at least one pair of artifacts that address the same question. For each pair, state
  what each artifact says about that question.

  Name a specific agreement or contradiction:
    Agreement: "[Artifact A, date] and [Artifact B, date] both say [X]."
    Contradiction: "[Artifact A, date] says [X]. [Artifact B, date] says [Y]. These disagree
    on [question]."

  If only one artifact covers each question: "No comparable pair exists for [question] --
  only one artifact covers it. This means there is nothing to cross-check against yet."

  Generic statements ("signals seem aligned") without named artifact pairs do not pass
  this item.

  STATUS: [OK / FLAG / OPEN]
  Basis: [artifact pairs examined]
  Finding: [named agreement, contradiction, or absence of a pair]

What you can do:
  Action: [if FLAG or OPEN: name the contradiction to resolve, or the second artifact
    needed for comparison, and which skill produces it]

=== CROSS-ITEM PATTERNS ===

Step back from the four items. Do two or more items share a common root cause?

This matters because addressing a shared root closes multiple gaps with one action, while
treating them as four independent issues can lead to incomplete fixes.

Look for it:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: both may trace to a single missing phase --
    the team has not run discovery. One root, two symptoms.
  - SEQUENCE FLAG + CAUSAL GAP OPEN: specification preceded discovery; the mechanism gap
    is likely a downstream effect of the same premature commitment.
  - STALENESS FLAG + COHERENCE FLAG: stale signals are the source of the contradiction --
    one artifact reflects old market conditions, one reflects current ones.

If a pattern exists: name it in one sentence. Name the dimensions it explains. Name the
single action that would address the root.

If no shared root: "No cross-item pattern found."

=== MISSING SIGNAL GUIDE ===

For every item with STATUS FLAG or OPEN, name the specific skill that would close it.
Use this format (one line per gap):

  [Dimension] gap: run /[namespace]:[skill] -- produces [what it creates]

Examples:
  CAUSAL GAP open: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE open: run /discover:competitors -- produces a dated discovery artifact to establish order
  STALENESS flag on competitors signal: run /discover:competitors -- refreshes competitive landscape

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
  artifact_count: {count}
  cross_dimension_pattern: true | false
  missing_signals_by_skill: true | false
  open_dimensions: [{list of FLAG or OPEN dimension names}]
```

---

## Design notes

**Why CAUSAL GAP first?** The natural narrative order (SEQUENCE -> COHERENCE -> STALENESS -> CAUSAL GAP)
puts the hardest dimension last. When three sections have already been written, the fourth receives less
attention. CAUSAL GAP is also the most commonly open -- discovery, coherence, and freshness are more
obvious to track; causal mechanism is easy to leave implicit. V-02, V-04, V-05 test whether leading with
it closes the silence pattern.

**Why status tags?** Prose dimension sections allow hedging ("some signals may be inconsistent") that
satisfies neither C-03 nor C-04. A forced `STATUS: OK / FLAG / OPEN` choice requires a discrete
conclusion, and the `Basis:` field requirement makes artifact citation structural rather than optional.
V-01, V-04, V-05 test whether this closes the most common essential-criteria failures.

**Why coaching scaffold in V-03?** C-05 fails not when models are told to be advisory but when the
analytical structure defaults to evaluation-register language. The preflight metaphor makes advisory
framing feel natural to the structure rather than an override instruction. The "What you can do:" field
in each section makes C-07 compliance structural.

**Expected scoring:**

| V | E (5) | R (3) | A (2) | Est. composite | Gold? |
|---|-------|-------|-------|---------------|-------|
| V-01 | 5 | 2-3 | 0-1 | 74-88 | maybe |
| V-02 | 4-5 | 2 | 1 | 70-82 | maybe |
| V-03 | 4-5 | 3 | 0-1 | 72-85 | maybe |
| V-04 | 5 | 3 | 1 | 85 | YES |
| V-05 | 5 | 3 | 2 | 100 | YES |

**Research questions from this round:**

1. Does the status-tag format (V-01) close C-02/C-03 failures more reliably than prose instruction alone?
2. Does CAUSAL GAP-first ordering (V-02) close the C-04 silence pattern, or does the model still hedge
   regardless of position?
3. Does the coaching scaffold (V-03) produce C-05 compliance more reliably than a stated "not punitive"
   instruction, or is register primarily controlled by structural format?
