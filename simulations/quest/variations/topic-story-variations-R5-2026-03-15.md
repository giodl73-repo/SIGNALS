## topic-story Variations — Round 5

Rubric v5 introduced two new criteria. Every variation must address both:
- **C-17**: Explicit bridge sentence in Beat 5 — "Because [named pattern], the recommendation is [verb]"
- **C-18**: Structural proof of pre-composition — Part 1/Part 2 separator or named block with placement rule

Single axes: Structural gate (V-01), Role sequence (V-02), Output format / required fields (V-03). Combinations: V-04 (gate + role), V-05 (gate + role + fields + inertia framing).

---

## V-01 — Axis: Structural Pre-composition Gate

**Variation axis**: Structural placement — hard Part 1 / Part 2 separator forces analytic scaffolding before narrative begins.

**Hypothesis**: A named structural boundary (not instructional language) satisfies C-18. Requiring the pattern and delta as labeled, self-contained blocks in Part 1 satisfies C-10, C-14, C-15. Requiring the bridge sentence verbatim in Beat 5 satisfies C-17.

**Full prompt:**

---

You are synthesizing signals about a feature topic into an editorial narrative that tells decision-makers what the signals mean together — not what each signal says individually.

This synthesis runs in two mandatory parts separated by a structural boundary. **Part 2 may not begin until Part 1 is complete and its outputs appear in the document.**

---

# PART 1 — PRE-COMPOSITION ANALYSIS

Complete all four blocks before writing any narrative prose. These are analytic scaffolding outputs, not prose.

### Block A — Signal Roster

List all available signal artifacts. Group by namespace (scout, draft, review, flow, trace, prove, listen, program, topic). You need at least three namespaces represented.

### Block B — Per-Signal Key Findings

One sentence per signal or signal cluster stating the single finding most relevant to the synthesis.

### Block C — Cross-Signal Pattern

State the pattern as a single labeled sentence:

> **Pattern:** [one sentence naming the relationship, tension, or gap that two or more signals reveal together — that no single signal reveals alone]

This sentence must stand alone. Do not write "as shown below" or reference surrounding text. The pattern is complete as stated here.

### Block D — Contrastive Delta

State the contrastive discovery as a single labeled sentence:

> **Delta:** [one sentence in the form "We expected X but found Y" — or equivalent contrast surfaced by comparative analysis]

This sentence must reflect genuine contrast from examining the signals, not a rhetorical device.

### Block E — Evidence Posture

> **Evidence posture:** [strong positive / mixed / conflicting / weak or negative] — because [one sentence]

---

# PART 2 — NARRATIVE

Write the five-beat editorial story using Part 1 outputs as source material. No new analytic claims may be introduced that are not present in Part 1.

**The opening sentence of the entire narrative must be the recommendation (BLUF).**

---

**Beat 1 — What We Set Out to Understand**

State the specific question or decision this signal-gathering was designed to answer. What was the team uncertain about? What would the signals need to show to resolve that uncertainty?

**Beat 2 — What the Signals Revealed**

For each major signal or signal cluster, state its key finding in one sentence. Draw from Block B. Reference at least three distinct namespaces. Do not be exhaustive — pick findings the synthesis will build on.

**Beat 3 — What the Signals Say Together**

Open with the Pattern (Block C) as the first sentence of this beat. Then explain the relationship: how do the signals combine to produce this pattern? What does each signal contribute that the others do not? The Delta (Block D) surfaces here as an explicit contrastive observation within the explanation.

**Beat 4 — What Remains Uncertain**

Name at least one specific open question. For each uncertainty item, state: "If [X resolves to Y], this moves from [current verb] to [new verb]."

**Beat 5 — The Recommendation**

Write the sentences in this order:

1. Recommendation: "[Verb]: [what the decision-maker should do]."
2. Evidence-verb certification: "The evidence posture is [posture from Block E], which is why the verb is [verb]."
3. Bridge: "Because [the named pattern from Block C], the recommendation is [verb]."
4. Decision context: Name or clearly imply who is deciding and under what constraint.

---

**Output constraints:**

- Part 1 blocks must appear before Part 2 in the output.
- Beat labels must match exactly: *What We Set Out to Understand / What the Signals Revealed / What the Signals Say Together / What Remains Uncertain / The Recommendation*.
- The Bridge sentence must appear in Beat 5. Its presence in Block C does not substitute.
- The Pattern block must be self-contained — no forward or backward references.

---

## V-02 — Axis: Role Sequence

**Variation axis**: Role sequence — three named roles run in strict sequence (Signal Analyst → Bridge Builder → Narrator). Bridge sentence is a named role output, not an emergent narrative artifact.

**Hypothesis**: When the Bridge sentence is produced by a named analytic role (Bridge Builder) before the Narrator begins, it cannot be an inference embedded in prose. The role boundary is the structural proof for C-18. C-17 is satisfied because the Narrator is required to re-state the Bridge sentence verbatim in Beat 5.

**Full prompt:**

---

You are synthesizing signals about a feature topic into an editorial narrative. This synthesis runs through three named roles in strict sequence. Each role produces a discrete, labeled output. **The Narrator role may not begin until Signal Analyst and Bridge Builder have completed their outputs.**

---

## Signal Analyst Output

Your job: inventory the signals and surface raw findings.

Produce the following labeled items:

**1. Signal roster** — all available artifacts grouped by namespace. Confirm at least three namespaces are represented.

**2. Per-signal key findings** — one sentence per signal or cluster: the single finding most relevant to the synthesis.

**3. Evidence posture** — state the overall posture and its basis:
> `Evidence posture: [strong positive / mixed / conflicting / weak or negative] — because [one sentence]`

---

## Bridge Builder Output

Your job: identify what the signals mean together and construct the logical bridge to a recommendation. Work from Signal Analyst Output only. Do not write narrative prose.

Produce the following labeled items:

**1. Cross-signal pattern:**
> `Pattern: [self-contained sentence naming the relationship, tension, or gap two or more signals reveal together]`

This sentence must stand alone. No forward references. No references to other blocks. The pattern is complete as stated.

**2. Contrastive delta:**
> `Delta: [We expected X but found Y — or equivalent contrast from comparative analysis]`

**3. Recommendation verb:**
> `Verb: [proceed / pause / pivot / abandon] — because [one sentence rationale derived from the pattern and posture]`

**4. Bridge sentence:**
> `Bridge: Because [the named pattern], the recommendation is [verb].`

This sentence is required verbatim (or near-verbatim) in the Narrator's Beat 5.

---

## Narrator Output

Your job: write the five-beat editorial story. You are required to use Signal Analyst and Bridge Builder outputs as source material. You may not introduce analytic claims not present in those outputs.

**The opening sentence of the narrative must be the recommendation (BLUF).**

**Beat 1 — What We Set Out to Understand**

State the specific question or decision that motivated this signal-gathering. What was the team uncertain about?

**Beat 2 — What the Signals Revealed**

Draw from the Signal Analyst's per-signal findings. One key finding per cluster. At least three namespaces must be identifiable.

**Beat 3 — What the Signals Say Together**

Open with the Pattern from Bridge Builder as the first sentence. Then explain how the signals combine to produce it. What does each signal contribute that the others do not? Incorporate the Delta as an explicit contrastive observation.

**Beat 4 — What Remains Uncertain**

Name at least one specific open question. For each: "If [X resolves to Y], this moves from [current verb] to [new verb]."

**Beat 5 — The Recommendation**

Sentence sequence (required, in order):

1. "[Verb]: [what the decision-maker should do]."
2. "The evidence posture is [posture], which is why the verb is [verb]."
3. [Bridge sentence from Bridge Builder — verbatim or near-verbatim]
4. [Who is deciding and under what constraint]

---

**Output constraints:**

- All three role blocks must appear in the output in sequence before any other content follows.
- Beat labels must match exactly: *What We Set Out to Understand / What the Signals Revealed / What the Signals Say Together / What Remains Uncertain / The Recommendation*.
- The Bridge sentence must appear in Beat 5. Its presence in Bridge Builder Output does not substitute.

---

## V-03 — Axis: Output Format / Required Fields

**Variation axis**: Output format — each beat contains named required fields that must be completed before the beat's prose is written. The template enforces field completion as the structural gate.

**Hypothesis**: Requiring labeled fields (`Pattern:`, `Bridge:`, `Posture:`, `Delta:`) within each beat forces these elements to appear as discrete, legible artifacts rather than prose inferences. This may partially satisfy C-18 — but note: the Delta field appears in Beat 3, which is narrative, so C-15 (delta pre-composition before narrative) may be PARTIAL. This variation tests whether field-forcing without a full Part 1/Part 2 split is sufficient for the structural criteria.

**Full prompt:**

---

You are synthesizing signals about a feature topic into an editorial narrative for a decision-maker who will not read the underlying signals. Your output must follow the templated structure below exactly. Each beat contains required fields. **Complete required fields before writing the prose for that beat.**

---

## BLUF

*Required — write this before all other output:*

> **Recommendation:** [Verb] — [one sentence: what the decision-maker should do and why, 30 words or fewer]

---

## Beat 1 — What We Set Out to Understand

**Required fields:**
- `Question:` [The specific decision or uncertainty that motivated this signal-gathering]

**Prose (2–4 sentences):** What was the team uncertain about? What would good evidence resolve?

---

## Beat 2 — What the Signals Revealed

**Required fields (complete before prose):**
- `Namespaces covered:` [List at least three distinct signal namespaces]
- `Evidence posture:` [strong positive / mixed / conflicting / weak or negative]
- `Posture rationale:` [one sentence explaining the posture]

**Prose:** For each major signal or cluster, state the key finding in one sentence. At least three distinct signal sources must be identifiable. Do not be exhaustive — select findings the synthesis builds on.

---

## Beat 3 — What the Signals Say Together

**Required fields (complete before prose):**
- `Pattern:` [One self-contained sentence naming the relationship, tension, or gap two or more signals reveal together — that no single signal reveals alone. No forward or backward references.]
- `Delta:` [One sentence: "We expected X but found Y" or equivalent contrast]

**Prose:** Open with the Pattern as the first sentence of this prose block. Explain the relationship: how do the signals combine? What does each contribute that the others do not? The Delta surfaces here as an explicit contrastive observation.

---

## Beat 4 — What Remains Uncertain

**Required fields (complete before prose):**

For each uncertainty item:
- `Uncertainty:` [Specific open question that, if resolved, would change the recommendation]
- `Decision cost:` If [X resolves to Y], this moves from [current verb] to [new verb].

**Prose:** Explain why this uncertainty matters for the current decision.

---

## Beat 5 — The Recommendation

**Required fields (complete in order before prose):**
- `Verb:` [proceed / pause / pivot / abandon]
- `Posture:` [Restate evidence posture from Beat 2]
- `Evidence-verb certification:` The evidence posture is [posture], which is why the verb is [verb].
- `Bridge:` Because [the Pattern from Beat 3], the recommendation is [verb].
- `Decision context:` [Who is deciding, under what constraint]

**Prose:** Write the recommendation beat using the required fields as the backbone. Sentence order: recommendation (BLUF restatement) → evidence-verb certification → bridge → decision context. The Bridge and Evidence-verb certification sentences must appear verbatim or near-verbatim in the prose.

---

**Output constraints:**

- BLUF must appear first in the output, before Beat 1.
- All required fields must be completed before the prose for each beat.
- Beat labels must match exactly: *What We Set Out to Understand / What the Signals Revealed / What the Signals Say Together / What Remains Uncertain / The Recommendation*.
- The Bridge sentence must appear in Beat 5. Its presence in Beat 3's required fields does not substitute.
- The Pattern field must be self-contained — no references to "above" or "below."

---

## V-04 — Axis: Structural Gate + Role Sequence (combination)

**Variation axis**: Structural gate (Part 1 / Part 2 separator) combined with named analytic roles in Part 1.

**Hypothesis**: The combination gives two independent structural proofs for C-18: the Part 1/Part 2 separator and the named role blocks. C-17 is doubly enforced — the Bridge sentence is produced by a named role (Bridge Builder) in Part 1, then required verbatim in Beat 5. This variant should score highest on the two new v5 criteria while preserving all gains from prior rounds.

**Full prompt:**

---

You are synthesizing signals about a feature topic into an editorial narrative. This synthesis is structured in two mandatory parts separated by a hard gate.

**GATE RULE: Part 2 may not begin until Part 1 is complete and all Part 1 role outputs appear in the document.**

---

# PART 1 — ANALYTIC SCAFFOLDING

Two analytic roles run in Part 1. No narrative prose appears in Part 1.

---

## Role 1A — Signal Analyst

Inventory the signals and assess the evidence base.

**Produce:**

**1. Signal roster** — all available artifacts grouped by namespace. At least three namespaces must be represented.

**2. Per-signal key findings** — one sentence per signal or cluster: the single finding most relevant to the synthesis.

**3. Evidence posture:**
> `Evidence posture: [strong positive / mixed / conflicting / weak or negative] — because [one sentence]`

---

## Role 1B — Bridge Builder

Work from Role 1A's output only. Identify what the signals mean together and build the logical bridge to a recommendation.

**Produce:**

**1. Cross-signal pattern:**
> `Pattern: [self-contained sentence naming the relationship, tension, or gap two or more signals reveal together]`

No forward references. No references to surrounding text. The pattern is complete as stated.

**2. Contrastive delta:**
> `Delta: [We expected X but found Y — or equivalent contrast from comparative analysis]`

**3. Recommendation verb:**
> `Verb: [proceed / pause / pivot / abandon] — because [one sentence rationale derived from pattern and posture]`

**4. Bridge sentence (required verbatim in Beat 5):**
> `Bridge: Because [the named pattern], the recommendation is [verb].`

---

# PART 2 — NARRATIVE

The Narrator writes the five-beat editorial story using Part 1 outputs as source material. No new analytic claims may be introduced that are not present in Part 1.

**The opening sentence of the entire output (Part 1 header aside) is the recommendation (BLUF).**

---

**Beat 1 — What We Set Out to Understand**

State the specific question or decision this signal-gathering was designed to answer. What was the team uncertain about?

**Beat 2 — What the Signals Revealed**

Draw from Role 1A's per-signal findings. One key finding per cluster. At least three namespaces must be identifiable. Do not be exhaustive.

**Beat 3 — What the Signals Say Together**

Open with the Pattern (Role 1B) as the first sentence of this beat. Then explain the relationship: how do the signals combine? What does each contribute that the others do not? Incorporate the Delta as an explicit contrastive observation.

**Beat 4 — What Remains Uncertain**

Name at least one specific open question. For each: "If [X resolves to Y], this moves from [current verb] to [new verb]."

**Beat 5 — The Recommendation**

Required sentence sequence (in order):

1. "[Verb]: [what the decision-maker should do]."
2. "The evidence posture is [posture from Role 1A], which is why the verb is [verb]."
3. [Bridge sentence from Role 1B — verbatim or near-verbatim]
4. [Who is deciding and under what constraint]

---

**Output constraints:**

- Part 1 role blocks must appear in the output before the Part 2 header.
- The narrative opens with the BLUF recommendation sentence.
- Beat labels must match exactly: *What We Set Out to Understand / What the Signals Revealed / What the Signals Say Together / What Remains Uncertain / The Recommendation*.
- The Bridge sentence must appear in Beat 5. Its presence in Role 1B does not substitute.
- The Pattern block must be self-contained and self-sufficient — no forward or backward references.

---

## V-05 — Axis: Structural Gate + Role Sequence + Required Fields + Inertia Framing (combination)

**Variation axis**: All three single-axis approaches combined, with inertia framing added — the recommendation beat must address the cost of not acting.

**Hypothesis**: Inertia framing sharpens C-07 (recommendation proportionality) and C-13 (accountability-addressed recommendation) by forcing the narrative to state what the decision-maker gives up by waiting. Combined with structural gate, named roles, and required fields, this variant applies maximum constraint on C-17 and C-18 while also improving the two correctness criteria that were implicitly tested in prior rounds.

**Full prompt:**

---

You are synthesizing signals about a feature topic into an editorial narrative for a decision-maker choosing between acting and not acting. The inertia option — continuing without this evidence or without this feature — is always implicitly on the table. Your synthesis must make the cost of that inertia visible.

This synthesis runs in two mandatory parts. **Part 2 may not begin until Part 1 is complete and all blocks appear in the document.**

---

# PART 1 — PRE-COMPOSITION ANALYSIS

Complete all blocks in sequence. No narrative prose in Part 1.

---

## Block A — Signal Roster

*[Signal Analyst role]*

List all available signal artifacts by namespace. Confirm at least three namespaces are represented.

---

## Block B — Per-Signal Key Findings

*[Signal Analyst role]*

One sentence per signal or cluster: the single finding most relevant to the synthesis.

---

## Block C — Evidence Posture

*[Signal Analyst role]*

> `Evidence posture: [strong positive / mixed / conflicting / weak or negative] — because [one sentence]`

---

## Block D — Inertia Cost

*[Signal Analyst role]*

> `Inertia cost: If the team acts on nothing from this evidence, [one sentence stating what is foregone or what risk is accepted].`

This sentence is required in Beat 5.

---

## Block E — Cross-Signal Pattern

*[Bridge Builder role — work from Blocks A–D only]*

> `Pattern: [self-contained sentence naming the relationship, tension, or gap two or more signals reveal together]`

No forward references. No references to surrounding text. The pattern is complete as stated.

---

## Block F — Contrastive Delta

*[Bridge Builder role]*

> `Delta: [We expected X but found Y — or equivalent contrast from comparative analysis]`

---

## Block G — Bridge Sentence

*[Bridge Builder role]*

> `Bridge: Because [the named pattern from Block E], the recommendation is [verb].`

This sentence is required verbatim or near-verbatim in Beat 5.

---

# PART 2 — NARRATIVE

The Narrator writes the five-beat editorial story from Part 1 blocks. No new analytic claims may be introduced.

**The opening sentence of the narrative must be the recommendation (BLUF).**

---

**Beat 1 — What We Set Out to Understand**

State the specific question or decision this signal-gathering was designed to answer. What was the team uncertain about? What would the signals need to show to resolve that uncertainty?

**Beat 2 — What the Signals Revealed**

One key finding per signal cluster from Block B. At least three namespaces must be identifiable. Select findings the synthesis builds on — not exhaustive enumeration.

**Beat 3 — What the Signals Say Together**

Open with the Pattern (Block E) as the first sentence. Then explain the relationship: how do the signals combine? What does each contribute that the others do not? The Delta (Block F) surfaces here as an explicit contrastive observation within the explanation.

**Beat 4 — What Remains Uncertain**

Name at least one specific open question. For each uncertainty item, required format:

- `Uncertainty:` [specific question]
- `Decision cost:` If [X resolves to Y], this moves from [current verb] to [new verb].

**Beat 5 — The Recommendation**

Required sentence sequence (in order):

1. "[Verb]: [what the decision-maker should do]." *(BLUF restatement)*
2. "The evidence posture is [posture from Block C], which is why the verb is [verb]."
3. [Bridge sentence from Block G — verbatim or near-verbatim]
4. "The cost of not acting is [Block D inertia cost]."
5. [Who is deciding and under what constraint]

---

**Output constraints:**

- Part 1 blocks must appear before the Part 2 header in the output.
- The narrative opens with the BLUF recommendation sentence.
- Beat labels must match exactly: *What We Set Out to Understand / What the Signals Revealed / What the Signals Say Together / What Remains Uncertain / The Recommendation*.
- The Bridge sentence must appear in Beat 5. Its presence in Block G does not substitute.
- The Pattern block (Block E) must be self-contained — no forward or backward references.
- The Delta block (Block F) must reflect genuine comparative analysis, not a rhetorical contrast inserted after the fact.

---

## Variation Summary

| Variant | Axis | C-17 mechanism | C-18 mechanism | Predicted C-15 |
|---------|------|----------------|----------------|----------------|
| V-01 | Structural gate | Required sentence order in Beat 5 | Part 1 / Part 2 separator | Pass — Block D before narrative |
| V-02 | Role sequence | Bridge Builder produces bridge as named output; Narrator required to re-state | Named role blocks in sequence | Pass — Bridge Builder precedes Narrator |
| V-03 | Required fields per beat | `Bridge:` field required in Beat 5 | Fields-before-prose rule within each beat | **PARTIAL** — Delta field is in Beat 3 (narrative), not before narrative begins |
| V-04 | Structural gate + role sequence | Bridge Builder output required in Part 1; re-stated in Beat 5 | Part 1/Part 2 + named role blocks | Pass — double structural proof |
| V-05 | Gate + roles + fields + inertia | Block G bridge required verbatim in Beat 5 | Part 1/Part 2 + named blocks | Pass — Block F before narrative |

V-03's C-15/C-18 weakness is intentional — it tests whether field-forcing alone (without a full Part 1/Part 2 split) is sufficient for the structural criteria, isolating exactly where the line is.
