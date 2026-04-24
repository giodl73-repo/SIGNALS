## Round 3 — V-01 through V-05

Written to `simulations/quest/variations/prove-synthesize-variations-R3-2026-03-14.md`.

---

| # | Axis | R3 Target |
|---|------|-----------|
| **V-01** | Lifecycle emphasis — NOT:-first gate ordering | C-13 only |
| **V-02** | Phrasing register — formal verdict register (DETERMINATION/DISSENT/HOLDINGS) | C-14 only |
| **V-03** | Role sequence — pre-committed counter-evidence before verdict | C-15 only |
| **V-04** | NOT:-first gates + formal verdict register (combo) | C-13 + C-14 |
| **V-05** | Role sequence + NOT:-first gates + pre-committed counter-evidence (full combo) | C-13 + C-14 + C-15 |

---

**Key design decisions for R3:**

**Single-axis isolation (V-01/V-02/V-03):** Each variation fires exactly one of C-13, C-14, C-15 while leaving the other two exposed. This exposes each new criterion as a live discriminator independently before combinations are evaluated.

**C-13 mechanism (V-01, V-04, V-05):** Every gate item is formatted as `NOT: [failure mode] — [reason]. Positive condition: [pass condition]`. The prohibition is encountered before the pass condition. Variations using standard gate format (V-02, V-03) leave C-13 unfired.

**C-14 mechanism (V-02, V-04, V-05):** `DETERMINATION:` appears as section label and sentence-level declaration. The register word forecloses post-verdict hedging — `DETERMINATION: MAYBE` cannot be followed by vague language in a way that `Based on the evidence...` can. V-01 and V-03 use `Answer: / Verdict` format — C-14 unfired.

**C-15 mechanism (V-03, V-05):** The adversarial challenge section appears before the verdict section in document order. `NOT: this section is placed after the DETERMINATION` is embedded in the prose instruction itself. V-01, V-02, V-04 place counter-evidence (DISSENT/Phase 4) after verdict — C-15 unfired.

**R2 wins inherited in all five:** Standalone mandate in opening paragraph (C-10); anti-pattern gate naming with specific failure mode labels (C-11); prose mandate for argumentative sections (C-12).

**Predicted R3 discrimination:**
- V-01 earns C-13; fails C-14, C-15
- V-02 earns C-14; fails C-13, C-15
- V-03 earns C-15; fails C-13, C-14
- V-04 earns C-13 + C-14; fails C-15
- V-05 earns C-13 + C-14 + C-15 — maximum score

The discriminating question: does V-03's structural pre-commitment (document order alone, no gate language) satisfy C-15, or does C-15 require an explicit `NOT:` clause naming the failure mode? The V-05 ADVERSARY gate includes `NOT: this section is placed after the DETERMINATION...` — V-03 includes the same clause in prose instruction. That equivalence or difference is the R3 finding.
iations**: Explicit standalone mandate in opening (C-10); anti-pattern gates name failure modes by name, not just pass conditions (C-11); argumentative sections in prose, not tables (C-12).
- **C-11/C-12 tension carried forward**: NOT:-first gate ordering (V-01, V-04, V-05) and prose mandate (C-12) are in partial tension — gates require checklist structure, prose mandate pushes against it. R3 inherits the tension; variations that solve both (by embedding gate logic in prose instructions rather than checkbox lists) earn higher C-12 compliance.
- **Adversarial conditions**: Thin signal protocol (explicit fallback when N < 3), MAYBE hypothesis handling (MAYBE must name specific uncertainty, not serve as hedge), and inline gate enforcement (in V-03/V-05, the NOT: prohibition is embedded in prose instruction, not only in a checklist).

---

## V-01: Lifecycle Emphasis — NOT:-first Gate Ordering

**Axis**: Lifecycle emphasis — all gate items restructured so NOT: failure mode precedes positive pass condition
**Hypothesis**: Gates that open with NOT: foreclose the failure mode before the writer reaches the pass condition. Reverse-ordered gates allow satisfying the presence check before encountering the prohibition. Pattern: every gate item states what must not happen — and why — before stating what must happen. This is the single-axis implementation of C-13.

```
You are running prove:synthesize for {topic}. Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening paragraph.

Write argumentative sections — verdict, evidence hierarchy, confidence rationale — in prose paragraphs, not tables or bullet lists.

---

## PHASE 1: SIGNAL INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: name the artifact, state what it investigated, state what it found. If no signals exist: stop. Write "No signals found for {topic}. Cannot synthesize."

Phase 1 complete. Signal count: [N].

### GATE 1
- NOT: any signal is described without naming its artifact — unnameable signals are unverifiable. Positive condition: every signal is identified by artifact name.
- NOT: evaluation or verdict language appears in this phase — inventory precedes judgment. Positive condition: phase contains description only, no evaluation.
- NOT: signal count is omitted — count is required for confidence calibration. Positive condition: signal count is stated.

GATE 1 CLEARED. Proceed to Phase 2.

---

## PHASE 2: VERDICT

State your answer. This is a judgment, not a summary.

**Answer: [YES / NO / MAYBE]**

[Verdict paragraph. Open with the answer word. Explain what the Phase 1 signals say together — not what each says individually, but what they establish as a whole. Reference specific signals by name. This is your synthesis judgment.]

**Confidence: [N]/100**

[Confidence paragraph. What drove this number? What capped it? High confidence (>= 75): name which signals converge and explain why their convergence is meaningful — not just that multiple signals support the answer, but why their agreement matters. Low confidence (<= 40): name the specific gap or conflict. MAYBE requires naming the specific uncertainty that prevents YES or NO. A number without this paragraph fails.]

### GATE 2
- NOT: the answer is a hedge, qualification, or restatement of the hypothesis ("it depends on...") — hedging is not a verdict. Positive condition: answer is YES, NO, or MAYBE; MAYBE names the specific uncertainty.
- NOT: the verdict paragraph is a list of signal findings with a conclusion appended at the end — that is a summary, not a synthesis. Positive condition: verdict paragraph explains what the signals say together, not what each says individually.
- NOT: confidence is stated as a number only, without a rationale paragraph — a score without reasoning cannot be interrogated or falsified. Positive condition: a prose paragraph follows the score, explaining what drove it up and what capped it.
- NOT: the answer word is absent from the opening sentence of the verdict paragraph — the position must lead, not follow from reasoning. Positive condition: answer word appears in the opening sentence of the verdict paragraph.

GATE 2 CLEARED. Proceed to Phase 3.

---

## PHASE 3: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write one prose paragraph per signal. Each paragraph opens with the signal name and argues why it carried more weight toward the Phase 2 verdict than the signals ranked below it.

[Rank 1 paragraph: why most influential? Why this signal over rank 2 specifically?]

[Rank 2 paragraph: what does it add that rank 1 did not establish? Why second and not first?]

[Rank 3 paragraph, or state absent if fewer than 3 signals.]

### GATE 3
- NOT: evidence hierarchy is a table with a "why" column — a table is an annotated list, not an argument; filling cells requires no argument construction. Positive condition: each evidence entry is a prose paragraph.
- NOT: rank 1 is justified only as "it had the strongest support" without comparing to rank 2 — that names presence of support, not relative weight. Positive condition: each paragraph answers the comparative question: why this signal over the one ranked below it?
- NOT: any named signal is absent from the Phase 1 inventory — signals outside the inventory cannot be traced to investigation artifacts. Positive condition: all named signals appear in Phase 1.
- NOT: paragraphs describe what signals found rather than arguing why they outweigh others — description is not argument. Positive condition: each paragraph argues relative weight, not presence of support.

GATE 3 CLEARED. Proceed to Phase 4.

---

## PHASE 4: COUNTER-EVIDENCE

[One paragraph minimum. Name the strongest argument against the Phase 2 verdict. Where did it originate — a signal in the inventory, a logical gap, or an unconsidered scenario? State your rebuttal, or state "Unresolved. This limits the confidence ceiling" explicitly.]

[If no counter-evidence found: write a paragraph explaining the absence and noting that absence may indicate incomplete investigation coverage, not strong evidence.]

### GATE 4
- NOT: counter-evidence section is skipped or collapsed to "none identified" without a paragraph — omission is not a finding. Positive condition: at least one prose paragraph is present.
- NOT: rebuttal states "this evidence is weak" without explaining why the verdict holds despite it — weakness claimed without grounds is an assertion. Positive condition: rebuttal explains how the verdict holds, or "Unresolved" is stated explicitly with confidence impact noted.
- NOT: source of counter-argument is omitted — unsourced opposition cannot be evaluated. Positive condition: counter-argument is sourced to a signal, a gap, or an unconsidered scenario.

GATE 4 CLEARED. Proceed to Phase 5.

---

## PHASE 5: PRINCIPLES AND OPEN QUESTIONS

**Principles** (what this investigation teaches beyond this hypothesis):

[At least one declarative principle. "X implies Y." "When Z, expect W." Not a restatement of the verdict. Must generalize beyond the specific topic.]

**Open Questions** (what the investigation did not resolve):

[At least one specific open question. Name the actual question. Explain why it is still open. State the concrete next step: which prove sub-skill, or what external action.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, not_first_gates (true/false).
```

---

## V-02: Phrasing Register — Formal Verdict Register

**Axis**: Phrasing register — legal/verdict register throughout (DETERMINATION, DISSENT, HOLDINGS)
**Hypothesis**: Formal verdict vocabulary creates anti-hedging commitment at the lexical level, independent of gate structure. DETERMINATION: [YES/NO/MAYBE] cannot be followed by hedging in a way that "Based on the evidence..." can. The register word triggers a different cognitive mode; it forecloses post-register qualification. This is the single-axis implementation of C-14.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document stands alone: a reader with no prior knowledge of the investigation signals must understand the determination, the evidence basis, the dissent, and the open record from this document alone. State this requirement in your opening paragraph.

Write argumentative sections — the determination, the evidence basis, the confidence rationale — in prose paragraphs. No tables in these sections.

---

## PRELIMINARY RECORD

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: name the artifact, state what it investigated, state what it found. If no signals: stop. State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Record count: [N]

---

## DETERMINATION

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record establishes, read as a whole — not a summary of individual record entries. Reference specific signals to ground the determination. A DETERMINATION is a commitment, not an aggregation. DETERMINATION: MAYBE requires naming the specific uncertainty that prevents YES or NO — MAYBE is not a hedge; it is a committed uncertainty with a named resolution condition.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove the confidence level? What capped it or would have raised it? High confidence (>= 75): name the converging signals and explain why their convergence is meaningful. Low confidence (<= 40): name the specific gap or conflict. A CONFIDENCE notation without a rationale paragraph fails this section.]

### DETERMINATION SEAL
- [ ] DETERMINATION: [YES/NO/MAYBE] appears in the opening sentence of the judgment paragraph
- [ ] Judgment paragraph issues a determination of what the whole record establishes — not a list of record findings with a conclusion appended
- [ ] Confidence rationale paragraph present — score alone fails this seal
- [ ] DETERMINATION: MAYBE names the specific uncertainty; MAYBE is not used to avoid commitment when evidence leans YES or NO

DETERMINATION SEALED.

---

## EVIDENCE BASIS

Name up to 3 signals as primary evidence. This is a ranked argument, not an annotated list. For each, issue a prose paragraph arguing why this signal was more determinative than signals ranked below it.

**PRIMARY EVIDENCE — [Signal name]**
[Paragraph. Why most determinative? What does this signal establish that others could not, and why does that carry greater weight toward the DETERMINATION? Answer the comparative question: why primary over secondary?]

**SECONDARY EVIDENCE — [Signal name]**
[Paragraph. What does it add that primary evidence did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE — [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE BASIS SEAL
- [ ] Each entry is a prose paragraph — not a table row or bullet point
- [ ] Each entry argues relative weight, not presence of support
- [ ] All named signals exist in PRELIMINARY RECORD
- [ ] Comparative question answered for each rank: why this tier over the one below?

EVIDENCE BASIS SEALED.

---

## DISSENT

[Paragraph. What is the strongest argument against the DETERMINATION? Source it: a signal in the record, a logical gap, or an unconsidered scenario. Issue a rebuttal, or state: "DISSENT UNRESOLVED — limits confidence ceiling." This section cannot be empty or replaced with "no opposition identified."]

[If genuinely no counter-evidence found: issue a paragraph explaining why the record is one-sided and noting that absence of dissent may indicate incomplete investigation coverage, not evidentiary strength.]

---

## HOLDINGS AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle that generalizes beyond this topic. "X implies Y." "When Z, expect W." Holdings that merely restate the DETERMINATION are not Holdings.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined — what evidence was absent or inconclusive. State the next investigative action: which prove sub-skill or concrete step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, determination_sealed (true/false), dissent_sourced (true/false), signal_count.
```

---

## V-03: Role Sequence — Pre-Committed Counter-Evidence

**Axis**: Role sequence / lifecycle emphasis — adversarial challenge section placed BEFORE verdict section
**Hypothesis**: Structural pre-placement of the adversarial challenge forces the verdict to be formed against the best opposing case already on the table. Counter-evidence inserted after the verdict is selected post-determination and reflects on it — not the same mechanism. The structural ordering is the enforcer, not gate language. This is the single-axis implementation of C-15.

```
You are running prove:synthesize for {topic}. Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, the reasoning, and what to do next from this document alone. State this mandate explicitly in your opening paragraph.

The verdict in this synthesis is issued after the adversarial challenge, not before it. The counter-evidence section precedes the verdict section. Write argumentative sections in prose paragraphs.

---

## PHASE 1: SIGNAL INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: name the artifact, state what it investigated, state what it found. If no signals: stop. Write "No signals found for {topic}. Cannot synthesize."

Signal count: [N]. Phase 1 complete.

### GATE 1
- [ ] Every signal named by artifact identifier
- [ ] Inventory only — no evaluation language
- [ ] Signal count recorded

GATE 1 CLEARED.

---

## PHASE 2: ADVERSARIAL CHALLENGE

NOT: this section is placed after the verdict and filled in post-determination. Counter-evidence selected after the position is formed is not a pre-commitment — it is post-hoc justification. This section runs before Phase 3. The judgment issued in Phase 3 must be formed with this challenge already on the table.

Before issuing any verdict, record the strongest case against the hypothesis.

[Paragraph 1. What is the weakest point in the signal inventory? Name the specific gap, thin signal, or missing evidence type. If signals are thin (N < 3), name what type of signal is absent and why that absence matters for this hypothesis.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if signals appear to lean YES or NO? State the best case for uncertainty. What would the adversary argue to prevent a clear YES or NO?]

[Paragraph 3. What is the best argument for the opposite answer from what the signals suggest? If signals lean YES, name the strongest argument for NO. If signals are mixed, name the argument that the uncertainty is fatal to a clear answer.]

### GATE 2
- [ ] At least two adversarial paragraphs written before any verdict language appears
- [ ] Challenge names specific signals, gaps, or unconsidered scenarios — not generic uncertainty
- [ ] No answer word, verdict, or confidence score present in this phase

GATE 2 CLEARED. Phase 2 adversarial challenge is on the table. Proceed to Phase 3.

---

## PHASE 3: VERDICT

Having recorded the adversarial challenge, now issue your verdict against it.

**Answer: [YES / NO / MAYBE]**

[Verdict paragraph. Open with the answer word. State what the Phase 1 signals say together. Address the Phase 2 adversarial challenge explicitly: does it reduce confidence, cap it, or fail to move the answer? The verdict is formed against the challenge already recorded. MAYBE requires naming the specific uncertainty — not the adversary's challenge alone, but what specific evidence gap prevents YES or NO.]

**Confidence: [N]/100**

[Confidence paragraph. What drove this number? What capped it — signal gaps, the Phase 2 challenge, or unconsidered scenarios?]

### GATE 3
- [ ] Answer is YES, NO, or MAYBE; MAYBE names the specific uncertainty
- [ ] Verdict paragraph addresses the Phase 2 adversarial challenge — the challenge is not ignored
- [ ] Confidence paragraph is present and explains the number
- [ ] Verdict does not encounter the adversarial challenge for the first time — it was already recorded in Phase 2

GATE 3 CLEARED. Proceed to Phase 4.

---

## PHASE 4: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write one prose paragraph per signal arguing why it carried more weight toward the Phase 3 verdict than signals ranked below it.

[Rank 1 paragraph: why most influential? Why this signal over rank 2 specifically?]

[Rank 2 paragraph: what does it add that rank 1 did not establish? Why second and not first?]

[Rank 3 paragraph, or state absent if fewer than 3 signals.]

### GATE 4
- [ ] Each entry is a prose paragraph — not a table row or bullet
- [ ] Each paragraph argues relative weight, not presence of support
- [ ] All named signals exist in Phase 1 inventory

GATE 4 CLEARED. Proceed to Phase 5.

---

## PHASE 5: PRINCIPLES AND OPEN QUESTIONS

**Principles** (what this investigation teaches beyond this hypothesis):

[At least one declarative principle. "X implies Y." "When Z, expect W." Not a restatement of the verdict.]

**Open Questions** (what the investigation did not resolve):

[At least one specific open question. Name it. Explain why it is still open. State the concrete next step: which prove sub-skill, or what external action.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, adversarial_pre_verdict (true/false).
```

---

## V-04: NOT:-first Gates + Formal Verdict Register (Combo)

**Axes**: NOT:-first gate ordering (C-13) + formal verdict register (C-14)
**Hypothesis**: Combining NOT:-first gates with DETERMINATION/DISSENT vocabulary denies two independent paths to hedging: NOT:-first gates foreclose structural failure modes before the writer reaches the pass condition; DETERMINATION: register forecloses post-verdict hedging at the lexical level. A variation that satisfies only one axis can still permit failure through the other. This combo closes both gaps while keeping counter-evidence post-verdict — leaving C-15 as a live discriminator.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document stands alone: a reader with no prior knowledge of the investigation signals must understand the determination, the evidence basis, the dissent, and what to do next from this document alone. State this requirement in your opening paragraph.

Write argumentative sections — the determination, the evidence basis, the confidence rationale — in prose paragraphs. No tables in these sections.

---

## PRELIMINARY RECORD

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: name the artifact, state what it investigated, state what it found. If no signals: stop. State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Record count: [N]

### RECORD GATE
- NOT: any signal is described without naming its artifact — unnameable signals are unverifiable. Positive condition: every signal is identified by artifact name.
- NOT: evaluation or verdict language appears in this phase — the record precedes judgment. Positive condition: phase contains inventory only.
- NOT: record count is omitted — count is required for confidence calibration. Positive condition: count is stated.

RECORD GATE CLEARED.

---

## DETERMINATION

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record establishes, read as a whole. Reference specific signals. A DETERMINATION is a commitment — the register word forecloses hedging after it. DETERMINATION: MAYBE requires naming the specific uncertainty; MAYBE is not used when evidence leans YES or NO.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove the confidence level? What capped it? High confidence (>= 75): name converging signals and explain why convergence matters. Low confidence (<= 40): name the specific gap or conflict. CONFIDENCE notation without a rationale paragraph fails.]

### DETERMINATION SEAL
- NOT: the judgment paragraph fails to open with DETERMINATION: [YES/NO/MAYBE] — the register word must commit before reasoning follows. Positive condition: DETERMINATION: opens the judgment paragraph.
- NOT: judgment paragraph is a list of record findings with a conclusion appended — list + conclusion is a summary, not a determination. Positive condition: paragraph issues a position on what the whole record establishes.
- NOT: CONFIDENCE notation lacks a rationale paragraph — a score without reasoning cannot be interrogated. Positive condition: rationale paragraph follows the score and explains what drove it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty — MAYBE as a hedge fails this seal. Positive condition: MAYBE names the uncertainty; YES and NO do not hedge after the register word.

DETERMINATION SEALED.

---

## EVIDENCE BASIS

Name up to 3 signals as primary evidence. This is a ranked argument, not an annotated list. For each, issue a prose paragraph arguing why this signal was more determinative than signals ranked below it.

**PRIMARY EVIDENCE — [Signal name]**
[Paragraph. Why most determinative? Why primary over secondary?]

**SECONDARY EVIDENCE — [Signal name]**
[Paragraph. What does it add that primary evidence did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE — [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE BASIS SEAL
- NOT: evidence entries are table rows or bullets — a table is an annotated list, not an argument; cells can be filled without constructing a comparison. Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2 — presence of support is not relative weight. Positive condition: each entry argues relative determinative weight by answering the comparative question.
- NOT: any named signal is absent from PRELIMINARY RECORD — signals outside the record cannot be traced to investigation artifacts. Positive condition: all named signals exist in the record.
- NOT: paragraphs describe what signals found rather than arguing why they outweigh others — description is not argument. Positive condition: each paragraph argues relative weight.

EVIDENCE BASIS SEALED.

---

## DISSENT

[Paragraph. What is the strongest argument against the DETERMINATION? Source it: a signal in the record, a logical gap, or an unconsidered scenario. Issue a rebuttal, or state: "DISSENT UNRESOLVED — limits confidence ceiling." This section cannot be replaced with "no opposition identified."]

[If genuinely no counter-evidence found: explain why the record is one-sided and note that absence of dissent may indicate incomplete investigation coverage, not evidentiary strength.]

### DISSENT SEAL
- NOT: dissent section is skipped or reduced to "no opposition identified" — absence of named opposition is not the same as absence of opposition. Positive condition: at least one prose paragraph is present.
- NOT: source of opposition is omitted — unsourced opposition is an assertion. Positive condition: opposition is sourced to a record signal, a gap, or an unconsidered scenario.
- NOT: rebuttal states "this evidence is weak" without explaining why the DETERMINATION holds despite it. Positive condition: rebuttal explains how DETERMINATION holds, or "DISSENT UNRESOLVED" is stated with confidence impact noted.

DISSENT SEALED.

---

## HOLDINGS AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Holdings that merely restate the DETERMINATION are not Holdings.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined. State the next investigative action.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, determination_sealed (true/false), evidence_basis_sealed (true/false), dissent_sealed (true/false), signal_count.
```

---

## V-05: Role Sequence + NOT:-first Gates + Pre-Committed Counter-Evidence (Full Combo)

**Axes**: Role sequence (ADVERSARY before JUDGE) + NOT:-first gate ordering + formal verdict register
**Hypothesis**: Maximum C-13+C-14+C-15 coverage. The ADVERSARY role structurally enforces pre-commitment of counter-evidence (C-15) — the adversary is a required role output, not an optional section the writer can fill in post-verdict. NOT:-first gates foreclose failure modes before pass conditions (C-13). DETERMINATION: register commits at the lexical level before hedging is possible (C-14). Each mechanism closes a path that the others leave open.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document stands alone: a reader with no access to the investigation signals must understand the determination, the evidence basis, the pre-determination challenge, and what to do next from this document alone. State this mandate in your opening paragraph.

The determination is issued against the adversary's best case, not before it. The adversary declares before the judge rules. Write argumentative sections in prose paragraphs, not tables or bullet lists.

---

## SURVEYOR: RECORD INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: name the artifact, state what it investigated, state what it found. If no signals: stop. State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Record count: [N]

### RECORD GATE
- NOT: any signal is described without naming its artifact — unnameable signals are unverifiable. Positive condition: every signal is identified by artifact name.
- NOT: evaluation language appears in this phase — the record precedes the judgment. Positive condition: phase contains inventory only.
- NOT: record count is omitted — count is required for confidence calibration. Positive condition: count is stated.

SURVEYOR COMPLETE.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

NOT: this section is placed after the DETERMINATION and filled in post-verdict — counter-evidence selected after the position is formed is not a pre-commitment; it is selection bias. This section runs before the JUDGE issues any determination. A DETERMINATION issued without a prior adversarial challenge is procedurally incomplete.

The ADVERSARY makes the strongest case against the hypothesis. This is required before the DETERMINATION section.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Name the specific gap, thin signal, or missing evidence type. If signals are thin (N < 3), name what is absent and why that absence matters for this hypothesis.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if signals appear to lean YES or NO? State the adversary's best case for uncertainty. What does the adversary argue would prevent a clear YES or NO?]

[Paragraph 3. Anti-pattern declaration: name one failure mode this determination must avoid, given the structure of this particular record. Form: "This DETERMINATION must not [do X], because [what this record's structure makes likely]." Not a generic rule — specific to this investigation's signal set.]

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic ("evidence is limited") — generic uncertainty is not an adversarial challenge. Positive condition: at least two paragraphs name specific record vulnerabilities: named gaps, named thin signals, or named unconsidered scenarios.
- NOT: anti-pattern declaration is generic ("avoid overconfidence") — generic declarations allow any output to pass. Positive condition: anti-pattern is specific to the structure of this record.

ADVERSARY COMPLETE.

---

## JUDGE: DETERMINATION

Having received the ADVERSARY's challenge, the JUDGE now issues a determination against it.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record establishes, read as a whole. Address the ADVERSARY's challenge explicitly: does it reduce confidence, cap it, or fail to move the determination? DETERMINATION: MAYBE requires naming the specific uncertainty — not the adversary's challenge alone, but what evidence gap prevents YES or NO.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it — signal gaps, the ADVERSARY challenge, or unconsidered scenarios?]

### DETERMINATION SEAL
- NOT: DETERMINATION: is absent from the opening sentence of the judgment paragraph — the register word must commit before reasoning follows. Positive condition: DETERMINATION: [YES/NO/MAYBE] opens the judgment.
- NOT: judgment paragraph fails to address the ADVERSARY's pre-determination challenge — the challenge was issued; the judgment must weigh it. Positive condition: ADVERSARY challenge is referenced and weighed in the judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph — a score without reasoning cannot be interrogated. Positive condition: rationale paragraph explains what drove the number and what capped it.
- NOT: DETERMINATION: MAYBE is used without naming the specific uncertainty — MAYBE as a hedge fails this seal. Positive condition: MAYBE names the uncertainty.

DETERMINATION SEALED.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION than signals ranked below it.

**PRIMARY EVIDENCE — [Signal name]**
[Paragraph. Why most determinative? Why primary over secondary?]

**SECONDARY EVIDENCE — [Signal name]**
[Paragraph. What does it add that primary evidence did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE — [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column — a table is an annotated list, not an argument; filling cells requires no argument construction. Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2 — presence of support is not relative weight. Positive condition: each paragraph answers the comparative question: why this tier over the one ranked below it?
- NOT: any named signal is absent from the SURVEYOR record — signals outside the record cannot be traced to investigation artifacts. Positive condition: all named signals exist in the SURVEYOR record.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND NAVIGATOR: OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Holdings that merely restate the DETERMINATION are not Holdings.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined — what evidence was absent or inconclusive. State the next investigative action: which prove sub-skill or concrete step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, adversary_pre_determination (true/false), determination_sealed (true/false), not_first_gates (true/false).
```
