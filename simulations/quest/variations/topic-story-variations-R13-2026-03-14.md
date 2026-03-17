# /quest:variate — topic-story — Round 13

**Skill**: topic-story
**Rubric**: v13
**New criteria targeted**: C-43 (dual-anchored entry conditions), C-44 (table-forward S2)
**Variation axes selected**: Role sequence (V-01), Output format (V-02), Lifecycle emphasis (V-03), Role sequence + Output format combined (V-04), Phrasing register + Inertia framing combined (V-05)

---

## V-01 — Role Sequence

**Variation axis**: Role sequence — three named roles (Cartographer → Synthesizer → Editor) with explicit entry conditions per role that name both the prior role's step completion and the prior section's inventory row status.

**Hypothesis**: When the protocol assigns distinct named roles to distinct stages, each role's entry condition naturally names both what the prior role *did* (process anchor) and what the inventory row *contains* (data anchor). C-43 dual-anchoring becomes a structural byproduct of role hand-offs rather than an explicit rubric target.

---

```
You are running /topic:story for topic: {{TOPIC}}

You will play three roles in strict sequence. Each role has an entry condition.
Do not begin a role until its entry condition is satisfied.
Record each section's output before advancing.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE 1: CARTOGRAPHER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: No prior role has run. Begin immediately.

Task: Locate every signal artifact for {{TOPIC}} under simulations/.
File pattern: {{TOPIC}}-*-*.md
Namespaces to check: scout, draft, review, flow, trace, prove, listen, program, topic

For each artifact located, record one row in S1. Do not read artifact content yet.

S1 — Signal Inventory

| Signal ID | Namespace | Skill | Date | Path | Status |
|-----------|-----------|-------|------|------|--------|
| (fill) | (fill) | (fill) | (fill) | (fill) | complete / partial / missing |

S1 exit condition: Every located artifact has a row. Status field is non-empty.
No artifact may be omitted. If a namespace has no artifacts for {{TOPIC}}, note that
in a single line below the table: "No artifacts: {namespace list}"

Cartographer step S1 complete when: table is written and all namespaces checked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE 2: SYNTHESIZER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Signal inventory axis, S1 row — all fields complete; AND
Cartographer step S1 completed — all signal artifacts located and catalogued.

Task A — S2 Signal Survey (data-collection section)

Open S2 with the table below. Do not write any text before the table.

S2 — Signal Survey

| Signal ID | Key Finding | Confidence | Signal Weight | Gaps |
|-----------|-------------|------------|---------------|------|
| (one row per S1 artifact) | one sentence | high / med / low | high / med / low | (or —) |

Column definitions:
- Key Finding: the single most important thing this artifact establishes.
  One sentence. No subordinate clauses.
- Confidence: how well-supported is the finding within the artifact itself.
- Signal Weight: how much this finding should move the recommendation.
- Gaps: what the signal does not cover that it was positioned to cover.

After the table: for each complete/partial artifact, write one paragraph
(2–4 sentences) elaborating on the key finding. Do not introduce new information
in the narrative that belongs in the table. The table is the canonical record.

S2 exit condition: All S1 artifacts have a row. Key Finding non-empty for
all complete artifacts. Partial artifacts have a note in Gaps.

Task B — S3 Pattern Synthesis

Entry condition: Signal survey axis, S2 row — all key findings recorded and
weights assigned; AND Synthesizer step S2 completed — all complete/partial
artifacts read and findings tabulated.

Write what the signals say together — not what each signal says individually.
Name the pattern. Describe what it predicts about {{TOPIC}}'s trajectory.
Do not list; synthesize. Length: 2–4 paragraphs, author's voice, first person plural.

S3 exit condition: Pattern statement is present. Does not restate S2 findings
in sequence. Makes a cross-signal claim.

Synthesizer step complete when: S2 table written, per-signal elaboration written,
S3 pattern written.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE 3: EDITOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Pattern synthesis axis, S3 row — pattern statement recorded; AND
Synthesizer step S3 completed — cross-signal pattern identified and written.

Task — S4 Uncertainty and Recommendation

S4a — What Remains Uncertain

Name what the signals do not resolve. Write as a numbered list.
For each item:
  1. State the unresolved question.
  2. Name the signal type or namespace that is absent or thin.
  3. Describe what a definitive signal for this question would look like.

Minimum 2 items. Maximum 5.

S4b — Recommendation

Choose exactly one: proceed / pause / pivot / abandon.

Write three paragraphs:
  Para 1: The recommendation and the single strongest signal pattern supporting it.
  Para 2: The strongest reason a reasonable team would resist this recommendation.
  Para 3: The decision trigger that would change the recommendation —
           name the specific signal, threshold, or event.

Do not hedge to two choices. Do not qualify with "it depends."
The synthesis commits.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT ARTIFACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write to: simulations/topic/story/{{TOPIC}}-story-{{DATE}}.md

Section order: S1 → S2 (table first) → S3 → S4a → S4b
Voice: editorial, first person plural. This is a decision document, not a report.
```

---

## V-02 — Output Format

**Variation axis**: Output format — table-forward S2 with a column schema derived from signal type taxonomy, making the inventory row structurally self-auditing.

**Hypothesis**: A richer S2 column schema (signal type + evidence class + weight) makes the table itself do the audit work: evidence class imbalances appear as column skews, coverage gaps appear as missing rows, and the narrative that follows annotates rather than contains the data. C-44 is the load-bearing structure, not an add-on.

---

```
You are running /topic:story for topic: {{TOPIC}}

This skill produces an editorial synthesis in four sections.
Sections S1 and S2 are data-collection sections: they lead with a table.
Sections S3 and S4 are editorial sections: they lead with prose.
Table placement is non-negotiable — no text may precede the table in S1 or S2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S1 — SIGNAL INVENTORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Locate all signal artifacts for {{TOPIC}} in simulations/.
Build the table before reading any artifact content.

| # | Signal ID | Namespace | Skill | Date | Status |
|---|-----------|-----------|-------|------|--------|
| | | | | | complete / partial / missing |

No prose in S1. The table is the section.
S1 exit condition: every located artifact is a row.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S2 — SIGNAL SURVEY (data-collection section)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Signal inventory axis, S1 row — all fields complete; AND
S1 signal-location step completed — all artifact paths confirmed and recorded.

Open S2 with the survey table. No text before the table.

S2 Survey Table

| Signal ID | Signal Type | Evidence Class | Key Finding | Weight | Completeness |
|-----------|-------------|----------------|-------------|--------|--------------|

Column definitions:

Signal Type (pick one):
  market     — competitive landscape, TAM, positioning, naming signals
  technical  — feasibility, architecture, performance, code-level signals
  user       — adoption, support, feedback, interview signals
  design     — spec, proposal, review signals
  flow       — lifecycle, trigger, throttle, resilience, conversation signals
  hypothesis — investigate, analysis, synthesis, websearch signals
  program    — plan, roadmap, stakeholder signals

Evidence Class (pick one):
  primary   — artifact produced by a skill run in this topic's corpus
  secondary — artifact references external source or prior topic
  inferred  — analyst judgment applied to incomplete artifact

Key Finding: one sentence. No subordinate clauses. What this artifact establishes.

Weight: high / medium / low — how much this signal should shift the recommendation.

Completeness: complete / partial / missing
  If partial or missing: add a Notes row directly below (single indented line).

After the table: one paragraph per signal (2–4 sentences) annotating the key finding.
The paragraph adds context; it does not replace the table row.
A reviewer auditing completeness should need only the table, not the narrative.

S2 exit condition: All S1 signals have a row. Key Finding non-empty for all
non-missing signals. Signal Type and Evidence Class populated for all rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S3 — PATTERN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Signal survey axis, S2 row — all key findings recorded and
weights assigned; AND S2 signal-survey step completed — all artifacts read
and tabulated.

Prose section. Lead with the pattern claim. Do not open with a table.

Write what the signals say together. Look for:
  - Convergences: two or more signal types pointing the same direction
  - Tensions: high-weight signals in conflict
  - Absences: signal types missing that would normally be present at this stage

Name the pattern. Describe the signal dynamic it represents. Predict what this
pattern implies about {{TOPIC}}'s trajectory if no new signals arrive.

Length: 3 paragraphs minimum. Author's voice. First person plural.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S4 — UNCERTAINTY AND RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Pattern synthesis axis, S3 row — pattern statement recorded; AND
S3 pattern-synthesis step completed — cross-signal interpretation written.

S4a — What Remains Uncertain

Numbered list. For each item:
  - The unresolved question
  - The signal type absent or thin (reference the Signal Type taxonomy above)
  - What a definitive signal would look like

2–5 items.

S4b — Recommendation

State: proceed / pause / pivot / abandon.

One paragraph: the recommendation and its primary signal support.
One paragraph: the strongest objection and how the current signals address or fail to address it.
One paragraph: the reversal condition — what specific signal event or threshold would
change this recommendation, and to which of the four options.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT ARTIFACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write to: simulations/topic/story/{{TOPIC}}-story-{{DATE}}.md
Section order: S1 → S2 → S3 → S4a → S4b
S1 and S2 lead with tables. S3 and S4 lead with prose.
```

---

## V-03 — Lifecycle Emphasis

**Variation axis**: Lifecycle emphasis — explicit paragraph-budget directives for each section, with equal weight between pattern (S3) and uncertainty (S4a), and a named prohibition on section asymmetry.

**Hypothesis**: When S3 and S4a carry the same paragraph budget, the synthesis cannot collapse into a list of findings followed by a thin uncertainty acknowledgment. The pattern section must work harder (no padding from signal summaries) and the uncertainty section must be substantive (no single-line hedge). The recommendation that follows both is more honest.

---

```
You are running /topic:story for topic: {{TOPIC}}

## Signal Story — Balance Protocol

This skill synthesizes signals into an editorial narrative.
The synthesis has four sections with explicit length contracts.
Section length contracts are binding — do not exceed or fall short of the range.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S1 — SIGNAL INVENTORY [no length contract — table only]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Locate all signal artifacts for {{TOPIC}} in simulations/.
Record in the S1 table. No prose.

| Signal ID | Namespace | Skill | Date | Status |
|-----------|-----------|-------|------|--------|

S1 exit condition: all located artifacts are rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S2 — SIGNAL SURVEY [length contract: 1 table row + 1 paragraph per signal]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Signal inventory axis, S1 row — all fields complete; AND
S1 signal-location step completed — all artifact paths confirmed and recorded.

Lead with the S2 table. One row per S1 artifact.

| Signal ID | Key Finding | Confidence | Weight |
|-----------|-------------|------------|--------|

After the table: one paragraph per signal (exactly 2–3 sentences).
The paragraph explains the finding. It does not restate the table row.

Length contract: table + (N signals × 1 paragraph). No more, no less.
S2 must not become a narrative account of signals. The table is primary.

S2 exit condition: table complete, one paragraph per signal.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S3 — PATTERN [length contract: 3–5 paragraphs, no signal enumeration]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Signal survey axis, S2 row — all key findings recorded and
weights assigned; AND S2 signal-survey step completed — all complete/partial
artifacts read and tabulated.

Write 3–5 paragraphs. Author's voice. First person plural.

Prohibited structures:
  - Do not open with "The signals show..." followed by a list
  - Do not reference signals in the order they appear in S2
  - Do not allocate one paragraph per signal — this is not a summary

Required structures:
  - Name the pattern explicitly in the first paragraph
  - Address at least one tension or contradiction in the signal set
  - State what this pattern predicts for {{TOPIC}} that the individual signals do not

Length contract: 3 paragraphs minimum, 5 paragraphs maximum.
If the pattern is clear in 3 paragraphs, stop at 3.
If the pattern requires 5 to be honest about its complexity, use 5.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S4a — UNCERTAINTY [length contract: 3–5 items, matching S3 depth]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Pattern synthesis axis, S3 row — pattern statement recorded; AND
S3 pattern-synthesis step completed — cross-signal interpretation written.

Balance rule: S4a must carry the same weight as S3.
If S3 is 5 paragraphs, S4a must have 5 uncertainty items.
If S3 is 3 paragraphs, S4a must have 3 items minimum.
The synthesis cannot be confident in proportion to evidence and thin on uncertainty.

For each item in S4a:
  1. The unresolved question (one sentence, no hedging)
  2. Why the current signals do not resolve it (one sentence)
  3. What a definitive signal would look like and how obtainable it is

S4a is complete only when its item count matches or exceeds S3's paragraph count.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
S4b — RECOMMENDATION [length contract: exactly 3 paragraphs]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Choose exactly one: proceed / pause / pivot / abandon.

Para 1: The recommendation. The pattern section (S3) that most directly supports it.
Para 2: The uncertainty item (S4a) that most directly threatens it.
Para 3: The decision trigger that would change the recommendation — specific signal,
         threshold, or event; and which of the four options it would move to.

Constraint: Para 1 must not quote S4b. Para 2 must not minimize S4a.
The recommendation must survive contact with the uncertainty section.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT ARTIFACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write to: simulations/topic/story/{{TOPIC}}-story-{{DATE}}.md
Section order: S1 → S2 → S3 → S4a → S4b
Voice: editorial. First person plural. This document authorizes or halts a commitment.
```

---

## V-04 — Combined: Role Sequence + Table-Forward (V-01 × V-02)

**Variation axes**: Role sequence (three named roles) + Table-forward S2 with typed column schema

**Hypothesis**: The V-01 role protocol produces C-43 dual-anchored entry conditions as a structural byproduct. The V-02 column schema produces a C-44-compliant table whose structure is derived from signal type taxonomy. Combining them means the same table serves as both the Cartographer's inventory (S1) and the Synthesizer's survey schema (S2), making hand-off between roles the natural audit checkpoint. Neither criterion requires explicit instruction — both emerge from the combined protocol design.

---

```
You are running /topic:story for topic: {{TOPIC}}

## Signal Story — Role-Sequence + Table-Forward Protocol

Three roles run in sequence. Two sections lead with tables. Four sections total.
Entry conditions name both inventory-row completion and role-step completion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE 1: CARTOGRAPHER
Purpose: Build the signal registry. Do not read artifact content.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: No prior role has run. Begin immediately.

Locate all signal artifacts for {{TOPIC}} in simulations/ by namespace:
  scout / draft / review / flow / trace / prove / listen / program / topic

S1 — Signal Registry (lead with table, no preceding text)

| # | Signal ID | Namespace | Skill | Date | Path | Status |
|---|-----------|-----------|-------|------|------|--------|
|   |           |           |       |      |      | complete / partial / missing |

For namespaces with no {{TOPIC}} artifacts: note below the table as a single line.
"No artifacts found: {namespaces}"

S1 exit condition: all located artifacts are rows. Path field non-empty. Status filed.
Cartographer step S1 complete: table written, all namespaces checked.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE 2: SYNTHESIZER
Purpose: Read each artifact. Build the survey table. Write the pattern.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

S2 entry condition: Signal registry axis, S1 row — all fields complete; AND
Cartographer step S1 completed — all namespaces checked, all artifacts located.

S2 — Signal Survey (data-collection section — table leads, narrative follows)

Open S2 with the survey table. No text precedes the table.

| Signal ID | Signal Type | Evidence Class | Key Finding | Weight | Status |
|-----------|-------------|----------------|-------------|--------|--------|

Column definitions:

Signal Type:
  market / technical / user / design / flow / hypothesis / program

Evidence Class:
  primary   — produced by a skill run in this topic's corpus
  secondary — references external source or adjacent topic
  inferred  — analyst judgment on incomplete artifact

Key Finding: one sentence. What this artifact most firmly establishes.

Weight: high (should move recommendation) / medium / low (background signal)

Status: carry over from S1. If partial, append notes directly below the row.

After the table: one paragraph per artifact (2–3 sentences).
Paragraph annotates the key finding. Does not restate the row. Does not introduce
table-eligible data that belongs in a column.

S2 exit condition: all S1 artifacts have rows. Key Finding non-empty for all
non-missing artifacts. Evidence Class assigned to all rows.
Synthesizer step S2 complete: all artifacts read, survey table complete.

S3 — Pattern Synthesis

S3 entry condition: Signal survey axis, S2 row — all key findings and evidence
classes recorded; AND Synthesizer step S2 completed — all complete/partial
artifacts read and tabulated.

Write the synthesis in the author's voice. 3–5 paragraphs. First person plural.

Structure requirements:
  Para 1: Name the pattern. State it as a claim, not a summary.
  Para 2–4: Develop the claim. Address convergences, tensions, absences.
  Final para: State what this pattern predicts for {{TOPIC}} without new signals.

Prohibitions:
  Do not walk through signals in S2 table order.
  Do not open with "The signals show..."
  Do not allocate one paragraph per signal.

S3 exit condition: pattern claim stated, tension addressed, prediction made.
Synthesizer step S3 complete: pattern written and exits into role hand-off.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE 3: EDITOR
Purpose: Write uncertainty and recommendation. Commit.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

S4 entry condition: Pattern synthesis axis, S3 row — pattern statement recorded,
prediction made; AND Synthesizer step S3 completed — cross-signal interpretation
written and exited.

S4a — What Remains Uncertain

Numbered list. 2–5 items.
Each item: question / absent signal type / what a definitive signal looks like.
Draw on the Evidence Class column — thin evidence classes generate this list.

S4b — Recommendation

One of: proceed / pause / pivot / abandon. State it in the first sentence.

Para 1: The recommendation and its primary S3 support.
Para 2: The S4a item that most threatens it, and whether current signals address that threat.
Para 3: Reversal condition — name the specific signal, threshold, or event that would
         change the recommendation, and to which option it would change.

No hedging. No dual recommendations. The synthesis commits.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT ARTIFACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write to: simulations/topic/story/{{TOPIC}}-story-{{DATE}}.md

Section order: S1 (table) → S2 (table, then paragraphs) → S3 (prose) → S4a (list) → S4b (prose)
Role attribution: above each section header, note which role produced it.
Voice: editorial. First person plural. Decision document, not report.
```

---

## V-05 — Combined: Formal Register + Inertia Framing

**Variation axes**: Phrasing register (formal/technical, imperative directives) + Inertia framing (the status-quo option — "continue without this feature" — is explicitly analyzed alongside the recommendation as a named competitor with its own signal assessment)

**Hypothesis**: A formal-register prompt with technical imperative directives (no conversational scaffolding) produces tighter outputs because the model is not prompted to explain reasoning that belongs in the artifact. Adding explicit inertia framing — naming and evaluating "continue without this feature" as a legitimate option — prevents the common failure mode where the recommendation section is implicitly biased toward proceeding because the skill only analyzes the feature's signals, not the signals supporting the status quo.

---

```
You are running /topic:story for topic: {{TOPIC}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1: SIGNAL INVENTORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Locate all signal artifacts for {{TOPIC}} in simulations/.
Enumerate namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.
Record each located artifact as a row. Do not read content. Produce the table.

| Signal ID | Namespace | Skill | Date | Status |
|-----------|-----------|-------|------|--------|

Record "No artifacts: {namespace}" below the table for each empty namespace.
Section 1 complete: all namespaces checked, all located artifacts are rows.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2: SIGNAL SURVEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Signal inventory axis, S1 row — all fields complete; AND
Section 1 signal-location step completed — all namespaces checked and
all located artifact paths confirmed.

Read each Section 1 artifact. Produce the survey table immediately — no text precedes it.

| Signal ID | Key Finding | Confidence | Weight | Gaps |
|-----------|-------------|------------|--------|------|

Definitions:
  Key Finding: one sentence. What this artifact establishes. No subordinate clauses.
  Confidence: high (artifact directly supports the finding) / med / low (inferred)
  Weight: high (should move recommendation) / med / low
  Gaps: what the signal was positioned to cover and did not.

After the table: one annotating paragraph per artifact (2–3 sentences).
The paragraph explains; the table records. Do not duplicate row data in the paragraph.

Section 2 complete: all Section 1 artifacts have survey rows; Key Finding non-empty
for all complete/partial artifacts; annotating paragraphs written.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3: PATTERN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Signal survey axis, S2 row — all key findings and weights recorded; AND
Section 2 signal-survey step completed — all artifacts read, tabulated, annotated.

Produce the editorial synthesis. 3–5 paragraphs. First person plural.

Requirements:
  - State the pattern as a claim in paragraph 1.
  - Address the primary tension in the signal set in paragraph 2.
  - State what the pattern predicts for {{TOPIC}} without new signals in the final paragraph.

Prohibitions:
  - Do not walk signals in survey order.
  - Do not allocate one paragraph per signal.
  - Do not open paragraph 1 with "The signals show..." or "Across the namespaces..."

Section 3 complete: pattern claim present, tension addressed, prediction stated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4a: WHAT REMAINS UNCERTAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Entry condition: Pattern synthesis axis, S3 row — pattern statement recorded; AND
Section 3 pattern-synthesis step completed — cross-signal interpretation written
and prediction stated.

Produce a numbered list of 2–5 unresolved questions.

Format per item:
  1. Question: [the specific unresolved question]
     Absent signal: [which namespace or signal type would resolve it]
     Definitive signal: [what that artifact would contain to be dispositive]

Section 4a is not a hedge. Each item names a specific open question, not
a general expression of uncertainty.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4b: INERTIA ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before stating the recommendation, analyze the inertia option.

The inertia option is: continue without {{TOPIC}} — do not proceed with the feature,
do not pivot, do not formally abandon it; maintain the current state.

Inertia analysis (two paragraphs):
  Para 1: What signals support the inertia option?
          Which Section 2 signals, if read as evidence for the status quo, are strongest?
          What would a team choosing inertia cite from the current signal set?
  Para 2: What does the inertia option cost?
          What signals indicate that deferral has a time-varying cost
          (market windows, competitive moves, team capacity decay)?

Inertia analysis is not a straw man. It is a genuine assessment of whether
the evidence supports doing nothing over the four recommendation options.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4c: RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Choose one: proceed / pause / pivot / abandon.

Do not choose inertia. The inertia analysis exists to sharpen the recommendation,
not to produce it. The recommendation must be preferable to inertia or it should
be abandon.

Para 1: The recommendation. Its primary support from Section 3.
Para 2: Why the recommendation is preferable to inertia — directly address
        the strongest inertia-supporting signal identified in Section 4b.
Para 3: Reversal condition — the specific signal, threshold, or event that
        would change the recommendation; the option it would change to;
        and whether that option is preferable to inertia at that trigger point.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT ARTIFACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write to: simulations/topic/story/{{TOPIC}}-story-{{DATE}}.md

Section order: S1 → S2 (table-forward) → S3 → S4a → S4b → S4c
Register: formal. Imperative mood in directives. First person plural in editorial sections.
The artifact is a decision document. Its purpose is to make a commitment legible,
not to demonstrate that signals were read.
```

---

## Variation Summary

| Variation | Axis | C-43 strategy | C-44 strategy |
|-----------|------|---------------|---------------|
| V-01 | Role sequence | Structural byproduct: each role entry condition names prior role step + prior inventory row | Table in S2 per protocol; role sequence makes it explicit |
| V-02 | Output format | Single step; entry conditions state both anchors | Load-bearing: column schema derived from signal taxonomy; table is the canonical record |
| V-03 | Lifecycle emphasis | Entry conditions present; balance rule governs depth parity | Table leads S2; balance contract forces narrative to annotate rather than contain |
| V-04 | Role sequence + Output format | Strongest: role hand-off IS the dual-anchor check — Cartographer's registry row + role-step completion are co-equal prerequisites for Synthesizer | Strongest: typed column schema + role protocol make table the Synthesizer's primary work product |
| V-05 | Formal register + Inertia framing | Formal imperative style states both anchors cleanly; no conversational softening | Table leads S2 per formal protocol; register suppresses prose-wrapping of table data |

**Predicted strongest for C-43**: V-04 (dual-anchor is structurally embedded in role hand-off logic)
**Predicted strongest for C-44**: V-02 and V-04 (column schema makes table the canonical data structure, not an optional display format)
**Predicted highest overall v13 score**: V-04 (both new criteria addressed as protocol design, not rubric compliance)
