---

## Round 1 Variations -- prove-publish

Written to `simulations/quest/variations/prove-publish-variations-R1-2026-03-14.md`.

---

### Summary

| ID | Axis | Core bet |
|----|------|----------|
| **V-01** | Role sequence: Skeptic-first | Skeptic pre-flight names the C-02/C-03 risks before authoring begins. Structurally harder to produce a paper with unresolved hypothesis or uncited claims when those are flagged as watch-points before a word is written. |
| **V-02** | Output format: pre-printed skeleton | Template with fill-in anchors and inline minimum-item requirements. Completeness (C-01, C-07, C-08) becomes structural -- you fill a form, you don't write prose that might omit sections. |
| **V-03** | Lifecycle emphasis: evidence-first | Evidence is written and citation-audited before Findings begins. Enforces cite-before-conclude ordering. Eliminates the drift where conclusions are written from memory and evidence is rationalized after. |
| **V-04** | Phrasing register: conversational transcript | Roles narrate in first person. The hypothesis verdict is a literal committed sentence the Lead Author must speak before any finding is enumerated. Eliminates verdict-evasion ("the evidence is mixed..."). |
| **V-05** | Role sequence + inertia framing (combined) | Skeptic establishes the status quo baseline before authoring. Every finding is tagged BASELINE MATCH or NEW SIGNAL. Papers with zero NEW SIGNAL findings are flagged. Serves C-10 because the `## Status Quo` section cold-orients new readers. |

**Design note:** V-01 and V-05 share the Skeptic-first axis but diverge on what the Skeptic does -- V-01 is a risk pre-flight, V-05 is a baseline-establishing exercise. V-03 is the purest single-axis variation: no new roles, no new format, just a mandatory gate between Evidence and Findings.
o-nothing baseline first-class. Aspirational C-10 (cold-start readable) is served because the Status Quo section gives new readers the context they'd otherwise have to infer. |

All five address the primary rubric failure mode: outputs that are well-structured narrative but
disconnected from investigation artifacts.

---

## V-01: Skeptic-First Role Sequence

**Axis:** Role sequence -- Skeptic runs before the paper body is written
**Hypothesis:** Pre-running a Skeptic before authoring forces the paper to address the hardest
objections (no traceable evidence, unresolved hypothesis) structurally rather than hoping review
catches them afterward. C-02 and C-03 pass rates should improve because the Skeptic names them
as risks before a single section is written.

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (pre-flight), Lead Author (primary writer), Domain Expert (review),
Practitioner (applicability review).

---

### Phase 1: Setup

Read all artifacts under `simulations/prove/` for the topic:
- hypothesis files: `*-hypothesis-*.md`
- analysis files: `*-analysis-*.md`
- interview files: `*-interview-*.md`
- websearch files: `*-websearch-*.md`
- synthesize files: `*-synthesize-*.md`

Disclose what you found before proceeding:

```
Prove artifacts loaded:
- hypothesis: signal-hypothesis-2026-03-14.md (1 hypothesis, H-01)
- analysis: signal-analysis-2026-03-14.md (4 findings)
- interview: [not found]
- websearch: signal-websearch-2026-03-14.md (3 sources)
- synthesize: [not found]
```

If no hypothesis file exists, output:
```
No hypothesis artifact found. Cannot publish without a stated hypothesis.
```
Stop and ask the user to supply the hypothesis text before continuing.

---

### Phase 2: Skeptic Pre-Flight

Skeptic runs before any section is written. Output a pre-flight checklist:

```
SKEPTIC PRE-FLIGHT:
[ ] Hypothesis stated in H-01 -- I will check Findings resolves it explicitly.
[ ] Evidence claims -- I will flag any claim in Evidence with no artifact anchor.
[ ] Findings quality -- I will check each finding is a conclusion, not a data restatement.
[ ] Principles actionability -- I will check each principle is a rule, not a summary.
[ ] Abstract completeness -- I will verify topic, hypothesis, method, key finding present.
```

Then output the Skeptic's prediction:

```
SKEPTIC PREDICTION:
Likely gap: [state the most probable failure in this paper given the available artifacts]
Watch point: [one specific section most at risk of C-02 or C-03 failure]
```

The Lead Author reads the Skeptic's prediction before writing a single section. The prediction
is not a veto -- it is a structural alert.

---

### Phase 3: Write the Paper

Lead Author writes all 8 sections in order. The Skeptic's prediction must be addressed by the
time the Findings section is complete.

**Required sections (in this order):**

**1. Abstract** (<200 words)
Must state: (a) what question was investigated, (b) how it was investigated, (c) what was found.
Must NOT describe structure ("this paper covers..."). Write the abstract as if it is the only
thing a future researcher will read.

**2. Hypothesis**
State the hypothesis exactly as it appeared in the investigation artifact (cite by file path).
If the hypothesis was amended during the investigation, note the original and final form.
Format: `H-01: [hypothesis text] (source: [file path])`

**3. Method**
Describe how the investigation was conducted: which prove skills ran, what artifacts were
produced, what inputs were used. A reader with no prior context should understand why the
evidence was gathered the way it was.

**4. Evidence**
Every evidentiary claim must have a citation anchor. Format:
```
- [Claim statement] [source: artifact-name.md, section or line reference]
```
General assertions with no backing fail C-03. If you cannot cite a claim, move it to
Limitations, not Evidence.

**5. Findings**
Write findings as interpreted conclusions, not data restatements.
Each finding must answer "what does this mean?" not "what happened?"
Minimum 3 findings. Number them F-01, F-02, ...

Before writing Findings, write a single line:
```
HYPOTHESIS VERDICT: [Confirmed / Refuted / Partially confirmed under X but not Y]
Rationale: [One sentence referencing the evidence above.]
```

The hypothesis verdict line must appear before the findings list. Findings that follow must be
consistent with it.

**6. Principles**
Minimum 2 principles. Each must be a rule, not a summary.
Accepted forms: "Always X", "When Y, do Z", "Prefer A over B because..."
Vague summaries ("this area requires care") fail C-05.
Number them P-01, P-02, ... Link each to the finding(s) that produced it: `[from F-02]`

**7. Limitations**
State what the investigation did not cover and what claims cannot be made from this evidence.
Be honest -- limitations build trust with future readers.

**8. Future Work**
Minimum 2 items. Each must be an investigable question or proposed experiment specific enough
that a team could start without further clarification.
Failing form: "More research is needed on X."
Passing form: "Investigate whether X holds when Y is changed to Z, using [method]."

---

### Phase 4: Panel Review

After the paper is complete, two named reviewers assess it.

**Domain Expert** -- Assesses whether the evidence and findings reflect accurate domain knowledge.
Provides: one substantive critique or endorsement + a score (1-10 for domain accuracy).

**Practitioner** -- Assesses whether the principles are actionable by a working team.
Provides: one substantive critique or endorsement + a score (1-10 for practical applicability).

Format:
```
DOMAIN EXPERT REVIEW:
Critique: [substantive critique or endorsement]
Score: [N/10 for domain accuracy]

PRACTITIONER REVIEW:
Critique: [substantive critique or endorsement]
Score: [N/10 for practical applicability]
```

---

### Phase 5: Amend

User may revise any section. Each amendment is recorded:
```
AMENDMENT A-01: [Section changed] -- [What changed and why]
```

After amendments, re-run the Skeptic's pre-flight checklist against the revised paper. Mark
each item [PASS] or [FAIL: reason].

---

### Output

Write the paper to: `simulations/prove/publications/{topic}-paper-{date}.md`

Paper signal written to: `simulations/prove/publications/signal-paper-{date}.md`
```

---

## V-02: Pre-Printed Section Skeleton

**Axis:** Output format -- the paper is a pre-printed template with fill-in anchors and
minimum-item checklists baked into each section
**Hypothesis:** Pre-printing the template with structural constraints (minimum item counts,
fill-in anchors, explicit failure modes noted inline) makes completeness violations (C-01,
C-07, C-08) structurally impossible -- the model fills a form rather than writing prose that
may omit sections.

```
You are running /prove:publish for Signal.

Fill in this structured paper template. All section headers are fixed. Do not reorder,
rename, or remove any section header or template fragment. Fill every [FILL] anchor.

Stock roles: Lead Author (fills template), Domain Expert (review), Practitioner (review).

---

### Phase 1: Setup

Read all artifacts under `simulations/prove/` for the topic. Disclose before proceeding:

```
Prove artifacts loaded:
- hypothesis: [file or "not found"]
- analysis: [file or "not found"]
- interview: [file or "not found"]
- websearch: [file or "not found"]
- synthesize: [file or "not found"]
```

If no hypothesis artifact exists, stop and output:
```
Cannot publish: no hypothesis artifact found at simulations/prove/hypothesis/*.
Supply hypothesis text or run /prove:hypothesis first.
```

---

### Phase 2: Write the Paper (Template Mode)

Fill every [FILL] anchor. Do not write prose outside the template structure.

---

## Abstract
<!-- Requirement: <200 words. Must state question, method, key finding. -->
<!-- Failure: "this paper covers..." describes structure, not content. -->

[FILL: State the question investigated in one sentence.]
[FILL: State the method (which investigation skills ran, what evidence was gathered) in 1-2 sentences.]
[FILL: State the key finding in 1-2 sentences.]
[FILL: State the practical implication in one sentence.]

Word count: [FILL: N] <!-- Must be <200. If over, trim. -->

---

## Hypothesis

Source artifact: [FILL: file path, e.g. simulations/prove/hypothesis/signal-hypothesis-2026-03-14.md]
Hypothesis ID: [FILL: H-01]

> [FILL: paste hypothesis text verbatim from source artifact]

---

## Method

Investigation skills used:
- [FILL: skill name] -- produced [FILL: artifact name]
- [FILL: skill name] -- produced [FILL: artifact name]
<!-- Add rows for each prove skill that ran. Minimum 1 row. -->

Evidence collection rationale:
[FILL: One paragraph explaining why evidence was gathered this way. Cold-start readable --
no undefined jargon.]

---

## Evidence

<!-- Requirement: every claim must cite a named artifact. -->
<!-- Failure: "we observed that..." with no citation anchor. -->

- [FILL: evidentiary claim] [source: FILL: artifact-name.md, section/line reference]
- [FILL: evidentiary claim] [source: FILL: artifact-name.md, section/line reference]
- [FILL: evidentiary claim] [source: FILL: artifact-name.md, section/line reference]
<!-- Minimum 3 cited claims. Add rows. For any claim you cannot cite, move to Limitations. -->

---

## Findings

<!-- Requirement: each finding is a conclusion, not a data restatement. -->
<!-- Test: does it answer "what does this mean?" rather than "what happened?"? -->

HYPOTHESIS VERDICT: [FILL: Confirmed / Refuted / Partially confirmed under X but not Y]
Rationale: [FILL: one sentence referencing evidence above by source citation]

F-01: [FILL: conclusion -- judgment, pattern, or causal claim]
F-02: [FILL: conclusion -- judgment, pattern, or causal claim]
F-03: [FILL: conclusion -- judgment, pattern, or causal claim]
<!-- Minimum 3 findings. Add F-04, F-05 if supported by evidence. -->

---

## Principles

<!-- Requirement: numbered rules a future team can apply without reading the full paper. -->
<!-- Accepted forms: "Always X", "When Y, do Z", "Prefer A over B because..." -->
<!-- Failure: "this area requires care" (vague summary, not a rule) -->

P-01 [from F-FILL]: [FILL: action-oriented rule]
P-02 [from F-FILL]: [FILL: action-oriented rule]
<!-- Minimum 2 principles. Add P-03, P-04 if supported. Each must cite its finding. -->

---

## Limitations

[FILL: What this investigation did not cover.]
[FILL: What claims cannot be made from this evidence.]
[FILL: Conditions under which the findings may not hold.]

---

## Future Work

<!-- Requirement: specific enough that a team could start without further clarification. -->
<!-- Failure: "more research is needed on X" -->

1. [FILL: investigable question or proposed experiment with enough specificity to start]
2. [FILL: investigable question or proposed experiment with enough specificity to start]
<!-- Minimum 2 items. -->

---

### Phase 3: Panel Review

Domain Expert and Practitioner each review the completed template.

**Domain Expert:**
```
Critique: [FILL: substantive critique or endorsement of domain accuracy]
Score: [FILL: N/10]
```

**Practitioner:**
```
Critique: [FILL: substantive critique of principle actionability]
Score: [FILL: N/10]
```

---

### Phase 4: Amend

User may revise any section. Record each change:
```
AMENDMENT A-01: [Section] -- [What changed]
```

---

### Output

Write to: `simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-03: Evidence-First Lifecycle

**Axis:** Lifecycle emphasis -- Evidence section is written before Findings; the sequence
enforces cite-before-conclude ordering
**Hypothesis:** Requiring the Evidence section to be fully written (with citations) before
the Findings section begins prevents the most common failure mode: conclusions written from
memory, evidence rationalized afterward. C-02 (hypothesis resolved) and C-03 (traceable
evidence) both improve because the author must have citable material in hand before
interpreting it.

```
You are running /prove:publish for Signal.

Stock roles: Lead Author, Domain Expert, Practitioner.

**Lifecycle rule: Evidence before Findings. The Findings section may not begin until the
Evidence section is complete and every claim in it has a citation anchor. This is not
negotiable -- it is the primary quality gate of this skill.**

---

### Phase 1: Setup

Read all prove artifacts for the topic under `simulations/prove/`:
- hypothesis, analysis, interview, websearch, synthesize

Disclose before proceeding:

```
Artifacts loaded:
- hypothesis: [file path or "not found"]  [hypothesis text: "..."]
- analysis: [file path, N findings noted]
- interview: [file path, N exchanges noted] or [not found]
- websearch: [file path, N sources noted] or [not found]
- synthesize: [file path, N synthesis items noted] or [not found]
```

If hypothesis is not found, stop. Do not proceed.

---

### Phase 2: Evidence First

Before writing any section of the paper, write only the Evidence section.

**Rule: Every claim must have a citation anchor in this form:**
`[claim text] [source: file-path.md, section or item ID]`

Write Evidence as a numbered list. Each item is one cited claim.

When Evidence is complete, output a citation audit:

```
CITATION AUDIT:
Total claims: N
Claims with citation anchor: N
Claims without citation anchor: 0  <-- must be 0 to proceed
```

If any claim lacks a citation, either add the anchor or remove the claim before proceeding.
Do not move to Phase 3 until the citation audit shows 0 uncited claims.

---

### Phase 3: Hypothesis Verdict

Before writing Findings, state the verdict:

```
HYPOTHESIS VERDICT
H-01: [hypothesis text]
Verdict: [Confirmed | Refuted | Partially confirmed under X but not Y]
Evidence basis: [Cite the 2-3 evidence items from Phase 2 that most directly support this verdict]
```

The verdict statement must be a complete sentence that a reader could quote standalone.
Accepted: "The hypothesis was confirmed: evidence items E-03 and E-05 show that..."
Accepted: "The hypothesis was refuted because E-02 demonstrates the opposite..."
Accepted: "Partially confirmed under condition X (E-01, E-04) but not under Y (E-02)."
Not accepted: "The evidence is mixed." (too vague -- name what mixed means)

---

### Phase 4: Write Remaining Sections

Now write the paper sections in this order:

**1. Abstract** (<200 words)
Written after you know the verdict. Must state: question, method, key finding. Not structure.

**2. Hypothesis** (from Phase 3 verdict block)

**3. Method**
What investigation skills ran. Why evidence was gathered this way. Cold-start readable.

**4. Evidence** (from Phase 2 -- paste completed section here)

**5. Findings**
Minimum 3 findings. Each is an interpreted conclusion (judgment, pattern, or causal claim)
drawn from the evidence in Phase 2. Findings must be consistent with the verdict in Phase 3.
Number: F-01, F-02, ...
The verdict line from Phase 3 appears at the top of this section.

**6. Principles**
Minimum 2 numbered rules. Action-oriented: "Always X", "When Y, do Z", "Prefer A over B."
Each principle cites the finding(s) that produced it: `[from F-01]`

**7. Limitations**
What was not covered. What cannot be concluded from this evidence.

**8. Future Work**
Minimum 2 specific investigable questions. Specific enough to start without clarification.

---

### Phase 5: Panel Review

**Domain Expert** reviews Evidence and Findings for domain accuracy.
One substantive critique or endorsement. Score /10.

**Practitioner** reviews Principles for actionability.
One substantive critique or endorsement. Score /10.

```
DOMAIN EXPERT: [critique] -- Score: [N/10]
PRACTITIONER: [critique] -- Score: [N/10]
```

---

### Phase 6: Amend

Record amendments:
```
AMENDMENT A-01: [Section] -- [Change] -- [Trigger: user / panel review]
```

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-04: Conversational Transcript + Explicit Verdict Sentence

**Axis:** Phrasing register -- roles speak in first-person transcript; hypothesis verdict is
a literal committed sentence before Findings begins
**Hypothesis:** Transcript-style narration forces the model to produce specific, committed
language at each stage. The hypothesis verdict sentence ("The hypothesis was confirmed: ...")
becomes a literal speech act the author must make before findings are enumerated -- preventing
the common evasion where Findings are written in a way that implies a verdict without stating
one. C-02 should reliably pass.

```
You are running /prove:publish for Signal.

**Voice rule:** Write this paper in authoring-transcript style. Each role speaks in first
person, present tense. The transcript is the process; the paper is the output at the end.

Roles: Lead Author, Skeptic, Domain Expert, Practitioner.

---

### Step 1: Load Context

**Lead Author:** I'm loading prove artifacts for this topic.

[Disclose what was found:]
> "I found: hypothesis at [path] (H-01: [text]). Analysis at [path] with [N] findings.
> Websearch at [path] with [N] sources. [Other artifacts or 'nothing else found'.]"

If no hypothesis exists:
> "I cannot publish without a stated hypothesis. No artifact found at
> simulations/prove/hypothesis/*. Please supply the hypothesis text or run
> /prove:hypothesis first."

Stop until hypothesis is supplied.

---

### Step 2: Skeptic Pre-Read

**Skeptic:** I'm reading the artifacts before authoring begins. My job is to surface the
hardest problem before a single section is written.

The Skeptic states one risk prediction:
> "My prediction: the most likely failure in this paper is [specific gap -- e.g., 'Evidence
> will have uncited claims because the analysis file uses prose conclusions without referencing
> primary sources']. I will check this explicitly in review."

The Lead Author acknowledges:
> "Noted. I will address [Skeptic's named risk] before submitting for review."

---

### Step 3: Write the Paper

**Lead Author** writes all 8 sections. Transcript narration wraps each section boundary:

Before Abstract:
> "Starting Abstract. I'll write it so a researcher can decide relevance from this alone --
> topic, hypothesis, method, key finding, under 200 words."

Before Evidence:
> "Starting Evidence. Every claim I make here will have a citation to a named artifact.
> If I can't cite it, it goes to Limitations, not here."

Before Findings -- mandatory verdict sentence:
> "I am now committing to the hypothesis verdict before writing any finding:
> [ONE OF:]
> - 'The hypothesis was confirmed: [evidence basis, citing E-01, E-02, ...].'
> - 'The hypothesis was refuted because [evidence basis, citing ...].'
> - 'Partially confirmed under [condition X] (E-01, E-03) but not under [condition Y] (E-02).'
> "

This verdict sentence must appear in the paper verbatim. Findings that follow must be
consistent with it. No evasions ("the evidence is mixed," "further investigation is needed").

Before Principles:
> "Principles are rules a team can apply without reading this paper. I'll use imperative
> form: 'Always X', 'When Y, do Z', 'Prefer A over B because...'. Each will link to the
> finding it came from."

**Paper sections (written in sequence):**

1. **Abstract** -- <200 words. Question, method, key finding. Not structure.
2. **Hypothesis** -- H-01 with source file path.
3. **Method** -- Skills run, artifacts produced, why this approach.
4. **Evidence** -- Numbered cited claims. `[claim] [source: file, reference]`
5. **Findings** -- Verdict sentence first. Then F-01, F-02, F-03+ (conclusions, not data).
6. **Principles** -- P-01 [from F-xx], P-02 [from F-xx]. Action-oriented rules.
7. **Limitations** -- Honest scope boundaries.
8. **Future Work** -- 2+ specific investigable questions.

---

### Step 4: Panel Review (Transcript)

**Domain Expert:**
> "I've read the paper. On domain accuracy: [substantive critique or endorsement].
> My score: [N/10]."

**Practitioner:**
> "I've read the principles. On practical applicability: [substantive critique or endorsement].
> My score: [N/10]."

**Skeptic:**
> "I'm checking my prediction from Step 2. [PREDICTION OUTCOME: CONFIRMED / RESOLVED / STILL PRESENT].
> [One sentence on what the author did or didn't address.]"

---

### Step 5: Amend

**Lead Author:**
> "Amendment A-01: [Section] -- [Change] because [reason]."

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```

---

## V-05: Skeptic-First + Inertia Framing (Combined)

**Axis:** Role sequence + inertia framing -- Skeptic runs before authoring; a pre-printed
`## Status Quo` section makes the do-nothing baseline first-class; all findings are tested
against what the team would have concluded without the investigation
**Hypothesis:** Framing inertia explicitly (what was already known, what could have been
assumed without any investigation work) forces the paper to justify its existence. Findings
that merely confirm prior assumptions are called out. Principles that add no new guidance
over conventional wisdom are flagged. C-10 (cold-start readable) improves because the Status
Quo section gives new readers the baseline they'd otherwise have to infer. This is the highest
ambition variation -- it asks the paper to answer "why did we need to investigate this at all?"

```
You are running /prove:publish for Signal.

Stock roles: Skeptic (pre-flight + post-review), Lead Author, Domain Expert, Practitioner.

**Inertia rule:** Before authoring begins, the Skeptic establishes the status quo baseline --
what a team could have concluded without any investigation. Every finding will be tested
against this baseline. A finding that merely confirms conventional wisdom is noted as
`[BASELINE MATCH]`. A finding that diverges from or refutes the baseline is noted as
`[NEW SIGNAL]`. Papers with no NEW SIGNAL findings are flagged for scope reconsideration.

---

### Phase 1: Setup

Read all prove artifacts for the topic under `simulations/prove/`. Disclose:

```
Artifacts loaded:
- hypothesis: [path or "not found"] (H-01: "[text]")
- analysis: [path, N findings]
- interview: [path, N exchanges] or [not found]
- websearch: [path, N sources] or [not found]
- synthesize: [path] or [not found]
```

If no hypothesis: stop and report. Do not proceed.

---

### Phase 2: Skeptic Pre-Flight + Status Quo Baseline

**Skeptic** runs before any section is written.

**Part A: Pre-flight checklist**
```
SKEPTIC PRE-FLIGHT:
[ ] Hypothesis (H-01) -- will verify Findings resolves it with an explicit verdict sentence.
[ ] Evidence traceability -- will flag any claim without a named artifact citation.
[ ] Findings quality -- will check each finding is a conclusion, not a data summary.
[ ] Principles actionability -- will check each principle is a rule, not a vague statement.
[ ] New signal check -- will verify at least one finding diverges from the baseline below.
```

**Part B: Status quo baseline**

The Skeptic establishes what a team could have assumed without this investigation:

```
STATUS QUO BASELINE (established before authoring):
Without this investigation, a team would likely have assumed:
- [Assumption 1 -- what conventional wisdom says about this topic]
- [Assumption 2 -- what could be inferred from general domain knowledge]
- [Assumption 3 -- what analogous prior work suggests]

Do-nothing cost: Without investigating H-01, the team would have
[FILL: proceeded with assumption X / remained uncertain about Y / used workaround Z].

Inertia saved: If all findings match the baseline, this paper confirms the obvious.
The investigation adds value only if at least one finding is a NEW SIGNAL.
```

The Lead Author reads both parts before writing any section.

---

### Phase 3: Write the Paper

**Required sections (in order):**

**1. Abstract** (<200 words: question, method, key finding. No structure descriptions.)

**2. Hypothesis**
H-01: [text] (source: [file path])

**3. Status Quo**
Paste the Skeptic's baseline from Phase 2 Part B here. This section explains what was
already known or assumed before the investigation. Cold-start readers use this section
to orient themselves without needing to know the project history.

```
## Status Quo
Before this investigation, conventional understanding held:
- [Assumption 1]
- [Assumption 2]
[...]
This investigation was motivated by: [tension, uncertainty, or gap in the baseline].
```

**4. Method**
Which prove skills ran. What evidence was gathered. Why this approach.
Cold-start readable: define any domain-specific terms.

**5. Evidence**
Every claim cites a named artifact: `[claim] [source: file, reference]`
Minimum 3 cited claims.

**6. Findings**

HYPOTHESIS VERDICT: [Confirmed / Refuted / Partially confirmed under X but not Y]
Rationale: [One sentence citing specific evidence items.]

F-01: [conclusion] [BASELINE MATCH / NEW SIGNAL]
F-02: [conclusion] [BASELINE MATCH / NEW SIGNAL]
F-03: [conclusion] [BASELINE MATCH / NEW SIGNAL]

**Inertia check:** If all findings are BASELINE MATCH, append:
```
INERTIA FLAG: All findings confirmed prior assumptions. The investigation validated
the baseline but produced no new signal. Future work should investigate [gap].
```

If at least one finding is NEW SIGNAL, append:
```
INVESTIGATION VALUE: Finding [F-xx] diverges from the status quo baseline --
this is the primary contribution of this paper.
```

**7. Principles**
P-01 [from F-xx]: [rule]
P-02 [from F-xx]: [rule]
Minimum 2. Each must be action-oriented.
Tag each: `[EXTENDS BASELINE]` if it refines conventional wisdom, `[REPLACES BASELINE]`
if it contradicts it.

**8. Limitations**
Honest scope boundaries. What cannot be concluded.

**9. Future Work**
Minimum 2 specific investigable questions.
At least one should target the gaps the Skeptic's baseline identified.

---

### Phase 4: Panel Review

**Domain Expert:**
Critique on domain accuracy + status quo baseline correctness.
Score: [N/10]

**Practitioner:**
Critique on principle actionability.
Score: [N/10]

**Skeptic Post-Review:**
```
SKEPTIC POST-REVIEW:
Pre-flight items resolved: [N/5]
New signal count: [N findings tagged NEW SIGNAL]
Verdict: [APPROVED / FLAG: reason]
```

---

### Phase 5: Amend

```
AMENDMENT A-01: [Section] -- [Change] -- [Triggered by: user / Domain Expert / Practitioner / Skeptic]
```

---

### Output

`simulations/prove/publications/{topic}-paper-{date}.md`
```
