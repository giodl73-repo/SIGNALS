---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 4
rubric: v4
---

# Variations: `topic:echo` -- Round 4

**Rubric:** v4 | **Date:** 2026-03-15

---

## Design Context

R3 differentiating evidence: V-01's typed verdict template made bare CUT structurally
unproducible (C-16 partial). V-03's Institutional Archaeologist role produced
correction-encoding names ("The name should encode the correction, not the discovery" --
C-17), forward-failure framing ("what the next team would get wrong if they carried the old
assumption" -- C-18), and register-specific close templates ("Before you start building..." /
"The design materials do not warn you that..." -- C-19). However, all three arrived as prose
instructions on a role inversion, not as structural constraints. A model following instructions
can still name a discovery, write a vague impact field, and close generically while technically
satisfying the letter of each instruction.

These four behaviors become C-16 through C-19 in v4:

- **C-16**: The filter is structurally enforced -- the template makes the disqualifying output
  form unproducible, not just instructed against. R3 V-01 applied this to the cut verdict.
  R4 extends structural enforcement to the naming step: a name validation gate that requires
  the correction template form and flags discovery labels before any entry is expanded.

- **C-17**: Each surprise name encodes the correction, not the discovery. The name tells the
  next team what was wrong, not what was found. "The Cascade Inversion" encodes the corrected
  relationship; "Unexpected Cascade Behavior" encodes the discovery event. C-17 formalizes
  this as a per-entry requirement rather than a style note.

- **C-18**: The design impact field uses forward-failure framing: "what the next team would
  get wrong if they carried the old assumption." Not "what changes in the design" -- what
  fails. The field must name the specific component, flow, or decision the next team would
  mis-design. A generic statement ("this is worth noting") is a malformed fill.

- **C-19**: The close is instantiated from a constrained register-specific template. Every
  slot filled with specific content from the echo. Generic forwarding is unproducible because
  no template in the menu produces a vague output -- each has required fills that force
  specificity.

**R4 strategy:**

- V-01: Single-axis targeting C-16 applied to naming -- a name validation gate step that
  requires the two-part correction template and makes the discovery-label form structurally
  unproducible before any entry is expanded.
- V-02: Single-axis targeting C-18 in isolation -- failure-mode-first organization where each
  entry derives from "what would the next team build wrong?" rather than "what surprised us?"
  The failure scenario is load-bearing, not appended.
- V-03: Single-axis targeting C-19 in isolation -- a constrained menu of four register-specific
  close templates requiring selection and full-slot instantiation. Generic closing is impossible
  because no template produces it.
- V-04: Combination of C-17 + C-18 -- correction-encoding names paired with forward-failure
  impact framing, validated as a pair before expansion. Tests whether the closed loop (name
  the correction, name the failure that follows) produces higher-quality C-03 as a side effect.
- V-05: Full combination -- C-13 (typed gate from R3) + C-16 (structurally-enforced naming)
  + C-17 (correction-encoding names) + C-18 (forward-failure framing) + C-19 (register-menu
  close). Each criterion at a structurally distinct moment: gate, name, impact, close.

**What C-16 adds over R3 V-01's typed gate:**

R3 V-01 made the cut verdict structurally typed -- "CUT -- {anti-pattern label}" -- so the
anti-pattern catalog became load-bearing at the filter stage. C-16 extends structural
enforcement one step further into the naming step: a name validation gate that requires the
form "The [Corrected Belief]: [Domain]" and flags names in the discovery form as malformed,
requiring revision before expansion. The naming step is now its own structural gate; a model
cannot proceed past it with "Unexpected X."

**What C-18 adds over R3 V-03's "why it still matters":**

R3 V-03's "Why it still matters" field asked "what the next team would get wrong." It was
appended after source, assumption, and correction -- all anchored to the discovery event.
C-18 makes the failure scenario the starting point: entries derive from failure first,
correction second. The downstream consequence is foundational rather than appended, forcing
specificity at the impact level because the model must commit to a specific failure before
identifying the correcting signal.

**What C-19 adds over R3 V-03's forward guidance register:**

R3 V-03 named two register templates as examples and left selection to the model. A model can
produce a close that resembles a template while leaving slots vague. C-19 requires selection
from a constrained menu and full-slot instantiation: every bracketed slot must contain specific
content traceable to a surprise or artifact in this echo. A slot filled with "the design" or
"the system" is flagged as a malformed fill, structurally visible as incomplete.

---

## V-01 -- Naming Gate axis

**Variation axis:** Output format -- a name validation gate step that makes the discovery-label
form structurally unproducible by requiring the two-part correction template and flagging
non-conforming names before any entry is expanded.

**Hypothesis:** R3 V-03 specified "the name should encode the correction, not the discovery"
as a prose instruction within the Archaeologist role. A model can still produce "Unexpected
Cascade Behavior" and rationalize it. When the template requires "The [Corrected Belief]:
[Domain]" and names in the discovery form are explicitly flagged as INVALID -- requiring
revision before expansion is permitted -- the discovery label becomes structurally unproducible.
The name validation gate extends C-16 from the cut step (R3 V-01) to the naming step: a model
that produces "Unexpected X" cannot proceed without revising the name, because the gate
requires a VALID verdict before expansion.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not expect?
It is institutional memory for the next team. Each surprise is named, sourced, and assessed
for its specific impact on the design direction.

---

**Name Template -- read and internalize before executing.**

Every surprise name in this echo must follow this two-part form:

> **The [Corrected Belief]: [Domain]**

Where:
- **[Corrected Belief]**: A noun phrase encoding what was wrong about the prior assumption --
  not what was found, but what was corrected. "The Scope Ceiling" names what was hit. "Lower
  Adoption Than Expected" names what happened. The corrected-belief form encodes the result
  of the correction; the discovery form encodes the experience of being surprised.
- **[Domain]**: 1-3 words situating the correction (e.g., "Resilience Path," "Permission
  Model," "Onboarding Flow").

**Deriving a valid name:**
1. State the prior assumption: "We assumed X."
2. State the correction: "The signal showed not-X."
3. Encode the correction: "The Not-X."
4. Compress and situate: "The Not-X: [Domain]."

**Malformed name test:** Does the draft name begin with "Unexpected," "Surprising,"
"Higher/Lower Than Expected," or describe an event rather than a corrected belief? That
is a discovery label. Revision required before expansion.

---

**Step 1 -- Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft, review,
flow, trace, prove, listen, program, topic). Note what each was investigating. Internal
scaffolding only.

---

**Step 2 -- Identify surprise candidates.**

Apply the prediction test to each noteworthy finding:

> "Would a person reading only the pre-investigation design materials have predicted this?"

YES -> confirmation. Not an echo entry. Belongs in `topic-story`.
NO -> surprise candidate.

Collect at least 3 candidates before proceeding.

---

**Step 3 -- Name Validation Gate.**

For each candidate, derive and validate a name before expansion:

```
Candidate: {one-sentence description}
Prior assumption: {what a reader of the design materials would have assumed}
Correction: {what the signal showed instead}
Draft name: The {Corrected Belief}: {Domain}
Name test:
  CORRECTION FORM -> VALID -- proceed to Step 4
  DISCOVERY FORM  -> INVALID -- revise name, re-run test
```

A candidate whose name cannot be revised to VALID is promoted to `topic-story`, not
`topic-echo` -- it may be a finding but not a correction worth naming in the echo.

The Name Validation Gate log is execution scaffolding -- do not include it in the output.

---

**Step 4 -- Write echo entries.**

For each candidate with a VALID name from Step 3:

**[Validated Name -- The {Corrected Belief}: {Domain}]**

- **Source signal**: Specific artifact name or skill type (e.g., `flow-resilience`,
  `prove-interview`, `scout-feasibility`).
- **Prior assumption**: What was expected before this signal. One sentence.
- **Finding**: What the signal revealed -- must oppose the prior assumption. One sentence.
- **Design impact**: The specific component, flow, or decision this changes. One sentence
  minimum. Must name something specific -- not "this affects the design."

Minimum 2 entries.

---

**Step 5 -- Synthesize.**

Write 2-4 sentences. Do 2 or more surprises share a root cause, reveal the same blind spot,
or together indicate a direction not previously visible? Name any pattern you see. State its
absence explicitly if none is evident.

---

**Step 6 -- Forward guidance.**

1-3 sentences addressed to the next team building `{topic}`. Specific to these surprises.
Register: "If you are about to build X, know that Y because we found Z."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 4-6. Steps 1-3 are execution scaffolding.

---

## V-02 -- Failure-First Organization axis

**Variation axis:** Lifecycle emphasis -- the production sequence inverts. Each entry begins
with the failure scenario ("what would the next team build wrong?") and traces backward to
the correcting signal, rather than beginning with the signal and appending a consequence.

**Hypothesis:** Standard forward-facing production -- find surprise, trace source, assess
impact -- leaves C-18 (forward-failure framing) as an afterthought. The impact field is
written after the entry is already anchored to a discovery event, and generic phrasings emerge
because the surprise moment, not the failure consequence, is load-bearing. When the production
sequence inverts -- failure first, source second -- the downstream consequence cannot be
approximate. The model must name a specific component or decision that would be built wrong
before identifying the correcting signal. Specificity at the impact level is forced rather than
requested.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not expect?
It is institutional memory for the next team. Each entry is a named correction -- something
that, if unknown going in, would cause the next team to build something specific wrong.

---

**The production sequence for this echo is inverted.**

Normally: find the surprise -> locate the signal -> assess the impact.
This echo: identify the failure -> locate the assumption that caused it -> find the correcting
signal.

Why: the failure scenario is the reason the echo exists. Starting from the failure anchors
every entry to a specific consequence. Entries that cannot be traced to a specific failure
scenario are omitted -- they may be interesting findings, but they are not the kind of
institutional memory this echo preserves.

---

**Step 1 -- Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft, review,
flow, trace, prove, listen, program, topic). Build a working list of what each was investigating
and what it found. Internal scaffolding only.

---

**Step 2 -- Enumerate failure modes.**

Read the signal record as a failure analyst. For each finding that contradicted a prior
assumption, answer:

> "If a new team read only the current design materials for `{topic}` -- the spec, the
> proposal, the drafts -- and then went to build it without knowing this finding, what would
> they build wrong? Name the specific component, flow, or decision that would fail or be built
> on a false premise."

Collect at least 3 failure scenarios before proceeding. Each must name:
- A specific component, flow, or decision
- The false assumption that would be carried into it
- What would go wrong as a result

A failure scenario that cannot name all three is too vague -- generalize upward or discard it.

---

**Step 3 -- Trace each failure to its correcting signal.**

For each failure scenario, locate the signal that revealed the correction:

```
Failure scenario: {component/flow/decision} fails because {false assumption}
Correcting signal: {artifact name or skill type}
What the signal showed: {the correction -- must directly oppose the false assumption}
Predictable from design materials alone? YES -> skip | NO -> proceed
```

A failure scenario with no traceable correcting signal, or one whose correction was
predictable from the design materials alone, is omitted from the echo.

---

**Step 4 -- Write echo entries.**

For each failure scenario with a traced correcting signal, produce one entry framed as a
correction for the next team -- not a discovery narrative.

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation. Name should encode the correction,
not the failure event.*

- **Source signal**: Specific artifact name or skill type that surfaces the correction.
- **Prior assumption**: What the current design materials imply. State as a belief a new team
  would carry: "A new team reading the spec would assume..."
- **Correction**: What the signal showed instead. Must directly contradict the prior
  assumption. One sentence.
- **What fails without this**: The specific component, flow, or decision the next team would
  build wrong if they carried the old assumption. One sentence. Must name something specific.

Minimum 2 entries.

---

**Step 5 -- Synthesize.**

Do the failure modes cluster around a shared false assumption or a category of design material
that consistently misleads? Write 2-4 sentences. Name any pattern you see. State its absence
if none is evident.

---

**Step 6 -- Forward guidance.**

1-3 sentences addressed to the next team. Derived directly from the failure scenarios in
Step 2. Register: "The `{topic}` design materials do not warn you that `{correction}`.
Without this knowledge, `{what fails}`."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 4-6. Steps 1-3 are execution scaffolding.

---

## V-03 -- Register-Menu Close axis

**Variation axis:** Phrasing register -- the forward guidance step provides a constrained menu
of four register-specific close templates. The model must select exactly one (or combine two)
and instantiate it with `{topic}`-specific content. Every bracketed slot must be filled with
specific content traceable to the echo; slots left generic are flagged as incomplete and
require revision before the artifact is written.

**Hypothesis:** R3 V-03 named two register templates as examples, leaving selection and
instantiation to the model. A model can produce a close that resembles a template while leaving
slots vague: "Before you start building `{topic}`, know that the design is more complex than
expected." The menu mechanism eliminates this by requiring the model to (a) name the template
it is using, (b) fill every bracketed slot with content traceable to a specific surprise or
artifact, and (c) flag any slot containing a generic phrase as a malformed fill. A generic
close cannot satisfy any template because each has required fills that force specificity.
Generic forwarding becomes structurally visible as an unfilled slot rather than a passable
approximation.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not expect?
It is institutional memory for the next team. Each surprise is named, sourced, and assessed
for its specific impact on the design direction. The echo closes with a forward guidance
statement the next team can use before they begin building -- not generic advice, but a
specific statement derived from the surprises in this echo.

---

**Forward Guidance Template Menu -- read before executing. Used in Step 5.**

Select exactly one template (or combine two if the surprises warrant it) and instantiate it
with specific content from this echo. Every bracketed slot must be filled with a specific
artifact name, component, correction, finding, or failure point traceable to an entry in this
echo. A slot filled with a generic phrase ("the design," "the system," "the assumptions") is
a malformed fill -- revise until every slot is specific and traceable.

**T-1 (Pre-build warning):**
> "Before you start building `[specific component or flow]`, know that `[specific correction
> from this echo]` -- `[specific signal artifact]` showed us that `[specific prior assumption]`
> is not how it actually works."

**T-2 (Spec gap):**
> "The `[specific design document or material]` for `{topic}` does not tell you that `[specific
> finding]`. You will encounter this when `[specific trigger condition or decision point]`."

**T-3 (Failure scenario):**
> "If you build `[specific component]` assuming `[specific prior assumption]`, it will fail at
> `[specific failure point]`. The correction is in `[specific signal artifact]`: `[one-sentence
> finding]`."

**T-4 (Velocity warning):**
> "The hardest part of `{topic}` is not `[what the design materials emphasize]` -- it is
> `[what the signals revealed instead]`. Build this in from the start; `[specific signal]`
> showed it cannot be retrofitted."

---

**Step 1 -- Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft, review,
flow, trace, prove, listen, program, topic). Note what each was investigating. Internal
scaffolding only.

---

**Step 2 -- Identify surprise candidates.**

Apply the prediction test to each noteworthy finding:

> "Would a person reading only the pre-investigation design materials have predicted this?"

YES -> confirmation. Not an echo entry. Belongs in `topic-story`.
NO -> surprise candidate.

Collect at least 3 candidates.

---

**Step 3 -- Write echo entries.**

For each candidate:

**[Surprise Name]**
*2-5 words, capitalized, reusable as a citation.*

- **Source signal**: Specific artifact name or skill type.
- **Prior assumption**: What was expected before this signal. One sentence.
- **Finding**: What the signal revealed -- must oppose the prior assumption. One sentence.
- **Design impact**: The specific component, flow, or decision this changes. One sentence
  minimum. Must name something specific.

Minimum 2 entries.

---

**Step 4 -- Synthesize.**

Write 2-4 sentences. Do 2 or more surprises share a root cause, reveal the same blind spot,
or together indicate a direction not previously visible? Name any pattern; state its absence
if none is evident.

---

**Step 5 -- Forward Guidance (register-menu instantiation).**

1. Name which template you are using (T-1, T-2, T-3, T-4, or a combination).
2. Instantiate it in full -- fill every bracketed slot with specific content from this echo.
3. Review: flag any slot not traceable to a specific surprise, artifact, component, or
   decision from Steps 3-4. Revise flagged slots before writing the artifact.

The forward guidance section of the artifact contains the instantiated template only -- not
the template label or review notes.

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 3-5. Steps 1-2 are execution scaffolding.

---

## V-04 -- Combination: Correction-Encoding Names + Forward-Failure Framing (C-17 + C-18)

**Variation axis:** Output format (correction-encoding name template) combined with lifecycle
emphasis (failure-mode-first impact framing), both validated as a pair before any entry is
expanded.

**Hypothesis:** C-17 (correction-encoding names) and C-18 (forward-failure framing) reinforce
each other structurally. A name that encodes the correction ("The Adoption Ceiling") already
points toward what was wrong. A "what fails without this" field that names the downstream
failure completes the arc: name the correction, describe what happens if the next team ignores
it. Together they form a closed loop that neither criterion achieves alone -- a correction-
encoding name without a failure consequence is a label; a failure scenario without a
correction-encoding name is a warning without a handle. Pairing them as co-validated
requirements before expansion tests whether the loop produces higher-quality C-03 (design
impact) as a side effect, and whether requiring both simultaneously produces more specific
entries than either criterion produces in isolation.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

**What the echo is.** The echo answers one question: what did we learn that we did not expect?
It is institutional memory for the next team. Each entry is a named correction: a prior belief,
the signal that overturned it, and the specific downstream failure that follows from carrying
the old belief into the build.

---

**Two structural requirements for every entry. Both are paired -- neither is optional.**

**Requirement 1 -- Correction-encoding name.** The name must encode the correction, not the
discovery. "The Scope Ceiling" encodes what was hit. "Lower Adoption Than Expected" describes
what happened. Names in the discovery form are malformed and require revision before expansion.

To derive a valid name:
1. State the prior assumption: "We assumed X."
2. State the correction: "The signal showed not-X."
3. Encode the correction: "The Not-X."
4. Compress and situate: "The Not-X: [Domain]."

**Requirement 2 -- Forward-failure framing.** The design impact field must state what the next
team would build wrong if they carried the old assumption -- not what changes, but what fails.
The field answers: "If the next team read only the current design materials and proceeded
without this correction, they would build `[specific component/flow/decision]` in a way that
`[specific failure mode]`."

A generic impact statement ("this affects the design," "this is worth noting") is a malformed
fill. Revise until the failure is specific and traceable to a named component or decision.

---

**Step 1 -- Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft, review,
flow, trace, prove, listen, program, topic). Note what each was investigating. Internal
scaffolding only.

---

**Step 2 -- Identify surprise candidates.**

Apply the prediction test to each noteworthy finding:

> "Would a person reading only the pre-investigation design materials have predicted this?"

YES -> confirmation. Not an echo entry. Belongs in `topic-story`.
NO -> surprise candidate.

Collect at least 3 candidates.

---

**Step 3 -- Paired Validation Gate.**

For each candidate, derive and validate both structural requirements before expansion:

```
Candidate: {one-sentence description}
Prior assumption: {what a reader of the design materials would have assumed}
Correction: {what the signal showed instead}

Draft name: The {Corrected Belief}: {Domain}
Name test:
  CORRECTION FORM -> VALID
  DISCOVERY FORM  -> INVALID -- revise

Draft failure: If the next team carries the old assumption, {component/flow/decision}
  would {specific failure mode}
Failure test:
  SPECIFIC (names a component, flow, or decision) -> VALID
  GENERIC ("the design would be affected" or similar) -> INVALID -- revise
```

Both must reach VALID before expansion. A candidate that cannot produce both a valid name
and a valid failure framing is omitted -- it may belong in `topic-story`.

The Paired Validation Gate log is execution scaffolding -- do not include it in the output.

---

**Step 4 -- Write echo entries.**

For each candidate with both VALID checks from Step 3:

**[Validated Name -- The {Corrected Belief}: {Domain}]**

- **Source signal**: Specific artifact name or skill type.
- **Prior assumption**: What the current design materials imply. One sentence.
- **Correction**: What the signal showed instead -- must directly contradict the prior
  assumption. One sentence.
- **What fails without this**: The specific component, flow, or decision the next team would
  build wrong if they carried the old assumption. One sentence. Must name something specific.

Minimum 2 entries.

---

**Step 5 -- Synthesize.**

Write 2-4 sentences. Do 2 or more corrections share a common false assumption or a category
of design material that consistently misleads? Name any pattern; state its absence if none
is evident.

---

**Step 6 -- Forward guidance.**

1-3 sentences addressed to the next team. Derived directly from the failure fields in Step 4.
Reference specific failures by component or decision. Register: "Before you build `[component]`,
know that `[correction]` -- without it, `[what fails]`."

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 4-6. Steps 1-3 are execution scaffolding.

---

## V-05 -- Full Combination: Typed Gate + Naming Gate + Failure Framing + Register-Menu Close
## (C-13 + C-16 + C-17 + C-18 + C-19)

**Variation axis:** All four new criteria (C-16 through C-19) combined with the typed gate from
R3 (C-13), each assigned to a structurally distinct moment in the production sequence.

**Hypothesis:** C-13 (typed gate), C-16 (structurally-enforced naming), C-17 (correction-
encoding names), C-18 (forward-failure framing), and C-19 (register-menu close) target
structurally distinct failure modes:
- C-13 prevents non-surprises from entering the echo at the filter stage
- C-16/C-17 enforce the naming step so discovery labels are structurally unproducible
- C-18 enforces the impact field so generic consequence statements are structurally unproducible
- C-19 enforces the close so generic forwarding is structurally visible as an unfilled slot

Because each criterion operates at a different structural moment, they compose without
interference. V-05 tests whether all five together produce a fully chain-enforced echo where
no structural moment permits a vague or malformed output to survive: the gate removes
non-surprises, the naming gate removes discovery labels, the failure test removes generic
impacts, and the template menu removes generic closes.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

---

**Anti-Pattern Catalog -- read before executing. You will cite these by name in Step 3.**

**finding-as-surprise substitution** -- an expected outcome stated in surprise language.
*Test:* "Would a reader of only the original design materials have predicted this?" YES -> cut.

**summary-in-disguise** -- a finding included for coverage, not because it contradicted an
assumption. Tell: your output as a whole could be described as "a summary of what the
investigation found."
*Test:* "Is this finding here because it overturned an assumption, or because it happened
and was notable?" If the latter -> cut.

**orphan-attribution** -- a genuine surprise attributed to "the research" or "the signals"
without a traceable artifact.
*Test:* "Can I name the specific artifact or skill type?" NO -> cut until you can.

---

**Name Template -- read before executing. Applied in Step 4.**

Every surprise name must follow this two-part form:

> **The [Corrected Belief]: [Domain]**

- **[Corrected Belief]**: Encodes what was wrong -- the correction, not the discovery.
- **[Domain]**: 1-3 words situating the correction.

**Malformed name test**: Names beginning with "Unexpected," "Surprising," "Higher/Lower Than
Expected," or describing an event rather than a corrected belief are discovery labels.
Revision required before inclusion.

---

**Forward Guidance Template Menu -- read before executing. Instantiated in Step 7.**

Select exactly one template (or combine two) and fill every bracketed slot with specific
content traceable to this echo. A slot filled with a generic phrase ("the design," "the
system") is a malformed fill -- revise until every slot is specific.

**T-1 (Pre-build warning):**
> "Before you start building `[component]`, know that `[correction]` -- `[signal]` showed
> that `[prior assumption]` is not how it actually works."

**T-2 (Spec gap):**
> "The `[design material]` for `{topic}` does not tell you that `[finding]`. You will
> encounter this when `[trigger condition]`."

**T-3 (Failure scenario):**
> "If you build `[component]` assuming `[prior assumption]`, it will fail at `[failure
> point]`. The correction is in `[signal artifact]`: `[one-sentence finding]`."

**T-4 (Velocity warning):**
> "The hardest part of `{topic}` is not `[what materials emphasize]` -- it is `[what signals
> revealed]`. Build this in from the start; `[signal]` showed it cannot be retrofitted."

---

**What the echo is.** It answers: what did we learn that we did not expect? Each entry is a
named correction -- typed through a filter gate, validated by name and failure framing, and
closed with a register-specific statement the next team can use before they begin.

---

**Step 1 -- Read signals.**

Read all signal artifacts from `simulations/{topic}/` across namespaces (scout, draft, review,
flow, trace, prove, listen, program, topic). Note what each was investigating. Internal
scaffolding only.

---

**Step 2 -- Assemble raw candidates.**

Scan the signals for noteworthy findings. One-sentence description per candidate. Do not
filter yet. Collect at least 4 candidates.

---

**Step 3 -- Typed Gate.**

You are now the **Skeptic**. Apply the Anti-Pattern Catalog to each candidate and issue a
verdict in this exact template:

```
Candidate: {one-sentence description}
Verdict: SURPRISE | CUT -- {anti-pattern label}
Rationale: {one sentence -- why this survives or which anti-pattern it triggers}
Destination: [SURPRISE -> echo] [CUT -> topic-story, not topic-echo]
```

Valid verdict states only:
- `SURPRISE`
- `CUT -- finding-as-surprise substitution`
- `CUT -- summary-in-disguise`
- `CUT -- orphan-attribution`

A bare `CUT` without an anti-pattern label is not valid. Multiple labels are valid when more
than one applies. Minimum 2 SURPRISE verdicts required.

The Skeptic log is execution scaffolding -- do not include it in the output artifact.

---

**Step 4 -- Paired Validation Gate.**

Receive the SURPRISE candidates from Step 3. For each, derive and validate both structural
requirements before expansion:

```
Candidate: {one-sentence description}
Prior assumption: {what a reader of the design materials would have assumed}
Correction: {what the signal showed instead}

Draft name: The {Corrected Belief}: {Domain}
Name test:
  CORRECTION FORM -> VALID
  DISCOVERY FORM  -> INVALID -- revise

Draft failure: If the next team carries the old assumption, {component/flow/decision}
  would {specific failure mode}
Failure test:
  SPECIFIC -> VALID
  GENERIC  -> INVALID -- revise
```

Both must reach VALID before expansion. A candidate that cannot pass both tests is demoted to
`topic-story`.

The Paired Validation Gate log is execution scaffolding -- do not include it in the output.

---

**Step 5 -- Write echo entries.**

For each candidate with both VALID checks from Step 4:

**[Validated Name -- The {Corrected Belief}: {Domain}]**

- **Source signal**: Specific artifact name or skill type.
- **Prior assumption**: What the current design materials imply. One sentence.
- **Correction**: What the signal showed instead -- must directly contradict the prior
  assumption. One sentence.
- **What fails without this**: The specific component, flow, or decision the next team would
  build wrong if they carried the old assumption. One sentence. Must name something specific.

Minimum 2 entries.

---

**Step 6 -- Synthesize.**

Write 2-4 sentences. Do 2 or more corrections share a common false assumption or a category
of design material that consistently misleads? Name any pattern; state its absence if none
is evident -- absence is itself information.

---

**Step 7 -- Forward Guidance (register-menu instantiation).**

1. Name the template you are using (T-1, T-2, T-3, T-4, or a combination).
2. Instantiate it in full -- fill every bracketed slot with specific content from this echo.
3. Review: flag any slot not traceable to a specific surprise, artifact, component, or
   decision from Steps 5-6. Revise flagged slots before writing the artifact.

The forward guidance section of the artifact contains the instantiated template only.

---

**Write the artifact** to `simulations/{topic}/{topic}-echo-{date}.md`.
Include Steps 5-7. Steps 1-4 are execution scaffolding.
