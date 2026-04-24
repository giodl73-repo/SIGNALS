Written to `simulations/quest/variations/prove-synthesize-variations-R4-2026-03-14.md`.

---

## Round 4 — V-01 through V-05

| # | Axis | R4 Target |
|---|------|-----------|
| **V-01** | Role sequence — explicit role prohibition statements | C-16 only |
| **V-02** | Lifecycle emphasis — record-specific anti-pattern diagnosis with structural template | C-17 only |
| **V-03** | Output format — frontmatter commitment declarations open before first prose | C-19 only |
| **V-04** | Role prohibition + record-specific diagnosis + register-word-first NOT: (combo) | C-16 + C-17 + C-18 |
| **V-05** | Full combo — all four new criteria + complete R3 inheritance | C-16 + C-17 + C-18 + C-19 |

---

**Key design decisions:**

**Why three single-axis, not four:** C-18 (register-word-first) fires in all five variations at the output level — `DETERMINATION: [YES/NO/MAYBE]` already puts DETERMINATION first, inherited from R3. C-18 becomes a gate-enforcement question: V-04 and V-05 add the explicit NOT: clause ("NOT: register word appears after introductory language..."); V-01/V-02/V-03 rely on output format alone. The discriminating question is whether the explicit gate instruction is required or whether the format is sufficient.

**Why V-02 uses PHASE 1/2/3/4/5 titles:** To isolate C-17 cleanly, V-02 must not fire C-16. Role-identity labels (SURVEYOR/ADVERSARY/JUDGE) foreclose output type; descriptive phase titles (SIGNAL INVENTORY, ADVERSARIAL CHALLENGE, DETERMINATION) do not. V-02 is the only variation without role labels.

**Two R4 calibration questions:**
1. Does C-16 require explicit prohibition language ("A JUDGE cannot hedge. Violation is a procedural breach."), or do role labels alone suffice? V-01 (explicit prohibitions) vs V-03 (role labels, no explicit prohibitions) will distinguish this.
2. Does C-18 fire from the DETERMINATION: format alone, or does it require the explicit NOT:-first gate? V-01/V-02/V-03 (format only) vs V-04/V-05 (format + explicit gate) will distinguish this.

**The RECORD DIAGNOSIS template** (C-17, V-02/V-04/V-05) is the most mechanically novel addition. It forces naming `Given this record's [structural property — N=[count], method diversity, signal concentration], the most likely failure mode is [X]. Rationale: [causal link].` The structural property must be derivable from the SURVEYOR inventory — a reader can falsify the diagnosis by checking the inventory. R3 V-05 had "specific to this investigation's signal set" without this verifiability requirement; C-17 closes the gap.

**The frontmatter DECLARATIONS block** (C-19, V-03/V-05) opens the artifact before first prose. Each boolean is filled at the structural point it becomes determinable, not retroactively. The explicit NOT: ("frontmatter completed after the artifact is finished defeats the mechanism") is the core enforcement: a post-hoc label cannot be a pre-commitment.
 final DETERMINATION is:', 'Based on the foregoing, DETERMINATION:') — a register word that does not open the sentence allows hedging to precede it. Positive condition: DETERMINATION: is the first word of the commitment sentence." All five variations produce DETERMINATION: [YES/NO/MAYBE] with DETERMINATION first (inherited from R3 DETERMINATION: format), so C-18 fires at the output level in all; V-04 and V-05 add the explicit NOT: instruction that forecloses the failure mode before the writer reaches the pass condition.

**C-19 mechanism (V-03, V-05):** The artifact opens with a FRONTMATTER DECLARATIONS block — machine-readable boolean fields — before the first prose sentence. Writer is instructed to complete each field at the structural point it becomes determinable, not after finishing the full artifact. Explicit NOT: "NOT: frontmatter fields are left blank during writing and filled retroactively — retroactive completion defeats the function of a pre-commitment declaration." V-01, V-02, V-04 retain standard bottom-of-artifact frontmatter (R3 format); only V-03 and V-05 require the block at document open.

**Why V-02 uses descriptive section titles:** To cleanly isolate C-17, V-02 must not fire C-16. Since C-16's mechanism rests on role-identity labels (SURVEYOR/ADVERSARY/JUDGE) foreclosing output type, V-02 uses PHASE 1/2/3/4/5 titles with descriptive names (SIGNAL INVENTORY, ADVERSARIAL CHALLENGE, DETERMINATION, EVIDENCE HIERARCHY, PRINCIPLES). The adversarial challenge still structurally precedes the determination (C-15 fires); all R3 gate mechanisms are present (C-13, C-14 fire) — but no role-identity labels appear.

**Predicted R4 discrimination:**
- V-01 earns C-16 explicit; fails C-17 template, C-18 explicit, C-19
- V-02 earns C-17; fails C-16 (no role labels), C-18 explicit, C-19
- V-03 earns C-19; may fire C-16 at label level (role labels present, no explicit prohibition — the calibration question); fails C-17 template, C-18 explicit
- V-04 earns C-16 + C-17 + C-18 explicit; fails C-19
- V-05 earns C-16 + C-17 + C-18 + C-19 — maximum score

**The R4 calibration questions:**
1. Does C-16 require an explicit prohibition statement, or do role labels alone (as in R3 V-05) suffice? V-01 vs V-03 will distinguish this: V-03 uses role labels without explicit prohibition; V-01 adds the prohibition statement. If they score identically on C-16, labels alone suffice and C-16 was already inherited.
2. Does C-18 require the explicit NOT: gate instruction, or does producing DETERMINATION: as the first word (via the R3 format) already satisfy it? V-01/V-02/V-03 produce DETERMINATION: first without the explicit NOT: clause; V-04/V-05 add it. If they score the same on C-18, the output format alone is sufficient.

---

## V-01: Role Sequence — Explicit Role Prohibition

**Axis**: Role sequence — explicit prohibition statements appended to each role section opener
**Hypothesis**: C-16 fires at the explicit prohibition level, not the label level. "A JUDGE cannot hedge. Violation is a procedural breach." adds the foreclusion mechanism that role labels alone do not supply. R3 V-05 used SURVEYOR/ADVERSARY/JUDGE but was silent about what each role cannot produce — the prohibition language is the missing mechanism. Single-axis implementation of C-16.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

Role assignments govern output type in this synthesis. Each phase is assigned a procedural
identity that forecloses what that phase may produce. Violating a role assignment is a
procedural breach, not a style deviation. Write argumentative sections in prose paragraphs,
not tables or bullet lists.

---

## SURVEYOR: RECORD INVENTORY

A SURVEYOR inventories. A SURVEYOR does not evaluate, compare, or reach conclusions about
signal quality, significance, or convergence. Any evaluative language in the SURVEYOR phase
is a procedural breach regardless of its accuracy.

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Record count: [N]

### SURVEYOR GATE
- NOT: any signal described without naming its artifact — unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluative language appears in this phase — the SURVEYOR cannot reach conclusions;
  inventory only. Positive condition: phase contains factual description, no comparative or
  evaluative language.
- NOT: record count omitted — count is required for confidence calibration. Positive
  condition: count stated as "Record count: [N]".

SURVEYOR COMPLETE.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, surface
supporting evidence, or assist the JUDGE's determination. Advocacy in the ADVERSARY phase
is a procedural breach. The ADVERSARY's sole function is to assemble the strongest case
against the hypothesis before the JUDGE issues any ruling.

NOT: this section is placed after the DETERMINATION and filled post-verdict — counter-
evidence selected after the position is formed is selection bias, not pre-commitment. This
section runs before the JUDGE phase. A DETERMINATION issued without a prior ADVERSARY
challenge is procedurally incomplete.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Name the specific gap,
thin signal, or missing evidence type. If signals are thin (N < 3), name what is absent
and why that absence matters for this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals appear to lean YES or NO? State the adversary's best case for uncertainty. What
would prevent a clear YES or NO from being defensible?]

[Paragraph 3. What is the best argument for the opposite of what the signals suggest?
If signals lean YES, name the strongest argument for NO. State it as a genuine case,
not a token counterpoint. Name one failure mode this synthesis must avoid — not a generic
warning, but one that fits this investigation's signal set.]

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic ("evidence is limited", "more research
  needed") — generic uncertainty is not an adversarial challenge; it is a declaration
  that the ADVERSARY did not run. Positive condition: at least two paragraphs name
  specific record vulnerabilities — named gaps, named thin signals, named unconsidered
  scenarios.
- NOT: the ADVERSARY phase contains language supporting or advocating for the hypothesis
  — advocacy in the ADVERSARY phase is a procedural breach. Positive condition: all
  paragraphs challenge the hypothesis or the record's adequacy.
- NOT: the source of the adversarial argument is omitted — unsourced opposition cannot
  be evaluated. Positive condition: each challenge paragraph is sourced to a specific
  signal gap, logical gap, or unconsidered scenario.

ADVERSARY COMPLETE.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, defer to signal ambiguity, or issue
qualified determinations without named conditions. Hedging language ("it depends",
"likely but not certain", "more investigation needed") in the JUDGE phase is a
procedural breach. The JUDGE issues a determination against the ADVERSARY's pre-recorded
challenge — the challenge is already on the table; the JUDGE weighs it and rules.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record
establishes, read as a whole. Address the ADVERSARY's challenge: does it reduce
confidence, cap it, or fail to move the answer? Reference specific signals. DETERMINATION:
MAYBE requires naming the specific uncertainty — not the adversary's challenge alone, but
what evidence gap prevents YES or NO. MAYBE is not a hedge; it is a committed uncertainty
with a named resolution condition. A JUDGE that issues MAYBE without naming what would
resolve it has hedged.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it — signal gaps, the ADVERSARY
challenge, or unconsidered scenarios? High confidence (>= 75): name converging signals and
explain why their convergence matters beyond mere agreement. Low confidence (<= 40): name
the specific gap or conflict. A CONFIDENCE notation without this paragraph is a procedural
breach in the JUDGE phase.]

### DETERMINATION SEAL
- NOT: DETERMINATION: is absent from the opening sentence — the register word must commit
  before reasoning follows. Positive condition: DETERMINATION: [YES/NO/MAYBE] opens the
  judgment paragraph.
- NOT: judgment paragraph fails to address the ADVERSARY's challenge — the JUDGE received
  the challenge; the ruling must weigh it. Positive condition: ADVERSARY challenge is
  referenced and weighed in the judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph — a score without reasoning cannot
  be interrogated. Positive condition: rationale paragraph follows the score and explains
  what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty — MAYBE without
  a named resolution condition is a judicial breach. Positive condition: MAYBE names the
  uncertainty; YES and NO do not equivocate after the register word.

DETERMINATION SEALED.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE — [Signal name]**
[Paragraph. Why most determinative? What does this signal establish that secondary does
not, and why does that carry greater weight? Answer the comparative question: why primary
over secondary specifically?]

**SECONDARY EVIDENCE — [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE — [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column — a table is an annotated list,
  not an argument; filling cells requires no argument construction. Positive condition:
  each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2 — presence
  of support is not relative weight. Positive condition: each paragraph answers the
  comparative question: why this tier over the one ranked below it?
- NOT: any named signal absent from SURVEYOR record — signals outside the record cannot
  be traced to investigation artifacts. Positive condition: all named signals exist in
  the SURVEYOR record.
- NOT: paragraphs describe signal findings rather than arguing relative weight —
  description is not argument. Positive condition: each paragraph argues why this signal
  outweighs the one ranked below it.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Holdings that
merely restate the DETERMINATION are not Holdings — they must generalize beyond this
specific hypothesis to apply to future investigations.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined —
what evidence was absent or inconclusive. State the next investigative action: which prove
sub-skill or concrete external step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count,
adversary_pre_determination (true/false), determination_sealed (true/false),
role_foreclusion_explicit (true/false).
```

---

## V-02: Lifecycle Emphasis — Record-Specific Anti-Pattern Diagnosis

**Axis**: Lifecycle emphasis — ADVERSARY phase restructured to require a RECORD DIAGNOSIS block with mandatory structural template
**Hypothesis**: C-17 requires more than "not a generic rule" advisory language. The mechanism is a required template that forces the writer to name the record's specific structural property before naming the failure mode: "Given this record's [N=count, method diversity, convergence pattern], the most likely failure mode is [X]." R3 V-05's instruction said "specific to this investigation's signal set" but did not require the structural property to be named — a writer could produce a plausible-sounding failure mode without referencing the record's actual structure. The template closes this gap. Single-axis implementation of C-17.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

The determination is issued against the adversarial challenge, not before it. The
adversarial challenge section runs before the determination section. Write argumentative
sections in prose paragraphs, not tables or bullet lists.

---

## PHASE 1: SIGNAL INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Signal count: [N]

### INVENTORY GATE
- NOT: any signal described without naming its artifact — unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluation language appears in this phase — inventory only. Positive condition:
  phase contains factual description, no evaluation.
- NOT: signal count omitted. Positive condition: count stated.

INVENTORY COMPLETE.

---

## PHASE 2: ADVERSARIAL CHALLENGE

NOT: this section is placed after the determination and filled in post-verdict —
counter-evidence selected after the position is formed is selection bias, not
pre-commitment. This phase runs before Phase 3. Issue the challenge before any
determination language appears.

[Paragraph 1. What is the weakest point in the Phase 1 signal inventory? Name the
specific gap, thin signal, or missing evidence type. If signals are thin (N < 3), name
what type of signal is absent and why that absence matters for this hypothesis.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals appear to lean YES or NO? State the best case for uncertainty. What would
prevent a clear YES or NO from being defensible?]

**RECORD DIAGNOSIS**

NOT: the record diagnosis names a generic anti-pattern warning ("avoid overconfidence",
"do not list signals instead of synthesizing", "consider alternative interpretations")
that could appear in any synthesis regardless of signal structure — a generic warning is
not a diagnosis. The diagnosis must be derived from the structure of this record: what
specific structural property makes this particular failure mode most likely here.

State the record diagnosis in this form: "RECORD DIAGNOSIS: Given this record's
[structural property — e.g., N=2 signals from a single investigation method; N=4
converging signals but all from one source; N=5 conflicting signals with no resolution
artifact; thin coverage of one hypothesis dimension], the most likely failure mode for
this synthesis is [specific failure mode]. Rationale: [why this structural property
produces this failure mode for this hypothesis rather than a different one]."

Positive condition: the structural property named is visibly derivable from the Phase 1
inventory — a reader who sees only the Phase 1 inventory can verify the diagnosis.

### ADVERSARIAL CHALLENGE GATE
- NOT: adversarial challenge is absent or generic — named record vulnerabilities required.
  Positive condition: at least two paragraphs name specific signal gaps, thin signals,
  or unconsidered scenarios from this record.
- NOT: RECORD DIAGNOSIS fails to name a structural property from the Phase 1 inventory
  — a diagnosis that cannot be verified against the inventory is a generic warning
  restated in specific-sounding language. Positive condition: structural property is
  explicitly named and derivable from Phase 1.
- NOT: RECORD DIAGNOSIS names the failure mode without explaining why this record's
  structure produces it rather than alternatives. Positive condition: rationale explains
  the record-structure-to-failure-mode causal link.
- NOT: no counter-argument is present — "no counter-evidence found" without a paragraph
  is not a finding; it is an omission. Positive condition: at least one substantive
  challenge paragraph.

ADVERSARIAL CHALLENGE COMPLETE.

---

## PHASE 3: DETERMINATION

Having issued the adversarial challenge and recorded the RECORD DIAGNOSIS, issue the
determination against them.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the Phase 1
signals establish, read as a whole. Address the Phase 2 challenge: does it reduce
confidence, cap it, or fail to move the determination? Address the RECORD DIAGNOSIS
explicitly — does the diagnosed failure mode apply here, or does the determination avoid
it? DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is not a hedge.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it? The RECORD DIAGNOSIS
should inform the confidence ceiling — if the diagnosed failure mode is a live risk, note
its effect on confidence.]

### DETERMINATION GATE
- NOT: DETERMINATION: is absent from the opening sentence — the register word must commit
  before reasoning follows. Positive condition: DETERMINATION: [YES/NO/MAYBE] opens the
  judgment paragraph.
- NOT: judgment paragraph ignores the Phase 2 RECORD DIAGNOSIS — the diagnosis was
  issued; the judgment must address whether it applies to this output. Positive condition:
  RECORD DIAGNOSIS is referenced in the judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph — a score without reasoning cannot
  be interrogated. Positive condition: rationale paragraph follows the score and explains
  what drove it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty. Positive
  condition: MAYBE names the uncertainty with a stated resolution condition.

DETERMINATION SEALED.

---

## PHASE 4: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

[Rank 1 paragraph: why most influential? Why this signal over rank 2 specifically? What
does it establish that rank 2 cannot, and why does that carry greater weight toward the
determination?]

[Rank 2 paragraph: what does it add that rank 1 did not establish? Why second and not
first?]

[Rank 3 paragraph, or state absent if fewer than 3 signals.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column — cells can be filled without
  constructing a comparison; filling cells is not argument construction. Positive
  condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2 — presence
  of support is not relative weight. Positive condition: each paragraph answers the
  comparative question: why this signal over the one ranked below it?
- NOT: any named signal absent from Phase 1 inventory — signals outside the inventory
  cannot be traced to investigation artifacts. Positive condition: all named signals exist
  in Phase 1.
- NOT: paragraphs describe what signals found rather than arguing why they outweigh others
  — description is not argument. Positive condition: each paragraph argues relative weight.

EVIDENCE GATE CLEARED.

---

## PHASE 5: PRINCIPLES AND OPEN QUESTIONS

**Principles** (what this investigation teaches beyond this hypothesis):

[At least one declarative principle. "X implies Y." "When Z, expect W." Not a restatement
of the verdict. Must generalize beyond this specific topic.]

**Open Questions** (what the investigation did not resolve):

[At least one specific question still open. Name it. State why it remains undetermined —
what evidence was absent or inconclusive. State the concrete next step: which prove
sub-skill, or what external action.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count,
adversary_pre_determination (true/false), determination_sealed (true/false),
record_specific_antipattern (true/false).
```

---

## V-03: Output Format — Frontmatter Commitment Declarations

**Axis**: Output format — machine-readable boolean declarations open the artifact before the first prose section
**Hypothesis**: C-19 requires the commitment declarations to appear BEFORE prose begins — at artifact open, not at artifact close. R3 V-05 placed boolean fields in the bottom frontmatter instruction ("Frontmatter: ... adversary_pre_determination (true/false)"). That is metadata about what to write, not a declaration that opens the artifact. C-19 fires when the writer fills boolean fields BEFORE writing prose, forcing compliance declarations to function as pre-commitments rather than post-hoc labels. Single-axis implementation of C-19.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

The determination is issued against the adversary's pre-recorded best case. The adversary
declares before the judge rules. Write argumentative sections in prose paragraphs, not
tables or bullet lists.

Open the artifact with the following FRONTMATTER DECLARATIONS block. Fill each field at
the structural point indicated, not after writing the full artifact. These are commitment
declarations — they cannot be retroactively satisfied by reading the finished prose.

NOT: frontmatter fields are left blank during writing and filled in after the artifact is
complete — retroactive completion converts commitment declarations into post-hoc labels
and defeats the mechanism. Each field must be set at the point it becomes determinable:
signal_count after SURVEYOR, adversary_pre_determination after ADVERSARY confirms it ran
before JUDGE, register_word_used after DETERMINATION is issued, record_specific_antipattern
after ADVERSARY phase is complete.

---

FRONTMATTER DECLARATIONS (open the artifact with this block):

  skill: prove-synthesize
  topic: {topic}
  date: {date}
  signal_count: [fill after SURVEYOR]
  answer: [fill after DETERMINATION]
  confidence: [fill after DETERMINATION]
  adversary_pre_determination: [true if ADVERSARY ran before JUDGE; false if not]
  register_word_used: [true if DETERMINATION: opened the commitment sentence; false if not]
  not_first_gates: [true if all gate items open with NOT:; false if any do not]
  record_specific_antipattern: [true if ADVERSARY named a record-derived failure mode; false if only generic]

---

## SURVEYOR: RECORD INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Record count: [N] — set signal_count in frontmatter now.

### SURVEYOR GATE
- NOT: any signal described without naming its artifact — unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluation language appears in this phase — inventory only. Positive condition:
  phase contains description, no evaluation.
- NOT: record count omitted. Positive condition: count stated; signal_count in frontmatter
  updated.

SURVEYOR COMPLETE.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

NOT: this section is placed after the DETERMINATION — counter-evidence selected post-
verdict is selection bias. Set adversary_pre_determination: true in frontmatter now if this
section runs before the JUDGE. This section is structurally required before the JUDGE phase.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Name the specific gap,
thin signal, or missing evidence type. If signals are thin (N < 3), name what is absent
and why that absence matters for this hypothesis.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? What would prevent a clear YES or NO?]

[Paragraph 3. What is the best argument for the opposite of what signals suggest? State
it as a genuine case. Name one failure mode this synthesis must avoid given the structure
of this record — not a generic warning, but derived from what the SURVEYOR found. Set
record_specific_antipattern: true in frontmatter if this failure mode references the
record's actual structural properties; false if it is a generic warning.]

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic — specific record vulnerabilities
  required. Positive condition: at least two paragraphs name specific gaps, thin signals,
  or unconsidered scenarios.
- NOT: source of opposition is omitted — unsourced opposition cannot be evaluated.
  Positive condition: each challenge paragraph sourced to a signal, gap, or scenario.
- NOT: no challenge present at all — "no counter-evidence found" without a paragraph is
  an omission. Positive condition: at least one substantive adversarial paragraph.

ADVERSARY COMPLETE.

---

## JUDGE: DETERMINATION

Having received the ADVERSARY's challenge, the JUDGE now issues a determination against it.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Set register_word_used: true in frontmatter
now. Issue a determination of what the record establishes as a whole. Address the
ADVERSARY's challenge explicitly: does it reduce confidence, cap it, or fail to move the
determination? DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is not
a hedge.]

**CONFIDENCE: [N]/100** — set confidence and answer in frontmatter now.

[Confidence paragraph. What drove this number? What capped it — signal gaps, the ADVERSARY
challenge, or unconsidered scenarios?]

### DETERMINATION SEAL
- NOT: DETERMINATION: is absent from the opening sentence — the register word must commit
  before reasoning follows. Positive condition: DETERMINATION: [YES/NO/MAYBE] opens the
  judgment paragraph. Set register_word_used: false if this condition is not met.
- NOT: judgment paragraph fails to address the ADVERSARY's challenge — the challenge was
  issued; the judgment must weigh it. Positive condition: ADVERSARY challenge referenced
  and weighed.
- NOT: CONFIDENCE notation lacks a rationale paragraph — a score without reasoning cannot
  be interrogated. Positive condition: rationale paragraph follows the score.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty. Positive
  condition: MAYBE names the uncertainty.

DETERMINATION SEALED.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE — [Signal name]**
[Paragraph. Why most determinative? Why primary over secondary?]

**SECONDARY EVIDENCE — [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE — [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table — filling cells requires no argument construction.
  Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2. Positive
  condition: each paragraph answers the comparative question.
- NOT: any named signal absent from SURVEYOR record. Positive condition: all signals
  traceable to inventory.
- NOT: paragraphs describe findings rather than arguing relative weight. Positive
  condition: each paragraph argues why this signal outweighs the next.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Not a restatement
of the verdict. Must generalize beyond this hypothesis.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined.
State the next investigative action: which prove sub-skill or concrete external step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
The FRONTMATTER DECLARATIONS block declared at document open is part of the artifact.
Verify all boolean fields are set before finalizing.
```

---

## V-04: Role Prohibition + Record-Specific Diagnosis + Register-Word-First NOT: (Combo)

**Axes**: Role prohibition (C-16) + record-specific anti-pattern diagnosis (C-17) + explicit register-word-first NOT: gate item (C-18). Leaves frontmatter at bottom (C-19 unfired) as the live R4 discriminator.
**Hypothesis**: Three of the four R4 mechanisms can be combined without requiring C-19. Explicit role prohibition language (C-16) forecloses output type at the identity level. Record-specific RECORD DIAGNOSIS (C-17) turns the adversarial challenge into a diagnostic instrument rather than a template exercise. Register-word-first NOT: clause (C-18) adds the lexical-position gate that R3 V-05 satisfied at the output level without explicit instruction. Leaving C-19 off creates a clean gap that V-05 closes.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

Role assignments govern output type. Each phase is assigned a procedural identity that
forecloses what that phase may produce. Violating a role assignment is a procedural breach,
not a style choice. Write argumentative sections in prose paragraphs, not tables or bullet
lists.

---

## SURVEYOR: RECORD INVENTORY

A SURVEYOR inventories. A SURVEYOR does not evaluate signal quality, compare signal
strength, or reach any conclusions. Evaluation by a SURVEYOR is a procedural breach
regardless of its accuracy.

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Record count: [N]

### SURVEYOR GATE
- NOT: any signal described without naming its artifact — unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluative language appears in this phase — the SURVEYOR role precludes evaluation;
  inventory only. Positive condition: phase contains factual description with no
  comparative or evaluative language.
- NOT: record count omitted — count is required for confidence calibration. Positive
  condition: count stated.

SURVEYOR COMPLETE.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, identify
supporting evidence, or assist the JUDGE. Advocacy in the ADVERSARY phase is a procedural
breach. The ADVERSARY's sole function is to assemble the strongest case against the
hypothesis before the JUDGE rules.

NOT: this section is placed after the DETERMINATION — counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Name the specific gap,
thin signal, or missing evidence type. If signals are thin (N < 3), name what is absent
and why that absence matters for this hypothesis.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty.]

**RECORD DIAGNOSIS**

NOT: the record diagnosis names a generic anti-pattern ("avoid overconfidence", "do not
list signals instead of synthesizing", "ensure counter-evidence is present") that could
apply to any synthesis regardless of this record's structure — a generic warning is a
template exercise, not a diagnosis. Diagnosis must be derived from this record's
observable structural properties.

State: "RECORD DIAGNOSIS: Given this record's [structural property — e.g., N=[count]
signals; all signals from a single investigation method; converging signals with thin
coverage of one dimension; conflicting signals without an arbitration artifact; one strong
signal and N-1 weak corroborators], the most likely failure mode for this synthesis is
[specific failure mode]. Rationale: [why this structural property makes this failure mode
more likely here than in a structurally different record]."

Positive condition: a reader who reviews only the SURVEYOR inventory can verify that the
named structural property is present and that the causal link to the failure mode is
plausible.

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic — "evidence is limited" is a declaration
  that the ADVERSARY did not run. Positive condition: at least two paragraphs name
  specific record vulnerabilities by name.
- NOT: RECORD DIAGNOSIS fails to name a structural property visible in the SURVEYOR
  inventory — diagnosis ungrounded in the record is a generic warning reformatted.
  Positive condition: structural property named and derivable from Phase 1.
- NOT: ADVERSARY phase contains advocacy language supporting the hypothesis — advocacy
  is a role breach. Positive condition: all content challenges the hypothesis or the
  record's adequacy.

ADVERSARY COMPLETE.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer. Hedging in the JUDGE phase
is a procedural breach. The JUDGE issues a determination against both the ADVERSARY's
challenge and the RECORD DIAGNOSIS — both are already on the table.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record
establishes as a whole. Address the ADVERSARY's challenge. Address the RECORD DIAGNOSIS:
does the diagnosed failure mode apply to this output, or has it been avoided?
DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is not a hedge.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it? The RECORD DIAGNOSIS
informs the confidence ceiling — if the diagnosed failure mode is live, note its effect.]

### DETERMINATION SEAL
- NOT: the register word appears after introductory language ("Our final DETERMINATION
  is:", "Based on the foregoing evidence, DETERMINATION:") — a register word that does not
  open the sentence allows hedging to precede the commitment point; the anti-hedging
  mechanism fires only when the register word is first. Positive condition: DETERMINATION:
  is the first word of the commitment sentence.
- NOT: judgment paragraph fails to address the ADVERSARY's challenge. Positive condition:
  ADVERSARY challenge referenced and weighed.
- NOT: judgment paragraph fails to address the RECORD DIAGNOSIS — the failure mode was
  named; the judgment must state whether it applies. Positive condition: RECORD DIAGNOSIS
  referenced in the judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph. Positive condition: rationale
  paragraph follows the score and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty. Positive
  condition: MAYBE names the uncertainty with a stated resolution condition.

DETERMINATION SEALED.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE — [Signal name]**
[Paragraph. Why most determinative? Why primary over secondary? What does primary establish
that secondary cannot, and why does that carry greater weight toward the DETERMINATION?]

**SECONDARY EVIDENCE — [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE — [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column — cells can be filled without
  constructing a comparison. Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2. Positive
  condition: each paragraph answers the comparative question: why this tier over the one
  ranked below?
- NOT: any named signal absent from SURVEYOR record. Positive condition: all named signals
  exist in the SURVEYOR record.
- NOT: paragraphs describe signal findings rather than arguing relative weight. Positive
  condition: each paragraph argues why this signal outweighs the next.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Holdings that
merely restate the DETERMINATION are not Holdings — must generalize beyond this hypothesis.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined.
State the next investigative action: which prove sub-skill or concrete external step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count,
adversary_pre_determination (true/false), determination_sealed (true/false),
role_foreclusion_explicit (true/false), record_specific_antipattern (true/false).
```

---

## V-05: Full Combo — All Four New Criteria + Complete R3 Inheritance

**Axes**: Role prohibition (C-16) + record-specific diagnosis (C-17) + register-word-first NOT: (C-18) + frontmatter commitment declarations (C-19). All R3 wins inherited: NOT:-first gates (C-13), DETERMINATION: register (C-14), ADVERSARY before JUDGE (C-15).
**Hypothesis**: The four R4 mechanisms are mutually reinforcing, not redundant. C-16 forecloses output type at the identity level — a JUDGE who hedges has violated a role, not just failed a checklist item. C-17 turns the ADVERSARY challenge from template exercise into record-specific diagnostic — the failure mode named is verifiable against the SURVEYOR inventory. C-18 forecloses hedging at the lexical point of commitment — the register word cannot appear after introductory language. C-19 requires compliance declarations before prose begins — commitments made before writing cannot be rationalized after. Each mechanism closes a path the others leave open; together they achieve maximum structural anti-hedging coverage.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

Role assignments govern output type in this synthesis. Each phase is assigned a procedural
identity that forecloses what that phase may produce. Violating a role assignment is a
procedural breach, not a style deviation. The adversary declares before the judge rules.
Write argumentative sections in prose paragraphs, not tables or bullet lists.

Open the artifact with the following FRONTMATTER DECLARATIONS block. Fill each field at
the structural point indicated. These are pre-commitments — they cannot be retroactively
satisfied by reading the finished artifact.

NOT: frontmatter fields are left blank during writing and completed after the artifact is
finished — retroactive completion converts pre-commitments into post-hoc labels and
defeats the mechanism. Each field is set at the point it becomes determinable.

---

FRONTMATTER DECLARATIONS (open the artifact with this block):

  skill: prove-synthesize
  topic: {topic}
  date: {date}
  signal_count: [fill after SURVEYOR, before ADVERSARY]
  answer: [fill after DETERMINATION is issued]
  confidence: [fill after DETERMINATION is issued]
  adversary_pre_determination: [true if ADVERSARY ran structurally before JUDGE; false if not]
  register_word_used: [true if DETERMINATION: is first word of commitment sentence; false if not]
  not_first_gates: [true if all gate items open with NOT:; false if any gate item does not]
  record_specific_antipattern: [true if ADVERSARY named structural-property-derived failure mode; false if named generic]
  role_foreclusion_explicit: [true if each role section states what the role cannot produce; false if labels only]

---

## SURVEYOR: RECORD INVENTORY

A SURVEYOR inventories. A SURVEYOR does not evaluate, compare, rank, or reach conclusions
about signal quality or significance. Evaluation by a SURVEYOR is a procedural breach
regardless of its accuracy. Set role_foreclusion_explicit: true in frontmatter only if
every role section in this artifact states what the role cannot produce.

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD — no signals found for {topic}. Determination cannot proceed."

Record count: [N] — set signal_count in frontmatter now.

### SURVEYOR GATE
- NOT: any signal described without naming its artifact — unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluative language appears in this phase — the SURVEYOR role precludes evaluation;
  inventory only. Positive condition: phase contains factual description, no comparative or
  evaluative language.
- NOT: record count omitted — count is required for confidence calibration. Positive
  condition: count stated; signal_count in frontmatter updated.

SURVEYOR COMPLETE.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, surface
supporting evidence, or assist the JUDGE's determination. Advocacy in the ADVERSARY phase
is a procedural breach. The ADVERSARY's sole function is to assemble the strongest case
against the hypothesis before the JUDGE rules.

NOT: this section is placed after the DETERMINATION — counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete. Set
adversary_pre_determination: true in frontmatter now.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Name the specific gap,
thin signal, or missing evidence type. If signals are thin (N < 3), name what type is
absent and why that absence matters for this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty. What specific
condition would need to be true for a confident YES or NO to be indefensible?]

**RECORD DIAGNOSIS**

NOT: the record diagnosis names a generic anti-pattern ("avoid overconfidence", "do not
list signals instead of synthesizing", "verify counter-evidence is present") that could
apply to any synthesis regardless of this record's structure — a generic warning is a
template exercise, not a diagnosis. The failure mode must be derived from what the
SURVEYOR found.

State: "RECORD DIAGNOSIS: Given this record's [structural property — e.g., N=[count]
signals; all from a single investigation method; converging signals with thin coverage
of one hypothesis dimension; conflicting signals without an arbitration artifact; one
strong signal and N-1 weak corroborators], the most likely failure mode for this
synthesis is [specific failure mode]. Rationale: [why this structural property produces
this failure mode more than others for this hypothesis]."

Positive condition: a reader who reviews only the SURVEYOR inventory can verify that the
named structural property is present and that the causal link to the failure mode is
plausible. Set record_specific_antipattern: true if this condition is met; false if the
diagnosis is generic.

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic ("evidence is limited") — a declaration
  that the ADVERSARY did not run is not an adversarial challenge. Positive condition: at
  least two paragraphs name specific record vulnerabilities — named gaps, named thin
  signals, named unconsidered scenarios.
- NOT: RECORD DIAGNOSIS fails to name a structural property visible in the SURVEYOR
  inventory — diagnosis ungrounded in the record is a generic warning reformatted.
  Positive condition: structural property named and derivable from the inventory.
- NOT: ADVERSARY phase contains advocacy language supporting the hypothesis — advocacy
  is a role breach in the ADVERSARY phase. Positive condition: all content challenges the
  hypothesis or the record's adequacy.

ADVERSARY COMPLETE.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer to signal ambiguity. Hedging
or equivocation in the JUDGE phase is a procedural breach. The JUDGE issues a determination
against both the ADVERSARY's challenge and the RECORD DIAGNOSIS — both are already on the
table.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Set register_word_used: true in frontmatter
now. Issue a determination of what the record establishes as a whole. Address the
ADVERSARY's challenge: does it reduce confidence, cap it, or fail to move the
determination? Address the RECORD DIAGNOSIS: does the diagnosed failure mode apply to this
output? DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is not a
hedge; it is a committed uncertainty with a named resolution condition.]

**CONFIDENCE: [N]/100** — set confidence and answer in frontmatter now.

[Confidence paragraph. What drove this number? What capped it — signal gaps, the ADVERSARY
challenge, the RECORD DIAGNOSIS risk, or unconsidered scenarios? High confidence (>= 75):
name converging signals and explain why convergence matters beyond mere agreement. Low
confidence (<= 40): name the specific gap or conflict.]

### DETERMINATION SEAL
- NOT: the register word appears after introductory language ("Our final DETERMINATION
  is:", "Based on the foregoing, DETERMINATION:") — a register word not first in its
  sentence allows hedging to precede the commitment point; the mechanism fires only when
  register-word-first. Positive condition: DETERMINATION: is the first word of the
  commitment sentence. Set register_word_used: false if this condition is not met.
- NOT: judgment paragraph fails to address the ADVERSARY's pre-determination challenge —
  the challenge was issued; the JUDGE must weigh it explicitly. Positive condition:
  ADVERSARY challenge referenced and weighed in judgment or confidence paragraph.
- NOT: judgment paragraph fails to address the RECORD DIAGNOSIS — the failure mode was
  named; the JUDGE must state whether it applies to this output. Positive condition: RECORD
  DIAGNOSIS referenced in the judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph — a score without reasoning cannot
  be interrogated or falsified. Positive condition: rationale paragraph follows the score
  and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition — MAYBE used as a hedge is a judicial breach. Positive condition: MAYBE names
  the uncertainty and the condition under which it would resolve to YES or NO.

DETERMINATION SEALED.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE — [Signal name]**
[Paragraph. Why most determinative? What does primary establish that secondary cannot, and
why does that carry greater weight toward the DETERMINATION? Answer the comparative
question: why primary over secondary specifically?]

**SECONDARY EVIDENCE — [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE — [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column — a table is an annotated list,
  not an argument; filling cells requires no argument construction. Positive condition:
  each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2 — presence
  of support is not relative weight. Positive condition: each paragraph answers the
  comparative question: why this tier over the one ranked below?
- NOT: any named signal absent from SURVEYOR record — signals outside the record cannot
  be traced to investigation artifacts. Positive condition: all named signals exist in the
  SURVEYOR record.
- NOT: paragraphs describe signal findings rather than arguing relative weight —
  description is not argument. Positive condition: each paragraph argues why this signal
  outweighs the one ranked below it.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Holdings that
merely restate the DETERMINATION are not Holdings — they must generalize beyond this
specific hypothesis to apply to future investigations with different topics.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined —
what evidence was absent or inconclusive. State the next investigative action: which prove
sub-skill or concrete external step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
The FRONTMATTER DECLARATIONS block declared at document open is part of the artifact.
Verify all boolean fields are set before finalizing. The frontmatter is a compliance
record, not formatting metadata.
```
