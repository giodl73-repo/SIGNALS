---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 9
rubric: v1
rubric_max: 100
---

# Variations: `topic:echo` -- Round 9 (Rubric v1)

**Rubric:** v1 | **Date:** 2026-03-15

---

## Design Context

This is a first-round variation pass against the v1 rubric. The v1 rubric defines the
essential structure of `topic-echo`:

- Surprise-only content (C-01) -- the hardest constraint to enforce without a filter
- Named surprises, >=2 words (C-02) -- reusable citation labels, not prose descriptions
- Signal attribution per surprise (C-03) -- traceable to a named artifact
- Design impact per surprise (C-04) -- specific, not generic
- Minimum 2 surprises (C-05) -- the floor for usefulness

Recommended and aspirational criteria (C-06 through C-10) reward expectation-delta
framing, cross-signal synthesis, future-team guidance, impact ranking, and rules of thumb.

The core design problem at v1 is the surprise filter: a naive execution of topic-echo
produces a findings summary with some surprises salted in. C-01 fails because the model
defaults to completeness rather than selectivity. The five variations below test different
structural mechanisms for enforcing selectivity.

**R9 design axes -- what each variation isolates:**

| Variation | Primary axis | Hypothesis |
|-----------|-------------|------------|
| V-01 | Role sequence | Assumption Archivist role before signal reading creates explicit baseline for C-01 filter |
| V-02 | Output format | Table schema makes C-01/C-03/C-04 missing fields immediately visible |
| V-03 | Phrasing register | Conversational register activates surprise retrieval rather than summary production |
| V-04 | Lifecycle emphasis + inertia framing | Hard phase gates + default-design baseline combines filter enforcement with contrast sharpness |
| V-05 | Role sequence + output format + inertia framing | Combined: archivist role + inertia baseline + structured list; tests full-rubric coverage at cost of prompt complexity |

---

## V-01 -- Role Sequence: Assumption Archivist First

**Variation axis:** Role sequence

**Hypothesis:** The surprise filter (C-01) fails when the model reads signals and then
asks "which of these were surprising?" That question is answered relative to an implicit,
unwritten sense of what was expected -- and implicit baselines drift toward "notable" rather
than "contradictory." An explicit Assumption Archivist role, run before signal reading,
forces the team prior into written form. The contrast test then operates against a specific
cataloged claim, not a vague sense. Predicted effect: C-01 pass rate improves because the
filter is applied against documented priors, not against what "seems surprising."

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

The echo answers one question: **what did we learn that we did not expect?** It is not a
findings report. It is institutional memory for the next team that walks this path -- a
record of what would have surprised them, sourced and assessed.

---

**Role 1 -- Assumption Archivist**

Before reading any signal artifacts, read the design materials for `{topic}`: the spec,
proposal, prior drafts, and any stated assumptions.

Produce a Prior Belief Catalog: a numbered list of specific claims the team held as true
before the investigation began. Each entry must be falsifiable -- a proposition that could
have been confirmed by the signals but might not have been. Goals and intentions are not
prior beliefs.

Format:

```
Prior Belief Catalog
1. We believed: [specific falsifiable claim]
2. We believed: [specific falsifiable claim]
...
```

Write at least 4 entries. This catalog is internal scaffolding and does not appear in the
final artifact. Do not read signal artifacts until this step is complete.

---

**Role 2 -- Signal Reader**

Read all signal artifacts from `simulations/{topic}/` across namespaces: scout, draft,
review, flow, trace, prove, listen, program, topic.

For each artifact, write one sentence: what did this signal find? One sentence per
artifact, flatly stated. Internal scaffolding -- does not appear in the final artifact.

---

**Role 3 -- Surprise Filter**

Compare each signal finding against the Prior Belief Catalog. A finding qualifies as a
surprise only if it directly contradicts a numbered entry in the catalog.

For each finding, complete: `[finding] contradicts Prior Belief [N]: [belief text]`.

If a finding does not contradict any cataloged belief, discard it. It may be notable; it
is not a surprise.

If fewer than 2 findings contradict cataloged priors, return to Role 1 and expand the
Prior Belief Catalog. Internal scaffolding -- does not appear in the final artifact.

---

**Role 4 -- Echo Composer**

For each qualified surprise, write one entry:

**[Surprise Name]** -- 2 words minimum, capitalized, specific enough to retrieve this
insight by name in six months.

- **Source:** The specific signal artifact or skill type that surfaced this finding (e.g.,
  `flow-resilience`, `prove-interview`, `scout-feasibility`).
- **We assumed:** The prior belief this finding contradicted. One full sentence.
- **We found:** What the signal showed instead. One sentence. Must directly contradict
  "We assumed."
- **Design impact:** One specific implication for how `{topic}` should be designed.

Minimum 2 entries.

---

**Synthesis (after all entries):**

1. If 2 or more surprises share a root cause, state it in one sentence. Label it
   `Pattern:`.
2. Write one statement addressed to the next team. Something specific they should know
   before they begin. Label it `For the next team:`.

---

**Output artifact:** `simulations/{topic}/{topic}-echo-{date}.md`

Include only: surprise entries and synthesis. Roles 1-3 are internal scaffolding and must
not appear in the artifact.

---

## V-02 -- Output Format: Table-Driven Surprise Registry

**Variation axis:** Output format

**Hypothesis:** Prose format allows C-03 (signal attribution) and C-04 (design impact) to
be elided inside flowing sentences -- the reader cannot verify their presence without
parsing. A fixed-column table makes each criterion a discrete cell: an empty or vague cell
is immediately auditable. The table schema also enforces C-02 (named surprise) by forcing a
distinct label per row rather than embedding the name inside a paragraph. Predicted effect:
C-02, C-03, C-04 compliance improves; C-01 compliance unchanged (the filter logic is the
same, only the output structure differs).

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

The echo is a **Surprise Registry**: a structured record of findings that contradicted what
the team believed before the investigation. It is not a summary of what was found. Every
entry must represent a genuine surprise -- a finding that overturned a specific prior
belief, not a finding that was merely notable or unexpected in tone.

---

**Step 1 -- Read.**

Read all signal artifacts from `simulations/{topic}/` across all namespaces (scout, draft,
review, flow, trace, prove, listen, program, topic). Also read the design materials for
`{topic}` (spec, proposal, prior drafts). Internal step -- do not include in the output.

---

**Step 2 -- Surprise test.**

For each notable finding, apply two tests before it can enter the registry:

**Test 1 -- Predictability:** "Would a reader of only the original design materials for
`{topic}` have predicted this finding before the investigation began?"
- YES: discard. This is a finding, not a surprise.
- NO: proceed to Test 2.

**Test 2 -- Contradiction:** "Does this finding contradict a specific belief the team held
before running the signals -- not 'it was unusual,' but 'it contradicted something we
thought was true'?"
- YES: this finding qualifies for the registry.
- NO: discard.

Internal step -- do not include in the output.

---

**Step 3 -- Build the registry.**

Produce the following table. Minimum 2 rows. Every cell is required.

| Surprise Name | Source Signal | We Assumed | We Found | Design Impact |
|---|---|---|---|---|
| >=2-word label, specific and reusable | Named artifact or skill type from `simulations/{topic}/` | One falsifiable prior belief the team held | The actual finding, one sentence, that contradicts "We Assumed" | One specific design decision this surprise changes, constrains, or opens |

Field rules:

- **Surprise Name:** Specific enough to cite in a design conversation without rereading the
  artifact. Not "Unexpected Behavior" -- name the behavior.
- **Source Signal:** Must be a named signal artifact or named skill type. No orphan
  surprises.
- **We Assumed:** A falsifiable claim -- something that could have been true but was not.
  Not a goal, hope, or area of uncertainty.
- **We Found:** One sentence. Must directly contradict "We Assumed."
- **Design Impact:** One concrete decision, constraint, or opened option. Must name
  something specific in `{topic}`.

---

**Step 4 -- Synthesis (below the table).**

After the table, add the following labeled sections:

**Pattern** (recommended): One sentence connecting 2 or more rows to a shared root cause
or blind spot. If no pattern is present, write `Pattern: none identified.`

**For the next team** (recommended): One forward-facing statement about what future
investigators should check first, given these surprises.

**Rules of thumb** (optional): Up to 3 one-liners, <=20 words each. Each must trace to a
specific row in the table by Surprise Name.

---

**Output artifact:** `simulations/{topic}/{topic}-echo-{date}.md`

Table and synthesis section only. No preamble, no executive summary.

---

## V-03 -- Phrasing Register: Conversational Retrospective

**Variation axis:** Phrasing register

**Hypothesis:** Formal imperative framing ("produce entries matching the following schema")
licenses a documentary mode -- the model composes a polished report that happens to
contain some surprises. Conversational framing activates a different register: closer to
a team retrospective, where the natural response is "what broke our assumptions?" rather
than "what is worth documenting?" C-01 compliance may improve because the mode itself
filters for genuine surprise. C-06 (expectation-delta framing) may improve because the
conversational template naturally produces "we thought X, but actually Y." Trade-off: less
structural scaffolding for C-03/C-04 compliance.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

Here is the situation. The team just finished running signals on `{topic}`. They
investigated across multiple namespaces. They found things. Some findings confirmed what
they already believed. Some didn't.

The echo captures only the ones that didn't.

---

**Before you read the signals, read what the team knew going in.**

Read the design materials for `{topic}` -- spec, proposal, prior drafts. You are
reconstructing the mental model the team had *before* the signals. What did they think
was true? What were they confident about?

Hold this picture while you read the signals. You don't need to write it out as a list.
But you need it clearly in mind.

---

**Now read the signals.**

Read all signal artifacts from `simulations/{topic}/` -- everything across scout, draft,
review, flow, trace, prove, listen, program, topic namespaces.

As you read, pay attention to the moments of friction: findings that a pre-investigation
reader would not have predicted, findings that contradict something the team thought they
knew. Not "interesting" or "notable" -- genuinely contradictory. Something that, if you'd
seen it in the spec, you would have said "that's not right."

---

**Write the surprises.**

For each genuine surprise, write one entry in this format:

**[Surprise Name]**
*2-5 words, capitalized. Specific enough that you could recall what this surprise was about
in six months without rereading the artifact.*

*We assumed:* What the team believed before this signal ran. A specific claim, not "we
didn't fully think about this area."

*We found:* What the signal showed instead. One sentence. It should plainly contradict
"We assumed."

*From:* The specific signal artifact or skill that surfaced this finding.

*What this changes:* One concrete implication for how `{topic}` gets designed.

---

Write at least 2 surprises.

Before writing each entry, ask: "If someone read only the spec and proposal, would they
have predicted this?" If yes, cut it. The echo is ruthless: expected findings belong in
the signal artifacts, not here.

---

**Close with two things.**

First: if two or more surprises share a common root -- some assumption that made the team
wrong about multiple things at once -- say so in one sentence.

Second: write one sentence addressed directly to the next team. Not a summary. A warning,
a redirect, or an instruction. Something they should know before they start `{topic}`.

---

**Output artifact:** `simulations/{topic}/{topic}-echo-{date}.md`

Surprise entries and closing items only. No headers beyond the surprise names. No preamble.

---

## V-04 -- Combined: Lifecycle Emphasis + Inertia Framing

**Variation axes:** Lifecycle emphasis + inertia framing

**Hypothesis:** Two problems compound at v1. First, without hard phase gates, the surprise
filter and the echo composition phases collapse into a single pass -- the filter fails
silently because it runs simultaneously with selection. Second, without a concrete baseline,
"would a reader have predicted this?" is answered relative to a fuzzy implicit prior.
Inertia framing -- "what would have shipped if no signals were run?" -- replaces the fuzzy
prior with a concrete Default Design. Phase gates then enforce that the Default Design is
written before signals are read, and that the classification step completes before
composition begins. Predicted effect: C-01 shows the largest improvement because both
failure modes are addressed together; C-06 improves because "We assumed" is grounded in
the Default Design rather than reconstructed post-hoc.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

The echo captures what changed because of the signals. Not what was found. Not what was
interesting. Specifically: what would have been wrong -- what would have shipped broken or
misaligned -- if the team had not run the investigation.

---

**PHASE A -- Default Design and Prior Inventory**

Complete Phase A before beginning Phase B.

Read the design materials for `{topic}` (spec, proposal, prior drafts, stated assumptions).

Produce two outputs. Write both before continuing:

**A1 -- Default Design (3-6 sentences):** What would `{topic}` have looked like if the
team had committed to the design without running any signals? What assumptions would have
gone unchallenged? This is the inertia baseline -- the design the signals are measured
against.

**A2 -- Prior Belief List:** 4 or more specific falsifiable claims the Default Design
encodes as true. Format: `1. We believed: [claim]`.

> **Phase A gate:** A1 and A2 are written. Do not read signal artifacts until this gate
> is cleared.

---

**PHASE B -- Signal Reading**

Complete Phase B before beginning Phase C.

Read all signal artifacts from `simulations/{topic}/` across all namespaces: scout, draft,
review, flow, trace, prove, listen, program, topic.

Produce:

**B1 -- Signal Finding List:** One sentence per artifact reviewed, stating its primary
finding.

> **Phase B gate:** B1 is written. Do not begin classification until every reviewed
> artifact has a B1 entry.

---

**PHASE C -- Inertia Classification**

Complete Phase C before beginning Phase D.

For each item in B1, apply this test against A1 (Default Design) and A2 (Prior Belief
List):

> "If the Default Design had shipped without this signal, would the design have been
> wrong, incomplete, or misaligned in a specific, nameable way?"

- YES: label `SURPRISE -- contradicts A2:[N]` and name the affected A2 prior.
- NO (the signal confirmed or was neutral to the Default Design): label `CONFIRMED`.

Write the labeled classification for every B1 finding.

> **Phase C gate:** Every B1 item is labeled SURPRISE or CONFIRMED. SURPRISE items
> include the A2 reference. Do not begin Phase D until all B1 items are classified.
> If fewer than 2 SURPRISE labels exist, return to Phase A and expand A2.

---

**PHASE D -- Echo Composition**

For each SURPRISE item from Phase C, write one entry:

**[Surprise Name]** -- 2-5 words, capitalized, specific and reusable.

- **Source:** Named signal artifact or skill type.
- **We assumed:** The A2 prior belief this finding contradicted. Full sentence, falsifiable.
- **We found:** The actual finding. Must directly contradict "We assumed."
- **Default design gap:** What would have been wrong or missing if the Default Design had
  shipped without this signal. One sentence.
- **Design redirect:** One specific change to `{topic}`'s design direction that this
  surprise produces.

Minimum 2 entries. Phase D is the only content included in the output artifact.

---

**PHASE E -- Synthesis**

Add the following after all Phase D entries:

**Pattern** (if applicable): One sentence identifying a shared gap in the Default Design
that links 2 or more surprises.

**For the next team:** One specific instruction -- what should the next team's Default
Design assume differently, given these surprises?

**Impact ranking** (optional): Label each surprise HIGH / MEDIUM / LOW based on its
effect on the Default Design's viability.

**Rules of thumb** (optional): Up to 3 one-liners, <=20 words each, each traceable by
name to a Phase D entry.

---

**Output artifact:** `simulations/{topic}/{topic}-echo-{date}.md`

Phase D entries and Phase E synthesis only. Phases A, B, and C are internal scaffolding.

---

## V-05 -- Combined: Role Sequence + Output Format + Inertia Framing

**Variation axes:** Role sequence + output format + inertia framing

**Hypothesis:** V-01 through V-04 each target one or two rubric failure modes in isolation.
V-05 tests whether full-rubric coverage (C-01 through C-10) is achievable at the cost of
prompt complexity. The combination is:

1. **Role sequence (from V-01):** Assumption Archivist role runs before signal reading,
   creating an explicit written baseline. A Surprise Auditor role applies the inertia test
   as a discrete committed step.
2. **Inertia framing (from V-04):** The Assumption Archivist writes a Default Design that
   anchors "what the team believed" in a concrete artifact, not a reconstruction.
3. **Output format (from V-02):** A structured named-list format (not a table) combines
   the discoverability benefit of V-02 with the narrative flow needed for C-06 and C-08.

Predicted effect: highest overall rubric score; risk is that complexity creates new failure
modes (role collapse, over-long scaffolding that crowds out the output).

---

### Prompt Body

You are executing `topic-echo` for `{topic}`.

The echo is institutional memory. It captures what changed because of the signals -- what
would have been wrong if the team had shipped the design they walked in with. Not a
summary. Not a findings report. A record of surprises: named, sourced, and assessed.

---

**Role 1 -- Default Design Archivist**

Before reading any signal artifacts, read the design materials for `{topic}`: spec,
proposal, prior drafts, stated assumptions.

Produce two outputs before proceeding to Role 2:

**Default Design (3-6 sentences):** What would `{topic}` have looked like if the team had
committed to design without running signals? What assumptions would have gone unchallenged?

**Prior Belief Catalog (numbered list, 4+ entries):**

```
Prior Belief Catalog
1. We believed: [specific falsifiable claim the Default Design encodes as true]
2. We believed: [...]
...
```

Entries must be falsifiable propositions -- claims that could have been confirmed but
might not have been. Goals, intentions, and uncertainty statements are not prior beliefs.

Do not read signal artifacts until the Default Design and Prior Belief Catalog are written.
Both are internal scaffolding.

---

**Role 2 -- Signal Reader**

Read all signal artifacts from `simulations/{topic}/` across namespaces: scout, draft,
review, flow, trace, prove, listen, program, topic.

For each artifact, write one sentence: what did this signal find? Internal scaffolding.

---

**Role 3 -- Surprise Auditor**

For each signal finding, apply the inertia test against the Default Design and Prior Belief
Catalog:

> "If the Default Design had shipped without this signal, would the design have been wrong
> or misaligned in a specific, nameable way -- and does this finding contradict a specific
> numbered entry in the Prior Belief Catalog?"

- YES to both: `SURPRISE -- contradicts Prior Belief [N].`
- NO to either: `CONFIRMED or neutral. Discard.`

Write the classification for every signal finding before proceeding. Internal scaffolding.

Minimum 2 SURPRISE verdicts required. If fewer than 2, return to Role 1 and expand the
Prior Belief Catalog.

---

**Role 4 -- Echo Writer**

For each SURPRISE verdict from Role 3, write one entry:

---

**[Surprise Name]**
*2-5 words, capitalized. Specific enough to retrieve by name in six months.*

- **Source:** Named signal artifact or skill type from `simulations/{topic}/`.
- **We assumed:** The Prior Belief Catalog entry this finding contradicted. Full sentence,
  falsifiable.
- **We found:** The actual finding. One sentence that directly contradicts "We assumed."
- **Default design gap:** What would have shipped wrong or missing if this signal had not
  run. One sentence.
- **Design redirect:** One specific change to `{topic}`'s design direction.

---

Minimum 2 entries.

---

**Synthesis (after all entries):**

**Pattern:** One sentence identifying a shared root cause or Default Design gap that
links 2 or more surprises. If none, write `Pattern: none identified.`

**For the next team:** One direct instruction -- what should the next team assume
differently in their Default Design, given these surprises? Address them directly.

**Impact ranking** (optional): Label each surprise HIGH / MEDIUM / LOW by its effect on
Default Design viability.

**Rules of thumb** (optional, up to 3): One-liners <=20 words each. Each must trace to a
named surprise entry.

---

**Output artifact:** `simulations/{topic}/{topic}-echo-{date}.md`

Role 4 entries and synthesis only. Roles 1-3 are internal scaffolding and must not appear
in the artifact.
