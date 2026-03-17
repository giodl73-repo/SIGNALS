Written to `simulations/quest/variations/prove-synthesize-variations-R1-2026-03-14.md`.

---

## V-01 through V-05 Summary

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Output format (table-dominant) | Tables enforce specificity and prevent narrative drift toward summarization — the C-05 failure mode |
| **V-02** | Role sequence (JUDGE leads) | Commitment before inventory forces a stronger position; provisional answer is harder to walk back once named |
| **V-03** | Phrasing register (conversational/imperative) | Direct questions ("State your answer now") reduce hedging better than fill-in templates because they create commitment pressure instead of format compliance |
| **V-04** | Role sequence + inertia framing | Foregrounding the status-quo anchor before verdict formation produces better-calibrated confidence — evidence must beat "doing nothing" |
| **V-05** | Output format + lifecycle emphasis | Prose + hard phase gates produces the most self-contained artifact (C-10) — prose forces self-explanation, gates enforce per-section completeness |

The single-axis variations isolate: **format** (V-01), **sequence** (V-02), **register** (V-03). The combos test interactions: **sequence × inertia** (V-04) and **format × gates** (V-05).
d -- not undecided.]

Confidence: [N]/100

Confidence rationale:
| Driver | Direction | Effect |
|--------|-----------|--------|
| [What pushed confidence up] | UP | [how much / why] |
| [What held confidence down] | DOWN | [how much / why] |

### COMMIT GATE
- [ ] Answer is YES/NO/MAYBE (no other values)
- [ ] Confidence is 0-100 integer
- [ ] Confidence table has at least one UP and one DOWN driver (or explicit "no downward pressure")
- [ ] Answer is a judgment, not a restatement of the SURVEYOR inventory

COMMITTED. Downstream sections read this verdict. Post-gate revisions require explicit justification in AMENDMENT NOTES.

---

## ADVOCATE: KEY EVIDENCE

[Source: SURVEYOR inventory only. Up to 3 signals. These are the signals that most influenced the JUDGE verdict -- not the most interesting, the most influential.]

| Rank | Signal | Why it influenced the verdict | Weight |
|------|--------|-------------------------------|--------|
| 1 | [artifact name] | [Why this signal moved the needle more than others] | HIGH |
| 2 | [artifact name] | [What it adds that rank 1 did not establish] | MEDIUM/HIGH |
| 3 | [artifact name or "none"] | [Marginal contribution, or absent] | MEDIUM |

[Fewer than 3 is acceptable if inventory is small. Inventing signals not in SURVEYOR inventory is not acceptable.]

---

## SKEPTIC: COUNTER-EVIDENCE

[What argues against the JUDGE verdict? Source: SURVEYOR inventory + logical analysis of gaps.]

| Source | Argument against verdict | Strength | Rebuttal (or "unresolved") |
|--------|--------------------------|----------|---------------------------|
| [artifact or "logical gap"] | [the argument] | STRONG / MEDIUM / WEAK | [how JUDGE addressed it] |

[If no counter-evidence exists: write one row with Source "none found", Argument "all investigated signals support the verdict", Strength "N/A", Rebuttal "Absence of counter-evidence noted -- may indicate incomplete investigation."]

---

## SCHOLAR: PRINCIPLES

[What does this investigation tell us beyond this hypothesis? Generalizable only. Declarative form required.]

| ID | Principle | Scope |
|----|-----------|-------|
| P-01 | [X implies Y. / When Z, expect W.] | [domain or condition where this applies] |

[Minimum 1 principle. Restatements of the verdict are not principles.]

---

## NAVIGATOR: OPEN QUESTIONS

[What did the investigation not resolve? Specific and actionable only.]

| ID | Question | Why unresolved | Next step |
|----|----------|----------------|-----------|
| Q-01 | [Specific question] | [What evidence was missing or inconclusive] | [prove sub-skill or action] |

[Minimum 1 question. "More research needed" is not an open question.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, key_evidence_count, counter_evidence_count, principles_count, open_questions_count.
```

---

## V-02: Role Sequence Axis

**Axis**: Role sequence — JUDGE leads (verdict before inventory) vs SURVEYOR leads (inventory before verdict)
**Hypothesis**: Commitment-first sequencing forces a stronger position by preventing evidence-seeking paralysis; the JUDGE must name what would change the answer before seeing all signals, which is harder to walk back.

```
You are running prove:synthesize. Merge all investigation signals for {topic} into an answer-first synthesis. Commitment comes before inventory -- state your answer before cataloging evidence.

---

## JUDGE: PROVISIONAL VERDICT

[State your answer before reading the signals. This is your prior. You will confirm or revise after SURVEYOR.]

Provisional answer: [ ] YES   [ ] NO   [ ] MAYBE

Provisional confidence: [N]/100

What would revise this: [One sentence. What evidence, if found in SURVEYOR inventory, would flip or significantly move the answer?]

---

## SURVEYOR: INVENTORY

[Now inventory the signals. Glob simulations/prove/investigations/{topic}-*.]

| Signal | File | Key finding | Supports / Refutes / Mixed |
|--------|------|-------------|---------------------------|
| [name] | [path] | [one sentence] | [direction] |

[If no signals found: stop. Cannot synthesize without signals.]

Signal count: [N]

---

## JUDGE: FINAL VERDICT

[Review SURVEYOR inventory. Confirm or revise provisional verdict. If revising: name what changed.]

Answer: [ ] YES   [ ] NO   [ ] MAYBE

Confidence: [N]/100

[If answer changed from provisional: "Revised from [provisional] to [final] because [signal name] showed [finding]."]
[If answer unchanged: "Provisional verdict confirmed. [Signal name] was the strongest convergence signal."]

Confidence rationale: [2-3 sentences. What drove it up? What capped it? If >= 75: evidence strongly converges -- name the signals. If <= 40: evidence is mixed or thin -- name the conflict.]

### SEAL GATE
- [ ] Answer is YES/NO/MAYBE
- [ ] Confidence has explicit rationale (not just score)
- [ ] Provisional vs. final comparison present (confirmed or revised with named reason)
- [ ] This is a judgment, not a signal summary

SEALED. Downstream sections read this verdict only.

---

## ADVOCATE: KEY EVIDENCE

[Up to 3 signals that most influenced the final verdict. Ranked by influence, not by interest. Prose per entry.]

**Rank 1 -- [Signal name]**
Why most influential: [Not what it found -- why it moved the needle more than others.]

**Rank 2 -- [Signal name]**
Why second: [What does it add that rank 1 did not establish?]

**Rank 3 -- [Signal name or "none" if fewer than 3 signals]**
Why third: [Marginal contribution, or state absent.]

---

## SKEPTIC: COUNTER-EVIDENCE

At least one argument against the verdict. If none exists, state that explicitly.

Counter-argument 1: [The strongest case against the answer.]
Source: [artifact name or "logical gap"]
Strength: STRONG / MEDIUM / WEAK
Rebuttal: [How JUDGE addressed it, or "unresolved -- limits confidence ceiling."]

[Add Counter-argument 2+ if present in inventory.]

---

## SCHOLAR: PRINCIPLES

What does this investigation teach us beyond this hypothesis? Declarative generalizations only. Minimum 1.

P-01: [X implies Y. / When Z, expect W.]
[P-02+: add if warranted.]

---

## NAVIGATOR: OPEN QUESTIONS

What did the investigation not resolve? Minimum 1. Specific questions only.

Q-01: [Specific question]
Why unresolved: [What evidence was missing]
Next step: [prove sub-skill or concrete action]

[Q-02+: add if warranted.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, provisional_answer, verdict_revised (true/false), signal_count, key_evidence_count.
```

---

## V-03: Phrasing Register Axis

**Axis**: Phrasing register — conversational/imperative vs formal/template-driven
**Hypothesis**: Direct imperative questions ("State your answer now") reduce hedging more effectively than fill-in templates because they create interpersonal commitment pressure rather than format compliance.

```
You are running prove:synthesize for {topic}.

Read every signal in simulations/prove/investigations/{topic}-*. Then answer six questions. Do not hedge. Do not qualify. If you are uncertain, say so in the confidence score -- not in the answer.

---

**QUESTION 1: What is your answer?**

State it. Pick one: YES, NO, or MAYBE.
- YES = evidence weight supports the hypothesis.
- NO = evidence weight refutes it.
- MAYBE = evidence is genuinely split. Not "I am avoiding commitment."

Your answer: ___

If you wrote anything other than YES, NO, or MAYBE: delete it. Try again.

---

**QUESTION 2: How confident are you? (0-100)**

Pick a number. Then explain it in two sentences:
- Sentence 1: What pushed the number up?
- Sentence 2: What held it down, or what would have pushed it higher if it were not present?

Confidence: ___/100
Because: ___

High confidence (>= 75) requires named convergent signals. Low confidence (<= 40) requires naming the gap or conflict. Mid-range requires both.

---

**QUESTION 3: What are your top 3 pieces of evidence?**

For each: name the signal artifact. Then say WHY it moved the needle more than the others -- not what it found, but why it outweighed the rest.

Evidence 1: [artifact name] -- [why it outweighed the rest, not what it found]
Evidence 2: [artifact name] -- [why second, not first]
Evidence 3: [artifact name or "none"] -- [marginal contribution, or state absent]

Invented artifact names are not acceptable. Check against your inventory.

---

**QUESTION 4: What argues against your answer?**

Name it. You must have an answer. If nothing argues against it: write "No counter-evidence found. This may indicate incomplete investigation coverage." Do not skip this question.

Counter-argument: [The best case against your answer]
Source: [artifact name, or "logical gap"]
Your rebuttal: [How you addressed it, or "unresolved -- caps confidence."]

---

**QUESTION 5: What did you learn that generalizes beyond this hypothesis?**

Write at least one principle. It must be declarative: "X implies Y" or "When Z, expect W." A restatement of your answer ("the hypothesis was true") is not a principle.

P-01: ___
[P-02+: add if warranted]

---

**QUESTION 6: What did the investigation NOT resolve?**

Name at least one specific open question. "More research needed" is not a question. Write the actual question, explain why it is still open, and name the concrete next step.

Q-01: [The actual question]
Why open: [What evidence was missing or inconclusive]
Next step: [prove sub-skill or action]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, questions_answered (must be 6).
```

---

## V-04: Role Sequence + Inertia Framing Combo

**Axes**: Role sequence + inertia framing
**Hypothesis**: Foregrounding the status-quo anchor before answer formation produces better-calibrated confidence scores by setting an explicit comparison baseline -- evidence must beat "doing nothing" to justify high confidence.

```
You are running prove:synthesize for {topic}. Before merging signals, anchor against status quo. The synthesis must answer: does the evidence overcome the inertia of doing nothing?

---

## ANCHOR: STATUS QUO BASELINE

[Run before examining investigation signals. Sets the comparison baseline for the JUDGE verdict.]

What does the team do today without this capability?
Current practice: [One sentence describing actual current behavior.]

Inertia rating: [ ] STRONG -- current practice is adequate for most cases
               [ ] MODERATE -- current practice has known gaps but teams tolerate them
               [ ] WEAK -- current practice clearly fails; cost of nothing is high

Inertia constraint: If STRONG, confidence >= 75 requires named evidence that directly overcomes current practice. If WEAK, inertia does not cap confidence.

---

## SURVEYOR: INVENTORY

[Glob simulations/prove/investigations/{topic}-*.]

| Signal | File | Finding summary | Direction |
|--------|------|-----------------|-----------|
| [name] | [path] | [one sentence] | supports / refutes / mixed |

Signal count: [N]

[If no signals: stop. Cannot synthesize.]

---

## JUDGE: VERDICT

[Does the evidence overcome the inertia baseline set in ANCHOR?]

Answer: [ ] YES   [ ] NO   [ ] MAYBE

Confidence: [N]/100

Inertia adjustment: [Did ANCHOR inertia rating change your confidence from what raw signal weight suggested? If yes: "Inertia (STRONG/MODERATE/WEAK) [raised/lowered] confidence by approximately [N] points because [reason]." If no adjustment: "Inertia did not change confidence -- evidence weight was decisive despite [STRONG/MODERATE/WEAK] inertia."]

Confidence rationale: [2-3 sentences covering signal convergence and inertia interaction. Both required.]

### COMMIT GATE
- [ ] Answer is YES/NO/MAYBE
- [ ] Inertia rating is declared in ANCHOR
- [ ] Inertia adjustment is explicit (even if zero)
- [ ] Confidence rationale addresses both signal evidence and inertia baseline
- [ ] This is a judgment call, not a signal summary

COMMITTED.

---

## ADVOCATE: KEY EVIDENCE

[Up to 3 signals. Rank by influence on the JUDGE verdict. For each: explain WHY it outweighed others. Signals that directly address the inertia weakness are candidates for rank 1.]

**1. [Signal name]**
Why most influential: [What did it show that moved the verdict against inertia? / Why rank 1 over others?]

**2. [Signal name]**
Why second: [What does it add that rank 1 did not?]

**3. [Signal name or "none"]**
Why third: [Marginal contribution, or state absent.]

---

## SKEPTIC: COUNTER-EVIDENCE

Two sources of counter-evidence are always present: (1) the inertia case, and (2) signal artifacts that argue against the verdict.

**Inertia counter-argument**: [Make the best case that current practice is sufficient. This case always exists.]
Inertia rebuttal: [How the ADVOCATE evidence addresses it, or "not fully addressed -- limits confidence ceiling."]

**Signal counter-arguments**:
| Source | Argument | Strength | Rebuttal |
|--------|----------|----------|---------|
| [artifact or gap] | [argument against verdict] | STRONG / MEDIUM / WEAK | [rebuttal or "unresolved"] |

[If no signal counter-evidence: "No signal counter-evidence found. Inertia counter-argument is the primary challenge."]

---

## SCHOLAR: PRINCIPLES

At minimum, one principle about the inertia relationship found in this investigation. Additional principles from signal findings are welcome.

P-01: [Inertia-related principle -- what does this tell us about when evidence is sufficient to overcome doing nothing?]
[P-02+: additional signal-derived principles.]

---

## NAVIGATOR: OPEN QUESTIONS

At minimum, one question about the inertia boundary condition. Additional signal-derived questions welcome.

Q-01: [Inertia boundary question: what would cause the inertia rating to flip, and what would that do to the verdict?]
[Q-02+: signal-derived open questions with next steps.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, inertia_strength, inertia_adjusted (true/false), signal_count, key_evidence_count.
```

---

## V-05: Output Format + Lifecycle Emphasis Combo

**Axes**: Output format (prose-dominant) + lifecycle emphasis (explicit phase gates)
**Hypothesis**: Prose synthesis with hard phase gates produces the most self-contained artifact (C-10) because gates enforce completeness checks per section, while prose forces each section to explain itself rather than rely on table column headers to carry meaning.

```
You are running prove:synthesize for {topic}. Produce a synthesis that stands alone. A reader with no access to the underlying signals must understand the answer, reasoning, and next steps from this document alone.

Write in prose. No tables. Each phase is gated.

---

## PHASE 1: SIGNAL INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence: what the signal investigated and what it found. Name each signal explicitly.

[One sentence per signal. Example: "The websearch signal found three independent industry sources confirming X." If no signals: stop. "No signals found for {topic}. Cannot synthesize."]

Phase 1 complete. Signal count: [N].

### GATE 1
- [ ] Every found signal has exactly one summary sentence
- [ ] Each sentence names the signal artifact by name
- [ ] No evaluation or verdict present in Phase 1 (inventory only)
- [ ] Signal count recorded

GATE 1 CLEARED. Proceed to Phase 2.

---

## PHASE 2: VERDICT

State your answer. This is a judgment based on Phase 1 inventory. It is not a summary.

**Answer: [YES / NO / MAYBE]**

[One paragraph. Open with the answer word. Explain what the Phase 1 signals, read as a whole, tell you. Reference specific signals by name. Do not restate each signal -- synthesize what they say together. The answer must be visible in the opening sentence.]

**Confidence: [N]/100**

[One paragraph. What drove this number? What capped it? If >= 75: state which signals converge and why their convergence is meaningful. If <= 40: name the gap or conflict that prevents higher confidence. A confidence score without a rationale paragraph is a fail.]

### GATE 2
- [ ] Answer is YES/NO/MAYBE (stated in opening sentence of verdict paragraph)
- [ ] Confidence is an integer 0-100
- [ ] Verdict paragraph is a synthesis judgment (not a list of signal findings)
- [ ] Confidence paragraph has explicit rationale explaining the number

GATE 2 CLEARED. Proceed to Phase 3.

---

## PHASE 3: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. For each: argue why it outweighed the others. This is a ranked argument, not a ranked list.

[One paragraph per signal. Opening sentence names the signal. Remaining sentences argue why it influenced the Phase 2 verdict more than others -- what did it show that other signals did not? Why did it carry more weight? "It supported the hypothesis" is not an argument for rank.]

### GATE 3
- [ ] Up to 3 signals named (fewer is acceptable if inventory is small)
- [ ] Each paragraph argues the signal's rank (not just restates its finding)
- [ ] All named signals exist in Phase 1 inventory (no invented signals)

GATE 3 CLEARED. Proceed to Phase 4.

---

## PHASE 4: COUNTER-EVIDENCE

[One paragraph minimum. Name the strongest argument against the Phase 2 verdict. Where did it come from: a signal, a logical gap, or an unconsidered scenario? How did the verdict account for it? If it was not fully addressed, say so explicitly. "Unresolved counter-evidence limits the confidence ceiling" is an acceptable conclusion.]

[If no counter-evidence found: write one paragraph explaining the absence and noting that absence of counter-evidence may indicate incomplete investigation coverage -- it is not necessarily a sign of strong evidence.]

### GATE 4
- [ ] Counter-evidence section present (not skipped)
- [ ] Source of counter-argument identified
- [ ] Rebuttal stated, or "unresolved" stated explicitly with confidence impact noted

GATE 4 CLEARED. Proceed to Phase 5.

---

## PHASE 5: PRINCIPLES AND OPEN QUESTIONS

**What this investigation teaches us beyond this hypothesis:**

[At least one declarative principle. "X implies Y." "When Z, teams should expect W." Not a restatement of the verdict. The principle must generalize beyond the specific topic.]

**What the investigation did not resolve:**

[At least one specific open question. Name the actual question. Explain why it remains open -- what evidence was missing or inconclusive? State the concrete next step: which prove sub-skill would address it, or what external action is needed.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count, gate_1_cleared (true/false), gate_2_cleared (true/false), gate_3_cleared (true/false), gate_4_cleared (true/false).
```
