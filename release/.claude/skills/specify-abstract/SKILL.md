---
name: specify-abstract
description: "Writes a structured academic abstract (200-250 words): Background / Gap / Claim / Method / Result / Implication. Supports journal variants (--for journal:pnas, --for journal:jcs, etc.)"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


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

**Gap** (1 sentence — the inertia)
What is not yet known, not yet solved, or contested? This is why the paper exists. Name it as a gap, not as a goal: "X remains unresolved" not "we aimed to study X."

**Claim** (1 sentence — the paper's contribution)
What does this paper show/demonstrate/argue? Active voice. Past tense for empirical results ("we found"), present tense for theoretical contributions ("we show").

**Method** (1-2 sentences)
How? Be specific: name the method, dataset, model, or approach. No vague "we investigated." Quantify sample size or scope if possible.

**Result** (1-2 sentences — the key finding)
What was found? Quantify: effect sizes, percentages, qualitative strength. Lead with the finding, not the procedure.

**Implication** (1 sentence — the so-what)
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

## PHASE 5 -- AMEND

Three targeted improvements:
1. [Sharpen the Gap — make it name the specific unresolved question, not a vague domain]
2. [Quantify the Result — add a number if it's missing]
3. [Tighten the Implication — one concrete thing this enables or changes]

Write artifact to: signals/specify/abstract/{{topic}}-abstract-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: specify-abstract, topic: {{topic}}, date: {{date}}, word_count: [n], journal: [if specified]
