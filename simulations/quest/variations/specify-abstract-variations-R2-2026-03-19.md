Written to `simulations/quest/variations/specify-abstract-variations-R2-2026-03-19.md`. Here are the 5 complete variations:

---

## Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Amendment rigor: before/after + non-triviality guard | Requiring Before/After pairs for each Phase 5 amendment eliminates trivial restatements — self-evident failures when Before and After say the same thing (C-07, C-13) |
| **V-02** | Dual-pass structure: completeness pass then precision pass | Separating "get all six parts down" from "make each part correct" means each pass has one job — reduces conflation that causes both completeness failures and precision failures simultaneously |
| **V-03** | Gap-first scaffold + constraint reasoning | Combines two new v2 rubric criteria: Gap drafted before Background (C-14) so Background scaffolds toward a known target, plus each section instruction includes a one-sentence *why* (C-11) |
| **V-04** | Signal-forward: quote-level extraction in Phase 1 | Extends Phase 1 to require verbatim or near-verbatim quotes from signal artifacts before writing — numbers surface in Phase 1, eliminating generic filler and raising C-05/C-06 pass rates |
| **V-05** | Minimal phases + maximum amendment (4 amendments with before/after) | Fast permissive draft, then hardened Phase 5 with before/after for all amendments plus a fourth prose-coherence amendment (C-10) — tests whether quality load can shift entirely to amendment phase |

**Key trade-offs:** V-02's precision checklist may produce mechanical output (C-10 risk). V-04 degrades gracefully when no signals exist ("NOT FOUND -- will synthesize") but the honest fallback means Phase 2 starts from zero. V-05's fourth amendment (prose coherence) is the only variation to directly target C-10 in Phase 5 rather than hoping for it from Phase 3 merge.

**R1 vs R2 territory:** R1 tested *how to draft*. R2 tests *how to verify and amend* (V-01, V-05), *how to separate concerns* (V-02), *how to ground* (V-03, V-04). These are complementary axes — the strongest R3 candidate may be a V-03/V-01 combination (constraint reasoning during draft + hardened amendment verification).
nt produces visible change (C-13). Trivial restatements become self-evident failures. This is a single-axis change -- only Phase 5 is modified.

---

You are running /specify-abstract for: {{topic}}

Academic abstracts are a specific artifact: 200-250 words, with a fixed six-part genre structure. specify-spec doesn't know this genre. This skill writes the abstract and enforces the structure.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read: paper draft, specify-spec artifact, discover-hypothesis artifact if present.
Extract: the central claim, the method, the key result, the target journal (if known).

---

## PHASE 2 -- SIX-PART ABSTRACT

Write each section as a distinct block, then merge:

**Background** (1-2 sentences)
What is the established context the reader already knows? Establish the domain. Do not start with "In recent years."

**Gap** (1 sentence -- the inertia)
What is not yet known, not yet solved, or contested? This is why the paper exists. Name it as a gap, not as a goal: "X remains unresolved" not "we aimed to study X."

**Claim** (1 sentence -- the paper's contribution)
What does this paper show/demonstrate/argue? Active voice. Past tense for empirical results ("we found"), present tense for theoretical contributions ("we show").

**Method** (1-2 sentences)
How? Be specific: name the method, dataset, model, or approach. No vague "we investigated." Quantify sample size or scope if possible.

**Result** (1-2 sentences -- the key finding)
What was found? Quantify: effect sizes, percentages, qualitative strength. Lead with the finding, not the procedure.

**Implication** (1 sentence -- the so-what)
What does this change? Who cares? What can now be done that couldn't before?

---

## PHASE 3 -- MERGE AND COUNT

Merge the six sections into a single flowing paragraph. Count words.

```
[merged abstract text]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: identify the longest section and compress it without removing a required structural element.

---

## PHASE 4 -- JOURNAL VARIANT

If --for journal:<name> specified, adjust register:

- **--for journal:nature** or **science**: Lead with broad significance in Background. Compress Method to 1 sentence. Implication should name societal impact.
- **--for journal:pnas**: Lead with the problem statement. Result must include effect size or statistic. Background can be shorter.
- **--for journal:cognitive-science**: Lead with theoretical contribution. Method section can be longer. Implication should name the theoretical advance.
- **--for journal:jcs** or phenomenology venues: Background may include phenomenological context. Claim can make interpretive assertions. Result may include qualitative findings.
- **--for journal:arxiv**: Word limit relaxed to 300. Technical precision prioritized over broad appeal.

---

## PHASE 5 -- AMEND (HARDENED)

Three targeted improvements. For each amendment:
1. Write the **Before** text (the sentence being changed).
2. Write the **After** text (the replacement).
3. Confirm the change is non-trivial: the After must differ from the Before in substance, not just wording.

A restatement of the prior sentence in different words is not an amendment. If Before and After say the same thing, rewrite After until they differ substantively.

**Amendment 1 -- Gap**
Target: Sharpen the Gap to name the specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened Gap sentence -- must name a specific unresolved question]
> Non-trivial? [Y / N -- if N, rewrite After]

**Amendment 2 -- Result**
Target: Add a number if missing. If a number genuinely cannot be provided, add an explicit qualitative strength word and name what it characterizes.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial? [Y / N -- if N, rewrite After]

**Amendment 3 -- Implication**
Target: Tighten to one concrete enabling action. Remove modal hedges ("may", "could potentially"). If it names two things, pick the stronger one.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial? [Y / N -- if N, rewrite After]

Write the final amended abstract as a complete paragraph below the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-02 -- Dual-Pass Structure: Completeness Pass Then Precision Pass

**Variation axis**: Lifecycle structure (single-pass draft -> two-pass: Pass A is completeness-only, Pass B is precision-only)
**Hypothesis**: The baseline conflates two different cognitive tasks -- getting all six parts present (completeness) and getting each part right (precision). Separating them into two explicit passes means Pass A can write quickly without self-correction overhead, and Pass B can focus entirely on known failure modes (gap framing, tense convention, quantification) without worrying about structure. Each pass has one job. Risk: Pass B may produce a mechanical second draft if the precision criteria feel like a checklist rather than a revision.

---

You are running /specify-abstract for: {{topic}}

Academic abstracts require two things that are easier to achieve separately: all six parts present (completeness) and each part meeting its precision requirement (gap framing, tense convention, quantification). This skill runs two explicit passes, then writes the artifact.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read: paper draft, specify-spec, discover-hypothesis if present.
Extract: the central claim, the method, the key result, the target journal.

---

## PHASE 2 -- PASS A: COMPLETENESS

Write all six sections. Do not self-correct as you write. The goal of Pass A is coverage: get something down for every section. Label each section. Speed over perfection.

**Background**: [1-2 sentences of domain context]
**Gap**: [1 sentence -- what is unresolved]
**Claim**: [1 sentence -- what this paper shows]
**Method**: [1-2 sentences -- how]
**Result**: [1-2 sentences -- what was found]
**Implication**: [1 sentence -- so what]

After Pass A, confirm: All six sections are present? Y / N. If N, add the missing section before proceeding.

---

## PHASE 3 -- PASS B: PRECISION

Revisit each section from Pass A and apply its single precision test. Rewrite if needed.

**Background**: Does it establish domain context without starting "In recent years"?
> Revised (or "no change needed"): [text]

**Gap**: Does it state a gap ("X remains unresolved / unknown / contested") rather than a goal ("we aimed / we sought to")?
> Revised (or "no change needed"): [text]

**Claim**: Is it active voice? Does it use past tense for empirical ("we found") or present tense for theoretical ("we show")?
> Paper type: empirical / theoretical
> Revised (or "no change needed"): [text]

**Method**: Does it name a specific method, dataset, or approach (not "we investigated")? Does it quantify scope?
> Revised (or "no change needed"): [text]

**Result**: Does it include a number, percentage, effect size, or explicit qualitative strength word? Does it lead with the finding?
> Revised (or "no change needed"): [text]

**Implication**: Does it name one concrete enabling action or change?
> Revised (or "no change needed"): [text]

---

## PHASE 4 -- MERGE AND COUNT

Merge the Pass B sections into a single flowing paragraph. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: identify the longest section and compress it. Keep all six parts. Re-count.

---

## PHASE 5 -- JOURNAL VARIANT

If --for journal:<name> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with the problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names the theoretical advance.
- **jcs** / phenomenology: Phenomenological framing and qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision over broad appeal.

---

## PHASE 6 -- THREE AMENDMENTS

Three targeted improvements:
1. [Sharpen the Gap -- specific unresolved question, not a domain]
2. [Quantify the Result -- add a number or explicit strength word if missing]
3. [Tighten the Implication -- one concrete enabling action, no hedges]

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output <path>: write flat into that path.
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-03 -- Gap-First Scaffold + Constraint Reasoning

**Variation axes**: Role sequence (Gap drafted before Background -- C-14) + Phrasing register (each section instruction includes a one-sentence rationale explaining why the constraint exists -- C-11)
**Hypothesis**: Two new rubric criteria are causally linked: writing Gap first gives Background a target to scaffold toward (C-14), and explaining why each constraint exists produces better generalization than asserting it (C-11). V-04 in R1 tested Gap-first with inertia framing. This variation tests Gap-first with constraint reasoning as the second axis -- a different combination. Risk: explanatory rationale may increase prompt length past the attention horizon for the later phases.

---

You are running /specify-abstract for: {{topic}}

An academic abstract answers six questions in a fixed order. This skill writes it from your signals. Two constraints shape the drafting order and the instruction style: the Gap is written before the Background because a known gap is the best scaffold for the context that precedes it; and each constraint below includes a brief rationale so you can apply the rule correctly in edge cases.

---

## PHASE 1 -- SIGNAL ACQUISITION

Glob: signals/**/{topic}-*
Read: paper draft, specify-spec, discover-hypothesis if present.
Extract: the central claim, the method, the key result, the target journal.

---

## PHASE 2 -- SIX-PART ABSTRACT (GAP-FIRST ORDER)

Write in this order: Gap first, then Background, then the remaining four in standard order. At merge time (Phase 3), reorder to the standard abstract sequence.

---

**Gap** (1 sentence -- write this first)
*Why this order:* Writing the Gap before the Background prevents Background from drifting into generic domain survey. Once the Gap is fixed, Background can be scaffolded specifically toward the gap -- which is all Background needs to do.

State what is unresolved, unknown, or contested in the field: "X remains unresolved." Do not use goal language ("we aimed to study X") -- goal language implies the paper might have failed; gap language states a field fact.

> [Gap sentence]

---

**Background** (1-2 sentences -- written after Gap)
*Why this order:* The Background you need is exactly the context that makes the Gap feel inevitable. No more, no less. Write toward the gap you just stated.

Establish the domain context the reader brings in. Do not start with "In recent years" -- readers want context, not chronology.

> [Background text]

---

**Claim** (1 sentence)
*Why active voice + tense convention:* Passive voice obscures agency and weakens the contribution claim. Past tense for empirical findings treats them as historical events ("we found X increased by 12%"). Present tense for theoretical contributions treats them as timeless truths ("we show that X implies Y"). The choice signals the paper's epistemic type to the reader.

What does this paper show, demonstrate, or argue? Active voice. Past tense for empirical results, present tense for theoretical contributions.

> [Claim sentence]

---

**Method** (1-2 sentences)
*Why specificity matters:* "We investigated" conveys no information about how the claim was established. Readers use the Method section to decide whether the evidence is strong enough to believe the Claim. A named method with scope gives them that.

Name the method, dataset, model, or approach. No vague "we investigated." Quantify scope or sample size if possible.

> [Method text]

---

**Result** (1-2 sentences)
*Why quantification:* Abstracts that say "we found improvements" are unfalsifiable and uninformative. A number, percentage, effect size, or explicit strength word gives the reader an anchor for assessing the paper's contribution before reading it.

What was found? Lead with the finding, not the procedure. Include a number, percentage, or qualitative strength descriptor.

> [Result text]

---

**Implication** (1 sentence)
*Why one concrete action:* A vague implication ("this has broad implications for the field") tells the reader nothing actionable. One concrete enabling action is more memorable and more honest about what the paper actually changes.

What can now be done, decided, or understood? Name one concrete enabling action.

> [Implication sentence]

---

## PHASE 3 -- MERGE AND COUNT

Reorder to standard sequence: Background -- Gap -- Claim -- Method -- Result -- Implication.
Merge into a single flowing paragraph. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Keep all six parts. Re-count.

---

## PHASE 4 -- JOURNAL VARIANT

If --for journal:<name> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

## PHASE 5 -- THREE AMENDMENTS

Three targeted improvements:
1. [Sharpen the Gap -- specific unresolved question, not just a domain area]
2. [Quantify the Result -- add a number or explicit strength word if missing]
3. [Tighten the Implication -- one concrete enabling action, remove hedges]

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output <path>: write flat into that path.
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-04 -- Signal-Forward: Explicit Quote Extraction in Phase 1

**Variation axis**: Signal acquisition depth (scan and extract summary -> required quote-level extraction with direct citation into Phase 2)
**Hypothesis**: The baseline Phase 1 says "extract: central claim, method, key result" but the extraction is implicit -- the AI summarizes rather than quotes. If Phase 1 requires surfacing verbatim or near-verbatim quotes from the signal artifacts (actual claim language from the paper draft, actual numbers from the specify-spec or hypothesis), then Phase 2 is grounded in real content rather than paraphrased summaries. This should raise C-05 (signal-grounded content) and C-06 (quantified result) pass rates because the numbers and specific claims are already on the page before writing begins. Risk: if no signals exist, Phase 1 produces scaffolding-speak ("signal not found"), which is honest but means Phase 2 must generate from zero.

---

You are running /specify-abstract for: {{topic}}

Academic abstracts are a specific artifact: 200-250 words, with a fixed six-part genre structure. This skill writes the abstract from your signals. The quality of the abstract depends entirely on the quality of the signal extraction -- vague extraction produces generic abstracts. Phase 1 is extended to require citation-level grounding before any writing begins.

---

## PHASE 1 -- SIGNAL EXTRACTION (EXTENDED)

Glob: signals/**/{topic}-*
Read every artifact you find: paper draft, specify-spec, discover-hypothesis, any other signal artifact.

For each artifact found, extract the following fields by direct quote or close paraphrase. If a field is not present in any artifact, write "NOT FOUND -- will synthesize."

**Central claim** (from paper draft or specify-spec):
> [direct quote or close paraphrase of the paper's main contribution sentence]
> Source: [artifact filename]

**Method** (from paper draft or specify-spec):
> [direct quote or close paraphrase of the method description]
> Source: [artifact filename]

**Key result with quantification** (from paper draft, hypothesis, or result section):
> [direct quote or close paraphrase including any numbers, percentages, effect sizes, or strength descriptors]
> Source: [artifact filename] / NOT FOUND

**Gap / unresolved question** (from hypothesis artifact or paper introduction):
> [direct quote or close paraphrase of the field gap being addressed]
> Source: [artifact filename] / NOT FOUND

**Target journal** (from any artifact):
> [journal name] / NOT SPECIFIED

After extraction: do any of the four fields read as generic or topic-independent? If so, note which ones -- those are the sections most at risk of generic filler in Phase 2.

---

## PHASE 2 -- SIX-PART ABSTRACT

Write each section. Where Phase 1 produced a direct extraction, use it as the anchor. Do not discard specific language from the signals in favor of paraphrase.

**Background** (1-2 sentences)
What established context does the reader bring? Do not start with "In recent years." Make the Background specific to the topic, not generic to the field.

**Gap** (1 sentence)
Use the extracted Gap field as the starting point. Reframe as a field-state observation: "X remains unresolved" / "it is unknown whether X." Do not use goal language.

**Claim** (1 sentence)
Use the extracted Central Claim as the anchor. Active voice. Past tense for empirical, present for theoretical.

**Method** (1-2 sentences)
Use the extracted Method directly. Name the specific method, dataset, or approach. Include any scope numbers from the extraction.

**Result** (1-2 sentences)
Use the extracted Key Result, including any quantification from the extraction. Lead with the finding. If quantification was NOT FOUND in Phase 1, generate a plausible qualitative strength descriptor and flag it: [ESTIMATED -- no signal found].

**Implication** (1 sentence)
What can now be done that couldn't before? One concrete enabling action.

---

## PHASE 3 -- MERGE AND COUNT

Merge into a single flowing paragraph. Count words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: identify the longest section and compress it. Keep all six parts. Re-count.

---

## PHASE 4 -- JOURNAL VARIANT

If --for journal:<name> present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

## PHASE 5 -- THREE AMENDMENTS

Three targeted improvements:
1. [Sharpen the Gap -- specific unresolved question, not just a domain area]
2. [Quantify the Result -- add a number or explicit strength word if still missing after Phase 1 extraction]
3. [Tighten the Implication -- one concrete enabling action, no hedges]

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output <path>: write flat into that path.
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]

---

## V-05 -- Minimal Phases + Maximum Amendment (4-Amendment Hardened Phase 5)

**Variation axes**: Lifecycle compression (phases 1-4 reduced to minimum -- V-02 style) + Amendment maximalism (Phase 5 expanded to four amendments with before/after required, adding a fourth prose-coherence amendment not in the baseline)
**Hypothesis**: The baseline splits quality work across all five phases. This variation hypothesizes that a fast, permissive draft followed by a rigorous amendment pass can produce equal or better output. Phase 5 is hardened with before/after text and a fourth amendment (prose coherence: does the merged paragraph read as one piece of writing, or six stapled sentences?). The prose coherence amendment directly targets C-10. Risk: four amendments may over-revise, producing academic formalism rather than clear prose. Also tests whether Phase 5 can reliably catch C-04/C-09 failures that weren't caught during drafting.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 200-250 words (300 for arxiv). This skill writes a fast draft from your signals, then runs a hardened four-amendment pass to reach final quality. The draft is permitted to be rough; the amendment pass is not.

---

**Acquire signals.** Glob signals/**/{topic}-*. Read what you find -- paper draft, specify-spec, discover-hypothesis. Extract the central claim, method, key result, and target journal before writing.

---

**Draft the abstract.** Write all six parts as labeled blocks, then merge into one paragraph and count words.

Six parts, in order:
- **Background** -- domain context the reader brings in (not "In recent years...")
- **Gap** -- what is still unresolved ("X remains unknown", not "we sought to...")
- **Claim** -- what this paper contributes (active voice; empirical = past tense, theoretical = present tense)
- **Method** -- named technique or dataset with scope/sample size
- **Result** -- the key finding, quantified (number, percentage, or explicit strength word)
- **Implication** -- what is now possible that wasn't before

Report word count: `Word count: N / 250 -- UNDER / ON TARGET / OVER`. If OVER: compress the longest section.

If --for journal:<name> present: Nature/Science -- broad significance lead, societal implication; PNAS -- problem lead, quantified result; cognitive-science -- theoretical lead, theoretical implication; arxiv -- 300-word limit, technical precision.

---

**Four-amendment pass.** For each amendment, write the Before text, write the After text, then confirm the change is non-trivial (After differs from Before in substance, not just wording).

**Amendment 1 -- Gap Sharpening**
Target: Gap must name a specific unresolved question, not just a domain area.
> Before: [original Gap sentence]
> After: [sharpened -- names a specific unresolved question]
> Non-trivial: Y / N

**Amendment 2 -- Result Quantification**
Target: Result must include a number, percentage, effect size, or explicit qualitative strength word.
> Before: [original Result sentence(s)]
> After: [quantified Result]
> Non-trivial: Y / N

**Amendment 3 -- Implication Tightening**
Target: One concrete enabling action. Remove modal hedges ("may", "could potentially"). If two actions named, pick the stronger.
> Before: [original Implication sentence]
> After: [tightened Implication]
> Non-trivial: Y / N

**Amendment 4 -- Prose Coherence**
Target: Does the merged paragraph read as one piece of continuous writing, or as six sentences stapled together? If the latter, identify the weakest transition and rewrite the surrounding two sentences to flow naturally.
> Before: [the two sentences with the weakest transition]
> After: [rewritten for prose flow]
> Non-trivial: Y / N

Write the final amended abstract as a complete paragraph after the amendment table.

---

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output <path>: write flat into that path.
Frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]
