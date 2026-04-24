Written to `simulations/quest/variations/specify-abstract-variations-R1-2026-03-19.md`.

---

## Summary

**5 variations across 3 axes:**

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Phrasing register: formal → imperative | Short commands reduce hedging and placeholder sentences |
| **V-02** | Lifecycle emphasis: explicit phases → minimal scaffold | Fewer phase markers produce more natural prose from the start (C-10) |
| **V-03** | Output format: flat → per-section self-assessment table | Inline checks catch C-04 (gap framing) and C-09 (tense) failures before merge |
| **V-04** | Role sequence (Gap-first) + Inertia framing (prominent) | Writing Gap as the inertia anchor first produces tighter causal structure across all sections |
| **V-05** | Phrasing register (explanatory) + Output format (connective phrases before merge) | Explaining *why* each constraint exists + requiring connectives makes C-10 prose flow a first-class output, not afterthought |

**Key trade-off to watch in simulation:** V-02 (compressed) is highest risk for C-01 (all six sections present) — the scaffold exists to ensure completeness. V-03 adds token cost but should have highest C-04/C-09 pass rate. V-04's Gap-first reorder is restored to standard sequence at merge time, so C-10 prose flow risk is bounded.
 about the world: "X remains unresolved." Not a goal: not "we aimed to study X."

**Claim** (1 sentence)
What does this paper prove, show, or argue? Active voice. Past tense if empirical ("we found"). Present tense if theoretical ("we show").

**Method** (1-2 sentences)
Name the method, dataset, or approach. Be specific. Give a number for sample size or scope if you have one.

**Result** (1-2 sentences)
Lead with the finding. Quantify it — a number, percentage, or explicit strength word. Do not lead with procedure.

**Implication** (1 sentence)
What can now be done, decided, or understood that couldn't before?

---

**STEP 3 — MERGE AND COUNT**

Merge the six labeled blocks into one flowing paragraph. Count the words.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: find the longest block. Compress it. Keep all six parts present.

---

**STEP 4 — JOURNAL VARIANT** (skip if no --for flag)

- `--for journal:nature` / `science`: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- `--for journal:pnas`: Lead with the problem. Result must include a statistic or effect size.
- `--for journal:cognitive-science`: Lead with the theoretical contribution. Implication names the theoretical advance.
- `--for journal:jcs` or phenomenology: Background may include phenomenological framing. Qualitative results accepted.
- `--for journal:arxiv`: Word limit is 300. Prioritize precision over broad appeal.

---

**STEP 5 — THREE AMENDMENTS**

Make three targeted improvements. Label them.

1. **Gap**: Make it name a specific unresolved question, not just a vague domain.
2. **Result**: Add a number if there isn't one.
3. **Implication**: Make it name one concrete thing this enables or changes.

---

Write to: `signals/specify/abstract/{{topic}}-abstract-{{date}}.md`
If `--output <path>` is given: write flat into that path instead.
Frontmatter required: `skill: specify-abstract`, `topic: {{topic}}`, `date: {{date}}`, `word_count: [n]`, `journal: [if specified]`

---

## V-02 — Lifecycle Emphasis: Compressed / Phase-Minimal

**Variation axis**: Lifecycle emphasis (explicit phase scaffold → minimal phase structure)
**Hypothesis**: Removing phase ceremony forces the AI to internalize the structure rather than perform it step-by-step. Output is more likely to read as prose from the start (C-10) rather than six labeled sentences. Risk: less reliable adherence to C-01 six-section completeness.

---

You are running /specify-abstract for: {{topic}}

An academic abstract has six required parts: Background, Gap, Claim, Method, Result, Implication. It runs 200-250 words (300 for arxiv). This skill writes it from your signals and writes it to disk.

---

**Acquire signals first.** Glob `signals/**/{topic}-*`. Read what you find — paper draft, specify-spec, discover-hypothesis. Extract the central claim, method, key result, and target journal before writing anything.

---

**Write the abstract.** Draft each of the six parts as a labeled block, then merge them into a single paragraph. Treat the merged result as the deliverable, not the blocks. The blocks are scaffolding.

Six parts, in order:
- **Background** — domain context the reader brings in (not "In recent years...")
- **Gap** — what is still unresolved ("X remains unknown", not "we sought to...")
- **Claim** — what this paper contributes (active voice; past tense for empirical, present for theoretical)
- **Method** — named technique, dataset, or approach with scope/sample size
- **Result** — the key finding, quantified (number, percentage, or explicit strength word)
- **Implication** — what is now possible that wasn't before

Count words after merging. Report: `Word count: N / 250 — UNDER / ON TARGET / OVER`. If OVER: compress the longest section without removing any part.

If `--for journal:<name>` is present, apply the register adjustment before outputting:
Nature/Science → broad significance lead, societal implication; PNAS → problem lead, quantified result; cognitive-science → theoretical lead, theoretical implication; arxiv → 300-word limit, technical precision.

---

**Amend.** Produce three labeled improvements to the draft:
1. Sharpen the Gap to name a specific unresolved question.
2. Add or strengthen quantification in the Result.
3. Tighten the Implication to one concrete enabling action.

---

Write to: `signals/specify/abstract/{{topic}}-abstract-{{date}}.md`
Frontmatter: `skill: specify-abstract`, `topic: {{topic}}`, `date: {{date}}`, `word_count: [n]`, `journal: [if specified]`

---

## V-03 — Output Format: Per-Section Self-Assessment Before Merge

**Variation axis**: Output format (flat prose output → section-level assessment table before merge)
**Hypothesis**: Requiring the AI to score each section against a criterion immediately after writing it activates error-correction before the merge step. C-04 (gap framing) and C-09 (claim tense) failures are caught at the section level, not post-hoc. Risk: adds output verbosity and may inflate token cost.

---

You are running /specify-abstract for: {{topic}}

Academic abstracts follow a fixed six-part structure in 200-250 words. This skill builds the abstract from your signals, self-checks each section before merging, then writes the artifact.

---

## PHASE 1 — SIGNAL ACQUISITION

Glob: `signals/**/{topic}-*`
Read: paper draft, specify-spec, discover-hypothesis (if present).
Extract: central claim, method, key result, target journal.

---

## PHASE 2 — SECTION DRAFTS WITH INLINE CHECKS

For each section: write the draft text, then immediately fill the check row.

**Background** (1-2 sentences)
What established context does the reader bring? Establish the domain. Do not start with "In recent years."

> Draft: [text]
> Check — Does it avoid "In recent years"? Y/N

---

**Gap** (1 sentence)
What is still unresolved or unknown? Frame as a field fact: "X remains unresolved." Not a goal statement.

> Draft: [text]
> Check — Does it name a gap ("remains unresolved / unknown / contested") rather than a goal ("we aimed / we sought")? Y/N
> If N: rewrite before continuing.

---

**Claim** (1 sentence)
What does this paper show? Active voice. Past tense for empirical, present for theoretical.

> Draft: [text]
> Check — Paper type: empirical / theoretical. Tense used: past / present. Match? Y/N
> If N: rewrite before continuing.

---

**Method** (1-2 sentences)
Named method, dataset, or approach. Quantify scope or sample size if possible.

> Draft: [text]
> Check — Is a specific method named (not "we investigated")? Y/N

---

**Result** (1-2 sentences)
Key finding. Lead with the finding, not the procedure. Include a number, percentage, or strength word.

> Draft: [text]
> Check — Does it include a number, percentage, or explicit strength word? Y/N
> If N: add quantification before continuing.

---

**Implication** (1 sentence)
What can now be done, decided, or understood?

> Draft: [text]
> Check — Does it name a concrete enabling action or change? Y/N

---

## PHASE 3 — MERGE AND COUNT

Merge all six sections into one flowing paragraph (no section labels in final text).

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress the longest section. Re-count.

---

## PHASE 4 — JOURNAL VARIANT

If `--for journal:<name>` present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology: Phenomenological framing accepted. Qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision over broad appeal.

---

## PHASE 5 — THREE AMENDMENTS

Produce three labeled improvements:
1. **Gap** — name the specific unresolved question (not just a domain)
2. **Result** — add or strengthen the quantification
3. **Implication** — one concrete enabling action

---

Write to: `signals/specify/abstract/{{topic}}-abstract-{{date}}.md`
If `--output <path>`: write flat into that path.
Frontmatter: `skill: specify-abstract`, `topic: {{topic}}`, `date: {{date}}`, `word_count: [n]`, `journal: [if specified]`

---

## V-04 — Combined: Role Sequence (Gap-First) + Inertia Framing (Prominent)

**Variation axes**: Role sequence (standard order → Gap drafted first as anchor) + Inertia framing (Gap is the inertia; every other section is positioned relative to it)
**Hypothesis**: The Gap is the argumentative fulcrum of an academic abstract — it is why the paper exists. Writing it first and treating it as the inertia the paper overcomes should produce a more causally tight abstract. The Background contextualizes the gap; the Claim resolves it; the Implication justifies why the gap mattered. This mirrors how inertia-first discovery works in the signal namespace. Risk: C-10 prose flow may suffer if Gap feels over-prominent after merge.

---

You are running /specify-abstract for: {{topic}}

An academic abstract is an argument against inertia. The Gap is the inertia: the thing the field has not solved, not answered, not resolved. Every other part of the abstract positions itself relative to that gap. This skill writes the abstract Gap-first, from your signals, and writes it to disk.

---

## PHASE 1 — SIGNAL ACQUISITION

Glob: `signals/**/{topic}-*`
Read: paper draft, specify-spec, discover-hypothesis.
Extract: the central unresolved question (the Gap), the contribution that resolves it (the Claim), the method, the key result, the so-what, the target journal.

Before writing any section, state:
> **Gap (raw)**: [one sentence — what the field has not yet resolved]

This sentence is your anchor. Every section you write next must connect to it.

---

## PHASE 2 — WRITE FROM THE GAP OUTWARD

Write sections in this order. The Gap is already anchored above.

**Gap** (final — 1 sentence)
Refine the raw Gap into its final form. State it as a fact about the state of the field: "X remains unresolved" / "X is not yet known" / "X is contested." Do not use goal language: not "we aimed," not "we sought."

**Background** (1-2 sentences)
Now that you have the Gap, write the Background that makes the Gap feel inevitable. What established context creates the conditions for that gap to exist? Do not start with "In recent years."

**Claim** (1 sentence)
What does this paper contribute that resolves the gap? Active voice. Past tense for empirical findings ("we found"), present tense for theoretical contributions ("we show"). The Claim should directly answer the Gap.

**Method** (1-2 sentences)
How was the Claim established? Name the method, dataset, or approach. Quantify scope if possible (n=, hours, cases, iterations).

**Result** (1-2 sentences)
What did you find? Quantify with a number, percentage, effect size, or explicit strength word. Lead with the finding, not the procedure.

**Implication** (1 sentence)
Now that the gap is closed, what is possible? Who benefits? What decision or action is now enabled?

---

## PHASE 3 — MERGE AND COUNT

Reorder to standard abstract sequence (Background → Gap → Claim → Method → Result → Implication) and merge into a single paragraph.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: compress. Do not remove any section. Re-count.

---

## PHASE 4 — JOURNAL VARIANT

If `--for journal:<name>` present:
- **nature / science**: Background leads with broad significance. Method compressed to 1 sentence. Implication names societal impact.
- **pnas**: Lead with the problem. Result must include statistic or effect size.
- **cognitive-science**: Lead with theoretical contribution. Implication names theoretical advance.
- **jcs** / phenomenology venues: Phenomenological framing and qualitative findings accepted.
- **arxiv**: Word limit 300. Technical precision prioritized.

---

## PHASE 5 — THREE AMENDMENTS

Produce three labeled improvements:
1. **Gap** — the gap must name a *specific* unresolved question, not a domain area. (e.g., not "reasoning in LLMs is not well understood" → "it is unknown whether chain-of-thought prompting improves reliability under distribution shift")
2. **Result** — add a number if one is missing. If a number cannot be provided, add an explicit qualitative strength word.
3. **Implication** — compress to one concrete enabling action. Remove hedges ("may", "could potentially").

---

Write to: `signals/specify/abstract/{{topic}}-abstract-{{date}}.md`
If `--output <path>`: write flat into that path.
Frontmatter: `skill: specify-abstract`, `topic: {{topic}}`, `date: {{date}}`, `word_count: [n]`, `journal: [if specified]`

---

## V-05 — Combined: Phrasing Register (Descriptive/Explanatory) + Output Format (Labeled Sentences with Required Connectives)

**Variation axes**: Phrasing register (imperative → descriptive/explanatory, explains *why* each constraint exists) + Output format (free-form blocks → labeled sentences with explicit connective requirements before merge)
**Hypothesis**: Explaining the *reason* behind each constraint (why Gap must not use goal language, why Result must be quantified) produces better generalization. The connective requirement before merge forces the AI to think about narrative flow (C-10) as a first-class output property, not an afterthought. Risk: increased prompt length may push less important content out of the AI's attention window.

---

You are running /specify-abstract for: {{topic}}

Academic abstracts serve a specific function: they allow a reader to determine in 30 seconds whether a paper is relevant to their work. To do that, the abstract must answer six questions in order, in under 250 words. This skill builds that abstract from your signal artifacts and writes it to disk.

---

## PHASE 1 — SIGNAL ACQUISITION

Before writing, read what you have. Glob `signals/**/{topic}-*` and read every artifact you find — paper draft, specify-spec, discover-hypothesis. The abstract must be grounded in actual topic content, not generic filler. Extract:

- The central claim (what the paper argues or demonstrates)
- The method (how the claim was established)
- The key result (the main finding, with any quantitative grounding available)
- The target journal (if known from the artifacts)

---

## PHASE 2 — LABELED SENTENCE DRAFTS

Write each part as a labeled sentence (or two). The label stays visible through Phase 2. You will remove it at merge time.

After drafting each section, write one explicit connective — a short phrase (3-8 words) that could bridge this section to the next. The connective is not part of the abstract text; it is a planning tool to ensure the merge produces prose, not six stapled sentences.

---

**[Background]** (1-2 sentences)
The Background establishes what is already known and accepted in the domain. It gives the reader a foothold. It should not be a historical survey ("In recent years...") — readers want context, not chronology.

> Draft: [text]
> Connective to Gap: [3-8 word bridge phrase]

---

**[Gap]** (1 sentence)
The Gap is the inertia: the question the field has not answered, the problem it has not solved. Without naming it, the paper has no justification for existing. Write it as a state-of-the-field observation ("X remains unresolved", "it is unknown whether..."), not as a research goal ("we aimed to study X"). The goal framing implies the paper might have failed; the gap framing states a fact.

> Draft: [text]
> Connective to Claim: [3-8 word bridge phrase]

---

**[Claim]** (1 sentence)
The Claim is the paper's answer to the Gap. It must logically complete the arc started by the Gap sentence. Use active voice. Follow tense convention: past tense for empirical findings ("we found that X increased Y by Z%"), present tense for theoretical or argument contributions ("we show that X implies Y"), because empirical findings are historical events while theoretical truths are timeless.

> Draft: [text]
> Connective to Method: [3-8 word bridge phrase]

---

**[Method]** (1-2 sentences)
The Method section gives the reader enough detail to evaluate the claim's credibility. Vague descriptions ("we investigated", "we analyzed") provide no information. Name the method, model, dataset, or corpus. Quantify scope where possible: sample size, number of cases, time period, number of iterations.

> Draft: [text]
> Connective to Result: [3-8 word bridge phrase]

---

**[Result]** (1-2 sentences)
The Result is the most important sentence in the abstract. Lead with the finding, not the procedure. Quantify it: a number, percentage, effect size, or an explicit strength word ("strong", "substantial", "no significant difference"). Abstracts that say only "we found improvements" are uninformative and signal a weak paper.

> Draft: [text]
> Connective to Implication: [3-8 word bridge phrase]

---

**[Implication]** (1 sentence)
The Implication answers "so what?" It tells the reader what is now possible that wasn't before — what decision, design, or understanding is now enabled. Concrete and specific beats general and aspirational.

> Draft: [text]

---

## PHASE 3 — MERGE AND COUNT

Remove all labels. Use the connective phrases as glue to knit the six sentences into a flowing paragraph. The connectives may be incorporated, adapted, or replaced — they are guides, not requirements. The final paragraph should read as if written in one pass, not assembled from parts.

```
[merged abstract]

Word count: N / 250
Status: UNDER / ON TARGET / OVER
```

If OVER: identify the section responsible for overage. Compress it. Preserve all six structural elements. Re-count and re-report.

---

## PHASE 4 — JOURNAL VARIANT

If `--for journal:<name>` is present, apply the following adjustments before finalizing:

- **nature / science**: Reopen the Background to lead with broad significance (not just domain). Compress Method to a single sentence. Implication must name a societal or cross-disciplinary impact.
- **pnas**: Lead the Background with the specific problem statement. Result must include a statistic, p-value, or effect size — qualitative strength words are insufficient.
- **cognitive-science**: Lead Background with the theoretical contribution being made. Implication should name the theoretical advance, not the application.
- **jcs** / phenomenology venues: Phenomenological framing in Background is acceptable. Qualitative findings in Result are accepted. Claim may make interpretive assertions.
- **arxiv**: Word limit relaxed to 300. Technical precision takes priority over broad appeal; specialist vocabulary is not a liability.

---

## PHASE 5 — THREE AMENDMENTS

Three targeted improvements. Each amendment must produce a visible change in the text. A restatement of the prior sentence is not an amendment.

1. **Gap** — Sharpen it to name the *specific* unresolved question, not just the domain area. Example: "the role of attention in LLMs is not well understood" → "it is unknown whether scaled attention improves factual recall under context window exhaustion."
2. **Result** — Add a number if one is absent. If a number genuinely cannot be provided (qualitative study), add an explicit qualitative strength word and name what it characterizes.
3. **Implication** — Tighten it to one concrete enabling action. Remove modal hedges ("may enable", "could potentially"). If it currently names two things, pick the stronger one.

---

Write to: `signals/specify/abstract/{{topic}}-abstract-{{date}}.md`
If `--output <path>`: write flat into that path instead.
Frontmatter required: `skill: specify-abstract`, `topic: {{topic}}`, `date: {{date}}`, `word_count: [n]`, `journal: [if specified]`
