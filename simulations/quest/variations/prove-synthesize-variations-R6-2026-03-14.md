Written to `simulations/quest/variations/prove-synthesize-variations-R6-2026-03-14.md`.

---

**Round 6 — V-01 through V-05**

| # | Axis | Base | New mechanism | v7 candidate |
|---|------|------|--------------|--------------|
| V-01 | Named violation categories (C-23) | R5 V-01 | Fill-window bounds name the violation type inline: PREMATURE COMPLETION VIOLATION / DEFERRED COMPLETION VIOLATION / PHASE-ADVANCE VIOLATION / FALSE ATTESTATION VIOLATION | C-26: violation-registry block at document open |
| V-02 | Arrow-chain diagnosis notation (C-24) | R5 V-02 | RECORD DIAGNOSIS uses `field: value -> failure mode: result` arrow-chain syntax; NOT: gate forecloses prose and bracket-placeholder formats | C-27: arrow-chain propagates through PRE-FLIGHT audit |
| V-03 | PRE-FLIGHT three-phase audit (C-25 extended) | R5 V-03 + INVENTORY SCHEMA | PRE-FLIGHT split into three named phases: (A) structural completeness / (B) SCHEMA-CITATION AUDIT / (C) register-word gate; Phase B is a distinct structural phase | C-27: schema audit as independent criterion beyond C-25 |
| V-04 | Named violations + arrow-chain (combo) | R5 V-04 | C-23 via phase-boundary attestation labels + C-24 via arrow-chain diagnosis; DETERMINATION SEAL for C-22 | C-23 + C-24 |
| V-05 | Full combo | R5 V-05 | All three sharpened + complete R5 V-05 inheritance; v7 candidates C-26, C-27 predicted from V-05 mechanisms | C-23 + C-24 + C-25 confirmed |

**Three R6 calibration questions:**

1. **C-23 embedding vs. standalone**: Does C-23 fire when violation type names are embedded in the NOT: gate text ("Filling X before Y is a PREMATURE COMPLETION VIOLATION"), or must the names appear as standalone citable labels outside the NOT: condition? V-01 tests inline embedding.
2. **C-24 prose-only vs. two-site**: Does C-24 fire with a two-field arrow chain in RECORD DIAGNOSIS prose alone, or does it additionally require verification through the PRE-FLIGHT schema-citation audit? V-02 tests prose-only arrow chains.
3. **C-25 phase count**: Does adding a SCHEMA-CITATION AUDIT as a named Phase B step within PRE-FLIGHT produce a v7 candidate, or does it represent a fuller realization of C-25 already? V-03 tests three-phase PRE-FLIGHT.

**Key mechanism differences from R5:**

- **C-23 vs. R5 V-01**: R5 had `NOT: signal_count filled before...` — writer knows what to avoid. R6 V-01 adds `Filling signal_count before... is a PREMATURE COMPLETION VIOLATION` — the failure has a name a reviewer can cite without quoting the full prohibition.
- **C-24 vs. R5 V-02**: R5 had `[INVENTORY SCHEMA field: exact value]` bracket placeholders that fill to prose. R6 V-02 requires the arrow-chain form `convergence_pattern: thin -> failure mode: false confidence ceiling` — a lookup path, not a prose clause.
- **C-25 extended vs. R5 V-03**: R5 PRE-FLIGHT had structural completeness + register-word gate (two steps). R6 V-03 inserts SCHEMA-CITATION AUDIT as Phase B between them — three distinct named audit phases.
ore any SURVEYOR content is written" -- the writer is told what to avoid but has no named category for what they did wrong. V-01 converts each bound to a named violation: "Filling signal_count before any SURVEYOR content is written is a PREMATURE COMPLETION VIOLATION." Named violations are citable: a reviewer can write "DEFERRED COMPLETION VIOLATION on adversary_pre_determination" as a complete finding.

**V-02 base -- R5 V-02 (INVENTORY SCHEMA, phase titles PHASE 1-5, structured RECORD DIAGNOSIS C-21, no role labels C-16, no frontmatter at open C-19/C-20, DETERMINATION: format C-18, no PRE-FLIGHT C-22/C-25):** C-24 extends C-21 -- isolating the sharpened mechanism requires C-21 present (schema-traceable diagnosis) but C-24 absent (arrow-chain syntax not required). R5 V-02 RECORD DIAGNOSIS uses bracket placeholders that when filled produce prose. V-02 sharpens to arrow-chain: `convergence_pattern: thin -> failure mode: false confidence ceiling`. The arrow is a lookup path, not a prose clause. A reader locates `convergence_pattern` in INVENTORY SCHEMA, confirms value is `thin`, judges the arrow -- one lookup, no parsing.

**V-03 base -- R5 V-03 (role prohibitions C-16, PRE-FLIGHT C-22/C-25, standard adversarial challenge, no INVENTORY SCHEMA, no frontmatter at open C-19/C-20):** C-25 extended -- isolating the sharpened mechanism requires C-25 present (PRE-FLIGHT as structural phase before JUDGE) but the schema-citation audit step absent. R5 V-03 PRE-FLIGHT had structural completeness and register-word gate. V-03 adds SCHEMA-CITATION AUDIT as the middle phase before the register-word gate. INVENTORY SCHEMA is introduced as a necessary dependency. Single axis: three-phase PRE-FLIGHT with schema audit as named middle phase.

**V-04 base -- R5 V-04 (role prohibitions C-16, INVENTORY SCHEMA C-21, structured RECORD DIAGNOSIS C-17, register-word C-18, no frontmatter at open C-19, phase-boundary attestations C-20):** Combines V-01 mechanism (named violation categories at phase exits) with V-02 mechanism (arrow-chain RECORD DIAGNOSIS). Without frontmatter-at-open, named violation categories appear at phase-boundary attestations: "Advancing without signal_count set is a PHASE-ADVANCE VIOLATION." C-22 remains at DETERMINATION SEAL level (explicit NOT: gate naming positional failure mode). Calibration: do C-23 and C-24 compose without C-19?

**V-05 base -- R5 V-05 (all 22 criteria, maximum scorer):** Inherits full R5 V-05 structure and sharpens all three new mechanisms. Named violation categories on every frontmatter field bound (C-23). Arrow-chain notation in RECORD DIAGNOSIS (C-24). PRE-FLIGHT expanded to three-phase audit with SCHEMA-CITATION AUDIT as named middle phase (C-25 extended). V7 candidates predicted: C-26 (violation registry at document open -- all named violation types indexed before frontmatter), C-27 (arrow-chain propagates from RECORD DIAGNOSIS through PRE-FLIGHT audit and into JUDGE confidence reference -- three-site chain of custody).

---

## V-01: Named Violation Categories

**Axis**: Output format -- fill-window bounds express violation type by name; violation types are citable labels independent of the NOT: prohibition text
**Hypothesis**: C-23 fires when fill-window bounds name the violation type, not merely state the prohibition. R5 V-01 had "NOT: signal_count filled before any SURVEYOR content is written" -- the writer knows what to avoid but has no named category for the failure. Converting each bound to a named violation: "Filling signal_count before any SURVEYOR content is written is a PREMATURE COMPLETION VIOLATION." A reviewer now cites "PREMATURE COMPLETION VIOLATION on signal_count" as a complete finding. Single-axis: C-23 sharpened. R5 V-01 base (C-19 present, role phase labels without explicit prohibition statements C-16 not fired, adversarial challenge without INVENTORY SCHEMA C-21 not fired, no PRE-FLIGHT C-25 not fired, DETERMINATION SEAL without explicit positional NOT: gate C-22 not fired).

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

The determination is issued against the adversary's pre-recorded best case. The adversary
declares before the judge rules. Write argumentative sections in prose paragraphs, not
tables or bullet lists.

Open the artifact with the following FRONTMATTER DECLARATIONS block. Each field carries a
fill window with named violation types. Violation types are citable labels: a reviewer who
finds a field filled outside its window states the violation type, the field, and the
structural moment -- a complete finding requiring no further reading.

---

FRONTMATTER DECLARATIONS (open the artifact here):

  skill: prove-synthesize
  topic: {topic}
  date: {date}

  signal_count: [fill after SURVEYOR COMPLETE, before ADVERSARY begins]
  Filling signal_count before any SURVEYOR content is written is a PREMATURE COMPLETION
  VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.
  Filling signal_count after ADVERSARY content begins is a DEFERRED COMPLETION VIOLATION.
  Named violation type: DEFERRED COMPLETION VIOLATION.

  adversary_pre_determination: [true if ADVERSARY ran structurally before JUDGE; false if not]
  Filling adversary_pre_determination before ADVERSARY content is written is a PREMATURE
  COMPLETION VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.
  Filling adversary_pre_determination after JUDGE content begins is a DEFERRED COMPLETION
  VIOLATION. Named violation type: DEFERRED COMPLETION VIOLATION.

  answer: [fill after DETERMINATION: line is written]
  Filling answer before DETERMINATION: line is written is a PREMATURE COMPLETION
  VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.
  Filling answer after DETERMINATION SEALED appears is a DEFERRED COMPLETION VIOLATION.
  Named violation type: DEFERRED COMPLETION VIOLATION.

  confidence: [fill after CONFIDENCE: notation is written]
  Filling confidence before CONFIDENCE: notation is written is a PREMATURE COMPLETION
  VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.

  register_word_used: [true if DETERMINATION: is the syntactically first word of the
                       commitment sentence; false if DETERMINATION: appears elsewhere]
  Filling register_word_used before DETERMINATION: line is written is a PREMATURE
  COMPLETION VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.

  not_first_gates: [true if every gate item in this artifact opens with NOT:]
  Filling not_first_gates before all gate sections are written is a PREMATURE COMPLETION
  VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.
  Setting not_first_gates: true when any gate item does not open with NOT: is a FALSE
  ATTESTATION VIOLATION. Named violation type: FALSE ATTESTATION VIOLATION.

  violation_categories_named: [true if every fill-window bound states a named violation
                               type; false if any bound uses only NOT: without a name]
  Filling violation_categories_named before all FRONTMATTER fields are written is a
  PREMATURE COMPLETION VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.

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
- NOT: signal_count in frontmatter remains unfilled after this gate clears. Failure to
  set signal_count before ADVERSARY begins is a DEFERRED COMPLETION VIOLATION. Named
  violation type: DEFERRED COMPLETION VIOLATION. Positive condition: signal_count set.

SURVEYOR COMPLETE. Set signal_count: [N] in frontmatter now.
Advancing to ADVERSARY without signal_count set is a PHASE-ADVANCE VIOLATION.
Named violation type: PHASE-ADVANCE VIOLATION.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

NOT: this section is placed after the DETERMINATION -- counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete.

Set adversary_pre_determination: true in frontmatter now.
Advancing to JUDGE without adversary_pre_determination set is a PHASE-ADVANCE VIOLATION.
Named violation type: PHASE-ADVANCE VIOLATION.

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
  name specific record vulnerabilities.
- NOT: source of opposition is omitted -- unsourced opposition cannot be evaluated.
  Positive condition: each challenge paragraph sourced to a specific gap or scenario.
- NOT: adversary_pre_determination in frontmatter remains unfilled after this gate.
  Failure to set before JUDGE begins is a DEFERRED COMPLETION VIOLATION. Named violation
  type: DEFERRED COMPLETION VIOLATION.

ADVERSARY COMPLETE.

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
Filling confidence before CONFIDENCE: notation is written is a PREMATURE COMPLETION
VIOLATION. Named violation type: PREMATURE COMPLETION VIOLATION.

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
- NOT: answer and confidence in frontmatter remain unfilled after this gate. Failure to
  set is a DEFERRED COMPLETION VIOLATION. Positive condition: both set now.

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
  exist in the SURVEYOR inventory.
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
NOT:; false if any gate item opened otherwise. Setting not_first_gates: true when any
gate item does not open with NOT: is a FALSE ATTESTATION VIOLATION.

Set violation_categories_named: true if every fill-window bound in FRONTMATTER states a
named violation type; false if any bound uses only NOT: without naming the category.

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
The FRONTMATTER DECLARATIONS block at document open is part of the artifact. Named
violation types are citable labels: PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION
VIOLATION, PHASE-ADVANCE VIOLATION, FALSE ATTESTATION VIOLATION. Each names a class of
structural failure -- a reviewer cites the class name to identify the failure without
re-reading the full prohibition.
```

---

## V-02: Arrow-Chain Field:Value RECORD DIAGNOSIS

**Axis**: Lifecycle emphasis -- RECORD DIAGNOSIS uses `field: value -> failure mode: result` arrow-chain notation; NOT: gate explicitly forecloses prose description without arrow chain
**Hypothesis**: C-24 requires arrow-chain syntax, not merely field-name citation. R5 V-02 RECORD DIAGNOSIS used bracket placeholders ("Given this record's [INVENTORY SCHEMA field: exact value]...") that when filled produce prose like "Given this record's convergence_pattern: thin..." A reader must parse prose to extract the claim. Arrow-chain notation converts the claim to a lookup path: `convergence_pattern: thin -> failure mode: false confidence ceiling`. A reader finds `convergence_pattern` in INVENTORY SCHEMA, confirms value is `thin`, judges whether "false confidence ceiling" is plausible -- one lookup, no parsing. Single-axis: C-24 sharpened. R5 V-02 base (INVENTORY SCHEMA 5-field named schema C-21, phase titles PHASE 1-5 no role labels C-16 not fired, no frontmatter at open C-19/C-20 not fired, DETERMINATION: format C-18, no PRE-FLIGHT C-22 not upgraded).

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
An incomplete schema cannot support an arrow-chain RECORD DIAGNOSIS.

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
- NOT: evaluative language appears in this phase -- inventory and schema production only.
  Positive condition: factual description; no evaluative language.
- NOT: INVENTORY SCHEMA is omitted or has unfilled fields -- a schema with blanks cannot
  support an arrow-chain diagnosis. Positive condition: all five schema fields are filled.
- NOT: signal_count omitted from schema. Positive condition: count stated.

INVENTORY COMPLETE.

---

## PHASE 2: ADVERSARIAL CHALLENGE

NOT: this section is placed after the determination -- counter-evidence selected post-
verdict is selection bias. This phase runs before Phase 3.

[Paragraph 1. What is the weakest point in the Phase 1 signal inventory? Reference the
INVENTORY SCHEMA: if convergence_pattern is thin or conflicting, name why that pattern
matters for this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals appear to lean YES or NO? State the best case for uncertainty. What specific
condition would prevent a clear YES or NO from being defensible?]

**RECORD DIAGNOSIS**

NOT: the RECORD DIAGNOSIS describes INVENTORY SCHEMA values in prose without arrow-chain
notation -- prose description is evaluable but not falsifiable in one lookup. "The record
has thin convergence suggesting overconfidence risk" is a prose description; a reader
cannot verify it without re-reading the inventory. The arrow chain binds the diagnostic
claim directly to a schema field and value.

NOT: the RECORD DIAGNOSIS uses bracket placeholder syntax ("[INVENTORY SCHEMA field:
exact value]") without converting to arrow-chain notation -- a filled placeholder produces
prose, not a lookup path.

NOT: the RECORD DIAGNOSIS cites only one INVENTORY SCHEMA field -- a single-field chain
does not distinguish record-specific from generic diagnosis. Positive condition: at least
two INVENTORY SCHEMA field names appear in the diagnosis chain.

State the RECORD DIAGNOSIS in arrow-chain form:
"RECORD DIAGNOSIS: [INVENTORY SCHEMA field]: [exact value from Phase 1 INVENTORY SCHEMA]
-> failure mode: [specific failure mode]; [INVENTORY SCHEMA field]: [exact value] ->
exposure: [why this schema value creates this risk for this hypothesis specifically]."

Arrow-chain verification: for each field in the chain, (a) locate the field name in
INVENTORY SCHEMA, (b) confirm the cited value matches exactly, (c) judge whether the
arrow produces a plausible consequence. One lookup per field. No re-reading required.
A diagnosis is falsified if any cited field value differs from the INVENTORY SCHEMA.

### ADVERSARIAL CHALLENGE GATE
- NOT: adversarial challenge is absent or generic -- named record vulnerabilities required.
  Positive condition: at least two paragraphs name specific signal gaps, thin signals, or
  unconsidered scenarios.
- NOT: RECORD DIAGNOSIS uses prose without arrow-chain notation. Positive condition:
  RECORD DIAGNOSIS expressed as field:value -> consequence chain with at least two
  INVENTORY SCHEMA fields cited with exact values.
- NOT: RECORD DIAGNOSIS cites field names without exact Phase 1 values -- a field name
  without its value leaves the lookup incomplete. Positive condition: exact INVENTORY
  SCHEMA values are stated in the chain.
- NOT: no counter-argument is present. Positive condition: at least one substantive
  adversarial paragraph.

ADVERSARIAL CHALLENGE COMPLETE.

---

## PHASE 3: DETERMINATION

Having issued the adversarial challenge and RECORD DIAGNOSIS, issue the determination.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the Phase 1
signals establish as a whole. Address the Phase 2 challenge. Address the RECORD DIAGNOSIS
arrow chain: does the failure mode named in the chain apply to this output, or has it been
avoided? DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is not a
hedge.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it? The RECORD DIAGNOSIS arrow
chain should inform the confidence ceiling: reference the chain if the diagnosed risk is
live -- e.g., "convergence_pattern: thin -> failure mode: false confidence ceiling limits
this score to X."]

### DETERMINATION GATE
- NOT: DETERMINATION: is absent from the opening sentence -- register word must commit
  before reasoning follows. Positive condition: DETERMINATION: [YES/NO/MAYBE] opens the
  judgment paragraph.
- NOT: judgment paragraph ignores the Phase 2 RECORD DIAGNOSIS arrow chain. Positive
  condition: RECORD DIAGNOSIS chain referenced in the judgment or confidence paragraph.
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
inventory_schema_produced (true/false), schema_arrow_chain_in_diagnosis (true/false --
true if RECORD DIAGNOSIS uses field:value -> notation with at least two INVENTORY SCHEMA
fields and exact values; false if diagnosis describes schema values in prose without
arrow-chain syntax).
```

---

## V-03: PRE-FLIGHT Three-Phase Schema-Citation Audit

**Axis**: Role sequence -- PRE-FLIGHT expanded to three named audit phases between ADVERSARY COMPLETE and JUDGE: (A) structural completeness, (B) SCHEMA-CITATION AUDIT, (C) register-word gate; schema-citation audit is a named structural phase distinct from the register-word gate
**Hypothesis**: C-25 extended beyond a single register-word gate: the PRE-FLIGHT structural audit should verify diagnosis quality (schema-citation) as an independent phase step. R5 V-03 PRE-FLIGHT had structural completeness and register-word gate. V-03 adds a SCHEMA-CITATION AUDIT as the middle phase: locate INVENTORY SCHEMA fields cited in RECORD DIAGNOSIS and verify exact values match before the register-word gate runs. This separates diagnostic quality verification from commitment-format verification -- two distinct audit concerns, each a named phase. V7 candidate: does SCHEMA-CITATION AUDIT as a named PRE-FLIGHT phase constitute a criterion beyond C-25? Single-axis: three-phase PRE-FLIGHT with schema audit as new named middle phase. R5 V-03 base (role labels + explicit prohibition statements C-16, PRE-FLIGHT block C-22/C-25, standard adversarial challenge, no frontmatter at open C-19/C-20); INVENTORY SCHEMA added as necessary dependency for Phase B audit.

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
about signal quality or significance. Evaluative language in the SURVEYOR phase is a
procedural breach regardless of its accuracy.

Glob simulations/prove/investigations/{topic}-*. For each signal found, write one sentence:
name the artifact, state what it investigated, state what it found. If no signals: stop.
State: "INCOMPLETE RECORD -- no signals found for {topic}. Determination cannot proceed."

After recording all signals, produce the INVENTORY SCHEMA. The schema provides named
fields for the PRE-FLIGHT SCHEMA-CITATION AUDIT in Phase B; without the schema, the audit
cannot run.

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
  support the PRE-FLIGHT SCHEMA-CITATION AUDIT. Positive condition: all five fields filled.
- NOT: record count omitted. Positive condition: signal_count stated in schema.

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

[Paragraph 1. What is the weakest point in the SURVEYOR record? Reference the INVENTORY
SCHEMA: if convergence_pattern is thin or conflicting, name why that pattern matters for
this hypothesis specifically. If signals are thin (N < 3), name what type is absent and
why the absence matters.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty. What specific
condition would prevent a clear YES or NO from being defensible?]

**RECORD DIAGNOSIS**

[State the failure mode most likely for this specific synthesis, derived from the
INVENTORY SCHEMA field values. Name at least two INVENTORY SCHEMA fields by name and
state their exact values as the basis for the diagnosis. The diagnosis must cite specific
INVENTORY SCHEMA fields and their values -- not generic synthesis failure modes. State
the causal link: why do these specific field values produce this failure mode for this
hypothesis.]

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic -- a declaration that the ADVERSARY did
  not run is not a challenge. Positive condition: at least two paragraphs name specific
  record vulnerabilities.
- NOT: ADVERSARY phase contains advocacy supporting the hypothesis -- advocacy is a role
  breach. Positive condition: all content challenges the hypothesis or the record.
- NOT: RECORD DIAGNOSIS names a failure mode without citing INVENTORY SCHEMA field names
  and values as basis. Positive condition: at least two field names appear with their exact
  schema values, with a stated causal link.
- NOT: source of each adversarial argument is omitted. Positive condition: each challenge
  paragraph sourced to a specific gap or unconsidered scenario.

ADVERSARY COMPLETE.

---

## PRE-JUDGE PRE-FLIGHT

This block is a three-phase structural audit. It is a gate, not prose. Each phase must
clear before the next begins. This block runs in full before any JUDGE content is written.

**PHASE A: STRUCTURAL COMPLETENESS**
[ ] ADVERSARY phase is written and ADVERSARY COMPLETE appears above.
[ ] At least two adversarial challenge paragraphs are present above.
[ ] RECORD DIAGNOSIS appears in the ADVERSARY section.
[ ] No DETERMINATION language appears anywhere above this point.

PHASE A CLEARED.

**PHASE B: SCHEMA-CITATION AUDIT**

This phase verifies that RECORD DIAGNOSIS cited INVENTORY SCHEMA fields by name and value.
Locate the INVENTORY SCHEMA in the SURVEYOR section. Run the audit:

[ ] Identify the first INVENTORY SCHEMA field name cited in RECORD DIAGNOSIS. Locate that
    field name in the INVENTORY SCHEMA above. Confirm the value cited in RECORD DIAGNOSIS
    matches the INVENTORY SCHEMA value exactly.
[ ] Identify the second INVENTORY SCHEMA field name cited in RECORD DIAGNOSIS. Confirm the
    value matches exactly.

NOT: SCHEMA-CITATION AUDIT skipped because RECORD DIAGNOSIS reads as record-specific --
the audit exists to catch diagnoses that sound specific but paraphrase the schema without
citing field names and values. A diagnosis that does not name INVENTORY SCHEMA fields
cannot be verified in a single lookup regardless of how specific it appears.

NOT: SCHEMA-CITATION AUDIT deferred to post-JUDGE review -- the audit is a pre-JUDGE
phase; deferring it makes the schema-citation check retroactive, not pre-committed.

Positive condition: both cited fields are located by name in INVENTORY SCHEMA and both
cited values match exactly. If either check fails: return to ADVERSARY section and restate
RECORD DIAGNOSIS with correctly cited field names and exact values before proceeding.

PHASE B CLEARED.

**PHASE C: REGISTER-WORD GATE**
(read before writing the commitment sentence)

NOT: the commitment sentence begins with any word other than the register word.
"Our final DETERMINATION is:" violates this gate before you write it.
"Based on the foregoing, DETERMINATION:" violates this gate before you write it.
"The evidence supports a DETERMINATION of:" violates this gate before you write it.

This prohibition is stated here -- before the JUDGE section begins -- so that it is
encountered before the failure mode can occur. NOT: this gate appears after the commitment
sentence -- a gate that names the failure mode at the commitment point cannot prevent the
failure mode from occurring before it is reached.

Positive condition: the commitment sentence begins DETERMINATION: [YES/NO/MAYBE] with
DETERMINATION as the syntactically first word.

PHASE C CLEARED. PRE-FLIGHT CLEARED. Proceed to JUDGE.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer to signal ambiguity. Hedging
in the JUDGE phase is a procedural breach. The JUDGE issues a determination against the
ADVERSARY's pre-recorded challenge.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record
establishes as a whole. Address the ADVERSARY's challenge: does it reduce confidence,
cap it, or fail to move the answer? Address the RECORD DIAGNOSIS: does the diagnosed
failure mode apply to this output, or has it been avoided? DETERMINATION: MAYBE requires
naming the specific uncertainty. MAYBE is not a hedge; it is a committed uncertainty with
a named resolution condition.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it -- signal gaps, the
ADVERSARY challenge, or the RECORD DIAGNOSIS risk? High confidence (>= 75): name
converging signals and explain why convergence matters beyond mere agreement. Low
confidence (<= 40): name the specific gap or conflict.]

### DETERMINATION SEAL
- NOT: judgment paragraph fails to address the ADVERSARY's challenge -- the challenge was
  issued; the JUDGE must weigh it explicitly. Positive condition: ADVERSARY challenge
  referenced and weighed.
- NOT: judgment paragraph ignores the RECORD DIAGNOSIS -- the failure mode was named; the
  JUDGE must state whether it applies. Positive condition: RECORD DIAGNOSIS referenced.
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
why does that carry greater weight toward the DETERMINATION? Answer the comparative
question: why primary over secondary specifically?]

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
PRE-JUDGE PRE-FLIGHT block appears between ADVERSARY COMPLETE and JUDGE with all three
phases A/B/C present and cleared), schema_citation_audit_passed (true/false -- true if
PHASE B confirmed both cited field values match INVENTORY SCHEMA exactly; false if audit
deferred, skipped, or either value mismatched).
```

---

## V-04: Named Violation Categories + Arrow-Chain Diagnosis (Combo)

**Axes**: Named violation categories at phase-boundary attestations (C-23 sharpened, without frontmatter at open) + arrow-chain field:value RECORD DIAGNOSIS (C-24 sharpened). C-22 at DETERMINATION SEAL level. R5 V-04 base (role prohibitions C-16, INVENTORY SCHEMA C-21, structured RECORD DIAGNOSIS C-17, register-word C-18, no frontmatter at open C-19, phase-boundary attestations C-20).
**Hypothesis**: C-23 and C-24 compose without C-19. Without frontmatter-at-open, named violation categories appear at phase exits: "Advancing to ADVERSARY without signal_count set is a PHASE-ADVANCE VIOLATION." The INVENTORY SCHEMA provides named fields for the arrow-chain diagnosis. Calibration: do named violation categories in phase-boundary attestations (without a frontmatter compliance ledger) represent the same strength of C-23 as violation categories in a frontmatter block? Does arrow-chain diagnosis hold C-24 quality in role-labeled sections?

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
  support an arrow-chain diagnosis. Positive condition: all five schema fields are filled.
- NOT: record count omitted. Positive condition: signal_count stated in schema.
- NOT: signal_count set in frontmatter remains unfilled after this gate clears. Positive
  condition: signal_count set in frontmatter before ADVERSARY begins.

SURVEYOR COMPLETE.
Advancing to ADVERSARY without signal_count set in frontmatter is a PHASE-ADVANCE
VIOLATION. Named violation type: PHASE-ADVANCE VIOLATION.
Advancing to ADVERSARY without INVENTORY SCHEMA complete is a PHASE-ADVANCE VIOLATION.

---

## ADVERSARY: PRE-DETERMINATION CHALLENGE

An ADVERSARY challenges. An ADVERSARY does not advocate for the hypothesis, surface
supporting evidence, or assist the JUDGE. Advocacy in the ADVERSARY phase is a procedural
breach. The ADVERSARY's sole function is to assemble the strongest case against the
hypothesis before the JUDGE rules.

NOT: this section is placed after the DETERMINATION -- counter-evidence selected post-
verdict is selection bias. This section runs before the JUDGE phase. A DETERMINATION
issued without a prior ADVERSARY challenge is procedurally incomplete. Set
adversary_pre_determination: true in frontmatter now.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Reference the INVENTORY
SCHEMA: if convergence_pattern is thin or conflicting, name why that pattern matters for
this hypothesis specifically.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty. What specific
condition would need to be true for a confident YES or NO to be indefensible?]

**RECORD DIAGNOSIS**

NOT: the RECORD DIAGNOSIS describes INVENTORY SCHEMA values in prose without arrow-chain
notation -- prose description is evaluable but not falsifiable in one lookup.

NOT: the RECORD DIAGNOSIS uses bracket placeholder syntax ("[INVENTORY SCHEMA field: exact
value]") that when filled produces prose -- a filled placeholder is prose.

NOT: the RECORD DIAGNOSIS cites only one INVENTORY SCHEMA field. Positive condition: at
least two INVENTORY SCHEMA field names appear in the diagnosis chain with exact values.

State the RECORD DIAGNOSIS in arrow-chain form:
"RECORD DIAGNOSIS: [INVENTORY SCHEMA field]: [exact value] -> failure mode: [specific
failure mode]; [INVENTORY SCHEMA field]: [exact value] -> exposure: [why this schema
value creates this risk for this hypothesis specifically]."

Positive condition: a reader verifies each arrow step by (a) locating the cited field name
in INVENTORY SCHEMA, (b) confirming the cited value matches exactly, (c) judging whether
the arrow produces a plausible consequence. One lookup per field.

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic -- named record vulnerabilities required.
  Positive condition: at least two paragraphs name specific record vulnerabilities.
- NOT: RECORD DIAGNOSIS uses prose without arrow-chain notation. Positive condition:
  RECORD DIAGNOSIS expressed as field:value -> consequence chain with at least two fields.
- NOT: RECORD DIAGNOSIS names a failure mode without citing exact INVENTORY SCHEMA values
  in the chain. Positive condition: exact values appear in the arrow chain.
- NOT: ADVERSARY phase contains advocacy language -- advocacy is a role breach. Positive
  condition: all content challenges the hypothesis or the record.

ADVERSARY COMPLETE.
Advancing to JUDGE without adversary_pre_determination set true in frontmatter is a
PHASE-ADVANCE VIOLATION. Named violation type: PHASE-ADVANCE VIOLATION.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer. Hedging in the JUDGE phase
is a procedural breach. The JUDGE issues a determination against both the ADVERSARY's
challenge and the RECORD DIAGNOSIS arrow chain.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Issue a determination of what the record
establishes as a whole. Address the ADVERSARY's challenge. Address the RECORD DIAGNOSIS
arrow chain: does the failure mode named in the chain apply to this output, or has it been
avoided? DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is not a
hedge.]

**CONFIDENCE: [N]/100**

[Confidence paragraph. What drove this number? What capped it? The RECORD DIAGNOSIS arrow
chain informs the confidence ceiling: reference the chain if the diagnosed risk is live.]

### DETERMINATION SEAL
- NOT: the register word appears after introductory language ("Our final DETERMINATION
  is:", "Based on the foregoing, DETERMINATION:") -- a register word not first in its
  sentence allows hedging to precede the commitment point. Positive condition:
  DETERMINATION: is the first word of the commitment sentence.
- NOT: judgment paragraph fails to address the ADVERSARY's pre-determination challenge.
  Positive condition: ADVERSARY challenge referenced and weighed.
- NOT: judgment paragraph fails to address the RECORD DIAGNOSIS arrow chain -- the failure
  mode was named; the JUDGE must state whether it applies. Positive condition: RECORD
  DIAGNOSIS chain referenced in judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph. Positive condition: rationale
  paragraph follows the score and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition. Positive condition: MAYBE names the uncertainty.

DETERMINATION SEALED.
Advancing to ADVOCATE without determination_sealed set true in frontmatter is a
PHASE-ADVANCE VIOLATION. Named violation type: PHASE-ADVANCE VIOLATION.

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
inventory_schema_produced (true/false), schema_arrow_chain_in_diagnosis (true/false --
true if RECORD DIAGNOSIS uses field:value -> notation with at least two INVENTORY SCHEMA
fields and exact values; false if prose without arrow-chain syntax),
violation_categories_named (true/false -- true if every phase-boundary attestation names
the violation type; false if any attestation uses only NOT: without naming the category).
```

---

## V-05: Full Combo -- C-23 + C-24 + C-25 Extended + R5 V-05 Inheritance

**Axes**: Named violation categories on all frontmatter field bounds (C-23 sharpened) + arrow-chain field:value RECORD DIAGNOSIS (C-24 sharpened) + PRE-FLIGHT with three-phase structural audit including SCHEMA-CITATION AUDIT as named middle phase (C-25 extended). Complete R5 V-05 inheritance: role prohibitions (C-16), structured RECORD DIAGNOSIS (C-17), register-word-first format (C-18), frontmatter at open (C-19), phase-sequenced filling (C-20), SURVEYOR-traceable diagnosis (C-21), dual-layer register-word enforcement (C-22).
**Hypothesis**: The three sharpening mechanisms are mutually reinforcing. Named violation categories (C-23) convert prohibition statements to citable types, making the frontmatter compliance ledger auditable by violation class. Arrow-chain notation (C-24) converts the RECORD DIAGNOSIS from evaluable to falsifiable in one lookup, enabling the PRE-FLIGHT SCHEMA-CITATION AUDIT to verify chain syntax as a structural pre-condition. Three-phase PRE-FLIGHT (C-25 extended) sequences structural completeness, schema citation, and register-word placement in that order before JUDGE begins. Together: INVENTORY SCHEMA creates addressable named fields; named violation categories create addressable failure types; arrow-chain diagnosis creates a verification path; three-phase PRE-FLIGHT clears all three pre-commitment checks as a structural sequence. V7 candidates: C-26 (violation registry at document open), C-27 (arrow-chain propagates from RECORD DIAGNOSIS through PRE-FLIGHT audit through JUDGE confidence reference -- three-site chain of custody).

```
You are running prove:synthesize for {topic}. Issue a formal determination. This document
stands alone: a reader with no access to the investigation signals must understand the
determination, the evidence basis, the pre-determination challenge, and what to do next
from this document alone. State this mandate in your opening paragraph.

Role assignments govern output type in this synthesis. Each phase is assigned a procedural
identity that forecloses what that phase may produce. Violating a role assignment is a
procedural breach, not a style deviation. The adversary declares before the judge rules.
Write argumentative sections in prose paragraphs, not tables or bullet lists.

Open the artifact with the following FRONTMATTER DECLARATIONS block. Each field carries a
fill window with named violation types. Named violation types in this artifact:
  PREMATURE COMPLETION VIOLATION -- field filled before its phase window opens.
  DEFERRED COMPLETION VIOLATION -- field filled after its phase window closes.
  PHASE-ADVANCE VIOLATION -- advancing to next phase without required fields set.
  FALSE ATTESTATION VIOLATION -- boolean set true when pass condition is not met.
Violation types are citable labels: a reviewer states the type, the field, and the
structural moment -- a complete finding requiring no further reading.

---

FRONTMATTER DECLARATIONS (open the artifact here):

  skill: prove-synthesize
  topic: {topic}
  date: {date}

  signal_count: [fill after SURVEYOR COMPLETE, before ADVERSARY begins]
  Filling signal_count before any SURVEYOR content is written is a PREMATURE COMPLETION
  VIOLATION. Filling signal_count after ADVERSARY content begins is a DEFERRED COMPLETION
  VIOLATION.

  adversary_pre_determination: [true if ADVERSARY ran structurally before JUDGE; false otherwise]
  Filling adversary_pre_determination before ADVERSARY content is written is a PREMATURE
  COMPLETION VIOLATION. Filling adversary_pre_determination after JUDGE content begins is
  a DEFERRED COMPLETION VIOLATION.

  answer: [fill after DETERMINATION: line is written]
  Filling answer before DETERMINATION: line is written is a PREMATURE COMPLETION VIOLATION.
  Filling answer after DETERMINATION SEALED appears is a DEFERRED COMPLETION VIOLATION.

  confidence: [fill after CONFIDENCE: notation is written]
  Filling confidence before CONFIDENCE: notation is written is a PREMATURE COMPLETION
  VIOLATION.

  register_word_used: [true if DETERMINATION: is the syntactically first word of the
                       commitment sentence; false otherwise]
  Filling register_word_used before DETERMINATION: line is written is a PREMATURE
  COMPLETION VIOLATION.

  not_first_gates: [true if every gate item in this artifact opens with NOT:]
  Filling not_first_gates before all gate sections are written is a PREMATURE COMPLETION
  VIOLATION. Setting not_first_gates: true when any gate item does not open with NOT: is
  a FALSE ATTESTATION VIOLATION.

  record_specific_antipattern: [true if RECORD DIAGNOSIS arrow chain cited INVENTORY
                                SCHEMA fields with exact values; false if diagnosis used
                                prose without arrow-chain notation]
  Filling record_specific_antipattern before ADVERSARY COMPLETE is a PREMATURE COMPLETION
  VIOLATION. Setting record_specific_antipattern: true when the diagnosis does not use
  arrow-chain notation is a FALSE ATTESTATION VIOLATION.

  role_foreclusion_explicit: [true if each role section states what the role cannot produce]
  Setting role_foreclusion_explicit: true when any role section lacks explicit prohibition
  statements is a FALSE ATTESTATION VIOLATION.

  preflight_confirmed: [true if PRE-JUDGE PRE-FLIGHT block with all three phases A/B/C
                        appears before JUDGE section and all phases cleared]
  Filling preflight_confirmed before PRE-JUDGE PRE-FLIGHT block is written is a PREMATURE
  COMPLETION VIOLATION.

  schema_arrow_chain_in_diagnosis: [true if RECORD DIAGNOSIS uses field:value -> notation
                                    with at least two INVENTORY SCHEMA fields and exact
                                    values; false if diagnosis describes schema in prose]
  Filling schema_arrow_chain_in_diagnosis before ADVERSARY COMPLETE is a PREMATURE
  COMPLETION VIOLATION. Setting schema_arrow_chain_in_diagnosis: true when the diagnosis
  does not use arrow-chain notation is a FALSE ATTESTATION VIOLATION.

  schema_citation_audit_passed: [true if PRE-FLIGHT PHASE B confirmed both cited field
                                  values match INVENTORY SCHEMA exactly; false if audit
                                  deferred, skipped, or found a mismatch]
  Filling schema_citation_audit_passed before PRE-FLIGHT PHASE B clears is a PREMATURE
  COMPLETION VIOLATION. Setting schema_citation_audit_passed: true without running PHASE B
  is a FALSE ATTESTATION VIOLATION.

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
The schema creates addressable named vocabulary propagating from SURVEYOR to RECORD
DIAGNOSIS arrow chains, PRE-FLIGHT PHASE B audit, JUDGE confidence calibration, and the
schema_arrow_chain_in_diagnosis and schema_citation_audit_passed frontmatter booleans.

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
  support the PRE-FLIGHT PHASE B SCHEMA-CITATION AUDIT. Positive condition: all five
  fields filled.
- NOT: signal_count in frontmatter remains unfilled after this gate clears. Filling
  signal_count after ADVERSARY content begins is a DEFERRED COMPLETION VIOLATION.
  Positive condition: signal_count set before ADVERSARY begins.

SURVEYOR COMPLETE. Set signal_count: [N] in frontmatter now.
Advancing to ADVERSARY without signal_count set is a PHASE-ADVANCE VIOLATION.
Advancing to ADVERSARY without INVENTORY SCHEMA complete is a PHASE-ADVANCE VIOLATION.

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
Filling adversary_pre_determination after JUDGE content begins is a DEFERRED COMPLETION
VIOLATION.

[Paragraph 1. What is the weakest point in the SURVEYOR record? Reference the INVENTORY
SCHEMA: if convergence_pattern is thin or conflicting, name why that pattern matters for
this hypothesis specifically. If signals are thin (N < 3), name what type is absent and
why the absence matters.]

[Paragraph 2. What is the strongest argument that the answer should be MAYBE even if
signals lean YES or NO? State the adversary's best case for uncertainty. What specific
condition would need to be true for a confident YES or NO to be indefensible?]

**RECORD DIAGNOSIS**

NOT: the RECORD DIAGNOSIS describes INVENTORY SCHEMA values in prose without arrow-chain
notation -- prose description is evaluable but not falsifiable in one lookup.

NOT: the RECORD DIAGNOSIS uses bracket placeholder syntax ("[INVENTORY SCHEMA field: exact
value]") that when filled produces prose -- a filled placeholder is prose, not a lookup
path.

NOT: the RECORD DIAGNOSIS cites only one INVENTORY SCHEMA field -- a single-field chain
does not distinguish record-specific from generic diagnosis.

State the RECORD DIAGNOSIS in arrow-chain form:
"RECORD DIAGNOSIS: [INVENTORY SCHEMA field]: [exact value from INVENTORY SCHEMA] ->
failure mode: [specific failure mode]; [INVENTORY SCHEMA field]: [exact value] ->
exposure: [why this schema value creates this risk for this hypothesis specifically]."

Arrow-chain verification: for each field, (a) locate the field name in INVENTORY SCHEMA,
(b) confirm the cited value matches exactly, (c) judge whether the arrow produces a
plausible consequence. One lookup per field. A diagnosis is falsified if any cited value
differs from the INVENTORY SCHEMA.

Set schema_arrow_chain_in_diagnosis: true in frontmatter if at least two INVENTORY SCHEMA
field names appear in arrow-chain notation with their exact values; false if prose.

### ADVERSARY GATE
- NOT: adversarial challenge is absent or generic -- a declaration that the ADVERSARY did
  not run is not a challenge. Positive condition: at least two paragraphs name specific
  record vulnerabilities.
- NOT: RECORD DIAGNOSIS uses prose without arrow-chain notation. Positive condition:
  RECORD DIAGNOSIS expressed as field:value -> consequence chain with at least two fields
  and exact values.
- NOT: RECORD DIAGNOSIS names a failure mode without explaining why the cited schema values
  produce it for this hypothesis. Positive condition: causal link stated in the chain.
- NOT: ADVERSARY phase contains advocacy language -- advocacy is a role breach. Positive
  condition: all content challenges the hypothesis or the record.

ADVERSARY COMPLETE.
Advancing to PRE-FLIGHT without adversary_pre_determination set true is a PHASE-ADVANCE
VIOLATION. Named violation type: PHASE-ADVANCE VIOLATION.

---

## PRE-JUDGE PRE-FLIGHT

This block is a three-phase structural audit. It is a gate, not prose. Each phase must
clear before the next begins. This block runs in full before any JUDGE content is written.

NOT: this pre-flight block is skipped because the preceding sections appear complete --
the block exists to catch structural violations that read as complete. Skipping this block
is a PHASE-ADVANCE VIOLATION. Named violation type: PHASE-ADVANCE VIOLATION.

**PHASE A: STRUCTURAL COMPLETENESS**
[ ] ADVERSARY phase is written and ADVERSARY COMPLETE appears above.
[ ] adversary_pre_determination is set true in frontmatter.
[ ] At least two adversarial challenge paragraphs are present above.
[ ] RECORD DIAGNOSIS appears in the ADVERSARY section.
[ ] No DETERMINATION language appears anywhere above this point.

PHASE A CLEARED.

**PHASE B: SCHEMA-CITATION AUDIT**

This phase verifies that RECORD DIAGNOSIS used arrow-chain notation with correctly cited
INVENTORY SCHEMA values. Locate the INVENTORY SCHEMA in the SURVEYOR section. Audit:

[ ] Identify the first INVENTORY SCHEMA field name cited in RECORD DIAGNOSIS arrow chain.
    Locate that field name in INVENTORY SCHEMA above. Confirm the value cited in the arrow
    chain matches INVENTORY SCHEMA exactly.
[ ] Identify the second INVENTORY SCHEMA field name cited in RECORD DIAGNOSIS arrow chain.
    Confirm the value matches INVENTORY SCHEMA exactly.

NOT: SCHEMA-CITATION AUDIT skipped because RECORD DIAGNOSIS reads as record-specific --
the audit exists to catch diagnoses that sound specific but paraphrase the schema without
arrow-chain notation. A diagnosis that does not use arrow-chain syntax fails this audit
regardless of how specific it appears.

NOT: SCHEMA-CITATION AUDIT deferred until after JUDGE -- a post-commitment audit is
retroactive, not pre-committed. Deferring this audit is a PHASE-ADVANCE VIOLATION on
schema_citation_audit_passed.

Positive condition: both cited fields are located by name in INVENTORY SCHEMA and both
cited values match exactly. If either fails: return to ADVERSARY and restate RECORD
DIAGNOSIS with correct field names and exact values before proceeding.

Set schema_citation_audit_passed: true in frontmatter now.

PHASE B CLEARED.

**PHASE C: REGISTER-WORD GATE**
(read before writing the commitment sentence)

NOT: the commitment sentence begins with any word other than the register word.
"Our final DETERMINATION is:" violates this gate before you write it.
"Based on the foregoing, DETERMINATION:" violates this gate before you write it.
"The record supports a DETERMINATION of:" violates this gate before you write it.
"Having reviewed the evidence, DETERMINATION:" violates this gate before you write it.

This prohibition is stated here -- before the JUDGE section begins -- so it is encountered
before the failure mode can occur. NOT: this gate appears after the commitment sentence --
a gate named at the commitment point has been passed before it is encountered.

Positive condition: the commitment sentence begins DETERMINATION: [YES/NO/MAYBE] with
DETERMINATION as the syntactically first word.

PHASE C CLEARED.

Set preflight_confirmed: true in frontmatter now.
PRE-FLIGHT CLEARED. Proceed to JUDGE.

---

## JUDGE: DETERMINATION

A JUDGE rules. A JUDGE does not hedge, equivocate, or defer to signal ambiguity. Hedging
or equivocation in the JUDGE phase is a procedural breach. The JUDGE issues a
determination against both the ADVERSARY's challenge and the RECORD DIAGNOSIS arrow chain.

**DETERMINATION: [YES / NO / MAYBE]**

[Open with DETERMINATION: and the answer word. Set register_word_used: true in frontmatter
now. Issue a determination of what the record establishes as a whole. Address the
ADVERSARY's challenge: does it reduce confidence, cap it, or fail to move the
determination? Address the RECORD DIAGNOSIS arrow chain: does the failure mode named in
the chain apply to this output, or has it been avoided? Reference the chain notation if
the risk is live. DETERMINATION: MAYBE requires naming the specific uncertainty. MAYBE is
not a hedge; it is a committed uncertainty with a named resolution condition.]

**CONFIDENCE: [N]/100** -- set confidence and answer in frontmatter now.
Filling confidence before CONFIDENCE: notation is written is a PREMATURE COMPLETION
VIOLATION.

[Confidence paragraph. What drove this number? What capped it? Reference the RECORD
DIAGNOSIS arrow chain if the diagnosed risk is live -- e.g., "convergence_pattern: thin
-> failure mode: false confidence ceiling limits this score." High confidence (>= 75):
name converging signals and explain why convergence matters beyond mere agreement.
Low confidence (<= 40): name the specific gap or conflict.]

### DETERMINATION SEAL
- NOT: the register word appears after introductory language ("Our final DETERMINATION
  is:", "Based on the foregoing, DETERMINATION:") -- a register word not first in its
  sentence allows hedging to precede the commitment point. Positive condition:
  DETERMINATION: is the first word of the commitment sentence. Set register_word_used:
  false in frontmatter if this condition is not met.
- NOT: judgment paragraph fails to address the ADVERSARY's pre-determination challenge --
  the challenge was issued; the JUDGE must weigh it explicitly. Positive condition:
  ADVERSARY challenge referenced and weighed.
- NOT: judgment paragraph fails to address the RECORD DIAGNOSIS arrow chain -- the failure
  mode was named; the JUDGE must state whether it applies. Positive condition: RECORD
  DIAGNOSIS chain referenced in judgment or confidence paragraph.
- NOT: CONFIDENCE notation lacks a rationale paragraph. Positive condition: rationale
  paragraph follows the score and explains what drove it and what capped it.
- NOT: DETERMINATION: MAYBE appears without naming a specific uncertainty and a resolution
  condition -- MAYBE as a hedge is a judicial breach. Positive condition: MAYBE names the
  uncertainty and the condition under which it resolves to YES or NO.
- NOT: answer and confidence in frontmatter remain unfilled after this gate. Filling after
  this gate is a DEFERRED COMPLETION VIOLATION. Positive condition: both set now.

DETERMINATION SEALED.
Advancing to ADVOCATE without determination_sealed set true is a PHASE-ADVANCE VIOLATION.
Named violation type: PHASE-ADVANCE VIOLATION.

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
its items with NOT:; false if any gate item opens otherwise. Setting not_first_gates: true
when any gate item does not open with NOT: is a FALSE ATTESTATION VIOLATION.

---

Write artifact: simulations/prove/investigations/{topic}-synthesis-{date}.md
The FRONTMATTER DECLARATIONS block at document open is part of the artifact. Named
violation types (PREMATURE COMPLETION VIOLATION, DEFERRED COMPLETION VIOLATION, PHASE-
ADVANCE VIOLATION, FALSE ATTESTATION VIOLATION) are citable labels. All boolean fields
carry their named violation statements and must be set at their declared phase gates.
The frontmatter is a compliance record, not formatting metadata.

Verify before finalizing:
- All fill-window bounds in FRONTMATTER state named violation types for both premature and
  deferred fill at each field (where applicable).
- INVENTORY SCHEMA produced by SURVEYOR with all five fields filled.
- RECORD DIAGNOSIS uses arrow-chain notation with at least two INVENTORY SCHEMA fields
  and exact values. Not prose description. Not bracket placeholders.
- PRE-FLIGHT three-phase block (A/B/C) appears between ADVERSARY COMPLETE and JUDGE.
- PHASE B SCHEMA-CITATION AUDIT confirmed both cited field values match INVENTORY SCHEMA.
- preflight_confirmed and schema_citation_audit_passed set true at PRE-FLIGHT CLEARED.
- schema_arrow_chain_in_diagnosis: true only if arrow-chain notation present with exact
  values; false if prose description used.
- All PHASE-ADVANCE VIOLATION statements name the violation type explicitly.
```
