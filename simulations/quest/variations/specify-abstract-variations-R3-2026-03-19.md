Written to `simulations/quest/variations/specify-abstract-variations-R3-2026-03-19.md`.

---

## Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Role sequence: Gap drafted before Background (C-14) | Gap-first gives Background a fixed scaffold target. Single-axis addition to V-05 base. |
| **V-02** | Phrasing register: constraint reasoning per section (C-11) | V-03 R2 proved this earns C-11; V-05 proved hardened amendments earn 88+. Graft V-03's why-explanations into V-05's infrastructure. |
| **V-03** | Lifecycle structure: explicit connective bridge phase before merge (C-12) | C-12 was structural debt — universal fail because no R2 variation added a dedicated bridge step. New Phase 2b composes one 3-8 word phrase per section boundary before the merge. |
| **V-04** | Gap-first + constraint reasoning (V-01 + V-02 axes) | V-03 R2 earned C-11 + C-14 but its weak amendments dragged it to 80. V-05 solved amendments. Combination should earn C-11 + C-14 without losing the 92-pt floor. |
| **V-05** | Full synthesis: gap-first + constraint reasoning + connective bridges | Theoretical ceiling. Three distinct mechanisms in three distinct phases: Phase 2 order (C-14), Phase 2 instruction register (C-11), new Phase 2b (C-12). All additive; none conflicts with Phase 5. |

**Predicted R3 scores under v3 rubric:**

| Variation | Base | C-14 | C-11 | C-12 | Predicted |
|-----------|------|------|------|------|-----------|
| V-01 | 92 (V-05 floor) | +2 | — | — | ~94 |
| V-02 | 92 | — | +4 | — | ~96 |
| V-03 | 92 | — | — | +2 | ~94 |
| V-04 | 92 | +2 | +4 | — | ~98 |
| V-05 | 92 | +2 | +4 | +2 | ~100 |

**Key trade-offs:** V-02 has the highest single-axis upside (+4 from C-11) because constraint reasoning is the highest-weighted remaining aspirational gap. V-03 is the riskiest — bridge phrases may be formulaic stock connectors rather than substantive transitions. V-05 adds three mechanisms to a single prompt; length may dilute Phase 5 execution.
ithout losing V-05's 92-pt floor. |
| **V-05** | Full synthesis: Gap-first + constraint reasoning + connective bridges (all three single-axis additions) | Ceiling candidate. Addresses every remaining aspirational gap: C-12 via bridge phase, C-11 via constraint reasoning, C-14 via gap-first order. Risk: prompt depth may dilute later-phase execution. |

---

## V-01 — Gap-First Draft Order

**Variation axis**: Role sequence (Gap drafted before Background in Phase 2; Background scaffolded toward the known Gap)
**Hypothesis**: V-05 (R2 best at 88/92) writes sections in Background-first order, which allows Background to drift into generic domain context. Writing Gap first makes the gap explicit before Background is written — Background then has exactly one job: make the gap feel inevitable. Targets C-14 without changing any other phase. C-15 preserved (coverage-only draft). C-16 preserved (prose coherence as named amendment).

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill writes a fast coverage draft from your signals, then runs a hardened four-amendment pass to reach final quality. The draft phase targets coverage only — no inline self-correction. The amendment phase carries the full precision load.

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write the six sections in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct as you write — the goal is coverage, not correctness. Label each section. Speed over precision.

Write in this order:

**Gap** (write this first — 1 sentence)
What is still unresolved, unknown, or contested in the field? State it as a field fact: "X remains unresolved." Do not use goal language ("we aimed to study X") — goal language implies the paper might have failed; gap language states a fact about the field.

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
Now that the Gap is fixed, write exactly the context that makes this gap feel inevitable. Do not start with "In recent years." Make the Background end where the Gap begins — one causal handoff.

> [Background text]

**Claim** (1 sentence)
What does this paper show, demonstrate, or argue? Active voice. Past tense for empirical results ("we found"), present tense for theoretical contributions ("we show").

> [Claim sentence]

**Method** (1-2 sentences)
Name the specific method, dataset, model, or approach. No vague "we investigated." Include scope or sample size if available.

> [Method text]

**Result** (1-2 sentences)
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
What can now be done, decided, or understood that couldn't before? One concrete enabling action.

> [Implication sentence]

---

**Phase 3 — Merge and count.** Reorder to standard abstract sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-02 — Constraint Reasoning Throughout

**Variation axis**: Phrasing register (each section instruction includes a one-sentence rationale explaining why the constraint exists)
**Hypothesis**: V-03 (R2) was the only variation to earn C-11 (constraint reasoning) — 4 pts that no other variation touched. V-03 scored only 80 because its amendment phase was unmodified. Grafting V-03's why-explanations into V-05's hardened amendment infrastructure should earn C-11 without losing any of V-05's amendment performance. Also adds an explicit tense-type declaration at the Claim step (the C-09 mechanism V-02-R2 discovered). Risk: per-section rationales add instruction length — attention may dilute in Phase 5.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill writes a fast coverage draft from your signals, then runs a hardened four-amendment pass to reach final quality. The draft phase targets coverage only — no inline self-correction. The amendment phase carries the full precision load.

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft.** Write all six sections. Do not self-correct as you write — the goal is coverage, not correctness. Label each section. Speed over precision. Each instruction below includes a one-sentence rationale so you can apply the rule correctly in edge cases.

**Background** (1-2 sentences)
*Why:* Background establishes the conditions that make the Gap feel inevitable — it needs to be just specific enough to scaffold the Gap, no more.
Establish the domain context the reader brings in. Do not start with "In recent years."

**Gap** (1 sentence)
*Why:* Goal framing ("we aimed to study X") implies the paper might have failed. Gap framing ("X remains unresolved") states a fact about the state of the field — a stronger epistemic claim.
State what is unresolved, unknown, or contested: "X remains unresolved." Not a goal.

**Claim** (1 sentence)
*Why:* Past tense for empirical results treats findings as historical events; present tense for theoretical contributions treats them as timeless truths. The tense choice signals the paper's epistemic type to the reader.
Identify paper type: empirical or theoretical. Then write: active voice, past tense if empirical ("we found"), present tense if theoretical ("we show").
> Paper type: empirical / theoretical

**Method** (1-2 sentences)
*Why:* "We investigated" conveys no information about how the claim was established. Readers use Method to decide whether the evidence is strong enough to believe the Claim — a named method with scope gives them that.
Name the specific method, dataset, model, or approach. No vague "we investigated." Quantify scope or sample size if possible.

**Result** (1-2 sentences)
*Why:* Abstracts that say only "we found improvements" are unfalsifiable. A number, percentage, or explicit strength word gives the reader an anchor for assessing the paper's contribution before reading it.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

**Implication** (1 sentence)
*Why:* A vague implication ("this has broad implications") tells the reader nothing they can act on. One concrete enabling action is more memorable and more honest about what the paper actually changes.
What can now be done, decided, or understood that couldn't before? Name one concrete enabling action.

---

**Phase 3 — Merge and count.** Merge into a single flowing paragraph. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-03 — Connective Bridge Phase

**Variation axis**: Lifecycle structure (new bridge composition phase inserted between Phase 2 draft blocks and Phase 3 merge)
**Hypothesis**: C-12 failed universally in R2 because every variation relied on bridges emerging from merge rather than being composed explicitly. The fix is structural — a dedicated bridge phase after draft, before merge. After all six section blocks are written, and before the merge step, this variation requires composing one 3-8 word transition phrase for each of the five section boundaries (Background→Gap, Gap→Claim, Claim→Method, Method→Result, Result→Implication). These phrases serve as the logical glue in Phase 3. Side benefit: explicitly composing bridges also increases natural flow at merge time, improving C-10. Risk: bridge phrases may be formulaic connectors ("however", "in this paper") rather than substantive transitions.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill writes a fast coverage draft from your signals, composes explicit connective bridges between sections, then merges using those bridges. The draft phase targets coverage only. The bridge phase is the mechanism for prose flow. The amendment phase carries the full precision load.

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft.** Write all six sections as labeled blocks. Do not self-correct as you write — the goal is coverage, not correctness. Label each section. Speed over precision.

**Background** (1-2 sentences)
Establish domain context. Do not start with "In recent years."

**Gap** (1 sentence)
State what is unresolved, unknown, or contested: "X remains unresolved." Not a goal ("we aimed to study X").

**Claim** (1 sentence)
What does this paper show, demonstrate, or argue? Active voice. Past tense if empirical, present tense if theoretical.

**Method** (1-2 sentences)
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

**Result** (1-2 sentences)
Lead with the finding. Include a number, percentage, effect size, or explicit qualitative strength word.

**Implication** (1 sentence)
What can now be done that couldn't before? One concrete enabling action.

---

**Phase 2b — Bridge composition.** Before merging, compose one short connective phrase (3-8 words) for each of the five section boundaries. These phrases do not need to be complete sentences — they are the logical handoff between sections. Write them now, before the merge step.

| Boundary | Bridge phrase |
|----------|--------------|
| Background → Gap | [e.g., "yet it remains unclear whether"] |
| Gap → Claim | [e.g., "this paper demonstrates that"] |
| Claim → Method | [e.g., "using a controlled experiment with"] |
| Method → Result | [e.g., "we found that"] |
| Result → Implication | [e.g., "enabling practitioners to"] |

These bridge phrases are the primary connective material for Phase 3. Do not discard or replace them during merge unless a stronger natural connector emerges from the prose.

---

**Phase 3 — Merge and count.** Merge the six sections into a single flowing paragraph, using the Phase 2b bridge phrases as connectives at each section boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-04 — Gap-First + Constraint Reasoning

**Variation axes**: Role sequence (Gap drafted before Background — C-14) + Phrasing register (constraint reasoning per section — C-11)
**Hypothesis**: V-03 (R2) earned both C-11 and C-14 — 6 pts of aspirational that no other variation reached — but scored only 80 because its amendment phase was unmodified baseline. V-05 proved that permissive draft + hardened 4-amendment phase earns 88-92. This combination grafts V-03's gap-first order and constraint reasoning onto V-05's amendment infrastructure. Expected to earn C-11 + C-14 + C-13 + C-15 + C-16 + C-07. The V-03 axes and the V-05 axes are additive — they modify different phases.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill writes a fast coverage draft from your signals — with Gap first so Background scaffolds toward a known target — then runs a hardened four-amendment pass to reach final quality. Each section instruction below explains why its constraint exists so you can generalize correctly in edge cases. The draft phase targets coverage only. The amendment phase carries the full precision load.

---

**Phase 1 — Signal acquisition.** Glob signals/**/{topic}-*. Read what you find: paper draft, specify-spec, discover-hypothesis. Extract the central claim, the method, the key result, and the target journal before writing.

---

**Phase 2 — Coverage draft (gap-first order).** Write in this sequence: Gap first, then Background, then Claim, Method, Result, Implication. Do not self-correct — the goal is coverage. Label each section.

**Gap** (write first — 1 sentence)
*Why gap-first:* Once the Gap is fixed, Background can be written to scaffold exactly toward it — no more, no less. Background written first tends to drift into generic domain survey.
*Why gap framing vs. goal framing:* Goal language ("we aimed to study X") implies the paper might have failed. Gap language ("X remains unresolved") states a fact about the state of the field.
State what is unresolved, unknown, or contested: "X remains unresolved" / "it is unknown whether X."

> [Gap sentence]

**Background** (write after Gap — 1-2 sentences)
*Why:* Background's only job is to make the Gap feel inevitable. Write toward the gap you just stated — establish exactly the context that creates the open question.
Do not start with "In recent years." Make the Background end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events ("we found X increased 12%"). Present tense for theoretical contributions treats them as timeless truths ("we show that X implies Y"). The choice signals the paper's epistemic type.
Identify paper type, then write: active voice, past tense if empirical, present tense if theoretical.
> Paper type: empirical / theoretical
> [Claim sentence]

**Method** (1-2 sentences)
*Why specificity:* "We investigated" conveys no information about how the claim was established. Readers use Method to judge whether the evidence supports the Claim. A named method with scope gives them that.
Name the specific method, dataset, model, or approach. Quantify scope or sample size if possible.

> [Method text]

**Result** (1-2 sentences)
*Why quantification:* Abstracts that say only "we found improvements" are unfalsifiable and uninformative. A number, percentage, or explicit strength word anchors the reader's assessment of the contribution.
Lead with the finding, not the procedure. Include a number, percentage, effect size, or explicit qualitative strength word.

> [Result text]

**Implication** (1 sentence)
*Why one concrete action:* "This has broad implications for the field" tells the reader nothing actionable. One concrete enabling action is more memorable and more honest about what the paper changes.
What can now be done, decided, or understood? Name one concrete enabling action.

> [Implication sentence]

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-05 — Full Synthesis: Gap-First + Constraint Reasoning + Connective Bridges

**Variation axes**: All three single-axis additions combined: role sequence (Gap-first, C-14) + phrasing register (constraint reasoning, C-11) + lifecycle structure (bridge phase, C-12) — on V-05 base (permissive draft + 4-amendment hardened phase, C-15 + C-16)
**Hypothesis**: The theoretical ceiling variation. C-12 (connective bridges), C-11 (constraint reasoning), and C-14 (gap-first) are the three remaining aspirational gaps not addressed by V-05's 92-pt floor. Each is targeted by a distinct mechanism in a distinct phase. The three mechanisms are additive: gap-first modifies draft order (Phase 2), constraint reasoning modifies instruction register (Phase 2), bridge composition adds a new phase (Phase 2b). All three operate before merge; none conflicts with Phase 5. Risk: total prompt depth may cause partial execution of later phases — gap-first + constraint reasoning together add the most instruction density, and bridging adds another phase.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 150-250 words (300 for arxiv). This skill writes a fast coverage draft from your signals — Gap first so Background scaffolds toward a known target — composes explicit connective bridges between all section boundaries, then runs a hardened four-amendment pass to reach final quality. Each section instruction explains why its constraint exists. The draft phase targets coverage only. The bridge phase produces the logical glue for merge. The amendment phase carries the full precision load.

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
*Why:* Background's only job is to establish the conditions that make the Gap feel inevitable. Write exactly the context that creates the open question — no more, no less.
Do not start with "In recent years." Make the last Background sentence end where the Gap begins.

> [Background text]

**Claim** (1 sentence)
*Why tense convention:* Past tense for empirical findings treats them as historical events. Present tense for theoretical contributions treats them as timeless truths. The choice signals the paper's epistemic type before the reader reaches the Methods.
Identify paper type, then write: active voice, past tense if empirical ("we found"), present tense if theoretical ("we show").
> Paper type: empirical / theoretical
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
What can now be done, decided, or understood? Name one concrete enabling action.

> [Implication sentence]

---

**Phase 2b — Bridge composition.** Before merging, compose one short connective phrase (3-8 words) for each of the five section boundaries. These are the logical handoffs between sections — compose them as purposeful transitions, not stock connectors ("however", "in this paper").

| Boundary | Bridge phrase |
|----------|--------------|
| Background → Gap | [names the specific gap tension created by Background] |
| Gap → Claim | [names what this paper does in response to the Gap] |
| Claim → Method | [connects the contribution claim to the how] |
| Method → Result | [transitions from approach to finding] |
| Result → Implication | [moves from what was found to what it enables] |

These bridge phrases are the merge glue for Phase 3. Incorporate them at section boundaries during the merge step.

---

**Phase 3 — Merge and count.** Reorder to standard sequence: Background — Gap — Claim — Method — Result — Implication. Merge into a single flowing paragraph, using the Phase 2b bridge phrases as connectives at each boundary. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

**Phase 4 — Journal variant.** If --for journal:\<name\> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

**Phase 5 — Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After must differ from Before in substance, not just wording). A restatement of the prior sentence in different words is not an amendment.

**Amendment 1 — Gap sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened — names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 — Result quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 — Implication tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions are named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 — Prose coherence**
Target: Does the merged paragraph read as one continuous piece of writing, or as six sentences stapled together? Identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output \<path\> provided: write the artifact flat into \<path\>/
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]
