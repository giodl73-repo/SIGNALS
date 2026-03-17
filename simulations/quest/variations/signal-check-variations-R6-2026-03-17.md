**Signal-Check R6 variations written** to `simulations/quest/variations/signal-check-variations-R6-2026-03-17.md`.

---

## What R6 delivers

Five variations incorporating the two new rubric criteria (C-17, C-18) as fixed structural requirements, testing new axes against the updated /10 denominator:

| V | Axis | Key Bet |
|---|------|---------|
| **V-01** | Role sequence — explicit mechanism handoff | [MECHANISM VERDICT] line that SEQUENCE quotes verbatim: C-17 structurally enforced, not instructionally encouraged |
| **V-02** | Inertia framing — C-18 as named PART 2 section | STEP A: INERTIA CASE STRENGTH before readiness and observations — promotes C-18 from embedded question (R5) to structural prominence |
| **V-03** | Output format — tabular PART 2 | Scannability table with advisory-phrase-only status column: tests whether C-05 tone holds under format pressure |
| **V-04** | Combination: mechanism handoff + C-18 section + inertia-relevance column | Full C-17/C-18 chain: tagged artifacts → MECHANISM VERDICT → SEQUENCE audit → PART 2 inertia case |
| **V-05** | Combination: conversational register + tabular PART 2 | "Working notes" voice + scan table: tests whether register preserves advisory tone where the phrase-constraint alone may not |

**Three R6 research questions:**
1. Does verbatim-quote MECHANISM VERDICT improve mechanism audit depth or produce rote outputs?
2. Does dedicated C-18 section (V-02/V-04) add coaching value over embedded question (R5 V-02), or create redundancy?
3. Does tabular PART 2 hold C-05 advisory tone with phrase-constraint? Does conversational voice (V-05) change the result vs formal register (V-03)?
in all 5: C-15 (inertia anchor at Step 0), C-16 (two-register by document
shape), C-17 (mechanism-aware SEQUENCE), and C-18 (PART 2 inertia case frame) are
architectural — not variation axes.

**Three open research questions** for the R6 scorecard:
1. Does an architecturally-enforced MECHANISM VERDICT line (V-01, V-04) improve SEQUENCE
   mechanism-audit depth beyond the instructional carry-forward in R5 V-01?
2. Does C-18 as a dedicated PART 2 section (V-02, V-04) produce richer inertia case
   assessment than embedding it as a question inside STEP 4 (R5 V-02)?
3. Does tabular PART 2 (V-03, V-05) maintain C-05 advisory tone when the status column
   uses advisory phrases ("worth exploring" / "looks solid") rather than PASS/FAIL?

---

## V-01 — Single Axis: Explicit Mechanism Handoff

**Axis**: Role sequence (architectural C-17 enforcement)
**Hypothesis**: R5 V-01 showed that running CAUSAL GAP first and prompting SEQUENCE to read
"in light of the mechanism verdict" qualitatively improves the SEQUENCE audit. But that
improvement depends on the analyst actively carrying the verdict forward — it is
instructionally encouraged, not architecturally enforced. This variation adds a one-line
`[MECHANISM VERDICT: ___]` summary that closes CAUSAL GAP, and SEQUENCE *must quote that
line verbatim* before proceeding. The verbatim-quote requirement makes C-17 mechanically
enforced: SEQUENCE cannot run without the mechanism context, because the mechanism context
is literally in the prompt answer. Tests whether mechanical enforcement improves mechanism
audit depth beyond the instructional prompt.

---

```markdown
Signal-check for {{topic}}. Advisory — observations the team can decide to act on,
not a gate.

Produce in two parts in order. Do not merge the parts.

PART 1 — ANALYTICAL RECORD: internal working analysis. Severity ratings, ranked flags.
  Not shown to the team as scores or gates.
PART 2 — TEAM COACHING REPORT: advisory observations only. No severity labels,
  no scores, no gates.

Structural feature: CAUSAL GAP runs first. It ends with a one-line MECHANISM VERDICT
summary. SEQUENCE must quote that verdict verbatim before proceeding — SEQUENCE is an
audit of whether discovery built the mechanism case, not just a temporal ordering check.

======================================================================
PART 1 — ANALYTICAL RECORD  (internal — not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor
you will reference throughout.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

List all signal artifacts for {{topic}}.

| Artifact | Namespace | Date | Signal Carried |
|----------|-----------|------|----------------|

Empty namespaces (which of the 9 — scout, draft, review, flow, trace, prove, listen,
program, topic — have no artifacts): list each with one sentence: expected gap or
meaningful blind spot?

Competitor / market / benchmark artifacts present?
  yes → staleness threshold = 14 days
  no  → staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS — CAUSAL GAP FIRST  (~420 words) ====

For each dimension: cite artifacts by name, record severity internally in parentheses
(working note — not a gate), write the coaching observation, give one concrete next
action if flagged.

### CAUSAL GAP — is there mechanism evidence?
Inertia anchor: [restate Step 0 in one phrase].
What would need to be true for {{topic}} to produce its outcome better than doing
nothing? Is there artifact evidence for that mechanism — not a restatement of the
hypothesis, but actual evidence for the pathway? State: present / partial / absent.
Name what is there and what is missing.
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

[MECHANISM VERDICT: present / partial / absent — key gap if any: ___]
← SEQUENCE quotes this line verbatim below.

### SEQUENCE — did discovery establish the mechanism evidence?
Quoting mechanism verdict: "[MECHANISM VERDICT from above]"
Read the artifact ordering through that lens. Cite 2+ artifacts with dates.
Did discovery precede specification? More importantly: given that verdict, did the
discovery phase actually establish the mechanism evidence — or was the mechanism gap
present before the team committed to a spec? If the verdict is partial or absent:
was the gap there before specification, or did it emerge after?
Inertia angle: did discovery include any validation against the status-quo alternative
before specifying?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### COHERENCE — do the signals agree?
Name 2+ signals and compare them on a specific claim: aligned / contradicting /
inconclusive. If contradicting, describe the specific disagreement. Does the
contradiction bear on the mechanism question from CAUSAL GAP?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### STALENESS — is the evidence fresh enough?
Apply the threshold from Step 1. For each namespace with artifacts: inside or outside
the window? Are the artifacts most relevant to the mechanism (from CAUSAL GAP) current?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

==== STEP 3: CROSS-DIMENSION PATTERN  (~50 words) ====

Do two or more flagged dimensions share a root cause? Name the pattern if yes.
Does it trace to a shared mechanism gap — e.g., CAUSAL GAP absent + SEQUENCE gap
tracing to mechanism evidence never appearing in discovery at all?
If no shared root: "No cross-dimension pattern detected."

======================================================================
PART 2 — TEAM COACHING REPORT  (advisory — no severity labels)
======================================================================

==== STEP 4: DRAFT READINESS + INERTIA CASE  (~100 words) ====

Two questions to open:

First: which dimensions look clean, which have something worth noticing, where does
this topic sit on the readiness spectrum? Two to three sentences.

Second: from the artifact record, is the case that {{topic}} beats doing nothing
clearly built, partially built, or still open? Name where that sits — the mechanism
verdict from CAUSAL GAP is the most direct artifact-backed answer to this question.

Label: [DRAFT — to be confirmed after coaching observations]

==== STEP 5: DIMENSION OBSERVATIONS  (~250 words) ====

Translate each STEP 2 finding into an advisory observation for the team. Present in
CAUSAL GAP-first order. No severity labels, no scores, no gates. Advisory language
throughout.

CAUSAL GAP: [coaching observation — what the evidence record says about the mechanism]
  If flagged → suggested next step:

SEQUENCE: [coaching observation — if the sequence gap traces to missing mechanism
  evidence before specification, name that connection; the verbatim MECHANISM VERDICT
  is the useful anchor: "discovery closed before [gap] was established"]
  If flagged → suggested next step:

COHERENCE: [coaching observation]
  If flagged → suggested next step:

STALENESS: [coaching observation]
  If flagged → suggested next step:

==== STEP 6: CONFIRMED READINESS  (~75 words) ====

Return to your STEP 4 draft. Does the dimension analysis confirm or change your read?
Label: [CONFIRMED] or [REVISED — what changed and why]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open
4. Overall read: proceed / loop once more / investigate further
```

---

## V-02 — Single Axis: C-18 as Named PART 2 Section

**Axis**: Inertia framing (C-18 structural prominence)
**Hypothesis**: R5 V-02 embedded the inertia summary question ("is the case built?") inside
STEP 4 readiness — a question within a larger paragraph. C-18 is now a rubric criterion,
which invites asking whether structural prominence changes coaching quality. This variation
promotes C-18 to a standalone named PART 2 section — STEP A: INERTIA CASE STRENGTH —
that runs before readiness and dimension observations, with an explicit three-option frame
("clearly built / partially built / still open") and a requirement to name what in the
artifact record tells you so. Tests whether a dedicated section produces a more substantive
inertia case assessment than embedding it as a question, or whether it creates redundancy
with the dimension observations.

---

```markdown
Signal-check for {{topic}}.
Advisory — observations the team can decide to act on, not a gate.

This report has two parts. Complete in order. Do not merge.
PART 1 — ANALYTICAL RECORD: internal. Severity scoring, inertia analysis. Not a gate.
PART 2 — TEAM COACHING REPORT: advisory observations. No severity labels or scores.

PART 2 structure: opens with a named INERTIA CASE STRENGTH section before readiness
and dimension observations. That section asks whether the case that {{topic}} beats
doing nothing is clearly built, partially built, or still open. Advisory framing
throughout — not a gate.

======================================================================
PART 1 — ANALYTICAL RECORD  (internal — not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

What is the team doing today if {{topic}} does not ship? State the status-quo
alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

List all signal artifacts for {{topic}}.

| Artifact | Namespace | Date | Signal Carried |
|----------|-----------|------|----------------|

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each — expected gap or meaningful blind spot?

Competitor / market / benchmark signals present?
  yes → staleness threshold = 14 days
  no  → staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS — CAUSAL GAP FIRST  (~400 words) ====

Analysis order: CAUSAL GAP → SEQUENCE → COHERENCE → STALENESS.
For each: cite artifacts, note severity internally (not a gate), write coaching
observation, give one next action if flagged.

### CAUSAL GAP
Inertia anchor: [restate Step 0 in one phrase]. Does evidence exist for the
pathway from {{topic}} to its outcome, specifically better than the status quo?
State: present / partial / absent. Name what is there and what is missing.
Do not restate the hypothesis.
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### SEQUENCE
With the CAUSAL GAP verdict in view: did the discovery phase establish the mechanism
evidence you just evaluated? Cite 2+ artifacts with dates. What does the ordering
tell you — did discovery build the mechanism case before the team committed to a spec,
or was the mechanism gap present from the start? Inertia angle: did discovery include
any validation against the status-quo alternative before specifying?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### COHERENCE
Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
If contradicting, describe the specific disagreement. Does the contradiction bear
on the mechanism question from CAUSAL GAP — does it weaken the case against doing
nothing?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### STALENESS
Apply threshold from Step 1. Artifacts inside / outside the window? Are the artifacts
most relevant to the mechanism (from CAUSAL GAP) current?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

==== STEP 3: CROSS-DIMENSION PATTERN  (~50 words) ====

Do 2+ flagged dimensions share a root cause? Name the pattern. Does it trace to a
shared mechanism gap?
If no shared root: "No cross-dimension pattern detected."

======================================================================
PART 2 — TEAM COACHING REPORT  (advisory — no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~75 words) ====

Before readiness or dimension observations: address the inertia case directly.
Based on the artifact record for {{topic}}, is the case that it beats doing nothing:
  □ Clearly built — mechanism evidence is present, status-quo comparison is addressed
  □ Partially built — some evidence exists but specific gaps remain; name the key one
  □ Still open — mechanism or comparison not yet established in the artifact record

State which applies and what in the artifacts tells you so. Advisory — not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

From Part 1: which dimensions look clean, which have something worth noticing, where
does this topic sit on the readiness spectrum? Write a short paragraph.
Label: [DRAFT — to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~250 words) ====

Translate each STEP 2 finding into an advisory observation for the team. CAUSAL
GAP-first order. No severity labels, no scores, no gates. Advisory language throughout.

CAUSAL GAP: [coaching observation — connect to inertia case from STEP A]
  If flagged → suggested next step:

SEQUENCE: [coaching observation — if the gap traces to missing mechanism evidence
  before specifying, name that connection explicitly]
  If flagged → suggested next step:

COHERENCE: [coaching observation]
  If flagged → suggested next step:

STALENESS: [coaching observation]
  If flagged → suggested next step:

==== STEP D: CONFIRMED READINESS  (~75 words) ====

Return to STEP B draft. Does the dimension analysis confirm or change your read?
Label: [CONFIRMED] or [REVISED — what changed and why]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-03 — Single Axis: Output Format (Tabular PART 2)

**Axis**: Output format
**Hypothesis**: All R5 variations produced PART 2 as prose coaching observations. A structured
table — | Dimension | How It Looks | Key Observation | Suggested Next Step | — is more
scannable for teams that need to act quickly. The risk is that a table can feel gate-like:
rows with status columns read as verdicts regardless of language. This variation tests
whether a table format can carry advisory tone when the status column uses advisory phrases
("worth exploring", "looks solid") rather than PASS/FAIL. C-17 and C-18 are incorporated:
mechanism-audit SEQUENCE in PART 1 and a named INERTIA CASE section before the table in
PART 2. Tests whether tabular PART 2 satisfies C-05 under the phrase-constraint.

---

```markdown
Signal-check for {{topic}}. Advisory — observations the team can decide to act on,
not a gate.

Two parts in order. Do not merge.
PART 1 (internal): full analysis, severity ratings. Not shown to team as gates or scores.
PART 2 (team): coaching brief in table format. Advisory language in all cells.
  No severity labels.

Table language rule for PART 2: the "How It Looks" column uses advisory phrases only.
  Clean dimension: "looks solid" / "well-covered" / "no concerns"
  Flagged dimension: "worth exploring" / "worth a closer look" / "something to notice"
  Never: PASS / FAIL / BLOCKED / RED / GREEN

======================================================================
PART 1 — ANALYTICAL RECORD  (internal — not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

State the status-quo alternative in one sentence. What does the team default to
if {{topic}} does not ship?

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried |
|----------|-----------|------|----------------|

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each — expected gap or meaningful blind spot?

Competitor / benchmark signals present?
  yes → threshold = 14 days  /  no → threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS — CAUSAL GAP FIRST  (~400 words) ====

Analysis order: CAUSAL GAP → SEQUENCE → COHERENCE → STALENESS.
For each: cite artifacts by name, severity internally (not a gate), coaching
observation, one concrete next action if flagged.

### CAUSAL GAP
Inertia anchor: [restate Step 0 in one phrase].
Is there mechanism evidence for the feature-to-outcome pathway, specifically better
than the status quo? State: present / partial / absent. Name what exists and what
is missing. Do not restate the hypothesis.
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### SEQUENCE
With the CAUSAL GAP verdict in view: cite 2+ artifacts with dates. Did discovery
precede specification? More importantly: did the discovery phase establish the
mechanism evidence you just evaluated — or was that gap present before the team
committed to a spec? Inertia angle: did discovery validate against the status quo
before specifying?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### COHERENCE
Name 2+ signals on a specific claim: aligned / contradicting / inconclusive. If
contradicting, name the specific disagreement. Does it bear on the mechanism question?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### STALENESS
Apply threshold from Step 1. Artifacts inside / outside the window? Are the
mechanism-relevant artifacts (from CAUSAL GAP) current?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

==== STEP 3: CROSS-DIMENSION PATTERN  (~50 words) ====

Do 2+ flagged dimensions share a root? Name the pattern. Does it trace to a
shared mechanism gap?
If no: "No cross-dimension pattern detected."

======================================================================
PART 2 — TEAM COACHING BRIEF  (advisory — no severity labels)
======================================================================

==== INERTIA CASE  (~50 words) ====

Before the table: is the case that {{topic}} beats doing nothing clearly built,
partially built, or still open? State which and what in the artifact record tells
you so. Advisory — not a gate.

==== READINESS OVERVIEW  (~30 words) ====

Label: [DRAFT]
[Short readiness sentence: which dimensions clean, which flagged, overall tone.]

==== DIMENSION COACHING TABLE ====

| Dimension | How It Looks | Key Observation | Suggested Next Step |
|-----------|-------------|-----------------|---------------------|
| CAUSAL GAP | [advisory phrase] | [one coaching observation] | [next step if flagged — "nothing urgent" if clean] |
| SEQUENCE | [advisory phrase] | [observation — note mechanism connection if relevant] | [next step if flagged — "nothing urgent" if clean] |
| COHERENCE | [advisory phrase] | [one coaching observation] | [next step if flagged — "nothing urgent" if clean] |
| STALENESS | [advisory phrase] | [one coaching observation] | [next step if flagged — "nothing urgent" if clean] |

Reminder: "How It Looks" uses the advisory phrase list above — never PASS/FAIL.
Every flagged row must have a specific Suggested Next Step.

==== CONFIRMED READINESS  (~40 words) ====

Label: [CONFIRMED] or [REVISED — reason]
Clean / flagged count. Inertia case: clearly built / partially built / still open.
Overall read: proceed / loop once more / investigate further
```

---

## V-04 — Combined Axes: Mechanism Handoff + C-18 Named Section

**Axes**: Role sequence (mechanism handoff, V-01) + Inertia framing (C-18 dedicated section,
V-02) + Inventory depth (inertia-relevance column, R5 V-04)
**Hypothesis**: V-01's explicit MECHANISM VERDICT enforces C-17 mechanically; V-02's
dedicated INERTIA CASE STRENGTH section gives C-18 structural prominence. This combination
tests whether the two strongest structural expressions of the new criteria compound: the
mechanism handoff feeds the PART 2 inertia case assessment directly (the MECHANISM VERDICT
is the most artifact-backed statement about whether the case is built), while the
inertia-relevance column from R5 V-04 pre-identifies which artifacts are load-bearing.
Full chain: Step 0 anchors inertia → Step 1 column tags artifacts → CAUSAL GAP consumes
tagged set → MECHANISM VERDICT closes → SEQUENCE quotes verdict → PART 2 STEP A reads
verdict into inertia case frame. Tests whether the explicit chain is the strongest
achievable expression of C-17/C-18 intent, or whether the added structure creates prompt
overhead that reduces usability.

---

```markdown
Signal-check for {{topic}}.
Advisory — observations the team can decide to act on, not a gate.

Two parts in order. Do not merge.
PART 1 — ANALYTICAL RECORD: internal. Severity, mechanism analysis, ranked flags.
PART 2 — TEAM COACHING REPORT: advisory observations. No severity labels or scores.

Two structural features:
1. CAUSAL GAP runs first. It ends with a one-line [MECHANISM VERDICT] that SEQUENCE
   must quote verbatim — SEQUENCE is an audit of whether discovery built the mechanism
   case, not just a temporal ordering check.
2. PART 2 opens with a named INERTIA CASE STRENGTH section before readiness and
   dimension observations. Advisory framing: clearly built / partially built / still open.

======================================================================
PART 1 — ANALYTICAL RECORD  (internal — not for team use)
======================================================================

==== STEP 0: INERTIA ANCHOR  (~30 words) ====

Before the inventory: what is the team doing today if {{topic}} does not ship?
State the status-quo alternative in one sentence. This is the inertia competitor.

==== STEP 1: ARTIFACT INVENTORY  (~150 words) ====

| Artifact | Namespace | Date | Signal Carried | Inertia Relevant? |
|----------|-----------|------|----------------|-------------------|
(Inertia Relevant: does this artifact speak to the comparison between {{topic}} and
the status-quo alternative — competitors, benchmarks, usage data, mechanism evidence?
Mark yes / no.)

Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic):
  list each — expected gap or meaningful blind spot?

Inertia-relevant artifact count (from column above):
  1 or more → staleness threshold = 14 days
  0         → staleness threshold = 30 days

==== STEP 2: DIMENSION ANALYSIS — CAUSAL GAP FIRST  (~450 words) ====

Analysis order: CAUSAL GAP → SEQUENCE → COHERENCE → STALENESS.
For each: cite artifacts, severity internally (not a gate), coaching observation,
one concrete next action if flagged.

### CAUSAL GAP
Pull the inertia-relevant artifacts from Step 1.
Inertia anchor: [restate Step 0 in one phrase].
Is there mechanism evidence for the pathway from {{topic}} to its claimed outcome,
specifically better than the status-quo alternative? Evaluate only the artifacts —
do not restate the hypothesis. State: present / partial / absent. Name what is there
and what is missing.
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

[MECHANISM VERDICT: present / partial / absent — key gap if any: ___]
← SEQUENCE quotes this line verbatim below.

### SEQUENCE
Quoting mechanism verdict: "[MECHANISM VERDICT from above]"
Cite 2+ artifacts with dates. Did discovery precede specification?
Read the ordering through the mechanism lens: did the inertia-relevant artifacts
(Step 1 column) appear in the discovery phase — or did the team specify before the
mechanism evidence existed? If the verdict is partial or absent: was the gap there
before specification, or did it emerge after?
Inertia angle: did discovery validate against the status-quo alternative before
committing to a specification?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### COHERENCE
Name 2+ signals on a specific claim: aligned / contradicting / inconclusive.
If contradicting, describe the specific disagreement. Do any contradictions involve
inertia-relevant artifacts — does the contradiction weaken or strengthen the
mechanism case?
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

### STALENESS
Apply threshold from Step 1 (14 or 30 days). Artifacts inside / outside the window?
Evaluate inertia-relevant artifacts (Step 1 column) with particular attention —
stale inertia signals mean the mechanism comparison may no longer be valid.
(internal: green / yellow / red)
Observation: ...
If yellow or red → next action:

==== STEP 3: CROSS-DIMENSION PATTERN  (~50 words) ====

Do 2+ flagged dimensions share a root? Name the pattern. Does it trace to a shared
mechanism gap — e.g., zero inertia-relevant artifacts causing both CAUSAL GAP and
STALENESS to flag on the same absence?
If no shared root: "No cross-dimension pattern detected."

======================================================================
PART 2 — TEAM COACHING REPORT  (advisory — no severity labels)
======================================================================

==== STEP A: INERTIA CASE STRENGTH  (~75 words) ====

Before readiness or dimension observations: address the inertia case directly.
Based on the artifact record for {{topic}}, is the case that it beats doing nothing:
  □ Clearly built — mechanism evidence present, status-quo comparison is addressed
  □ Partially built — some evidence exists but specific gaps remain; name the key one
  □ Still open — mechanism or comparison not established in the artifact record

Connect to the MECHANISM VERDICT from CAUSAL GAP — that verdict is the most direct
artifact-backed statement about the inertia case. Advisory — not a gate.

==== STEP B: DRAFT READINESS  (~75 words) ====

From Part 1: which dimensions look clean, which have something worth noticing, where
does this topic stand? Short paragraph.
Label: [DRAFT — to be confirmed after coaching observations]

==== STEP C: DIMENSION OBSERVATIONS  (~250 words) ====

Translate each STEP 2 finding into an advisory observation. CAUSAL GAP-first order.
No severity labels, no scores, no gates. Advisory language throughout.

CAUSAL GAP: [coaching observation — reference inertia-relevant artifact count from
  Step 1; if zero inertia-relevant artifacts, name that specifically]
  If flagged → suggested next step:

SEQUENCE: [coaching observation — connect to MECHANISM VERDICT; if the gap traces to
  inertia-relevant evidence appearing after specification, name that explicitly]
  If flagged → suggested next step:

COHERENCE: [coaching observation]
  If flagged → suggested next step:

STALENESS: [coaching observation — call out stale inertia-relevant artifacts
  specifically if they are outside the threshold]
  If flagged → suggested next step:

==== STEP D: CONFIRMED READINESS  (~75 words) ====

Return to STEP B. Does the dimension analysis confirm or change your read?
Label: [CONFIRMED] or [REVISED — what changed and why]

Team summary:
1. Dimensions clean vs. flagged (count)
2. Most useful thing to address before committing
3. Inertia case: clearly built / partially built / still open (restate from STEP A)
4. Overall read: proceed / loop once more / investigate further
```

---

## V-05 — Combined Axes: Phrasing Register + Tabular PART 2

**Axes**: Phrasing register (conversational) + Output format (tabular PART 2)
**Hypothesis**: R5 V-05 showed that conversational "working notes" register scales to the
full 18-criterion rubric and makes the two-register architecture feel natural rather than
formal. V-03 tests tabular PART 2 in formal register. This combination tests whether the
same table format reads differently when introduced with a casual voice: "here's what I'd
flag for each dimension" vs. a structured coaching brief header. The bet is that conversational
voice makes the table feel like a teammate handing off notes rather than a formal report,
preserving C-05 advisory tone through register rather than relying entirely on the phrase-
constraint in the status column. C-17 and C-18 are incorporated: mechanism-aware SEQUENCE
framing in PART 1 and an inertia case section before the table in PART 2.

---

```markdown
Signal-check for {{topic}}. Advisory only — things to notice, not a gate.

Two parts. Run them in order. Keep them separate.

PART 1 is your working notes: internal analysis, severity grades, inertia angle.
  Not shown to the team as scores or gates.
PART 2 is what you hand to the team: a quick scan table they can act on.
  No severity language, no scores, no gates.

Table language rule for PART 2: the "How It Looks" column is advisory phrases only.
  Never PASS / FAIL / BLOCKED / grades.
  Clean: "looks solid" / "no concerns" / "well-covered"
  Flagged: "worth a closer look" / "something to notice" / "worth exploring"

---PART 1 — WORKING NOTES  (internal — not for team use)---

---STEP 0 --- INERTIA ANCHOR  (~30 words) ---

Before you look at the artifacts: what does the team default to if {{topic}} doesn't
ship? One sentence. That's your inertia competitor.

---STEP 1 --- ARTIFACT INVENTORY  (~150 words) ---

List every signal artifact for {{topic}}.

| Artifact | Namespace | Date | Signal Carried |
|----------|-----------|------|----------------|

Which of the 9 namespaces have no artifacts (scout, draft, review, flow, trace,
prove, listen, program, topic)? For each empty one: expected gap, or something
worth noticing?

Any competitor, benchmark, or market comparison signals?
  yes → threshold = 14 days  /  no → threshold = 30 days

---STEP 2 --- DIMENSION ANALYSIS — CAUSAL GAP FIRST  (~400 words) ---

Work through all four dimensions in this order: CAUSAL GAP → SEQUENCE → COHERENCE
→ STALENESS. For each: cite artifacts, note your internal severity in parentheses
(working grade — not a gate), write what you'd flag, add a next step if yellow or red.

CAUSAL GAP — is there mechanism evidence?
  Inertia anchor: [restate Step 0 in one phrase].
  What would need to be true for {{topic}} to produce its outcome better than doing
  nothing? Is there actual artifact evidence for that pathway? Name what's there and
  what's missing. State: present / partial / absent.
  (internal: green / yellow / red)
  What I'm seeing: ...
  If yellow or red → what to do:

SEQUENCE — did discovery establish the mechanism evidence?
  With CAUSAL GAP just evaluated: cite 2+ artifacts with dates. Did discovery precede
  specification? More importantly: did the discovery phase build the mechanism case?
  If CAUSAL GAP is partial or absent — was that gap there before specification, or
  did it emerge after? Inertia angle: did discovery check against the status quo
  before committing to spec?
  (internal: green / yellow / red)
  What I'm seeing: ...
  If yellow or red → what to do:

COHERENCE — do the signals agree?
  Pick 2+ signals and a specific claim they both address. Aligned, contradicting, or
  inconclusive? If contradicting, name the actual disagreement. Does it bear on the
  mechanism question?
  (internal: green / yellow / red)
  What I'm seeing: ...
  If yellow or red → what to do:

STALENESS — is the evidence fresh?
  Apply the threshold from Step 1. For each namespace with artifacts: inside or
  outside the window? Are the mechanism-relevant artifacts still current?
  (internal: green / yellow / red)
  What I'm seeing: ...
  If yellow or red → what to do:

---STEP 3 --- CROSS-DIMENSION PATTERN  (~50 words) ---

Do two or more flagged dimensions share a root? Name it if yes. Does it trace to
a shared mechanism gap?
If not: "No cross-dimension pattern."

---PART 2 — WHAT I'D HAND THE TEAM  (advisory — no severity language)---

---INERTIA CASE --- (~50 words) ---

Before the table: is the case that {{topic}} beats doing nothing clearly built,
partially built, or still open? State which and what in the artifacts tells you so.
Advisory — not a gate or score.

---DRAFT READ --- (~30 words) ---

Quick readiness take: which dimensions look good, which have something worth noticing,
where this topic stands overall.
Label: [DRAFT]

---DIMENSION TABLE ---

Here's what I'd flag across the four dimensions:

| Dimension | How It Looks | What's Worth Noticing | What to Do Next |
|-----------|-------------|----------------------|-----------------|
| CAUSAL GAP | [advisory phrase] | [one observation] | [next step, or "nothing urgent"] |
| SEQUENCE | [advisory phrase] | [observation — note mechanism connection if relevant] | [next step, or "nothing urgent"] |
| COHERENCE | [advisory phrase] | [one observation] | [next step, or "nothing urgent"] |
| STALENESS | [advisory phrase] | [one observation] | [next step, or "nothing urgent"] |

Every flagged row must have a specific "What to Do Next" — that's the useful part.
If a row is clean, "nothing urgent" is fine.

---CONFIRMED READ --- (~30 words) ---

[CONFIRMED] or [REVISED — reason]
Clean / flagged count. Inertia case: clearly built / partially built / still open.
Most important next action. Overall: proceed / loop / investigate.
```

---

## Summary of variation axes

| Variation | Primary Axis | Secondary Axis | Key Structural Bet | R5 Heritage |
|-----------|-------------|---------------|-------------------|-------------|
| V-01 | Role sequence (mechanism handoff) | — | Explicit [MECHANISM VERDICT] line that SEQUENCE quotes verbatim — C-17 architecturally enforced | Extends R5 V-01 (instructional → structural) |
| V-02 | Inertia framing (C-18 dedicated section) | — | STEP A: INERTIA CASE STRENGTH as named PART 2 section before readiness — C-18 structural prominence | Extends R5 V-02 (embedded question → section) |
| V-03 | Output format (tabular PART 2) | — | PART 2 as scannability table; advisory-phrase-only status column tests C-05 under format pressure | New axis |
| V-04 | Role sequence (mechanism handoff) | Inertia framing (C-18 named section) + inertia-relevance column | Full C-17/C-18 chain: tagged artifacts → MECHANISM VERDICT → SEQUENCE audit → PART 2 inertia case | V-01 + V-02 + R5 V-04 |
| V-05 | Phrasing register (conversational) | Output format (tabular PART 2) | "Working notes" voice + scan table — register preserves C-05 advisory tone where phrase-constraint alone may not | R5 V-05 register + V-03 format |

**R6 research questions:**
1. Does an architecturally-enforced MECHANISM VERDICT line (V-01, V-04) improve SEQUENCE
   mechanism-audit depth beyond the instructional carry-forward in R5 V-01, or does the
   verbatim-quote requirement feel mechanical and produce rote rather than substantive audits?
2. Does C-18 as a dedicated PART 2 section (V-02, V-04) produce richer inertia case
   assessment than embedding it as a question inside STEP 4 (R5 V-02), or does the
   dedicated section create redundancy with dimension observations?
3. Does tabular PART 2 (V-03, V-05) maintain C-05 advisory tone when the status column
   uses advisory phrases — or does the row/column structure create verdictive reads
   regardless of language? Does conversational voice (V-05) change that result vs formal
   register (V-03)?
