## `topic-story` Prompt Variations — Round 3

---

### V-01 — Single axis: Output format (template with explicit slot placeholders)

**Hypothesis**: Providing a rigid named-slot template forces structural compliance with C-01, C-02, C-10, C-13 before the AI touches prose — structural requirements become fill-in-the-blank, not editorially derived.

---

```
You are writing a signal story for a feature topic. A signal story is NOT a
summary of each artifact — it is an editorial synthesis in the author's voice
that interprets what the signals say together.

You have access to the signal artifacts collected for this topic. Read them,
then fill in the template below EXACTLY as structured. Do not rename sections.
Do not reorder sections. Do not omit sections.

---

## Signal Story: {TOPIC}

**Recommendation** _(first sentence — complete this before writing anything else)_:
> {One sentence: [proceed|pause|pivot|abandon], naming the decision and the
> decision-maker role it addresses. Example: "A product lead deciding whether to
> staff this feature in Q3 should proceed — the signals are positive on user need
> and technically feasible within scope."}

---

### What We Set Out To Understand

{2–3 sentences. State the original question or decision this signal work was
opened to answer. Name the uncertainty that existed before gathering signals.}

---

### What The Signals Revealed

{One bullet per signal source or namespace represented. Format each bullet as:
**[Signal type / namespace]** — {Key finding in one sentence. Not exhaustive.
The one thing this signal contributed that no other signal contributed.}

Minimum three distinct signal namespaces or artifact types must appear.}

---

### The Pattern

> **{A single, labeled, self-contained claim. This sentence must be readable
> without consulting the bullets above or the recommendation below. Name the
> relationship, tension, or gap that only becomes visible when the signals are
> read together — not what any single signal says alone. Format: "The pattern:
> [claim]." Example: "The pattern: users articulate a strong need and the
> technical path is clear, but adoption depends on a workflow change that the
> current spec does not address — that gap is the primary risk."}**

{1–2 sentences of elaboration if needed. Do not repeat the labeled claim.}

---

### What Remains Uncertain

{One bullet per open question. Each bullet must state:
(a) the specific question that is unresolved, AND
(b) what resolving it would change about the recommendation verb — e.g., "if
this resolves to X, the recommendation moves from pause to proceed."

Generic hedges ("more research may be needed") without a named direction fail.}

---

### The Recommendation

{2–4 sentences. State the recommendation verb (proceed / pause / pivot /
abandon). Name the role making this decision and the constraint they are under
(time, resource, information). Cite the pattern by name or by summary as the
explicit reason for this verb. A reader must be able to identify the sentence
where the pattern produces the recommendation.}

---

COMPLETION RULE: Before submitting, verify:
1. The Recommendation section opens the document (the block above the first
   horizontal rule is the recommendation, not context-setting).
2. The Pattern block reads as a complete claim with no forward or backward
   references to the surrounding narrative.
3. Each uncertainty bullet names a direction the recommendation would shift.
4. The final Recommendation paragraph names a role and a constraint.
```

---

### V-02 — Single axis: Phrasing register (imperative/command)

**Hypothesis**: Imperative directives ("Do X", "Name Y", "Write Z") produce more reliable compliance than descriptive guidance ("the output should contain X") because they eliminate the AI's interpretive latitude on whether a requirement is optional.

---

```
Write a signal story for the topic below. Follow every instruction in order.

A signal story synthesizes signals into a narrative in the author's voice. It
is NOT a list of artifact summaries. It interprets what the signals reveal
together.

---

STEP 1 — WRITE THE OPENING RECOMMENDATION FIRST.

Before writing the story, write a single sentence that states your
recommendation (proceed, pause, pivot, or abandon) and names the role who is
making this decision and what constraint they face. Anchor the entire story to
this sentence. Example format: "A [role] deciding [decision] under [constraint]
should [verb] — [one-line reason]."

Do not write any context, setup, or hedging before this sentence.

---

STEP 2 — USE THESE FIVE SECTION HEADERS EXACTLY.

Write five sections in this order:

1. What We Set Out To Understand
2. What The Signals Revealed
3. What The Signals Say Together
4. What Remains Uncertain
5. The Recommendation

Do not rename them. Do not merge them. Do not reorder them.

---

STEP 3 — BEFORE WRITING SECTION 3, STOP AND NAME THE PATTERN.

Before composing the "What The Signals Say Together" section, write a single
labeled sentence in this format:

   The pattern: [claim].

This sentence must:
- Name a relationship, tension, or gap that requires at least two signals to be
  true simultaneously.
- Be readable on its own without consulting the sections above or below it.
- Contain no phrases like "as described above", "as shown below", or "see
  the following".

Place this labeled sentence as the first element of section 3. Write the
section prose after it.

---

STEP 4 — IN SECTION 2, COVER AT LEAST THREE NAMESPACES.

Name the signal source or namespace for each finding. At minimum, reference
three distinct signal types. One sentence per signal source. The sentence
states the key finding that source contributed — not a summary of the artifact.

---

STEP 5 — IN SECTION 4, ATTACH A DECISION-COST TO EVERY UNCERTAINTY.

For each open question you name, state explicitly: if this resolves one way,
the recommendation moves to [verb]; if it resolves the other way, the
recommendation stays at [verb] or moves to [verb]. Name the direction. Do not
write uncertainties without a stated consequence.

---

STEP 6 — IN SECTION 5, CITE THE PATTERN AS THE REASON FOR THE VERB.

Write: "Because [restate the pattern in brief], the recommendation is
[verb]." The bridge between the pattern and the recommendation must be explicit.
A reader must identify the sentence where the pattern causes the
recommendation.

Name the role who is deciding. Name the constraint they face (time, resource,
information). Do not write the recommendation as a finding ("the signals
suggest") — write it as a decision ("a [role] deciding [X] should [verb]").

---

STEP 7 — VERIFY BEFORE SUBMITTING.

Check: Does the opening sentence name a role, a constraint, and a verb?
Check: Does the pattern block contain no references to surrounding text?
Check: Does every uncertainty item name a direction the verb would shift?
Check: Does section 5 explicitly cite the pattern as the cause of the verb?

If any check fails, revise before submitting.
```

---

### V-03 — Single axis: Lifecycle emphasis (mandatory analytic pre-pass before writing)

**Hypothesis**: Requiring a separate analytic step — identify the pattern, map signal coverage, list uncertainties with decision-costs — before starting the narrative forces C-10 (pre-composition pattern artifact) and C-14 (self-sufficiency) because the pattern was named analytically, not discovered mid-prose.

---

```
You are writing a signal story. A signal story synthesizes all gathered signals
into a narrative interpreting what they say together. It is authored in an
editorial voice — not a list of artifact summaries.

There are two phases. Complete Phase 1 in full before beginning Phase 2.

---

## PHASE 1 — ANALYTIC PRE-PASS (do not write the story yet)

Work through the following steps. Output each step as a short working note.
These notes will not appear in the final story — they are your preparation.

**A. Pattern identification**
Read the available signal artifacts. Identify the cross-signal claim — the
relationship, tension, or gap that only becomes visible when two or more
signals are read together. Write it as one sentence starting with "The
pattern:". This sentence is your analytic anchor. Every section of the story
must be consistent with it.

**B. Signal inventory**
List the distinct namespaces or artifact types represented. Count them. If
fewer than three distinct signal sources exist, note that coverage is thin and
the synthesis will need to acknowledge this.

**C. Delta inventory**
Identify at least one place where the signals surprised or contradicted the
initial assumption about the topic. Write it as: "We expected [X], but found
[Y]." If no surprises exist, note that the story will lack contrastive
substance.

**D. Uncertainty inventory**
List the open questions that remain after the signals. For each, write:
"If [question] resolves to [A], the recommendation moves to [verb]. If it
resolves to [B], the recommendation stays at [verb]."

**E. Recommendation pre-commitment**
Before writing a word of narrative, commit to the recommendation verb:
proceed, pause, pivot, or abandon. State the verb and the decision-maker role.
State the constraint they face (time, resource, information). This pre-commitment
is binding — the story must be consistent with it.

---

## PHASE 2 — WRITE THE STORY

Now write the signal story using the five required sections:

1. **What We Set Out To Understand**
2. **What The Signals Revealed**
3. **What The Signals Say Together**
4. **What Remains Uncertain**
5. **The Recommendation**

Apply the following rules:

**Opening rule**: The recommendation verb must appear in the opening paragraph
of the story — not at the end. The story does not build to a conclusion. It
opens with the conclusion and the narrative supports it.

**Section 3 rule**: The first element of "What The Signals Say Together" must
be the labeled pattern sentence you wrote in Phase 1 Step A, verbatim or with
only minor refinement. It must be self-contained — readable without any
surrounding prose. Do not embed the pattern in flowing text. Do not add forward
or backward references inside the pattern sentence.

**Section 2 rule**: Cover the namespaces you inventoried in Phase 1 Step B.
One sentence per source. Each sentence states the one thing that source
contributed that no other source showed.

**Section 4 rule**: Use the uncertainty items from Phase 1 Step D verbatim or
refined. Each item names a direction the recommendation verb would shift.

**Section 3 delta rule**: Incorporate the "we expected X, but found Y"
contrastive statement from Phase 1 Step C. Place it in section 3 or as a
transition into section 3. Do not bury it. Do not make it inferential.

**Section 5 rule**: Cite the pattern explicitly as the reason for the
recommendation verb. Name the role. Name the constraint. The bridge between
pattern and recommendation must be a sentence a reader can point to.

---

Begin with Phase 1.
```

---

### V-04 — Combination: Accountability-addressed + Pattern block self-sufficiency (directly targeting v3 Pattern A and Pattern B)

**Hypothesis**: Naming the two v3 excellence patterns explicitly as output requirements — with the exact failure mode described — produces the output properties more reliably than embedding them as abstract criteria. Failure modes described directly reduce the interpretive surface.

---

```
Write a signal story for the topic below.

A signal story is an editorial synthesis in the author's voice. It interprets
what the signals say together — NOT a summary of each artifact.

---

## REQUIRED STRUCTURE

Use these five sections in order. Do not rename or omit any.

1. What We Set Out To Understand
2. What The Signals Revealed
3. What The Signals Say Together
4. What Remains Uncertain
5. The Recommendation

---

## TWO CRITICAL OUTPUT PROPERTIES

The following two properties distinguish a usable story from an excellent one.
Read them carefully. Each includes the exact failure mode to avoid.

---

### Property 1 — The Pattern Block Is Self-Sufficient

Section 3 must open with a single labeled sentence in this format:

   The pattern: [claim].

This sentence must convey the full cross-signal claim on its own. Test: cover
the rest of the document and read this sentence alone. If a reader needs the
surrounding narrative to understand what the claim means, the block fails.

**Failure modes to avoid**:
- "As described in the signals above, the pattern is..." — backward reference, fails.
- "The pattern, which will be important for the recommendation below, is..." — forward reference, fails.
- "The pattern is complex but..." — incomplete claim that defers to prose, fails.
- A pattern that is only an inference from the flowing narrative (never stated as a labeled sentence) — fails.

The claim must name a relationship, tension, or gap that requires two or more
signals to be true simultaneously.

---

### Property 2 — The Recommendation Is Decision-Addressed, Not Finding-Stated

Section 5 (The Recommendation) and the opening paragraph must frame the
recommendation as a decision for a named role under a named constraint — not
as a finding the reader observes.

**Failure modes to avoid**:
- "The signals suggest that X may be a viable path forward." — finding-stated, fails.
- "Based on the evidence, it appears the feature has merit." — finding-stated, fails.
- "The recommendation is to proceed." — no decision-maker, no constraint, fails.

**Passing format**:
"A [role] deciding [decision] with [constraint] should [proceed|pause|pivot|abandon]
because [one-line reason tied to the pattern]."

Name the role. Name the constraint (time, budget, information availability,
deadline). The reader must know who is deciding and what they are up against.

---

## ADDITIONAL REQUIREMENTS

**Bottom line up front**: The recommendation verb appears in the opening
paragraph of the story. The story opens with the conclusion. It does not build
to a conclusion.

**Signal coverage**: Section 2 references at least three distinct signal
namespaces or artifact types. One sentence per source: the key finding that
source contributed that no other source showed.

**Specific uncertainty**: Section 4 names at least one open question that, if
resolved, would change the recommendation verb. State the direction: "if this
resolves to X, the recommendation moves from [verb] to [verb]."

**Pattern-to-recommendation bridge**: Section 5 contains an explicit sentence
where the pattern (stated in Section 3) causes the recommendation verb. A
reader must be able to point to the sentence.

**Delta moment**: Somewhere in the story, write at least one "we expected X,
but found Y" or equivalent contrastive statement. Do not make this inferential.
State it directly.

---

## FINAL CHECK

Before submitting, verify:
- The opening paragraph contains the recommendation verb, a named role, and a named constraint.
- "The pattern:" sentence reads as a complete, standalone claim.
- The pattern sentence contains no phrases referencing other parts of the document.
- Every uncertainty item names a direction the verb would shift.
- The recommendation paragraph names the pattern as the explicit reason for the verb.
```

---

### V-05 — Combination: Role sequence + Inertia framing

**Hypothesis**: Running two sequential roles — an Analyst who extracts the pattern from the signals, then an Author who writes the story against the Analyst's output — forces the pattern to be pre-composed (C-10, C-14) and produces a stronger narrative arc (C-08). Adding inertia framing (what the team was already doing before these signals) makes the recommendation proportionality (C-07) and delta surfacing (C-09) structurally unavoidable.

---

```
You will complete this task in two sequential roles. Do not merge the roles.
Complete Role 1 entirely before beginning Role 2.

---

## ROLE 1 — SIGNAL ANALYST

You are a signal analyst. Your job is NOT to write the story. Your job is to
extract the analytic inputs the story author will need. Produce the following
four outputs and label each clearly.

---

**OUTPUT A — Inertia statement**
What was the team already doing, planning, or assuming BEFORE these signals
were gathered? Name the default path — the status quo, the existing plan, the
assumption that was in place. Write one sentence: "Before these signals, the
team was [doing/assuming/planning X]."

This is the inertia the signals either confirm, challenge, or redirect.

**OUTPUT B — The pattern (labeled, self-contained)**
Read all available signal artifacts. Write the cross-signal claim as one
sentence starting with "The pattern:". The sentence must:
- Name a relationship, tension, or gap that requires two or more signals.
- Be readable without consulting any other part of this document.
- Contain no references to "above" or "below" or "as described."

If you cannot name the pattern without forward or backward references, the
pattern is not yet identified — try again.

**OUTPUT C — Signal inventory with key findings**
List each distinct signal namespace or artifact type present. For each, write
one sentence: the key finding that source contributed that no other source
contributed. Minimum three distinct sources.

**OUTPUT D — Uncertainty table**
List the open questions that remain. For each, write:
- The specific question.
- If resolved one way: recommendation moves to [verb].
- If resolved the other way: recommendation stays at [verb] / moves to [verb].

**OUTPUT E — Recommendation pre-commitment**
Based on Outputs A–D, commit to a recommendation verb: proceed, pause, pivot,
or abandon. Name the role making this decision. Name the constraint they face.
State whether the signals confirm the inertia path (Output A) or redirect it —
this is the delta. Write: "We expected [inertia state from A], but the signals
[confirm it / redirect to X / complicate it by Y]."

---

## ROLE 2 — SIGNAL AUTHOR

You are the story author. Using the outputs from Role 1 as your inputs, write
the signal story. Do not re-derive the pattern. Do not re-analyze the signals.
Write the story from Role 1's outputs.

**Structure** — use these five sections in order:

1. **What We Set Out To Understand**
2. **What The Signals Revealed**
3. **What The Signals Say Together**
4. **What Remains Uncertain**
5. **The Recommendation**

**Opening rule**: The recommendation verb from Role 1 Output E must appear in
the opening paragraph. Open with the conclusion. Do not build to it.

**Section 3 rule**: Place Role 1 Output B verbatim (or with minor copy
refinement) as the first element of this section, labeled "The pattern:". Do
not paraphrase the pattern into flowing prose. The labeled block must remain
self-contained.

**Section 3 inertia rule**: Include Role 1 Output E's contrastive statement
("We expected X, but the signals...") in this section or as a transition into
it. This is the delta moment — make it explicit.

**Section 2 rule**: Draw directly from Role 1 Output C. One sentence per
source. The finding sentence, not a summary of the artifact.

**Section 4 rule**: Draw from Role 1 Output D. Each uncertainty item names the
direction the verb would shift. Do not soften the consequence language.

**Section 5 rule**: Name the role from Role 1 Output E. Name the constraint.
Write the explicit bridge: "Because [pattern in brief], the recommendation is
[verb]." A reader must be able to point to this sentence as the place where the
pattern causes the recommendation. Frame the recommendation as a decision for
the named role — not as a finding.

---

Begin with Role 1.
```

---

### Variation Summary

| # | Axis | Hypothesis | Key structural bet |
|---|------|------------|--------------------|
| V-01 | Output format | Slot template → structural compliance before prose | Named placeholder slots force C-01, C-02, C-10, C-13 |
| V-02 | Phrasing register | Imperative voice → less interpretive latitude | "Do X" vs "output should contain X" |
| V-03 | Lifecycle emphasis | Analytic pre-pass → pattern pre-composed before writing | Phase 1 produces the labeled block; Phase 2 uses it |
| V-04 | Pattern A + Pattern B | Naming failure modes directly → higher hit rate | Exact failure mode descriptions for C-13 and C-14 |
| V-05 | Role sequence + Inertia framing | Analyst → Author separation → pattern structurally pre-composed | Inertia baseline makes delta surfacing and proportionality structural |
