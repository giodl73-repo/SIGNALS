Written to `simulations/quest/variations/prove-synthesize-variations-R2-2026-03-14.md`.

---

## Round 2 — V-01 through V-05

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Lifecycle emphasis — anti-pattern-first gates | Gates that open with "NOT: X" foreclose failure modes before the writer reaches them; balanced gates let compliant-but-wrong outputs through |
| **V-02** | Phrasing register — formal verdict language | FINDING/RULING/DISSENT/HOLDINGS trigger a different cognitive mode than PHASE/SECTION — verdict register prevents hedging at the lexical level |
| **V-03** | Output format — continuous prose, no section headers | Removing section headers forces structural work into transitions; C-12 becomes the only available path when there are no table boundaries to retreat to |
| **V-04** | Role sequence + anti-pattern gates (combo) | ADVERSARY role must name a specific failure mode before the verdict is sealed — pre-verdict anti-pattern declaration is stronger than post-hoc gate checking |
| **V-05** | Imperative register + phase gates (combo — V-03 R1 × V-05 R1) | V-03 R1 prevented hedging but had no standalone mandate (C-10 fail); V-05 R1 had standalone mandate but permissive framing; the combination inherits both mechanisms |

**Key design decisions for R2:**

- **Every variation carries C-10 explicitly.** R1 found V-01–V-04 all failed C-10 because standalone mandate was assumed, not declared. All five R2 variations open with an explicit mandate.
- **C-11 and C-12 are structural targets, not checkboxes.** V-01 makes anti-pattern gates the default gate structure. V-03 eliminates tables structurally. V-04 embeds anti-pattern declaration inside a required role. V-05 names the anti-pattern inline ("a table with a 'why' column is a ranked list").
- **Single-axis isolation**: V-01, V-02, V-03 each vary one axis cleanly. V-04 and V-05 are the combinations.
- **V-05 is the R1-recommended combo** (V-03 R1 imperative register × V-05 R1 phase gates). Expected to score near 100 under v2 rubric. The R2 discriminator will be whether V-04's adversarial pre-challenge produces a stronger C-04/C-11 combination than V-05's imperative/gate structure.
e ("ranked argument, not ranked list") and it stopped. This variation makes anti-pattern naming the default gate structure.

```
You are running prove:synthesize for {topic}. Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate in your opening paragraph before any inventory or verdict.

Write argumentative sections -- verdict, evidence hierarchy, confidence rationale -- in prose paragraphs, not tables or bullet lists.

---

## PHASE 1: SIGNAL INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: name the signal artifact, state what it investigated, state what it found. If no signals exist: stop. "No signals found for {topic}. Cannot synthesize."

Phase 1 complete. Signal count: [N].

### GATE 1 -- Anti-pattern check
- [ ] NOT: signals listed without naming the artifact
- [ ] NOT: evaluation or verdict present in this phase (inventory only)
- [ ] NOT: signal count omitted
- [ ] Positive check: every signal has exactly one summary sentence

GATE 1 CLEARED. Proceed to Phase 2.

---

## PHASE 2: VERDICT

State your answer. This is a judgment, not a summary.

**Answer: [YES / NO / MAYBE]**

[Verdict paragraph. Open with the answer word. Explain what the Phase 1 signals say together. Reference specific signals by name. The verdict paragraph is your synthesis judgment.]

**Confidence: [N]/100**

[Confidence paragraph. What drove this number up? What capped it? High confidence (>= 75): name which signals converge and explain why their convergence is meaningful. Low confidence (<= 40): name the specific gap or conflict.]

### GATE 2 -- Anti-pattern check
- [ ] NOT: answer is a hedge, qualification, or restatement of the hypothesis ("this depends on...")
- [ ] NOT: verdict paragraph is a list of signal findings with a one-sentence conclusion appended at the end
- [ ] NOT: confidence stated as a number only, without rationale paragraph
- [ ] NOT: answer is anything other than YES, NO, or MAYBE
- [ ] Positive check: answer word appears in the opening sentence of the verdict paragraph

GATE 2 CLEARED. Proceed to Phase 3.

---

## PHASE 3: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write one prose paragraph per signal. Each paragraph opens with the signal name and argues why it carried more weight toward the Phase 2 verdict than the signals ranked below it.

[Rank 1 paragraph: why most influential. Answer: why this signal over rank 2?]

[Rank 2 paragraph: what does it add that rank 1 did not establish? Why second, not first?]

[Rank 3 paragraph, or state absent if fewer than 3 signals.]

### GATE 3 -- Anti-pattern check
- [ ] NOT: evidence hierarchy is a table with a "why" column -- a table is an annotated list, not an argument
- [ ] NOT: rank 1 justified only as "it had the strongest support" without comparing to rank 2
- [ ] NOT: any named signal is absent from the Phase 1 inventory (invented signals fail this gate)
- [ ] Positive check: each paragraph argues relative weight, not presence of support

GATE 3 CLEARED. Proceed to Phase 4.

---

## PHASE 4: COUNTER-EVIDENCE

[One paragraph minimum. Name the strongest argument against the Phase 2 verdict. Where did it originate -- a signal in the inventory, a logical gap, or an unconsidered scenario? State your rebuttal, or state "unresolved -- limits confidence ceiling" explicitly.]

[If no counter-evidence found: write a paragraph explaining the absence and noting that absence may indicate incomplete investigation coverage, not strong evidence.]

### GATE 4 -- Anti-pattern check
- [ ] NOT: counter-evidence section skipped or collapsed to "none identified"
- [ ] NOT: rebuttal stated as "this evidence is weak" without explaining why the verdict holds despite it
- [ ] NOT: source of counter-argument omitted
- [ ] Positive check: section present, sourced, and either rebutted or "unresolved" stated

GATE 4 CLEARED. Proceed to Phase 5.

---

## PHASE 5: PRINCIPLES AND OPEN QUESTIONS

**What this investigation teaches beyond this hypothesis:**

[At least one declarative principle. "X implies Y." "When Z, expect W." Not a restatement of the verdict. Must generalize beyond the specific topic.]

**What the investigation did not resolve:**

[At least one specific open question. Name the actual question. Explain why it is still open. State the concrete next step: which prove sub-skill, or what external action.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, anti_pattern_gates_cleared (true/false).
```

---

## V-02: Phrasing Register -- Formal Verdict Language

**Axis**: Phrasing register -- legal/verdict register (FINDING, RULING, DISSENT, HOLDINGS)
**Hypothesis**: Formal verdict register creates cognitive commitment weight that prevents hedging more effectively than phase-and-gate framing. A RULING cannot be "it depends" -- the register forecloses that answer at the lexical level. The vocabulary triggers a different cognitive mode than SURVEYOR/JUDGE/ADVOCATE.

```
You are running prove:synthesize for {topic}. Issue a formal synthesis ruling. This document stands alone: a reader with no prior knowledge of the investigation signals must understand the ruling, the evidence basis, the dissent, and the open record from this document alone. State this requirement in your opening paragraph.

Write argumentative sections -- the ruling, the evidence basis, the confidence rationale -- in prose paragraphs. No tables in these sections.

---

## PRELIMINARY FINDINGS

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: the signal artifact name, what it investigated, what it found. If no signals: stop. Issue: "INCOMPLETE RECORD -- no signals found for {topic}. Ruling cannot proceed."

Record count: [N]

---

## RULING

**FINDING: [YES / NO / MAYBE]**

[Ruling paragraph. Open with FINDING and the answer word. Issue a determination of what the record establishes, read as a whole -- not a summary of individual findings. Reference specific signals to ground the ruling. A RULING is a position, not an aggregation.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove the confidence level? What capped it or would have raised it? High confidence (>= 75): name the converging signals and explain why their convergence is meaningful. Low confidence (<= 40): name the specific gap or conflict that prevents higher confidence. A CONFIDENCE notation without a rationale paragraph fails this section.]

### RULING SEAL
- [ ] FINDING is YES/NO/MAYBE -- no other values permitted
- [ ] FINDING stated in the opening sentence of the ruling paragraph
- [ ] Ruling paragraph is a determination, not a list of findings with a conclusion appended
- [ ] Confidence rationale paragraph present (score alone is insufficient)

RULING SEALED.

---

## EVIDENCE BASIS

Name up to 3 signals as primary evidence. This is a ranked argument, not an annotated list. For each, issue a prose paragraph arguing why this signal was more determinative than signals ranked below it -- not what it found, but why its weight exceeded the others.

**PRIMARY EVIDENCE -- [Signal name]**
[Paragraph. Why most determinative: what does this signal establish that others could not, and why does that carry greater weight toward the RULING? Answer the comparative question: why primary over secondary?]

**SECONDARY EVIDENCE -- [Signal name]**
[Paragraph. What does it add that primary evidence did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE -- [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE BASIS SEAL
- [ ] Each evidence entry is a prose paragraph -- not a table row or bullet
- [ ] Each entry argues relative weight, not presence of support
- [ ] All named signals exist in PRELIMINARY FINDINGS
- [ ] Comparative question answered for each rank

EVIDENCE BASIS SEALED.

---

## DISSENT

[Paragraph. What is the strongest argument against the RULING? Source it: a signal in the record, a logical gap, or an unconsidered scenario. Issue a rebuttal from the ruling's perspective, or state "dissent unresolved -- limits confidence ceiling" explicitly. This section cannot be empty or replaced with "no opposition identified."]

[If genuinely no counter-evidence found: issue a paragraph explaining why the record is one-sided and noting that absence of dissent may indicate incomplete investigation coverage, not evidentiary strength.]

---

## HOLDINGS AND OPEN RECORD

**Holdings** (what this ruling establishes beyond this case):

[At least one declarative principle that generalizes beyond this topic. "X implies Y." "When Z, expect W." Holdings that merely restate the FINDING are not Holdings.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined -- what evidence was absent or inconclusive. State the next investigative action: which prove sub-skill or concrete step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, finding, signal_count, dissent_sourced (true/false).
```

---

## V-03: Output Format -- Continuous Prose, No Section Headers

**Axis**: Output format -- continuous prose with no section breaks, phase labels, or gate checklists
**Hypothesis**: Section headers do structural work. Removing them forces that work into the prose: the writer must construct explicit transitions ("Having inventoried the signals, the verdict follows...") and embed structural signals in sentences. This produces denser C-10 compliance and makes C-12 the only available path -- there is no table to fall back on because there are no section boundaries to contain one.

```
You are running prove:synthesize for {topic}. Write a continuous prose synthesis -- no section headers, no phase labels, no gate checklists. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening sentence. The structure of the synthesis must emerge from the prose itself, not from headers that label it.

Write argumentative content -- verdict, evidence ranking, confidence rationale -- as prose paragraphs. There are no tables permitted. The synthesis is prose from start to finish.

---

Begin by inventorying the signals. Glob simulations/prove/investigations/{topic}-*. Write one sentence per signal: name the artifact, state what it investigated, state what it found. Count them. If no signals exist, write: "No signals found for {topic}. Synthesis cannot proceed." and stop.

With the inventory complete, state your answer. The answer word -- YES, NO, or MAYBE -- is the opening word of your verdict paragraph. Follow it with a paragraph explaining what the signals say together: not what each one found individually, but what they establish as a whole. Reference specific signals by name. This is your synthesis judgment. Do not hedge in the verdict paragraph. If you are uncertain, that belongs in the confidence score.

Immediately after the verdict paragraph, write your confidence paragraph. State a number (0-100). Then explain it in prose: what pushed it up, what capped it. High confidence (>= 75) requires naming the signals that converge and explaining why their convergence is meaningful -- not just that multiple signals support the answer, but why their agreement matters. Low confidence (<= 40) requires naming the specific gap or conflict. A confidence number without this explanation fails the synthesis.

Next, argue your evidence hierarchy. Name up to three signals as most influential. For each, write a paragraph that opens with the signal name and argues why it carried more weight toward your verdict than the signals you ranked below it. This is a ranked argument, not a ranked list. "It supported the hypothesis" is not an argument for rank. Each paragraph must answer the comparative question: why this signal over the one ranked below it?

Then write your counter-evidence paragraph. Identify the strongest argument against your verdict. Where does it come from -- a signal in the inventory, a logical gap in coverage, an unconsidered scenario? Write your rebuttal, or write: "Unresolved. This limits the confidence ceiling." Do not skip this. If you found no counter-evidence, write a paragraph explaining that absence and noting it may indicate incomplete investigation coverage, not evidentiary strength.

Close with two paragraphs on what the investigation revealed beyond itself. First, state at least one principle that generalizes beyond this topic -- declarative form, "X implies Y" or "When Z, expect W." A restatement of your verdict is not a principle. Second, name at least one specific open question the investigation did not resolve -- not "more research needed" but the actual question, why it is still open, and the concrete next step.

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, format (continuous_prose).
```

---

## V-04: Role Sequence + Anti-Pattern Gates (Combo)

**Axes**: Role sequence (ADVERSARY role added pre-verdict) + anti-pattern gates
**Hypothesis**: A dedicated ADVERSARY role that must name a specific failure mode before the verdict is sealed produces stronger C-04 and C-11 simultaneously -- the adversary's challenge is a required anti-pattern declaration, not an optional reflection. Combining this with anti-pattern-first gates produces the maximum foreclosure of compliant-but-wrong outputs.

```
You are running prove:synthesize for {topic}. Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening paragraph.

Write argumentative sections -- verdict, evidence hierarchy, confidence rationale -- in prose paragraphs, not tables or bullet lists.

---

## SURVEYOR: INVENTORY

Glob simulations/prove/investigations/{topic}-*. Write one sentence per signal: name the artifact, state what it investigated, state what it found. If no signals: stop.

Signal count: [N]

---

## ADVERSARY: PRE-VERDICT CHALLENGE

[Run before the verdict. The ADVERSARY makes the strongest case that the evidence does not yet support a verdict -- or that the verdict the evidence seems to suggest is wrong. This is not counter-evidence to a verdict that has been issued. It is a pre-verdict challenge.]

What is the weakest point in the SURVEYOR inventory? [Name the specific gap, thin signal, or missing evidence type that an adversary would exploit.]

What is the strongest argument that the answer should be MAYBE even if signals appear to lean YES or NO? [State the adversary's best case for uncertainty.]

Anti-pattern gate: [Name one specific failure mode this synthesis must avoid, given the structure of this particular signal set. Not a generic rule -- specific to what the SURVEYOR inventory makes likely. Example form: "This synthesis must not [do X], because [what the inventory structure makes likely]."]

---

## JUDGE: VERDICT

[Read the SURVEYOR inventory and the ADVERSARY challenge. Issue your verdict against the adversary's best case.]

**Answer: [YES / NO / MAYBE]**

[Verdict paragraph. Open with the answer word. What do the signals say together? Address the ADVERSARY challenge explicitly: did it reduce confidence, cap it, or fail to move the answer? The verdict is a judgment against the adversary's best case, not a summary of signal findings.]

**Confidence: [N]/100**

[Confidence paragraph. What drove it up? What capped it -- signal gaps, the ADVERSARY challenge, or unconsidered scenarios? A confidence number without this paragraph fails this section.]

### VERDICT GATE -- Anti-pattern check
- [ ] NOT: verdict is a list of signal summaries with a conclusion attached
- [ ] NOT: ADVERSARY challenge was acknowledged but not addressed
- [ ] NOT: confidence stated without explaining what capped it or drove it
- [ ] NOT: answer is anything other than YES/NO/MAYBE
- [ ] Positive check: answer word in opening sentence; ADVERSARY challenge addressed in verdict or confidence paragraph

VERDICT SEALED.

---

## ADVOCATE: KEY EVIDENCE

Name up to 3 signals. This is a ranked argument, not a ranked list. Write one prose paragraph per signal. Each paragraph opens with the signal name and argues why it carried more weight toward the verdict than signals ranked below it.

[Rank 1 paragraph: why most influential. Not just "strongest support" -- why stronger than rank 2 specifically?]

[Rank 2 paragraph: what does it add that rank 1 did not establish? Why second and not first?]

[Rank 3 paragraph, or state absent.]

### EVIDENCE GATE -- Anti-pattern check
- [ ] NOT: evidence hierarchy is a table with a "why" column -- a table is an annotated list, not an argument
- [ ] NOT: rank 1 justified only as "strongest support" without comparison to rank 2
- [ ] NOT: any named signal absent from SURVEYOR inventory

EVIDENCE GATE CLEARED.

---

## SKEPTIC: COUNTER-EVIDENCE

[This section resolves the ADVERSARY pre-verdict challenge and names any additional signal-based counter-evidence.]

[Paragraph. The ADVERSARY raised a challenge. State it again briefly and issue the JUDGE's rebuttal. If the challenge was not fully addressed: "Unresolved. This limits the confidence ceiling." If the strongest counter-evidence is the ADVERSARY challenge itself, say so explicitly and explain how the verdict holds despite it.]

[If additional signal counter-evidence exists beyond the ADVERSARY challenge: name it, source it, and state rebuttal or "unresolved."]

---

## SCHOLAR: PRINCIPLES AND NAVIGATOR: OPEN QUESTIONS

**Principles** (declarative, generalizable -- not restatements of the verdict):

P-01: [X implies Y. / When Z, expect W.]

**Open Questions** (specific, actionable):

Q-01: [Specific question]
Why open: [what evidence was absent or inconclusive]
Next step: [prove sub-skill or concrete action]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, adversary_challenge_resolved (true/false), anti_pattern_named (true/false), signal_count.
```

---

## V-05: Imperative Register + Phase Gates (Combo -- V-03 R1 + V-05 R1)

**Axes**: Phrasing register (direct imperative) + lifecycle emphasis (explicit phase gates)
**Hypothesis**: V-03 R1 was strongest for C-05 (anti-hedging pressure through direct questions); V-05 R1 was strongest for C-10 (explicit standalone mandate + prose gates). Combining them addresses their individual gaps: V-03 R1 had no standalone mandate (C-10 fail); V-05 R1 used instructional framing that could permit hedging. The combined variation inherits both mechanisms.

```
You are running prove:synthesize for {topic}. Produce a synthesis that stands alone. State this now, in your opening sentence: a reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. Do not assume context. Explain everything.

Write in prose. No tables in argumentative sections. Answer directly -- no hedging, no qualification. If you are uncertain, put it in the confidence score, not the answer. Each phase is gated.

---

## PHASE 1: SIGNAL INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal: write one sentence. Name it. What did it investigate? What did it find?

If no signals exist: stop. Write "No signals found for {topic}. Cannot synthesize." Do not proceed to Phase 2.

Phase 1 complete. Signal count: [N].

### GATE 1
- [ ] Every found signal has exactly one summary sentence
- [ ] Each sentence names the signal by artifact name
- [ ] No evaluation present -- inventory only
- [ ] Signal count recorded

GATE 1 CLEARED. Proceed to Phase 2.

---

## PHASE 2: VERDICT

What is your answer? Pick one: YES, NO, or MAYBE.
- YES = evidence weight supports the hypothesis.
- NO = evidence weight refutes it.
- MAYBE = evidence is genuinely split. Not "I am avoiding commitment."

Write the answer word first. Then write a prose paragraph: what do the Phase 1 signals say together? Reference specific signals by name. Do not list each signal's finding -- synthesize what they establish as a whole. This paragraph is your judgment.

How confident are you? Write a number (0-100). Then write a prose paragraph explaining it: what pushed the number up, what capped it. High confidence (>= 75): name which signals converge and explain why their convergence is meaningful. Low confidence (<= 40): name the specific gap or conflict. A number without this paragraph fails -- "confidence is X" does not pass.

### GATE 2
- [ ] Answer is YES/NO/MAYBE -- no other values
- [ ] Answer stated in the opening sentence of the verdict paragraph
- [ ] Verdict paragraph is a synthesis judgment, NOT a list of signal findings with a conclusion attached
- [ ] Confidence paragraph present and explains the number -- score alone fails this gate

GATE 2 CLEARED. Proceed to Phase 3.

---

## PHASE 3: EVIDENCE HIERARCHY

Which signals most influenced your verdict? Name up to 3. For each: write a prose paragraph. Open with the signal name. Then argue why it carried more weight toward your verdict than the signals ranked below it.

This is a ranked argument, not a ranked list. A table with a "why" column is a ranked list -- it allows you to fill cells without constructing an argument. Each paragraph must answer the comparative question: why this signal over the one below it?

[Rank 1 paragraph: why most influential? Not "strongest support" -- why stronger than rank 2 specifically?]

[Rank 2 paragraph: what does it add that rank 1 did not establish? Why second and not first?]

[Rank 3 paragraph, or state absent if fewer than 3 signals.]

### GATE 3
- [ ] Up to 3 signals named
- [ ] Each entry is a prose paragraph (NOT a table row or bullet point)
- [ ] Each paragraph answers the comparative question -- not just restates the finding
- [ ] All named signals exist in Phase 1 inventory -- invented signals fail this gate

GATE 3 CLEARED. Proceed to Phase 4.

---

## PHASE 4: COUNTER-EVIDENCE

What argues against your verdict? Name the strongest case. Where does it come from: a signal in the inventory, a logical gap in coverage, or an unconsidered scenario?

Write at least one prose paragraph. State your rebuttal -- how does the verdict hold despite this argument? If it does not fully hold: write "Unresolved. This limits the confidence ceiling." Do not skip this phase. Do not replace it with "no counter-evidence found" without writing a paragraph explaining the absence and noting that absence may indicate incomplete investigation coverage.

### GATE 4
- [ ] Counter-evidence section is NOT skipped
- [ ] Source of counter-argument is named (signal, gap, or scenario)
- [ ] Rebuttal is stated, or "unresolved" is stated explicitly with confidence impact noted

GATE 4 CLEARED. Proceed to Phase 5.

---

## PHASE 5: PRINCIPLES AND OPEN QUESTIONS

What did you learn that generalizes beyond this hypothesis?

Write at least one principle. Declarative form required: "X implies Y" or "When Z, expect W." A restatement of your verdict is not a principle.

What did the investigation NOT resolve?

Name at least one specific open question. "More research needed" is not a question. Write the actual question, explain why it is still open, and name the concrete next step: which prove sub-skill or what action.

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, gate_1_cleared, gate_2_cleared, gate_3_cleared, gate_4_cleared (all true/false).
```
