You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill opens with an inertia declaration naming three shortcuts this run will not take, declares paper type, acquires signals, writes a fast coverage draft — Gap first so Background scaffolds toward a known target — builds a unified boundary quality card across three incremental passes (coupling, bridge type+phrase, integration), then runs a hardened five-amendment pass with self-diagnosis first. Each section instruction explains why its constraint exists. Paper type declared in Phase 0 governs all sections. Three R5 enforcement layers (structured revision directive, bridge integration audit, self-diagnosis amendment) and three R6 structural changes (unified card, commitment framing, diagnosis-first order).

---

**Inertia declaration.** Before any work begins, name what a minimal-effort execution of this skill would do instead. The purpose is not to describe a failure mode — it is to commit, in advance, to the behaviors this run will not take.

> A nominal execution would: (1) skip signal acquisition and write the abstract from the topic name alone, producing generic content that could apply to any paper in the field; (2) frame the Gap section with a vague insufficiency claim ("X remains poorly understood") rather than naming the specific unresolved question the paper addresses; (3) comply nominally with the non-triviality guard by making surface wording changes that do not alter the informational content of the sentence.

> This run will instead: (1) execute Phase 1 signal acquisition and ground every section in the extracted content; (2) frame the Gap as a specific field-state claim that a knowledgeable reader would recognize as pointing to exactly this paper's contribution; (3) show substantive Before/After changes in Phase 5 that alter the informational content of the amended sentence, not just its phrasing.

> Confirm: [I confirm the above commitment before proceeding.]

---

**Phase 0 — Paper type declaration.** Before reading any signals, declare the paper type. This governs tense convention, Background register, Gap framing strength, and Implication form for every section that follows.

> Paper type: empirical / theoretical

- **Empirical**: Reports experimental or observational findings. Background establishes the domain condition that makes the measurement question urgent. Gap identifies a specific untested or unmeasured question. Claim uses past tense ("we found", "we observed"). Implication names a concrete practitioner decision or action enabled by the finding.
- **Theoretical**: Develops or extends a formal framework, argument, or model. Background establishes the conceptual landscape and its tensions. Gap identifies an unresolved construct or logical inconsistency. Claim uses present tense ("we show", "we argue", "we demonstrate that"). Implication names what the framework makes tractable that was previously intractable.

> Paper type: [empirical / theoretical]

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write — the goal is coverage, not correctness. Label each section.

**Gap** (write first — 1 sentence)
*Why gap-first:* A fixed Gap gives Background a precise target to scaffold toward. Background written first drifts into generic survey; Background written after the Gap ends exactly where the Gap begins.
*Why gap framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a field fact — a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question — no more, no less. For empirical papers: the domain condition that makes the measurement urgent. For theoretical papers: the conceptual tension that creates the logical gap.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Paper type was declared in Phase 0. Confirm it now and write the Claim with the correct tense.
> Paper type: [confirmed from Phase 0 — do not change]
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information. Readers use Method to judge whether the evidence supports the Claim — a named method with scope gives them that judgment.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* "We found improvements" is unfalsifiable. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* Vague implications ("broad implications for the field") are unmemorable and unverifiable. One concrete enabling action is honest and actionable.
What can now be done, decided, or understood? For empirical: name a practitioner decision enabled. For theoretical: name a research or design question now tractable.

> [Implication sentence]

---

**Boundary quality card — Pass 1: Coupling status.** After drafting all six sections, fill the Coupling column for each boundary before proceeding. Leave the remaining columns blank.

| Boundary | Coupling: COUPLED / WEAK / REVISE | Bridge type | Bridge phrase (3-8 words) | Integrated? Y / N |
|----------|-----------------------------------|-------------|---------------------------|-------------------|
| Background -> Gap | [fill now] | — | — | — |
| Gap -> Claim | [fill now] | — | — | — |
| Claim -> Method | [fill now] | — | — | — |
| Method -> Result | [fill now] | — | — | — |
| Result -> Implication | [fill now] | — | — | — |

Coupling question per boundary:
- **Background -> Gap**: Does Background establish the **exact** conditions that make this Gap feel inevitable — not just the general topic area?
- **Gap -> Claim**: Does Claim directly resolve the **specific** open question stated in Gap — not a nearby or related question?
- **Claim -> Method**: Does Method name the **specific** mechanism or approach used to establish the Claim — not a generic description of the field?
- **Method -> Result**: Does Result report the finding produced by **this** Method — not a different or more general finding?
- **Result -> Implication**: Does Implication name what **this** Result enables — not a general insight the field already knew?

For each boundary marked WEAK or REVISE, complete a revision directive before proceeding:

> Boundary: [name the boundary pair]
> Deficient section: [Background / Gap / Claim / Method / Result / Implication]
> Deficiency: [one sentence naming exactly what the section lacks that the adjacent section requires]
> Before: [the deficient section text as drafted]
> After: [revised section text that addresses the deficiency]
> Coupling status: [re-verify — COUPLED / still WEAK]

Update the card's Coupling column after each revision. Do not proceed until all five boundaries show COUPLED.

---

**Boundary quality card — Pass 2: Bridge type and phrase.** Fill the Bridge type and Bridge phrase columns for each boundary. Identify the semantic type first.

**Semantic type vocabulary:**
- **contrast** — Prior section established something; next section names what it fails to resolve. ("yet it remains unclear whether")
- **causation** — Prior section created conditions; next section's claim is the direct causal consequence. ("we therefore demonstrate that")
- **resolution** — Prior section named a problem; next names the mechanism used to address it. ("using a controlled experiment with")
- **escalation** — Prior section stated what was expected; next names a finding that exceeds or sharpens it. ("finding not merely X but Y")
- **application** — Prior section reported a finding; next converts it to a concrete action. ("enabling practitioners to")

Do not use the same type for more than two consecutive boundaries. These bridge phrases are the merge glue for Phase 3.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the bridge phrases from the boundary quality card as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Boundary quality card — Pass 3: Integration status.** Fill the Integrated? column. Integration is Y if the bridge phrase from Pass 2 was used verbatim or incorporated with minor grammatical adaptation that preserves the semantic type. Integration is N if the bridge phrase was dropped or replaced with a stock connector ("however", "additionally", "in this paper") that does not express the intended type relationship.

Complete card — all five columns filled:

| Boundary | Coupling | Bridge type | Bridge phrase | Integrated? |
|----------|----------|-------------|---------------|-------------|
| Background -> Gap | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Gap -> Claim | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Claim -> Method | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Method -> Result | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |
| Result -> Implication | [from Pass 1] | [from Pass 2] | [from Pass 2] | [fill now] |

If any bridge is N: revise the merged paragraph to restore the bridge phrase at that boundary. Show the revised paragraph with word count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Five-amendment pass (diagnosis-first).** Amendment 1 is a self-diagnosis sweep — it runs before the targeted amendments so the model reads the abstract without knowing which specific weaknesses will be fixed next. Amendments 2-5 are the four targeted categories. For each amendment, write the Before text, write the After text, then confirm the change is non-trivial. A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Self-diagnosis (runs first)**
Read the merged abstract before any targeted fixing. Identify the single sentence or element most likely to cause a reviewer to pause, question the contribution, or request clarification. Name it as a specific one-sentence claim about the weakness — not a general quality assessment.
> Diagnosis: [name the specific weakest element and why it weakens the abstract]
> Before: [the sentence or element]
> After: [the improved version]
> Non-trivial: Y / N

**Amendment 2 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 3 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 4 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 5 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified], paper_type: [empirical/theoretical from Phase 0]
