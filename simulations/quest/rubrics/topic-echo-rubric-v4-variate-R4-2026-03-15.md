# Variations: `topic:echo` — Round 4

**Rubric:** v4 (max 135) | **Date:** 2026-03-15

---

## Design Context

R3 identified three excellence signals that became C-15, C-16, and C-17 in v4:

- **C-15 (from V-01/R3 discard rule)**: C-13 can be satisfied by writing a softer version
  of the finding. The discard rule showed that the Expected field must force genuine
  opposition in direction, mechanism, or actor — not just a smaller magnitude of the same
  direction. This is structural: the gap is not in author intent but in schema definition.

- **C-16 (from V-01/R3 inline failure-mode naming)**: C-02, C-03, and C-07 each check field
  presence. V-01 showed that field presence without content specificity delivers no
  institutional value. Named anti-patterns at the field level ("this is worth noting",
  "keep an eye on this", "signals indicated") catch the pattern. The portability test is
  a necessary precision mechanism: content that could be moved to a different echo unchanged
  is generic by definition.

- **C-17 (from V-01/R3 artifact-level new-reader framing)**: C-09 (transferable framing)
  is an artifact-level property. V-01 showed that artifact readability and per-entry
  independence are structurally distinct. An artifact can read well end-to-end while
  individual entries depend on the introduction or on each other. C-17 requires the
  constraint to operate at entry scope, not artifact scope.

**R4 structural goal:** Three single-axis variations (V-01, V-02, V-03) isolate one new
criterion per variation. Two combined variations (V-04, V-05) test pairwise and full-set
interaction. All five maintain C-01 through C-14 without degradation.

**Variation axes selected:**

1. **Phrasing register** — how the divergence test (C-15) is expressed: imperative binary
   gate embedded in the schema field vs. rule statement vs. descriptive aspiration.
2. **Lifecycle emphasis** — when the portability test (C-16) fires: discrete named audit
   phase after all entries are drafted vs. inline annotation vs. post-hoc review rule.
3. **Output format** — structural enforcement of per-entry self-containedness (C-17):
   mandatory CONTEXT BLOCK within each entry schema vs. framing rule vs. authoring advice.

**Predicted score map (v4 rubric, max 135):**

| Variant | C-15 | C-16 | C-17 | Predicted |
|---------|------|------|------|-----------|
| V-01    | PASS | FAIL | FAIL | 115       |
| V-02    | FAIL | PASS | FAIL | 115       |
| V-03    | FAIL | FAIL | PASS | 115       |
| V-04    | PASS | PASS | FAIL | 125       |
| V-05    | PASS | PASS | PASS | 135       |

Scoring note: All essential (C-01–C-05, 50 pts) and recommended (C-06–C-08, 30 pts) must
pass in every variation. Aspirational (C-09–C-14, 30 pts) must pass in every variation —
these are proven from R3. New criteria C-15/C-16/C-17 (5 pts each) are unproven; the
predicted map reflects single/combination axis activation, not score floor adjustment.
The 115 predictions assume C-09–C-14 pass uniformly; each new criterion adds 5 pts.

---

## V-01 — Single-axis: Phrasing register — Imperative divergence gate in Expected field

**Axis:** The Expected field in the schema is redesigned as a two-part structure: (1) the
prior belief statement, (2) an inline DIVERGE? gate written as imperative binary syntax.
The gate executes at write time — the author cannot draft the entry without answering
YES or NO. A NO answer triggers a mandatory discard-or-rewrite instruction. This converts
the divergence test from a rubric property to a schema enforcement point.

**Hypothesis:** Embedding the gate inside the field definition — rather than as a separate
rule, step, or post-hoc review — fires the test at the moment the assumption is written,
before the finding is stated. An author who writes a congruent pair encounters the gate
immediately and cannot advance without resolving it. This predicts lower congruent-pair
rates than C-13-only prompts because the failure mode is caught at draft time, not at
evaluation time. C-16 is not structurally enforced in this variation (generic field content
can still pass through). C-17 is not structurally enforced (no per-entry CONTEXT BLOCK).

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something that
could not have been written before the signals were gathered.

== SCHEMA =====================================================================

Apply to every surprise. All fields required. No field may be blank or N/A.

  Name:            [memorable label specific to the content — e.g., "The Adoption Inversion",
                   "The Silent Veto Problem". Not "Finding 1", "Surprise A", or any generic
                   header.]

  Source:          [namespace:skill:artifact — e.g., listen:adoption:signal-adoption-2026-03-14.md.
                   Not "signals indicated", "research showed", or "the data suggested".]

  Expected:        [State the team's prior belief as a direct, confident claim — the assumption
                   held before any signals were run. Then execute the divergence test:

                   DIVERGE?
                     Claim the direction of the assumption: [up/down/high/low/user-driven/
                     system-driven — or equivalent for this domain].
                     Claim the direction of the finding: [same vocabulary].
                     Does the finding oppose the assumption in direction, mechanism, or actor?
                       YES → This is a genuine overthrow. Proceed.
                       NO  → This pair records a difference of degree, not a genuine surprise.
                             A smaller-than-expected X is not an inversion of X. Either:
                             (a) identify the assumption that the finding truly inverts and
                                 rewrite this field, or
                             (b) discard this entry — it is a confirmation dressed as a surprise.
                   Only proceed to the Finding field if DIVERGE? = YES.]

  Finding:         [The surprise — stated as a direct claim. No hedges. Prohibited everywhere:
                   "may suggest" / "appears to indicate" / "seems like" / "could mean" /
                   "might be" / "it is possible that" / "could indicate". Uncertainty is a
                   rewrite instruction, not a qualifier.]

  Design impact:   [How this changes, challenges, or forces a decision on the design direction.
                   One sentence minimum. Prohibited: "this is worth noting", "bears watching",
                   "important to keep in mind". Name the specific design consequence.]

  Next move:       [One specific action or open question the next team must resolve. Prohibited:
                   "further investigation needed", "keep an eye on this", "monitor this".]

  Severity:        [HIGH / MEDIUM / LOW — relative to impact on design direction]

== RULES ======================================================================

Rule 1 — Counterfactual filter:
  Before writing any surprise, ask: "Could a passive, attentive team have found this
  through normal observation of the feature, without running active signals?" If yes,
  exclude it. Echo scope is active-signal discoveries only. Apply this as a discard
  filter, not an annotation.

Rule 2 — Claim-only voice:
  State every finding as a direct claim. The eight prohibited constructs above (Finding
  field) apply to every field in every entry. No hedging anywhere in the artifact.

Rule 3 — Entry readability:
  Write each entry so that a new team member reading only that entry — without the
  introduction, without other entries, without any source artifact — can understand
  what was expected, what was found, and why it matters for the design. Define domain
  terms on first use within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one surprise must emerge from the intersection of two or more signals. For that
entry, the Source field names both sources. After the Finding field, add one sentence:

  "Neither [source A] nor [source B] alone revealed this — together they produced [Y],
  which neither would have surfaced independently."

Co-citation without a named convergence delta fails this requirement.

== SEVERITY ORDERING ==========================================================

Order all entries HIGH → MEDIUM → LOW by Severity field value. Unordered lists fail.

== META-REFLECTION ============================================================

After all entries, one section: "What the surprise distribution reveals."

Answer two questions with direct claims:
  1. In which namespace, skill, or phase did surprises concentrate?
  2. For topics structured like this one, what gathering sequence adjustment does this
     concentration prescribe? Not observation only — prescribe: "For topics like this,
     run [X] before [Y] to surface [Z class of surprise] earlier."

== SCOPE NEGATION =============================================================

Final section: "What this artifact excludes."

Name at least two categories of content that were encountered and deliberately omitted —
for example: "Expected outcomes — [N] items confirmed prior assumptions and were excluded",
"Status confirmations — [N] items reported known state and were excluded". The categories
and counts must be stated. Implicit exclusion (simply not including non-surprises) does
not satisfy this requirement.

== OUTPUT =====================================================================

Structure:
  1. Surprises — ordered HIGH → MEDIUM → LOW
  2. What the surprise distribution reveals
  3. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-02 — Single-axis: Lifecycle emphasis — PORTABILITY AUDIT as discrete named phase

**Axis:** The portability test (C-16) is moved from an inline field annotation or rule
statement to a mandatory named phase executed after all entries are drafted and before
the meta-reflection is written. The PORTABILITY AUDIT is a discrete step in the output
lifecycle, not an authoring reminder. It names specific anti-patterns, provides a binary
pass/fail gate per field, and blocks advancement to the meta-reflection until all fields
are cleared. An author who drifts into generic language during drafting still encounters
the audit as a structural barrier.

**Hypothesis:** A lifecycle-phase gate fires after drafting, catching generic field content
that was written under cognitive load without triggering at every field boundary. This is
structurally different from field-level annotations (which require active recall during
drafting) and post-hoc reviewer guidance (which has no structural enforcement surface).
The prediction is that authors who drift into generic language mid-draft will rewrite
before writing the file, because the audit presents a checklist they must clear rather
than guidance they may observe. C-15 is not structurally enforced (divergence test is a
rule statement, not a gate). C-17 is not structurally enforced (no per-entry CONTEXT BLOCK).

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something that
could not have been written before the signals were gathered.

== SCHEMA =====================================================================

Apply to every surprise. All fields required.

  Name:            [memorable label specific to this finding]
  Source:          [namespace:skill:artifact path — specific artifact, not vague attribution]
  Expected:        [the team's prior belief before signals — stated as a direct confident claim.
                   Must state an assumption the finding contradicts, not merely falls short of.
                   "We expected high adoption; adoption was moderate" records a degree difference.
                   Name the assumption that the finding factually overturns.]
  Finding:         [the surprise — direct claim, no hedges]
  Design impact:   [how this changes or challenges the design direction — one sentence minimum]
  Next move:       [specific action or open question the next team must resolve]
  Severity:        [HIGH / MEDIUM / LOW]

== RULES ======================================================================

Rule 1 — Counterfactual filter:
  Before drafting any surprise: "Could a passive, attentive team have found this through
  normal observation without running signals?" If yes, exclude it. Active-signal scope only.

Rule 2 — Claim-only voice:
  No hedges. Prohibited: "may suggest" / "appears to indicate" / "seems like" / "could mean" /
  "might be" / "it is possible that". Delete the hedge. State the claim directly.

Rule 3 — Entry readability:
  Write each entry so that a new team member reading only that entry can understand what was
  expected, what was found, and why it matters. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one surprise must emerge from two or more signals. Source field names both sources.
Name the convergence delta: "Neither [A] nor [B] alone showed this — together they revealed
[Y], which neither source would have produced independently."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all surprise entries using the schema above. Order: HIGH → MEDIUM → LOW by Severity.
Do not write the meta-reflection or scope negation sections yet.

== PHASE 2: PORTABILITY AUDIT =================================================

Before writing the meta-reflection, execute this audit against every entry in sequence.
The audit does not modify the structure — it catches and replaces generic field content.

For each entry, apply the portability test to every non-Name field:

  Portability test: "Could this exact text appear unchanged in an echo about a different
  topic, for a different surprise?" If YES, the field fails. Rewrite it.

Named failure patterns — any match in any field is an automatic rewrite:

  Source field:      "signals indicated" / "research showed" / "the data suggested" /
                     "findings revealed" — these are vague attribution, not source traces.
                     Replace with: namespace:skill:artifact.

  Design impact:     "this is worth noting" / "important to keep in mind" / "bears watching" /
                     "merits attention" / "has implications" — these name no design consequence.
                     Replace with: the specific decision, constraint, or redesign forced by
                     this finding.

  Next move:         "further investigation needed" / "keep an eye on this" / "monitor this" /
                     "investigate further" — these name no specific action.
                     Replace with: the specific next team action or the open question that
                     blocks design progress.

The portability test applies to all non-Name fields. A field passes the audit when its
content is specific enough that moving it to a different surprise about a different topic
would require rewriting it. Generic content that survives a topic swap fails.

Complete the PORTABILITY AUDIT for all entries before proceeding to Phase 3.

== PHASE 3: META-REFLECTION ===================================================

One section: "What the surprise distribution reveals."

Where did surprises concentrate (namespace, phase, signal type)? What does that
concentration prescribe for future signal-gathering on this topic type? Prescribe,
do not only observe: "For topics like this one, run [X] before [Y] to surface [Z
class of surprise] earlier."

== PHASE 4: SCOPE NEGATION ====================================================

One section: "What this artifact excludes."

Name at least two categories of excluded content with counts or examples:
  e.g., "Expected outcomes: [N] items confirmed prior assumptions and were excluded"
       "Status updates: excluded as non-informative to future teams"
Making exclusion legible is not the same as simply not including expected findings.

== OUTPUT =====================================================================

Structure (in order):
  1. Surprises — post-portability-audit, ordered HIGH → MEDIUM → LOW
  2. What the surprise distribution reveals
  3. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-03 — Single-axis: Output format — Per-entry CONTEXT BLOCK enforces C-17

**Axis:** Each entry in the output uses a mandatory two-block format: a CONTEXT BLOCK
and a FINDING BLOCK. The CONTEXT BLOCK is a structural schema component, not a framing
guideline — it appears before the finding fields within each entry and contains three
required fields: topic scope sentence, domain term definitions, and signal context.
This makes per-entry self-containedness a format property: an entry without a completed
CONTEXT BLOCK is structurally incomplete regardless of finding quality.

**Hypothesis:** Artifact-level new-reader framing (C-09) can be achieved by a strong
introduction section that provides context for all subsequent entries. This satisfies
C-09 but enables C-17 failures: entries written after an introduction can assume the
reader has read it. The CONTEXT BLOCK requirement removes that assumption structurally —
each entry carries its own context, and an evaluator testing C-17 by reading a single
entry out of order finds what they need within the entry itself. C-15 is present as a
rule statement but not a gate. C-16 is present as field-level annotation but not a phase.

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something that
could not have been written before the signals were gathered.

== SCHEMA =====================================================================

Each surprise uses a two-block structure. Both blocks are required for every entry.
A surprise with an incomplete CONTEXT BLOCK is structurally incomplete.

-- CONTEXT BLOCK (required per entry) -----------------------------------------

  Topic scope:     [One sentence stating what feature, system, or decision this surprise
                   concerns — written for a reader who has not read any other part of this
                   artifact. Do not reference prior entries or assume shared context.]

  Domain terms:    [Define every term used in this entry that is not plain English, using
                   the form "As used here, [term] means [definition]." If the entry uses
                   no domain-specific terms, write "No domain terms used in this entry."
                   Omitting this field when terms are present fails C-17.]

  Signal context:  [One sentence: "This surprise surfaced while running [skill] against
                   [namespace] signals for topic [X] on [date]." Specific enough that a
                   reader unfamiliar with the signal-gathering process can locate the source.]

-- FINDING BLOCK (required per entry) -----------------------------------------

  Name:            [memorable label specific to this finding — not "Finding 1"]
  Source:          [namespace:skill:artifact — specific, not "signals indicated"]
  Expected:        [the team's prior belief — a direct claim stating the assumption the
                   finding contradicts. Must oppose in direction, mechanism, or actor —
                   not merely differ in degree. "Expected high X; X was moderate" is a
                   degree difference, not a genuine overthrow.]
  Finding:         [the surprise — direct claim, no hedges]
  Design impact:   [specific design consequence — one sentence minimum]
  Next move:       [specific action or open question — not "further investigation needed"]
  Severity:        [HIGH / MEDIUM / LOW]

== RULES ======================================================================

Rule 1 — Counterfactual filter:
  Before drafting any surprise: "Could a passive, attentive team have found this through
  normal observation?" If yes, exclude it.

Rule 2 — Claim-only voice:
  No hedges. Prohibited: "may suggest" / "appears to indicate" / "seems like" / "could mean" /
  "might be" / "it is possible that". State every finding as a direct claim.

Rule 3 — Entry isolation test:
  After completing each entry, read the FINDING BLOCK in isolation — without the CONTEXT
  BLOCK, without the introduction, without other entries. Does the finding make sense?
  Is its significance evaluable without context from elsewhere in the artifact?
    YES → proceed.
    NO  → the CONTEXT BLOCK is incomplete. Add what is missing there, not in the finding.
  The CONTEXT BLOCK is the designated context container. Findings must not carry context
  inline — context belongs in the CONTEXT BLOCK so entries are structurally separable.

Rule 4 — Generic field prohibition:
  Prohibited in any field: "this is worth noting" (impact), "keep an eye on this" (next
  move), "further investigation needed" (next move), "signals indicated" / "research
  showed" (source). These populate fields while delivering no institutional value.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one surprise must emerge from two or more signals. Source field names both.
Name the convergence delta: "Neither [A] nor [B] alone surfaced this — their intersection
revealed [Y], which neither would have produced independently."

== SEVERITY ORDERING ==========================================================

Order all entries HIGH → MEDIUM → LOW. Unordered lists fail.

== META-REFLECTION ============================================================

After all entries: "What the surprise distribution reveals."

Where did surprises concentrate? Prescribe: "For topics like this one, run [X] before
[Y] to surface [Z] earlier." Not observation only — include a forward gathering adjustment.

== SCOPE NEGATION =============================================================

"What this artifact excludes."

Name at least two excluded categories with counts or examples. State the exclusion
explicitly — implicit exclusion (simply not including expected findings) does not satisfy
this requirement.

== OUTPUT =====================================================================

Structure:
  1. Surprises — each with complete CONTEXT BLOCK + FINDING BLOCK, ordered HIGH → MEDIUM → LOW
  2. What the surprise distribution reveals
  3. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-04 — Combined: Phrasing register + Lifecycle emphasis (C-15 + C-16)

**Axes combined:** V-01's DIVERGE? gate in the Expected field + V-02's PORTABILITY AUDIT
as discrete Phase 2.

**Hypothesis:** The two mechanisms address orthogonal failure modes at non-overlapping
execution points. DIVERGE? fires during entry drafting — it intercepts congruent pairs
before the finding field is written. PORTABILITY AUDIT fires after all entries are drafted
— it intercepts generic content that accumulated across the drafting session. Together they
provide sequential coverage: DIVERGE? prevents C-13 form-filling from the start; PORTABILITY
AUDIT prevents C-02/C-03/C-07 form-filling before the artifact is written to disk. No
interaction surface exists between them — a YES answer from DIVERGE? does not influence
whether a field passes the portability test. C-17 is present as Rule 3 (entry readability
guidance) but is not structurally enforced by a per-entry CONTEXT BLOCK.

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something that
could not have been written before the signals were gathered.

== SCHEMA =====================================================================

Apply to every surprise. All fields required. No field may be blank or N/A.

  Name:            [memorable label specific to this finding — not "Finding 1" or "Surprise A"]

  Source:          [namespace:skill:artifact — e.g., scout:feasibility:signal-feasibility-2026-03-14.md.
                   Not "signals indicated", "research showed", or "the data suggested".]

  Expected:        [State the team's prior belief as a direct, confident claim. Then:

                   DIVERGE?
                     Direction of assumption: [e.g., "adoption would be high",
                     "resistance would come from end users", "X would be the primary bottleneck"]
                     Direction of finding: [same vocabulary, opposite or orthogonal]
                     Does the finding oppose the assumption in direction, mechanism, or actor?
                       YES → genuine overthrow. Proceed.
                       NO  → degree difference only. Either rewrite the Expected field to name
                             the assumption the finding truly inverts, or discard this entry.]

  Finding:         [direct claim, no hedges. Prohibited: "may suggest" / "appears to indicate" /
                   "seems like" / "could mean" / "might be" / "it is possible that"]

  Design impact:   [specific design consequence — one sentence minimum. Prohibited: "this is
                   worth noting" / "bears watching" / "important to keep in mind"]

  Next move:       [specific action or open question. Prohibited: "further investigation needed" /
                   "keep an eye on this" / "monitor this"]

  Severity:        [HIGH / MEDIUM / LOW]

== RULES ======================================================================

Rule 1 — Counterfactual filter:
  Before drafting any surprise: "Could a passive, attentive team have found this through
  normal observation?" If yes, exclude it.

Rule 2 — Claim-only voice:
  No hedges anywhere in the artifact. Prohibited constructs listed in the Finding field
  above apply to every field.

Rule 3 — Entry readability:
  Write each entry so that a new team member reading only that entry can understand what
  was expected, what was found, and why it matters. Define domain terms within each entry.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one surprise must emerge from two or more signals. Source field names both.
Name the convergence delta: "Neither [A] nor [B] alone revealed this — together they
produced [Y], which neither would have surfaced independently."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries using the schema above. Order: HIGH → MEDIUM → LOW by Severity.
Do not write the meta-reflection or scope negation yet.

== PHASE 2: PORTABILITY AUDIT =================================================

Before writing the meta-reflection, execute this audit against every entry.

Portability test (apply to every non-Name field in every entry):
  "Could this exact text appear unchanged in an echo about a different topic?"
  If YES, rewrite it.

Named failure patterns — automatic rewrite triggers:

  Source field:      "signals indicated" / "research showed" / "the data suggested" /
                     "findings revealed"
                     → Replace with: namespace:skill:artifact

  Design impact:     "this is worth noting" / "important to keep in mind" / "bears watching" /
                     "merits attention" / "has implications"
                     → Replace with: the specific design decision, constraint, or change
                       this finding forces

  Next move:         "further investigation needed" / "keep an eye on this" / "monitor this" /
                     "investigate further"
                     → Replace with: the specific action or blocking open question

  Expected field:    Also verify DIVERGE? was answered YES for each entry. If any entry
                     passed DIVERGE? with a NO that was not discarded or rewritten,
                     correct it now.

Clear the PORTABILITY AUDIT for all entries before proceeding.

== PHASE 3: META-REFLECTION ===================================================

"What the surprise distribution reveals."

Where did surprises concentrate? Prescribe (do not only observe): "For topics like this
one, run [X] before [Y] to surface [Z class of surprise] earlier."

== PHASE 4: SCOPE NEGATION ====================================================

"What this artifact excludes."

Name at least two excluded categories with counts or examples. Implicit exclusion does
not satisfy this requirement.

== OUTPUT =====================================================================

Structure:
  1. Surprises — post-portability-audit, ordered HIGH → MEDIUM → LOW
  2. What the surprise distribution reveals
  3. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## V-05 — Combined: All three axes (C-15 + C-16 + C-17)

**Axes combined:** V-01's DIVERGE? gate + V-02's PORTABILITY AUDIT phase + V-03's
per-entry CONTEXT BLOCK.

**Hypothesis:** Three mechanisms at three distinct scopes: (1) DIVERGE? operates within
a single field at draft time — entry scope, drafting phase; (2) CONTEXT BLOCK operates
across the entry structure at draft time — entry scope, structural layer; (3) PORTABILITY
AUDIT operates across all entries after drafting — artifact scope, post-draft phase. No
mechanism occupies the same scope + phase as another. The prediction is full C-15/C-16/C-17
coverage with no interaction friction: DIVERGE? fires before the CONTEXT BLOCK is
considered; the CONTEXT BLOCK is part of the schema that PORTABILITY AUDIT reviews;
the PORTABILITY AUDIT includes a context-appropriateness check for CONTEXT BLOCK fields
that would not have existed without V-03's structural addition. The compound variation
does not require any mechanism to do double duty — each addresses exactly one failure mode.

```
Topic: $ARGUMENTS

Synthesize what was unexpected. This is not a summary. Every item must be something that
could not have been written before the signals were gathered.

== SCHEMA =====================================================================

Each surprise uses a two-block structure. Both blocks required. A surprise with an
incomplete CONTEXT BLOCK is structurally incomplete regardless of finding quality.

-- CONTEXT BLOCK (required per entry) -----------------------------------------

  Topic scope:     [One sentence stating what feature, system, or decision this surprise
                   concerns — written for a reader who has not read any other part of this
                   artifact and has no prior context on this topic. Do not reference prior
                   entries.]

  Domain terms:    [Define every domain-specific term used in this entry: "As used here,
                   [term] means [definition]." If no domain terms appear in this entry,
                   write "No domain terms used in this entry." Do not omit this field.]

  Signal context:  [One sentence: "This surprise emerged while running [skill] against
                   [namespace] signals for topic [X] on [date]." Specific enough that a
                   reader unfamiliar with the signal-gathering process can locate the source.]

-- FINDING BLOCK (required per entry) -----------------------------------------

  Name:            [memorable label specific to this finding — not "Finding 1"]

  Source:          [namespace:skill:artifact — e.g., prove:interview:signal-interview-2026-03-14.md.
                   Not "signals indicated" / "research showed" / "the data suggested".]

  Expected:        [State the team's prior belief as a direct, confident claim. Then:

                   DIVERGE?
                     Direction of assumption: [e.g., "resistance would come from end users",
                     "adoption would scale with feature availability", "X would block Y"]
                     Direction of finding: [same vocabulary — must oppose in direction,
                     mechanism, or actor, not merely differ in degree]
                     Does the finding oppose the assumption in direction, mechanism, or actor?
                       YES → genuine overthrow. Proceed.
                       NO  → degree difference only. Either identify the assumption the
                             finding truly inverts and rewrite, or discard this entry.]

  Finding:         [direct claim, no hedges. Prohibited: "may suggest" / "appears to
                   indicate" / "seems like" / "could mean" / "might be" / "it is possible
                   that". Uncertainty is a rewrite instruction, not a qualifier.]

  Design impact:   [specific design consequence — one sentence minimum. Prohibited:
                   "this is worth noting" / "bears watching" / "important to keep in mind"]

  Next move:       [specific action or open question. Prohibited: "further investigation
                   needed" / "keep an eye on this" / "monitor this"]

  Severity:        [HIGH / MEDIUM / LOW]

== RULES ======================================================================

Rule 1 — Counterfactual filter:
  Before drafting any surprise: "Could a passive, attentive team have found this through
  normal observation?" If yes, exclude it.

Rule 2 — Claim-only voice:
  No hedges. Prohibited constructs listed in the Finding field apply to every field.

Rule 3 — Entry isolation test:
  After completing each entry, read the FINDING BLOCK alone — without the CONTEXT BLOCK,
  without the introduction, without other entries. Does the finding make sense in isolation?
  Is its significance evaluable without context from elsewhere?
    YES → proceed.
    NO  → the CONTEXT BLOCK is incomplete. Add the missing context there, not in the finding.
  The CONTEXT BLOCK is the designated context container. Findings carry claims, not context.

== CROSS-SIGNAL REQUIREMENT ===================================================

At least one surprise must emerge from two or more signals. Source field names both.
Name the convergence delta: "Neither [A] nor [B] alone surfaced this — their intersection
produced [Y], which neither would have revealed independently."

== PHASE 1: DRAFT ALL ENTRIES =================================================

Write all entries using the schema above. For each entry, complete the CONTEXT BLOCK
before the FINDING BLOCK — context declared before claims. Order entries HIGH → MEDIUM → LOW
by Severity. Do not write the meta-reflection or scope negation yet.

== PHASE 2: PORTABILITY AUDIT =================================================

Before writing the meta-reflection, execute this audit against every entry.

Portability test (apply to every non-Name field in every block):
  "Could this exact text appear unchanged in an echo about a different topic?"
  If YES, rewrite it.

Named failure patterns — automatic rewrite triggers:

  Signal context (CONTEXT BLOCK):
                     "signals were gathered" / "signal-gathering was performed" — these
                     name no specific skill, namespace, or date. Replace with specifics.

  Source field:      "signals indicated" / "research showed" / "the data suggested" /
                     "findings revealed" → Replace with: namespace:skill:artifact

  Design impact:     "this is worth noting" / "important to keep in mind" / "bears watching" /
                     "merits attention" / "has implications"
                     → Replace with: the specific design decision or constraint this forces

  Next move:         "further investigation needed" / "keep an eye on this" / "monitor this"
                     → Replace with: the specific action or blocking open question

  Expected field:    Verify DIVERGE? was answered YES for each entry. Any entry with an
                     unanswered or NO-answered DIVERGE? that was not discarded: correct now.

Clear the PORTABILITY AUDIT for all entries before proceeding.

== PHASE 3: META-REFLECTION ===================================================

"What the surprise distribution reveals."

Where did surprises concentrate (namespace, skill, phase)? What gathering-sequence
adjustment does this concentration prescribe? Prescribe: "For topics like this one,
run [X] before [Y] to surface [Z class of surprise] earlier." Not observation only.

== PHASE 4: SCOPE NEGATION ====================================================

"What this artifact excludes."

Name at least two excluded categories with counts or examples. Stating the exclusion
explicitly is not the same as simply not including expected findings.

== OUTPUT =====================================================================

Structure:
  1. Surprises — each with complete CONTEXT BLOCK + FINDING BLOCK (CONTEXT first),
     ordered HIGH → MEDIUM → LOW
  2. What the surprise distribution reveals
  3. What this artifact excludes

Write to: simulations/topic/echo/$ARGUMENTS-echo-{YYYY-MM-DD}.md
```

---

## Round 4 Design Notes

**Why these three axes:**

- **Phrasing register** targets C-15 because the failure mode is authorial, not structural:
  authors know the expectation field exists (C-13 is proven) but write congruent pairs
  because nothing stops them at write time. The DIVERGE? gate is a register choice —
  binary, imperative, blocking — that converts awareness into enforcement.

- **Lifecycle emphasis** targets C-16 because portability failures accumulate during
  drafting (cognitive load, formula writing) and are invisible at the field level. A phase
  gate after drafting is complete creates a full-artifact review moment that inline
  annotations cannot reliably produce.

- **Output format** targets C-17 because C-09 (artifact-level readability) can be
  satisfied by an introduction section that provides context for all entries. The CONTEXT
  BLOCK eliminates this loophole structurally — context must be present per-entry, not
  aggregated in a preamble.

**Predicted interaction in V-05:**

The three mechanisms share no execution scope: DIVERGE? runs within the Expected field
during drafting; CONTEXT BLOCK is a schema layer added to every entry before the finding;
PORTABILITY AUDIT runs across all entries after drafting. V-04 tests that DIVERGE? and
PORTABILITY AUDIT are additive. V-05 adds CONTEXT BLOCK and tests that all three coexist
without the portability audit flagging context-block fields that are legitimately
entry-specific (e.g., a Signal context field that names the same skill across multiple
entries is not generic — it is correctly specific to each entry's source).
