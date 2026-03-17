Written to `simulations/quest/variations/topic-echo-variations-R1-2026-03-15.md`.

---

# Variations: `topic:echo` -- Round 1

**Rubric:** v1 | Single-axis: Output Format, Phrasing Register, Lifecycle Emphasis | Combos: Role Sequence + Lifecycle, Inertia + Output Format

---

## V-01 -- Output Format axis

**Hypothesis:** A sparse fill-in-blank template with zero prose instruction shifts cognitive load entirely to the writer. Heavily annotated forms teach the model what to do; a sparse template forces it to demonstrate that it already knows. Drift exposes a gap no amount of instruction would have caught.

**Key mechanism:** Minimal slots — Name, Source, Prior Assumption, Finding, Design Impact — with one enforcement rule embedded as a negative gate ("could this have been written before the signals?"). The Cross-Signal Pattern block is required but unfenced — the model must produce it without being coached on what to put there.

---

## V-02 -- Phrasing Register axis

**Hypothesis:** Two-condition formal definition ("a finding F qualifies as a surprise if and only if...") eliminates the boundary ambiguity between surprise and confirmation. The failure mode is a boundary problem; formal constraint language is the correct tool for boundary problems.

**Key mechanism:** Explicit two-condition definition with strict dominance — if in doubt, classify CONFIRMATION. Step 3 adds a sufficiency check that forbids relaxing the definition to hit the count. The register is technical-precise throughout; no narrative warmth.

---

## V-03 -- Lifecycle Emphasis axis

**Hypothesis:** Three gates (inventory, qualify, document) with 60% of instruction space on Gate 2 produces higher precision than longer phase sequences. The skill lives or dies at the qualify gate. Giving it maximum space makes it impossible to rush.

**Key mechanism:** Gate 2 runs a first-person internal monologue ("I am standing before this investigation began...") as the challenge format. The challenge is quoted in full — the model cannot abbreviate it. Gate 3 is short and mechanical; the weight is all on Gate 2.

---

## V-04 -- Combination: Role Sequence + Lifecycle Emphasis

**Hypothesis:** An Archaeologist role surfaces the prior assumption for each signal before any surprise testing occurs. This makes the Prior Assumption field researchable rather than inferred — which is the hardest part of C-09 (counterfactual awareness). The Chronicler receives a prepared ledger and runs the gate against it, enforcing lifecycle through role handoff rather than prose instruction.

**Key mechanism:** Archaeologist produces a (signal, prior assumption) ledger as working memory. Chronicler receives the ledger and applies the surprise gate — never re-derives assumptions on the fly. The Counterfactual field in the table is optional but explicitly placed, making C-09 achievable without being required.

---

## V-05 -- Combination: Inertia Framing + Output Format

**Hypothesis:** Showing the wrong output as a labeled concrete example creates a comparison target the model can hold against its own draft. Pairing it with a tight template whose slots cannot accommodate story-shaped content completes the constraint: the model knows what wrong looks like and has no structural slot to put it in.

**Key mechanism:** A 6-sentence fake "wrong output" example is labeled and dissected — it names the specific failure pattern (confirmation buried inside story-shaped output). The output template is rendered as a literal fenced code block with no room for narrative additions. The forbidden additions are listed explicitly: no introduction, no summary, no narrative between entries.

---

**Axis coverage summary:**

| Variation | Primary Axis | Secondary Axis |
|---|---|---|
| V-01 | Output Format (sparse template) | — |
| V-02 | Phrasing Register (formal/constraint) | — |
| V-03 | Lifecycle Emphasis (3-gate, gate-weighted) | — |
| V-04 | Role Sequence (Archaeologist + Chronicler) | Lifecycle Emphasis |
| V-05 | Inertia Framing (labeled wrong example) | Output Format |

**Rubric coverage prediction:** V-01 enforces C-01/C-02/C-03/C-04 structurally. V-02 enforces C-01 definitionally. V-03 front-loads C-01 gate weight. V-04 enables C-09 (counterfactual) by making prior assumptions explicit. V-05 most directly addresses the named failure mode that causes C-01 misses.
s would have
  predicted. One sentence.}
- *Actual (post-signal)*: {What the signal revealed. Must violate the Expected clause.}
- *Design impact*: {What specifically must change in the design as a result. Name the
  artifact, decision, flow, or assumption. Not permitted: "this is worth noting,"
  "this matters," "consider this carefully."}

Step 5 -- Synthesis. After all entries, write 2-4 sentences: do the surprises share
a root violation of the two-condition definition -- i.e., the same assumption was
false in multiple signals? Name the shared assumption if one exists.

Write the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.

---

## V-03 -- Lifecycle Emphasis axis

**Hypothesis:** A three-gate execution model -- inventory, qualify, document -- with
maximum weight on the qualify gate produces higher precision than longer phase sequences.
More phases diffuse attention; the qualify gate is where the skill lives or dies. Giving
it 60% of the instruction space makes the gate impossible to rush through.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`. Execute three gates in order. Do not skip
forward. Each gate has a clear done condition before the next opens.

---

**Gate 1 -- Inventory.** Done when complete.

Read signal artifacts from `simulations/{topic}/`. For each artifact, note:
- Artifact slug
- Namespace (scout, draft, review, flow, trace, prove, listen, program, topic)
- One phrase: the question this signal was investigating

Gate 1 is done when every artifact has been read and noted. This inventory is working
memory -- do not include it in the final artifact.

---

**Gate 2 -- Qualification.** This is the critical gate. Done when every finding has
been ruled on.

Review the findings across all signals. For each finding that seems worth naming,
run the following challenge in full -- do not abbreviate it:

> "I am standing before this investigation began. I have read the spec, the proposal,
> and the design materials for `{topic}`. I have not seen any of the signals.
>
> If someone told me this finding right now, would I be surprised?
>
> - YES, this contradicts or significantly extends what I believed: this is a
>   **SURPRISE CANDIDATE**. Hold it.
> - NO, this confirms what I expected, or I could have deduced it from the design:
>   this is a **CONFIRMATION**. Release it. (Confirmations belong in `topic-story`.)"

Apply this challenge to every candidate. A candidate must survive it to proceed to
Gate 3. You need a minimum of 2 SURPRISE CANDIDATES to proceed. If you have fewer,
re-examine the signals -- you may have treated genuine surprises as confirmations.
Do not relax the challenge to make the count.

---

**Gate 3 -- Documentation.** Done when every SURPRISE CANDIDATE has a complete entry.

For each SURPRISE CANDIDATE, write:

**{Surprise Name}** -- a distinct 2-5 word handle, capitalized, citable in future
conversation without additional context.

- **Source**: {artifact slug or skill slug. Traceable. Specific.}
- **Prior assumption**: {what the pre-signal design posited or implied}
- **Finding**: {what the signal actually revealed -- must oppose the prior assumption}
- **Design impact**: {the specific component, flow, or decision this forces to change}

After all entries, add a **Pattern Note** (2-4 sentences): do the SURPRISE CANDIDATES
share a root cause? Reveal the same design blind spot? Name any pattern. If there is
none, say so explicitly -- isolated surprises are a valid and important finding.

Write the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include only Gate 3 output in the artifact. Gates 1 and 2 are execution scaffolding.

---

## V-04 -- Combination: Role Sequence + Lifecycle Emphasis

**Hypothesis:** A handoff-based execution model -- Archaeologist unearths hidden
assumptions per signal, then Chronicler applies the surprise gate and documents what
survives -- achieves two things simultaneously: the lifecycle phases are enforced by
the role transition (not just by instruction), and the Archaeologist's pre-work makes
the prior-assumption field in each entry researchable rather than inferred. The hardest
part of C-09 (counterfactual awareness) is knowing what you assumed. The Archaeologist
makes that explicit before the gate runs.

---

### Prompt Body

You are executing `topic-echo` for `{topic}`. Two roles run in sequence with an
explicit handoff. Complete each role fully before beginning the next.

---

**Role 1: Archaeologist**

Your job is to surface what was assumed before the signals existed. You do not judge
whether anything was surprising yet -- that is the next role's work.

Read each signal artifact from `simulations/{topic}/`. For each, produce:

- Artifact slug
- One sentence: what this signal was investigating
- One sentence: what the original design or spec implied would be true in this area
  (the implicit assumption the signal was testing)

Present this as a list. This is the Archaeologist's output -- the assumption ledger.

This output is working memory. Do not include it in the final artifact.

---

**Handoff.** The Archaeologist's output -- a list of (signal, prior assumption) pairs --
is passed to the Chronicler. The Chronicler does not re-read assumptions from the spec.
They use the ledger the Archaeologist has already surfaced.

---

**Role 2: Chronicler**

Receive the Archaeologist's assumption ledger. For each (signal, assumption) pair,
examine the signal's actual finding. Apply the surprise gate:

> Did the signal's finding contradict, substantially extend, or overturn
> the prior assumption surfaced by the Archaeologist?
>
> YES: retain as SURPRISE. NO: release as CONFIRMATION.

You need at least 2 surprises. If fewer survive the gate, flag it -- do not produce
padding entries.

For each SURPRISE, write one entry:

**{Surprise Name}** -- 2-5 words, capitalized, citable

| Field | Content |
|---|---|
| Source Signal | {artifact slug or skill slug} |
| Prior Assumption | {from Archaeologist's ledger -- not inferred now} |
| Finding | {what the signal actually revealed, in opposition to the assumption} |
| Design Impact | {specific component, decision, or flow that must change} |
| Counterfactual | {optional -- "Without this signal, we would have [specific wrong path]"} |

After all entries, write a **Synthesis** section (2-4 sentences): what do the
surprises tell the next team collectively? Is there a shared assumption the design
was wrong about? Name it if so.

Write the artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
Include only the Chronicler's entries + Synthesis. The Archaeologist's ledger stays
in execution scaffolding.

---

## V-05 -- Combination: Inertia Framing + Output Format

**Hypothesis:** Showing the wrong output as a concrete labeled example -- not just
describing it -- creates a comparison target the model can hold against its own draft.
The failure mode for `topic-echo` is producing a well-written story with surprise
language sprayed over it. A labeled wrong example makes that pattern immediately
recognizable in one's own output. Pairing this with a tight output template whose
slots cannot accommodate story-shaped content completes the constraint: the model
knows what wrong looks like and has no structural slot to put it in.

---

### Prompt Body

You are writing `topic-echo` for `{topic}`.

---

**The wrong output looks like this** (do not produce this):

> ## Summary of Investigation
>
> The team investigated throttle behavior, permissions, and lifecycle flows for `{topic}`.
> Key findings included confirmation that throttle sequencing works as designed, that
> permissions behave correctly under load, and that lifecycle events fire in the
> expected order. One unexpected result: the resilience fallback triggered earlier than
> anticipated under certain race conditions. Overall the investigation confirmed the
> design direction.

This is a story. It is a useful document. It is not an echo. Notice what it does:
it reports findings, confirms expectations, and buries one genuine surprise in a
sentence alongside confirmations. The surprise is present but indistinguishable from
routine reporting. A future team cannot extract it as actionable institutional memory.

The echo inverts this. It contains only the surprises -- isolated, named, sourced,
and assessed. A reader should be able to read the echo and know, in under two minutes,
what assumptions to discard before they begin.

---

**Execution.**

Read the signal artifacts from `simulations/{topic}/`. Apply the prediction test to
every finding: would someone who had read only the design materials -- before any
signals were gathered -- have predicted this finding? If yes, it is a confirmation.
Do not include confirmations. Include only findings that would have surprised a
pre-investigation reader.

Minimum 2 surprises must survive the prediction test.

---

**Output template.** Produce exactly this structure. Do not add narrative between
entries. Do not add an introduction. Do not add a summary. The template is the
entire artifact.

```
# Echo: {topic}
*{date} | Signals: {comma-separated artifact slugs}*

---

## {Surprise Name}

- **Source:** {artifact slug}
- **Assumed:** {what was believed before this signal}
- **Found:** {what the signal revealed -- must contradict Assumed}
- **Consequence:** {what specifically changes in the design -- name the thing}

---

## {Surprise Name}

[repeat block]

---

## Pattern

{2-4 sentences. Do the surprises cluster? Name the pattern if yes.
State absence if no. Mandatory -- do not omit.}
```

Write the completed artifact to `simulations/{topic}/{topic}-echo-{date}.md`.
