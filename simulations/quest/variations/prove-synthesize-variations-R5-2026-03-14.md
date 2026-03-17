Written to `simulations/quest/variations/prove-synthesize-variations-R5-2026-03-14.md`.

---

**Round 5 summary:**

| # | Axis | Base | New mechanism | v6 candidate |
|---|------|------|--------------|--------------|
| V-01 | Per-field phase-gate NOT: | R4 V-03 | NOT: prohibitions on premature + deferred fill at each frontmatter field | C-23 |
| V-02 | SURVEYOR INVENTORY SCHEMA | R4 V-02 | 5-field named schema; RECORD DIAGNOSIS must cite field:value pairs | C-24 |
| V-03 | PRE-JUDGE PRE-FLIGHT block | R4 V-01 | Register-word gate positioned before JUDGE section, not inside DETERMINATION SEAL | C-25 |
| V-04 | Phase gates + schema (combo) | R4 V-04 | V-01 + V-02 mechanisms; C-22 at standard level | C-23 + C-24 |
| V-05 | Full combo | R4 V-05 | All three sharpened + complete R4 V-05 inheritance | C-23 + C-24 + C-25 |

**Three R5 calibration questions:**
1. Does C-20 already fire at max with "fill now" instructions, or do per-field NOT: prohibitions (V-01) add something new?
2. Does C-21 already fire at max with "derivable from inventory," or does schema citation by field:value (V-02) add something new?
3. Does C-22 already fire at max with the gate inside DETERMINATION SEAL, or does a pre-phase pre-flight block (V-03) add something new?
-16/C-17 absent. R4 V-03 provides this: frontmatter at document open, role labels without explicit prohibition statements, adversarial challenge without structured RECORD DIAGNOSIS template. The single new axis: each frontmatter field gains an explicit NOT: prohibition for premature filling (before its phase is written) and deferred filling (after subsequent phases begin). R4 V-05 instructs "fill X now" at each phase boundary but does not prohibit a writer who fills all fields at artifact start -- the per-field NOT: gate closes this gap by making premature filling a named violation.

**V-02 base -- R4 V-02 (structured diagnosis without role labels or frontmatter at open):** C-21 extends C-17 -- isolating the sharpened mechanism requires C-17 present but C-16/C-19 absent. R4 V-02 used a RECORD DIAGNOSIS template requiring a "structural property derivable from the Phase 1 inventory." V-02 sharpens this by requiring SURVEYOR to produce a named INVENTORY SCHEMA with five fields (signal_count, method_set, convergence_pattern, dominant_signal, coverage_gaps), and RECORD DIAGNOSIS to cite schema fields by name with exact values. "Derivable from" requires re-reading the inventory; "cited by name and value" is falsifiable in a single lookup.

**V-03 base -- R4 V-01 (role prohibitions without structured diagnosis or frontmatter at open):** C-22 extends C-18 -- isolating the sharpened mechanism requires C-18 present but C-17/C-19 absent. R4 V-01 had role prohibitions and DETERMINATION: format but no explicit register-word NOT: gate at the instruction level (V-05 R4 added the gate inside DETERMINATION SEAL). V-03's PRE-JUDGE PRE-FLIGHT block positions the register-word gate BEFORE the commitment sentence -- the prohibition is encountered before the failure mode can occur, not after.

**V-04 base -- R4 V-04 (C-16 + C-17 + C-18, no C-19):** Combines V-01's mechanism (inline phase-transition NOT: gates at each boundary) with V-02's mechanism (INVENTORY SCHEMA + schema citation). Without a frontmatter-at-open block, per-field gates appear as transition attestations at phase exits: "NOT: ADVERSARY begins with signal_count unset." C-22 remains at R4 V-05 standard level (NOT: gate inside DETERMINATION SEAL). Calibration question: do C-20 sharpening and C-21 sharpening compose cleanly without C-19?

**V-05 base -- R4 V-05 (all 22 criteria):** Inherits full R4 V-05 structure and sharpens all three new mechanisms: per-field NOT: conditions on each frontmatter field in the opening block (C-20 sharpened), INVENTORY SCHEMA citation in RECORD DIAGNOSIS (C-21 sharpened), PRE-JUDGE PRE-FLIGHT block before JUDGE section (C-22 sharpened). Designed to surface v6 candidates.

**Three R5 calibration questions:**
1. Does C-20 require explicit per-field NOT: prohibitions, or do inline "fill now" instructions (as in R4 V-05) already represent the strongest form? V-01 (per-field NOT: gates) vs R4 V-03 (fill-now without NOT:) will distinguish this.
2. Does C-21 require schema field citation by name-and-value, or does "derivable from the inventory" (as in R4 V-05) already represent the strongest form? V-02 (schema citation) vs R4 V-02 (template without schema) will distinguish this.
3. Does C-22 require the register-word gate to precede the JUDGE phase (pre-flight), or does the gate inside the DETERMINATION SEAL (as in R4 V-05) already represent the strongest form? V-03 (pre-flight) vs R4 V-01 (output format alone) will distinguish this.

**V6 candidates predicted from R5 mechanisms:**
- C-23: Phase-boundary transition gates -- explicit NOT: conditions at each phase exit prevent advancing without frontmatter field confirmation; phase-advance without attestation is a procedural breach (sharpened C-20).
- C-24: Schema-quoted diagnosis -- RECORD DIAGNOSIS cites INVENTORY SCHEMA field names and exact values; paraphrase without citation fails; a reader verifies in one check without re-reading the SURVEYOR section (sharpened C-21).
- C-25: Pre-JUDGE pre-flight block -- register-word gate positioned structurally before the commitment sentence is written; gate-first means the prohibition is encountered before the failure mode can occur, not after (sharpened C-22).

**Predicted R5 discrimination:**
- V-01 fires C-20 sharpened; fails C-21/C-22 sharpened, C-16 explicit, C-17 structured
- V-02 fires C-21 sharpened; fails C-20/C-22 sharpened, C-16 explicit, C-19/C-20
- V-03 fires C-22 sharpened; fails C-20/C-21 sharpened, C-17 structured, C-19/C-20
- V-04 fires C-20 + C-21 sharpened; fails C-22 sharpened, C-19
- V-05 fires all three sharpened; surfaces C-23, C-24, C-25

---

## V-01: Per-Field Phase-Gate NOT: Conditions

**Axis**: Output format -- each frontmatter field carries explicit NOT: prohibitions for premature filling (before phase is written) and deferred filling (after subsequent phase begins)
**Hypothesis**: C-20 fires more reliably with per-field NOT: prohibitions than with "fill now" instructions alone. R4 V-05 uses inline "set signal_count in frontmatter now" at the SURVEYOR boundary but does not prohibit a writer who fills all fields at document open before writing any phase. The per-field NOT: gate closes this gap: "NOT: signal_count filled before SURVEYOR content is written" is enforceable where "fill now" is not. Single-axis: C-20 sharpened. R4 V-03 base: C-19 present, role labels without explicit prohibitions (C-16 not fired), adversarial challenge without INVENTORY SCHEMA (C-21 not fired), no pre-flight block (C-22 not upgraded).

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

The determination is issued against the adversary's pre-recorded best case. The adversary
declares before the judge rules. Write argumentative sections in prose paragraphs, not
tables or bullet lists.

Open the artifact with the following FRONTMATTER DECLARATIONS block. Each field is a
commitment declaration with an explicit phase gate. The gate specifies the structural
moment at which the field becomes truthfully fillable. Each field carries two NOT:
prohibitions: one for premature filling and one for deferred filling. Both violations
produce false declarations.

---

FRONTMATTER DECLARATIONS (open the artifact here):

  skill: prove-synthesize
  topic: {topic}
  date: {date}

  signal_count: [fill after SURVEYOR COMPLETE, before ADVERSARY begins]
  NOT: signal_count filled before any SURVEYOR content is written.
  NOT: signal_count filled after ADVERSARY content begins.

  adversary_pre_determination: [true if ADVERSARY ran before JUDGE; false otherwise]
  NOT: adversary_pre_determination filled before ADVERSARY content is written.
  NOT: adversary_pre_determination filled after JUDGE content begins.

  answer: [fill after DETERMINATION: line is written]
  NOT: answer filled before DETERMINATION: line is written.
  NOT: answer filled after DETERMINATION SEALED appears.

  confidence: [fill after CONFIDENCE: notation is written]
  NOT: confidence filled before CONFIDENCE: notation is written.

  register_word_used: [true if DETERMINATION: is syntactically first in commitment sentence]
  NOT: register_word_used filled before DETERMINATION: line is written.

  not_first_gates: [true if every gate item in this artifact opens with NOT:]
  NOT: not_first_gates filled before all gate sections are written.
  NOT: not_first_gates set true if any gate item in the artifact does not open with NOT:.

---

## SURVEYOR: RECORD INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD -- no signals found for {topic}. Determination cannot proceed."

Record count: [N]

### SURVEYOR GATE
- NOT: any signal described without naming its artifact -- unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluative language appears in this phase -- inventory only. Positive condition:
  factual description, no comparative or evaluative language.
- NOT: record count omitted. Positive condition: count stated.
- NOT: signal_count in frontmatter remains unfilled after this gate clears. Positive
  condition: signal_count set before ADVERSARY begins.

SURVEYOR COMPLETE. Set signal_count: [N] in frontmatter now.
NOT: ADVERSARY begins with signal_count unset in frontmatter.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

NOT: this section is placed after the DETERMINATION -- counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Name the specific gap,
thin signal, or missing evidence type. If signals are thin (N < 3), name what is absent
and why that absence matters for this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals appear to lean YES or NO? State the best case for uncertainty. What specific
condition would prevent a clear YES or NO from being defensible?]

[Paragraph 3. What is the best argument for the opposite of what signals suggest? State
it as a genuine case. Name one failure mode this synthesis must avoid -- not generic, but
derived from what the SURVEYOR found.]

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic ("evidence is limited") -- generic
  uncertainty is not an adversarial challenge. Positive condition: at least two paragraphs
  name specific record vulnerabilities -- named gaps, named thin signals, named scenarios.
- NOT: source of opposition is omitted -- unsourced opposition cannot be evaluated.
  Positive condition: each challenge paragraph sourced to a specific gap or scenario.
- NOT: adversary_pre_determination in frontmatter remains unfilled after this gate clears.
  Positive condition: set adversary_pre_determination: true in frontmatter now.

ADVERSARY COMPLETE. Set adversary_pre_determination: true in frontmatter now.
NOT: JUDGE begins with adversary_pre_determination unset in frontmatter.

---

## JUDGE: DETERMINATION

Having received the ADVERSARY's challenge, issue a determination against it.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Set register_word_used: true in frontmatter
now. Issue a determination of what the record establishes as a whole. Address the
ADVERSARY's challenge: does it reduce confidence, cap it, or fail to move the answer?
DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is not a hedge; it
is a committed uncertainty with a named resolution condition.]

**CONFIDENCE: [N]/100** -- set confidence and answer in frontmatter now.

[Confidence paragraph. What drove this number? What capped it -- signal gaps, the
ADVERSARY challenge, or unconsidered scenarios?]

### DETERMINATION SEAL
- NOT: DETERMINATION: is absent from the opening sentence -- the register word must commit
  before reasoning follows. Positive condition: DETERMINATION: [YES/NO/MAYBE] opens the
  judgment paragraph.
- NOT: judgment paragraph fails to address the ADVERSARY's challenge. Positive condition:
  ADVERSARY challenge referenced and weighed.
- NOT: CONFIDENCE notation lacks a rationale paragraph. Positive condition: rationale
  paragraph follows the score and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition. Positive condition: MAYBE names the uncertainty.
- NOT: answer and confidence in frontmatter remain unfilled after this gate. Positive
  condition: both set now.

DETERMINATION SEALED.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE -- [Signal name]**
[Paragraph. Why most determinative? Why primary over secondary specifically? What does
primary establish that secondary cannot, and why does that carry greater weight?]

**SECONDARY EVIDENCE -- [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE -- [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column -- filling cells requires no
  argument construction. Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2. Positive
  condition: each paragraph answers the comparative question: why this tier over the one
  ranked below?
- NOT: any named signal absent from SURVEYOR record. Positive condition: all named signals
  exist in the SURVEYOR record.
- NOT: paragraphs describe findings rather than arguing relative weight. Positive condition:
  each paragraph argues why this signal outweighs the one ranked below.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Not a restatement
of the verdict. Must generalize beyond this hypothesis to apply to future investigations.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined.
State the next investigative action: which prove sub-skill or concrete external step.]

Set not_first_gates: true in frontmatter now if every gate section opened its items with
NOT:; false if any gate item opened otherwise.
NOT: not_first_gates set before all gate sections are written.

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
The FRONTMATTER DECLARATIONS block at document open is part of the artifact. All boolean
fields carry their NOT: prohibitions and must be set at their declared phase gates.
The frontmatter is a compliance record, not formatting metadata.
```

---

## V-02: SURVEYOR INVENTORY SCHEMA with Schema-Cited RECORD DIAGNOSIS

**Axis**: Lifecycle emphasis -- SURVEYOR phase produces a named INVENTORY SCHEMA block with five structured fields; RECORD DIAGNOSIS must cite schema field names and exact values rather than paraphrase
**Hypothesis**: C-21 requires more than "derivable from the inventory" -- it requires direct citation. R4 V-05's RECORD DIAGNOSIS asks for a structural property "a reader who reviews only the SURVEYOR inventory can verify." A reader who re-reads the inventory can verify a paraphrase; a reader who checks the INVENTORY SCHEMA can verify a citation in a single lookup. V-02 forces the schema to be named (signal_count, method_set, convergence_pattern, dominant_signal, coverage_gaps) and requires RECORD DIAGNOSIS to cite field names and exact values explicitly. A diagnosis is falsified if the cited values do not match the schema. Single-axis: C-21 sharpened. R4 V-02 base: phase titles (no role labels, C-16 not fired), structured diagnosis (C-17), no frontmatter at open (C-19/C-20 not fired), no pre-flight block (C-22 not upgraded).

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

The determination is issued against the adversarial challenge, not before it. The
adversarial challenge runs before the determination section. Write argumentative sections
in prose paragraphs, not tables or bullet lists.

---

## PHASE 1: SIGNAL INVENTORY

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD -- no signals found for {topic}. Determination cannot proceed."

After recording all signals, produce the INVENTORY SCHEMA. All five fields are required.
An incomplete schema cannot support a verifiable RECORD DIAGNOSIS.

INVENTORY SCHEMA:
  signal_count: [N]
  method_set: [list each prove sub-skill represented; or "single method" if all signals
               share one sub-skill]
  convergence_pattern: [converging -- signals align on answer direction; conflicting --
                        signals contradict; thin -- N < 3; mixed -- partially aligned
                        with named divergence point]
  dominant_signal: [name of signal with most specific stated finding; or "none identified"]
  coverage_gaps: [hypothesis dimensions with no signal coverage; or "none identified"]

### INVENTORY GATE
- NOT: any signal described without naming its artifact -- unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluation language appears in this phase -- inventory and schema production only.
  Positive condition: factual description and schema values; no evaluative language.
- NOT: INVENTORY SCHEMA is omitted or has unfilled fields -- a schema with blanks cannot
  support a cited diagnosis. Positive condition: all five schema fields are filled.
- NOT: signal_count omitted from schema. Positive condition: count stated.

INVENTORY COMPLETE.

---

## PHASE 2: ADVERSARIAL CHALLENGE

NOT: this section is placed after the determination -- counter-evidence selected post-
verdict is selection bias. This phase runs before Phase 3.

[Paragraph 1. What is the weakest point in the Phase 1 signal inventory? If
convergence_pattern is "thin" or "mixed" in the INVENTORY SCHEMA, name why that pattern
matters for this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals appear to lean YES or NO? State the best case for uncertainty. What specific
condition would prevent a clear YES or NO from being defensible?]

**RECORD DIAGNOSIS**

NOT: the record diagnosis names a generic anti-pattern ("avoid overconfidence", "do not
list signals instead of synthesizing") that could apply to any synthesis -- a diagnosis
that does not cite the INVENTORY SCHEMA by field name is not a diagnosis; it is a generic
warning stated in specific-sounding language. The failure mode must cite INVENTORY SCHEMA
field names and exact values from Phase 1.

State the record diagnosis in this form: "RECORD DIAGNOSIS: Given this record's
[INVENTORY SCHEMA field: exact value] and [INVENTORY SCHEMA field: exact value] from
the Phase 1 INVENTORY SCHEMA, the most likely failure mode for this synthesis is
[specific failure mode]. Rationale: [why these specific schema values produce this failure
mode rather than alternatives for this hypothesis]."

Positive condition: a reader can falsify the diagnosis by (a) locating the named
INVENTORY SCHEMA fields in Phase 1, (b) confirming the cited values match exactly, and
(c) judging whether the causal link is plausible. A diagnosis that paraphrases the schema
without citing field names and values cannot be falsified in a single check.

### ADVERSARIAL CHALLENGE GATE
- NOT: adversarial challenge is absent or generic -- named record vulnerabilities required.
  Positive condition: at least two paragraphs name specific signal gaps, thin signals, or
  unconsidered scenarios.
- NOT: RECORD DIAGNOSIS fails to cite INVENTORY SCHEMA field names with exact values --
  paraphrase without citation cannot be verified by cross-reference. Positive condition:
  at least two INVENTORY SCHEMA field names appear in the RECORD DIAGNOSIS with their
  exact Phase 1 values.
- NOT: RECORD DIAGNOSIS names a failure mode without explaining why the cited schema
  values produce it. Positive condition: rationale explains the schema-value-to-failure-
  mode causal link for this hypothesis specifically.
- NOT: no counter-argument is present. Positive condition: at least one substantive
  adversarial paragraph.

ADVERSARIAL CHALLENGE COMPLETE.

---

## PHASE 3: DETERMINATION

Having issued the adversarial challenge and RECORD DIAGNOSIS, issue the determination.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the Phase 1
signals establish as a whole. Address the Phase 2 challenge. Address the RECORD DIAGNOSIS:
does the diagnosed failure mode apply to this output? DETERMINATION: MAYBE requires naming
the specific uncertainty. MAYBE is not a hedge.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it? The RECORD DIAGNOSIS should
inform the confidence ceiling -- if the diagnosed failure mode is a live risk, note its
effect on confidence.]

### DETERMINATION GATE
- NOT: DETERMINATION: is absent from the opening sentence -- register word must commit
  before reasoning follows. Positive condition: DETERMINATION: [YES/NO/MAYBE] opens the
  judgment paragraph.
- NOT: judgment paragraph ignores the Phase 2 RECORD DIAGNOSIS. Positive condition:
  RECORD DIAGNOSIS is referenced in the judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph. Positive condition: rationale
  paragraph follows the score and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition. Positive condition: MAYBE names the uncertainty.

DETERMINATION SEALED.

---

## PHASE 4: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

[Rank 1 paragraph: why most influential? Why this signal over rank 2 specifically? What
does it establish that rank 2 cannot, and why does that carry greater weight?]

[Rank 2 paragraph: what does it add that rank 1 did not establish? Why second and not
first?]

[Rank 3 paragraph, or state absent if fewer than 3 signals.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column -- cells can be filled without
  constructing a comparison. Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2. Positive
  condition: each paragraph answers the comparative question.
- NOT: any named signal absent from Phase 1 inventory. Positive condition: all named
  signals exist in Phase 1.
- NOT: paragraphs describe what signals found rather than arguing why they outweigh others.
  Positive condition: each paragraph argues relative weight.

EVIDENCE GATE CLEARED.

---

## PHASE 5: PRINCIPLES AND OPEN QUESTIONS

**Principles** (what this investigation teaches beyond this hypothesis):

[At least one declarative principle. "X implies Y." "When Z, expect W." Not a restatement
of the verdict. Must generalize beyond this specific topic.]

**Open Questions** (what the investigation did not resolve):

[At least one specific question still open. Name it. State why it remains undetermined.
State the concrete next step: which prove sub-skill, or what external action.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count,
adversary_pre_determination (true/false), determination_sealed (true/false),
record_specific_antipattern (true/false), inventory_schema_produced (true/false),
schema_citation_in_diagnosis (true/false -- true if RECORD DIAGNOSIS cited INVENTORY
SCHEMA field names with exact values; false if diagnosis paraphrased without citation).
```

---

## V-03: PRE-JUDGE PRE-FLIGHT Block

**Axis**: Role sequence -- a PRE-JUDGE PRE-FLIGHT gate block is inserted between ADVERSARY COMPLETE and the JUDGE section header; the register-word NOT: condition appears in this block before the commitment sentence is written
**Hypothesis**: C-22 fires more completely when the register-word prohibition gate is positioned BEFORE the JUDGE phase begins rather than INSIDE the DETERMINATION SEAL. R4 V-05 places the NOT: gate inside the DETERMINATION SEAL -- after the DETERMINATION: line is already present in the prompt structure. A writer who misrenders the commitment sentence encounters the NOT: condition after the failure mode has already been committed. The PRE-FLIGHT block positions the gate before the JUDGE section header: the prohibition is read before writing the commitment sentence, not alongside it. Single-axis: C-22 sharpened. R4 V-01 base: role labels + explicit prohibitions (C-16), standard adversarial challenge without INVENTORY SCHEMA (C-21 not fired), no frontmatter at open (C-19/C-20 not fired).

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

Role assignments govern output type in this synthesis. Each phase is assigned a procedural
identity that forecloses what that phase may produce. Violating a role assignment is a
procedural breach, not a style deviation. The adversary declares before the judge rules.
Write argumentative sections in prose paragraphs, not tables or bullet lists.

---

## SURVEYOR: RECORD INVENTORY

A SURVEYOR inventories. A SURVEYOR does not evaluate, compare, rank, or reach conclusions
about signal quality or significance. Any evaluative language in the SURVEYOR phase is a
procedural breach regardless of its accuracy.

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD -- no signals found for {topic}. Determination cannot proceed."

Record count: [N]

### SURVEYOR GATE
- NOT: any signal described without naming its artifact -- unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluative language appears in this phase -- the SURVEYOR role precludes evaluation;
  inventory only. Positive condition: factual description, no comparative or evaluative
  language.
- NOT: record count omitted -- count is required for confidence calibration. Positive
  condition: count stated.

SURVEYOR COMPLETE.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, surface
supporting evidence, or assist the JUDGE. Advocacy in the ADVERSARY phase is a procedural
breach. The ADVERSARY's sole function is to assemble the strongest case against the
hypothesis before the JUDGE rules.

NOT: this section is placed after the DETERMINATION -- counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Name the specific gap,
thin signal, or missing evidence type. If signals are thin (N < 3), name what is absent
and why that absence matters for this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty. What specific
condition would prevent a clear YES or NO from being defensible?]

[Paragraph 3. What is the best argument for the opposite of what signals suggest? State
it as a genuine case. Name one failure mode this synthesis must avoid -- not a generic
warning, but one that fits this investigation's signal set.]

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic ("evidence is limited") -- a declaration
  that the ADVERSARY did not run is not an adversarial challenge. Positive condition: at
  least two paragraphs name specific record vulnerabilities by name.
- NOT: ADVERSARY phase contains advocacy language supporting the hypothesis -- advocacy
  is a role breach. Positive condition: all content challenges the hypothesis or the record.
- NOT: source of each adversarial argument is omitted -- unsourced opposition cannot be
  evaluated. Positive condition: each challenge paragraph sourced to a specific gap,
  logical gap, or unconsidered scenario.

ADVERSARY COMPLETE.

---

## PRE-JUDGE PRE-FLIGHT

This block appears between ADVERSARY COMPLETE and the JUDGE section. It is a gate, not
prose. Run this block before beginning any JUDGE content.

PRE-FLIGHT CHECKLIST:
[ ] ADVERSARY phase is written and ADVERSARY COMPLETE appears above.
[ ] At least two adversarial challenge paragraphs are present above.
[ ] No DETERMINATION language appears anywhere above this point.

REGISTER-WORD GATE (read before writing the commitment sentence):

NOT: the commitment sentence begins with any word other than the register word.
"Our final DETERMINATION is:" violates this gate before you write it.
"Based on the foregoing, DETERMINATION:" violates this gate before you write it.
"The record leads to a DETERMINATION of:" violates this gate before you write it.

This prohibition is stated here -- before the JUDGE section -- so that it is encountered
before the failure mode can occur. NOT: this pre-flight block appears after the commitment
sentence -- a gate that names the failure mode after the commitment point has been passed
closes nothing.

Positive condition: the commitment sentence begins DETERMINATION: [YES/NO/MAYBE] with
DETERMINATION as the syntactically first word and no preceding language.

PRE-FLIGHT CLEARED. Proceed to JUDGE.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer to signal ambiguity. Hedging
in the JUDGE phase is a procedural breach. The JUDGE issues a determination against the
ADVERSARY's pre-recorded challenge.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record
establishes as a whole. Address the ADVERSARY's challenge: does it reduce confidence,
cap it, or fail to move the answer? DETERMINATION: MAYBE requires naming the specific
uncertainty. MAYBE is not a hedge; it is a committed uncertainty with a named resolution
condition. A JUDGE that issues MAYBE without naming what would resolve it has hedged.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it -- signal gaps, the
ADVERSARY challenge, or unconsidered scenarios? High confidence (>= 75): name converging
signals and explain why convergence matters beyond mere agreement. Low confidence (<= 40):
name the specific gap or conflict.]

### DETERMINATION SEAL
- NOT: judgment paragraph fails to address the ADVERSARY's challenge -- the challenge was
  issued; the JUDGE must weigh it explicitly. Positive condition: ADVERSARY challenge
  referenced and weighed.
- NOT: CONFIDENCE notation lacks a rationale paragraph. Positive condition: rationale
  paragraph follows the score and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition. Positive condition: MAYBE names the uncertainty and the condition under which
  it resolves.

DETERMINATION SEALED.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE -- [Signal name]**
[Paragraph. Why most determinative? What does primary establish that secondary cannot, and
why does that carry greater weight? Answer the comparative question: why primary over
secondary specifically?]

**SECONDARY EVIDENCE -- [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE -- [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column -- a table is an annotated list,
  not an argument. Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2. Positive
  condition: each paragraph answers the comparative question: why this tier over the one
  ranked below?
- NOT: any named signal absent from SURVEYOR record. Positive condition: all named signals
  traceable to the SURVEYOR inventory.
- NOT: paragraphs describe signal findings rather than arguing relative weight. Positive
  condition: each paragraph argues why this signal outweighs the one ranked below.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Holdings that
merely restate the DETERMINATION are not Holdings -- must generalize beyond this hypothesis
to apply to future investigations with different topics.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined.
State the next investigative action: which prove sub-skill or concrete external step.]

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
Frontmatter: skill, topic, date, answer, confidence, signal_count,
adversary_pre_determination (true/false), determination_sealed (true/false),
role_foreclusion_explicit (true/false), preflight_confirmed (true/false -- true if
PRE-JUDGE PRE-FLIGHT block appears between ADVERSARY COMPLETE and JUDGE section header).
```

---

## V-04: Phase-Gate Attestations + INVENTORY SCHEMA Citation (Combo)

**Axes**: Phase-gate transition attestations at each phase boundary (C-20 sharpened, without frontmatter at open) + SURVEYOR INVENTORY SCHEMA with schema-cited RECORD DIAGNOSIS (C-21 sharpened). C-22 at R4 V-05 standard level (NOT: gate inside DETERMINATION SEAL). R4 V-04 base (C-16 + C-17 + C-18, no C-19).
**Hypothesis**: C-20 and C-21 sharpening compose without C-19. Without a frontmatter-at-open block, per-field phase gates appear as inline transition attestations at each phase exit: "NOT: ADVERSARY begins with signal_count unset in frontmatter." The INVENTORY SCHEMA provides the named field structure that RECORD DIAGNOSIS must cite -- making the failure mode diagnosis falsifiable in a single lookup rather than re-readable from inventory prose. Calibration question: does C-20 sharpening without C-19 produce clean phase-sequential compliance? Does C-21 sharpening hold when embedded in role-labeled phases rather than schema-aware phase titles?

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

Role assignments govern output type in this synthesis. Each phase is assigned a procedural
identity that forecloses what that phase may produce. Violating a role assignment is a
procedural breach, not a style deviation. The adversary declares before the judge rules.
Write argumentative sections in prose paragraphs, not tables or bullet lists.

---

## SURVEYOR: RECORD INVENTORY

A SURVEYOR inventories. A SURVEYOR does not evaluate, compare, rank, or reach conclusions
about signal quality or significance. Evaluation by a SURVEYOR is a procedural breach
regardless of its accuracy.

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD -- no signals found for {topic}. Determination cannot proceed."

After recording all signals, produce the INVENTORY SCHEMA:

INVENTORY SCHEMA:
  signal_count: [N]
  method_set: [list each prove sub-skill represented; or "single method" if all signals
               share one sub-skill]
  convergence_pattern: [converging / conflicting / thin (N < 3) / mixed with named
                        divergence point]
  dominant_signal: [name of signal with most specific stated finding; or "none identified"]
  coverage_gaps: [hypothesis dimensions with no signal coverage; or "none identified"]

### SURVEYOR GATE
- NOT: any signal described without naming its artifact -- unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluative language appears in this phase -- the SURVEYOR role precludes evaluation;
  inventory and schema production only. Positive condition: factual description, no
  comparative or evaluative language.
- NOT: INVENTORY SCHEMA is omitted or has unfilled fields -- an incomplete schema cannot
  support a cited diagnosis. Positive condition: all five schema fields are filled.
- NOT: record count omitted. Positive condition: signal_count stated in schema.
- NOT: signal_count set in frontmatter remains unfilled after this gate clears. Positive
  condition: signal_count set in frontmatter before ADVERSARY begins.

SURVEYOR COMPLETE.
NOT: ADVERSARY begins before INVENTORY SCHEMA is produced and signal_count is set in
frontmatter.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, surface
supporting evidence, or assist the JUDGE. Advocacy in the ADVERSARY phase is a procedural
breach. The ADVERSARY's sole function is to assemble the strongest case against the
hypothesis before the JUDGE rules.

NOT: this section is placed after the DETERMINATION -- counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Reference the INVENTORY
SCHEMA: if convergence_pattern is thin or conflicting, name why that pattern matters for
this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty. What specific
condition would prevent a clear YES or NO from being defensible?]

**RECORD DIAGNOSIS**

NOT: the record diagnosis names a generic anti-pattern ("avoid overconfidence", "do not
list signals") that could apply to any synthesis -- a diagnosis that does not cite
INVENTORY SCHEMA field names with their exact values is not a diagnosis; it is a generic
warning stated in specific-sounding language.

NOT: the record diagnosis paraphrases the INVENTORY SCHEMA without citing field names and
exact values -- paraphrase cannot be falsified in a single lookup.

State: "RECORD DIAGNOSIS: Given this record's [INVENTORY SCHEMA field: exact value] and
[INVENTORY SCHEMA field: exact value] from the SURVEYOR INVENTORY SCHEMA, the most likely
failure mode for this synthesis is [specific failure mode]. Rationale: [why these specific
schema values produce this failure mode for this hypothesis rather than alternatives]."

Positive condition: a reader can falsify this diagnosis by locating the cited INVENTORY
SCHEMA fields in the SURVEYOR section and confirming the values match exactly. A diagnosis
is falsified if any cited field value differs from the INVENTORY SCHEMA.

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic -- named record vulnerabilities required.
  Positive condition: at least two paragraphs name specific record vulnerabilities.
- NOT: RECORD DIAGNOSIS fails to cite INVENTORY SCHEMA field names with exact values.
  Positive condition: at least two INVENTORY SCHEMA field names appear with their exact
  SURVEYOR values.
- NOT: RECORD DIAGNOSIS names a failure mode without explaining why the cited schema
  values produce it. Positive condition: rationale explains the causal link.
- NOT: ADVERSARY phase contains advocacy language supporting the hypothesis -- advocacy
  is a role breach. Positive condition: all content challenges the hypothesis or the record.

ADVERSARY COMPLETE.
NOT: JUDGE begins before adversary_pre_determination is set true in frontmatter.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer. Hedging in the JUDGE phase
is a procedural breach. The JUDGE issues a determination against both the ADVERSARY's
challenge and the RECORD DIAGNOSIS -- both are already on the table.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record
establishes as a whole. Address the ADVERSARY's challenge. Address the RECORD DIAGNOSIS:
does the diagnosed failure mode apply to this output? DETERMINATION: MAYBE requires naming
the specific uncertainty. MAYBE is not a hedge.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it? The RECORD DIAGNOSIS
informs the confidence ceiling -- if the diagnosed failure mode is a live risk, note its
effect on confidence.]

### DETERMINATION SEAL
- NOT: the register word appears after introductory language ("Our final DETERMINATION
  is:", "Based on the foregoing, DETERMINATION:") -- a register word not first in its
  sentence allows hedging to precede the commitment point. Positive condition:
  DETERMINATION: is the first word of the commitment sentence.
- NOT: judgment paragraph fails to address the ADVERSARY's pre-determination challenge.
  Positive condition: ADVERSARY challenge referenced and weighed.
- NOT: judgment paragraph fails to address the RECORD DIAGNOSIS -- the failure mode was
  named; the JUDGE must state whether it applies. Positive condition: RECORD DIAGNOSIS
  referenced in judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph. Positive condition: rationale
  paragraph follows the score and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition. Positive condition: MAYBE names the uncertainty.

DETERMINATION SEALED.
NOT: ADVOCATE begins before determination_sealed is set true in frontmatter.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE -- [Signal name]**
[Paragraph. Why most determinative? What does primary establish that secondary cannot, and
why does that carry greater weight? Answer the comparative question: why primary over
secondary specifically?]

**SECONDARY EVIDENCE -- [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE -- [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column -- a table is an annotated list,
  not an argument. Positive condition: each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2. Positive
  condition: each paragraph answers the comparative question.
- NOT: any named signal absent from SURVEYOR record. Positive condition: all named signals
  exist in the SURVEYOR inventory.
- NOT: paragraphs describe signal findings rather than arguing relative weight. Positive
  condition: each paragraph argues why this signal outweighs the one ranked below.

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
Frontmatter: skill, topic, date, answer, confidence, signal_count,
adversary_pre_determination (true/false), determination_sealed (true/false),
role_foreclusion_explicit (true/false), record_specific_antipattern (true/false),
inventory_schema_produced (true/false), schema_citation_in_diagnosis (true/false).
```

---

## V-05: Full Combo -- All Three Sharpened Mechanisms + R4 V-05 Inheritance

**Axes**: Per-field phase-gate NOT: conditions on each frontmatter field (C-20 sharpened) + SURVEYOR INVENTORY SCHEMA with schema-cited RECORD DIAGNOSIS (C-21 sharpened) + PRE-JUDGE PRE-FLIGHT block with register-word gate before commitment sentence (C-22 sharpened). Complete R4 V-05 inheritance: role prohibitions (C-16), structured RECORD DIAGNOSIS (C-17), register-word-first format (C-18), frontmatter at open (C-19).
**Hypothesis**: The three sharpening mechanisms are mutually reinforcing and together advance the artifact from "compliance declared after writing" to "compliance gated before proceeding" at every critical structural transition. Per-field NOT: conditions make premature frontmatter filling a named violation -- not just a missed instruction. Schema-cited RECORD DIAGNOSIS makes the failure mode falsifiable in a single lookup -- not re-readable from inventory prose. PRE-JUDGE PRE-FLIGHT positions the register-word gate before the commitment sentence can be written -- the failure mode is foreclosed before it can occur. Together: INVENTORY SCHEMA produces addressable fields; per-field gates track phase compliance against those fields; PRE-FLIGHT enforces the commitment sequence before the commitment point is reached. V6 candidates C-23, C-24, C-25 emerge from this structure.

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

Role assignments govern output type in this synthesis. Each phase is assigned a procedural
identity that forecloses what that phase may produce. Violating a role assignment is a
procedural breach, not a style deviation. The adversary declares before the judge rules.
Write argumentative sections in prose paragraphs, not tables or bullet lists.

Open the artifact with the following FRONTMATTER DECLARATIONS block. Each field is a
commitment declaration with an explicit phase gate. Each field carries two NOT:
prohibitions: one for premature filling and one for deferred filling. Both violations
produce false declarations, not pre-commitments.

NOT: any frontmatter field filled before its gate is reached -- premature filling produces
a false declaration. NOT: any frontmatter field left unfilled until after the full artifact
is written -- deferred filling produces a post-hoc label. Each field is set at the
structural moment its gate becomes reachable.

---

FRONTMATTER DECLARATIONS (open the artifact here):

  skill: prove-synthesize
  topic: {topic}
  date: {date}

  signal_count: [fill after SURVEYOR COMPLETE, before ADVERSARY begins]
  NOT: signal_count filled before any SURVEYOR content is written.
  NOT: signal_count filled after ADVERSARY content begins.

  adversary_pre_determination: [true if ADVERSARY ran structurally before JUDGE; false if not]
  NOT: adversary_pre_determination filled before ADVERSARY content is written.
  NOT: adversary_pre_determination filled after JUDGE content begins.

  answer: [fill after DETERMINATION: line is written]
  NOT: answer filled before DETERMINATION: line is written.

  confidence: [fill after CONFIDENCE: notation is written]
  NOT: confidence filled before CONFIDENCE: notation is written.

  register_word_used: [true if DETERMINATION: is the first word of the commitment sentence]
  NOT: register_word_used filled before DETERMINATION: line is written.

  not_first_gates: [true if every gate item in this artifact opens with NOT:]
  NOT: not_first_gates filled before all gate sections are written.
  NOT: not_first_gates set true if any gate item in the artifact does not open with NOT:.

  record_specific_antipattern: [true if RECORD DIAGNOSIS cited INVENTORY SCHEMA fields
                                with exact values; false if paraphrased without citation]
  NOT: record_specific_antipattern filled before ADVERSARY COMPLETE.

  role_foreclusion_explicit: [true if each role section states what the role cannot produce]
  NOT: role_foreclusion_explicit set true if any role section lacks explicit prohibition
  statements.

  preflight_confirmed: [true if PRE-JUDGE PRE-FLIGHT block appears before JUDGE section]
  NOT: preflight_confirmed filled before PRE-JUDGE PRE-FLIGHT block is written.

---

## SURVEYOR: RECORD INVENTORY

A SURVEYOR inventories. A SURVEYOR does not evaluate, compare, rank, or reach conclusions
about signal quality or significance. Evaluation by a SURVEYOR is a procedural breach
regardless of its accuracy. Set role_foreclusion_explicit: true in frontmatter only if
every role section in this artifact states what the role cannot produce.

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD -- no signals found for {topic}. Determination cannot proceed."

After recording all signals, produce the INVENTORY SCHEMA. All five fields are required.

INVENTORY SCHEMA:
  signal_count: [N]
  method_set: [list each prove sub-skill represented; or "single method" if all signals
               share one sub-skill]
  convergence_pattern: [converging / conflicting / thin (N < 3) / mixed with named
                        divergence point]
  dominant_signal: [name of signal with most specific stated finding; or "none identified"]
  coverage_gaps: [hypothesis dimensions with no signal coverage; or "none identified"]

### SURVEYOR GATE
- NOT: any signal described without naming its artifact -- unnameable signals are
  unverifiable. Positive condition: every signal identified by artifact name.
- NOT: evaluative language appears in this phase -- the SURVEYOR role precludes evaluation;
  inventory and schema production only. Positive condition: factual description, no
  comparative or evaluative language.
- NOT: INVENTORY SCHEMA is omitted or has unfilled fields -- an incomplete schema cannot
  support a cited diagnosis. Positive condition: all five schema fields are filled.
- NOT: signal_count in frontmatter remains unfilled after this gate clears. Positive
  condition: signal_count set in frontmatter before ADVERSARY begins.

SURVEYOR COMPLETE. Set signal_count: [N] in frontmatter now.
NOT: ADVERSARY begins with signal_count unset in frontmatter.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, surface
supporting evidence, or assist the JUDGE's determination. Advocacy in the ADVERSARY phase
is a procedural breach. The ADVERSARY's sole function is to assemble the strongest case
against the hypothesis before the JUDGE rules.

NOT: this section is placed after the DETERMINATION -- counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete. Set
adversary_pre_determination: true in frontmatter now.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Reference the INVENTORY
SCHEMA: if convergence_pattern is thin or conflicting, name why that pattern matters for
this hypothesis specifically. If signals are thin (N < 3), name what type is absent and
why that absence matters.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty. What specific
condition would need to be true for a confident YES or NO to be indefensible?]

**RECORD DIAGNOSIS**

NOT: the record diagnosis names a generic anti-pattern ("avoid overconfidence", "do not
list signals instead of synthesizing", "verify counter-evidence is present") that could
apply to any synthesis -- a generic warning is a template exercise, not a diagnosis. The
failure mode must be derived from the INVENTORY SCHEMA's actual field values.

NOT: the record diagnosis paraphrases the INVENTORY SCHEMA without citing field names and
exact values -- a diagnosis that cannot be checked against the schema in a single lookup
is not falsifiable. At least two INVENTORY SCHEMA field names must appear with their exact
values.

State: "RECORD DIAGNOSIS: Given this record's [INVENTORY SCHEMA field: exact value] and
[INVENTORY SCHEMA field: exact value] from the SURVEYOR INVENTORY SCHEMA, the most likely
failure mode for this synthesis is [specific failure mode]. Rationale: [why these specific
schema values produce this failure mode for this hypothesis rather than alternatives]."

Positive condition: a reader can falsify this diagnosis by (a) locating the cited
INVENTORY SCHEMA fields in the SURVEYOR section, (b) confirming the cited values match
exactly, and (c) judging whether the causal link is plausible. Set
record_specific_antipattern: true in frontmatter if conditions (a) and (b) are met; false
if the diagnosis paraphrases without citation.

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic -- a declaration that the ADVERSARY did
  not run is not an adversarial challenge. Positive condition: at least two paragraphs
  name specific record vulnerabilities -- named gaps, named thin signals, named scenarios.
- NOT: RECORD DIAGNOSIS fails to cite INVENTORY SCHEMA field names with exact values --
  paraphrase without citation cannot be falsified. Positive condition: at least two
  INVENTORY SCHEMA field names appear with their exact SURVEYOR values.
- NOT: RECORD DIAGNOSIS names a failure mode without explaining why the cited schema
  values produce it. Positive condition: rationale explains the schema-value-to-failure-
  mode causal link for this hypothesis.
- NOT: ADVERSARY phase contains advocacy language supporting the hypothesis -- advocacy
  is a role breach. Positive condition: all content challenges the hypothesis or the record.

ADVERSARY COMPLETE.
NOT: JUDGE begins before adversary_pre_determination is set true in frontmatter.

---

## PRE-JUDGE PRE-FLIGHT

This block appears between ADVERSARY COMPLETE and the JUDGE section. It is a gate, not
prose. This block runs before any JUDGE content is written.

PRE-FLIGHT CHECKLIST:
[ ] ADVERSARY phase is written and ADVERSARY COMPLETE appears above.
[ ] RECORD DIAGNOSIS appears in ADVERSARY phase and cites INVENTORY SCHEMA fields.
[ ] At least two adversarial challenge paragraphs are present.
[ ] No DETERMINATION language appears anywhere above this point.

REGISTER-WORD GATE (read before writing the commitment sentence):

NOT: the commitment sentence begins with any word other than the register word.
"Our final DETERMINATION is:" violates this gate before you write it.
"Based on the foregoing, DETERMINATION:" violates this gate before you write it.
"The record supports a DETERMINATION of:" violates this gate before you write it.

This prohibition is stated here -- before the JUDGE section begins -- so that it is
encountered before the failure mode can occur. NOT: this pre-flight block appears after
the commitment sentence -- a gate that names the failure mode after the commitment point
has been passed closes nothing.

Positive condition: the commitment sentence begins DETERMINATION: [YES/NO/MAYBE] with
DETERMINATION as the syntactically first word.

Set preflight_confirmed: true in frontmatter now.
PRE-FLIGHT CLEARED. Proceed to JUDGE.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer to signal ambiguity. Hedging
or equivocation in the JUDGE phase is a procedural breach. The JUDGE issues a
determination against both the ADVERSARY's challenge and the RECORD DIAGNOSIS -- both are
already on the table.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Set register_word_used: true in frontmatter
now. Issue a determination of what the record establishes as a whole. Address the
ADVERSARY's challenge: does it reduce confidence, cap it, or fail to move the
determination? Address the RECORD DIAGNOSIS: does the diagnosed failure mode apply to
this output, or has it been avoided? DETERMINATION: MAYBE requires naming the specific
uncertainty. MAYBE is not a hedge; it is a committed uncertainty with a named resolution
condition.]

**CONFIDENCE: [N]/100** -- set confidence and answer in frontmatter now.

[Confidence paragraph. What drove this number? What capped it -- signal gaps, the
ADVERSARY challenge, the RECORD DIAGNOSIS risk, or unconsidered scenarios? High confidence
(>= 75): name converging signals and explain why convergence matters beyond mere agreement.
Low confidence (<= 40): name the specific gap or conflict.]

### DETERMINATION SEAL
- NOT: the register word appears after introductory language ("Our final DETERMINATION
  is:", "Based on the foregoing, DETERMINATION:") -- a register word not first in its
  sentence allows hedging to precede the commitment point; the mechanism fires only when
  register-word-first. Positive condition: DETERMINATION: is the first word of the
  commitment sentence. Set register_word_used: false if this condition is not met.
- NOT: judgment paragraph fails to address the ADVERSARY's pre-determination challenge --
  the challenge was issued; the JUDGE must weigh it explicitly. Positive condition:
  ADVERSARY challenge referenced and weighed in judgment or confidence paragraph.
- NOT: judgment paragraph fails to address the RECORD DIAGNOSIS -- the failure mode was
  named; the JUDGE must state whether it applies. Positive condition: RECORD DIAGNOSIS
  referenced in judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph -- a score without reasoning cannot
  be interrogated or falsified. Positive condition: rationale paragraph follows the score
  and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition -- MAYBE used as a hedge is a judicial breach. Positive condition: MAYBE names
  the uncertainty and the condition under which it would resolve to YES or NO.
- NOT: answer and confidence in frontmatter remain unfilled after this gate. Positive
  condition: both set now.

DETERMINATION SEALED.
NOT: ADVOCATE begins before determination_sealed is set true in frontmatter.

---

## ADVOCATE: EVIDENCE HIERARCHY

Name up to 3 signals as key evidence. This is a ranked argument, not a ranked list. Write
one prose paragraph per signal arguing why it carried more weight toward the DETERMINATION
than signals ranked below it.

**PRIMARY EVIDENCE -- [Signal name]**
[Paragraph. Why most determinative? What does primary establish that secondary cannot, and
why does that carry greater weight toward the DETERMINATION? Answer the comparative
question: why primary over secondary specifically?]

**SECONDARY EVIDENCE -- [Signal name]**
[Paragraph. What does it add that primary did not establish? Why secondary and not primary?]

**TERTIARY EVIDENCE -- [Signal name, or "record insufficient for three tiers"]**
[Paragraph, or state absent with reason.]

### EVIDENCE GATE
- NOT: evidence hierarchy is a table with a "why" column -- a table is an annotated list,
  not an argument; filling cells requires no argument construction. Positive condition:
  each entry is a prose paragraph.
- NOT: rank 1 justified as "strongest support" without comparison to rank 2 -- presence
  of support is not relative weight. Positive condition: each paragraph answers the
  comparative question: why this tier over the one ranked below?
- NOT: any named signal absent from SURVEYOR record -- signals outside the record cannot
  be traced to investigation artifacts. Positive condition: all named signals exist in
  the SURVEYOR inventory.
- NOT: paragraphs describe signal findings rather than arguing relative weight --
  description is not argument. Positive condition: each paragraph argues why this signal
  outweighs the one ranked below it.

EVIDENCE GATE CLEARED.

---

## SCHOLAR: PRINCIPLES AND OPEN RECORD

**Holdings** (what this determination establishes beyond this case):

[At least one declarative principle. "X implies Y." "When Z, expect W." Holdings that
merely restate the DETERMINATION are not Holdings -- they must generalize beyond this
specific hypothesis to apply to future investigations with different topics.]

**Open Record** (what the investigation did not determine):

[At least one specific question still open. Name it. State why it remains undetermined --
what evidence was absent or inconclusive. State the next investigative action: which prove
sub-skill or concrete external step.]

Set not_first_gates: true in frontmatter now if every gate section in this artifact opens
its items with NOT:; false if any gate item opens otherwise.
NOT: not_first_gates set before all gate sections are written.

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
The FRONTMATTER DECLARATIONS block at document open is part of the artifact. All boolean
fields carry their NOT: prohibitions and must be set at their declared phase gates.
The frontmatter is a compliance record, not formatting metadata. Verify before finalizing:
- All per-field NOT: prohibitions are present in the opening block.
- INVENTORY SCHEMA was produced by SURVEYOR with all five fields filled.
- RECORD DIAGNOSIS cited at least two INVENTORY SCHEMA fields with exact values.
- PRE-JUDGE PRE-FLIGHT block appears between ADVERSARY COMPLETE and JUDGE section.
- preflight_confirmed set true at PRE-FLIGHT CLEARED.
```
