# prove-interview — Skill Body Variations — R16

**Skill:** prove-interview
**Round:** 16
**Rubric version:** v14
**Date:** 2026-03-15

---

## R16 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|---|---|---|---|
| V-01 | Single | Document-head contract with 4 numbered sub-schemas (C-33 target) | Declaring SECTION 0 with sub-schemas 0.1–0.4 before any phase begins makes the head contract a resolvable pointer target rather than a flat declaration block; any downstream phase that derives its format from SECTION 0 satisfies C-33 structurally rather than authorialy |
| V-02 | Single | Downstream sub-schema citation: phase gates name "per 0.N schema" as their contract authority (approaching C-35) | When phase exit gates close checklist items with explicit numbered citations ("— per 0.2 evidence schema", "— per 0.3 moment-label format"), the gate's completion conditions become traceable pointers to the document-level authority rather than self-asserted format claims |
| V-03 | Single | C-36 framework dimension column — evidence table maps each item to INERTIA PROFILE framework dimension | When the INERTIA PROFILE TABLE is elevated to a named subject framework with discrete labeled dimensions and Phase 3's evidence table adds an explicit FRAMEWORK DIMENSION column, C-36's declaration-enforcement closure is met: the framework is opened in setup and closed in extraction |
| V-04 | Combined | Document-head numbered sub-schemas + downstream sub-schema citation (C-33 + C-35 approach) | Combining SECTION 0 numbered sub-schemas with downstream gate citations creates a two-layer contract chain: head declares authority (C-33 satisfied); gates cite which sub-schema governs them (C-35 approached); each layer is independently auditable |
| V-05 | Combined | Full R16 apparatus: numbered sub-schemas + downstream citation + C-36 framework dimension + C-37 dual-source moment labels + C-41 vocabulary in gate scope | When all R16 innovations operate simultaneously — SECTION 0 with 0.1–0.4 (C-33), gates cite "per 0.N" (C-35 approach), Phase 3 carries FRAMEWORK DIMENSION column (C-36), 0.3 template bridges both Expectation Register and framework as named sources (C-37), and framework vocabulary is gate-embedded in Phase 0A gate block (C-41) — the document achieves maximum structural audit depth through a single traceable citation chain |

Single-axis variations: V-01 (C-33 only), V-02 (downstream citation only), V-03 (C-36 only)
Combined variations: V-04 (C-33 + C-35 chain), V-05 (full apparatus)

New R16 territory probed:
- **SECTION 0 with numbered sub-schemas 0.1–0.4** (V-01, V-04, V-05): head declares gate format (0.1), evidence schema (0.2), moment-label format (0.3), subject schema (0.4); all phases derive from it
- **Phase gate items cite "— per 0.N schema"** (V-02, V-04, V-05): gates close with numbered sub-schema citations making the head contract a live navigation target, not just a preamble
- **Framework dimension column in evidence extraction** (V-03, V-05): INERTIA PROFILE elevated to named subject framework; Phase 3 table maps each item to STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL
- **Dual-source moment-label template** (V-05): 0.3 template names both Expectation Register and INERTIA PROFILE FRAMEWORK as valid "expected:" sources, closing C-37

---

## V-01 — Document-Head Contract with Numbered Sub-Schemas

**Variation axis:** Format contract — document-head with 4 numbered sub-schemas only
**Hypothesis:** Declaring SECTION 0 with four numbered sub-schemas (0.1 gate format, 0.2 evidence schema, 0.3 moment-label format, 0.4 subject schema) converts the head contract from a flat preamble into a navigable citation system. Downstream phases that reference "per 0.2 schema" are making pointers to a named, resolvable section rather than self-asserted format claims. This structural move makes C-33 fully satisfiable: enforcement is not per-section but per-head-contract. V-01 does not add downstream citation tags — the head exists but gates do not yet cite back to it.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## SECTION 0 — DOCUMENT-HEAD CONTRACT

This section declares all format contracts for this document. Every phase that follows derives
its format requirements from the numbered sub-schemas below. No phase may introduce a format
requirement not traceable to one of these sub-schemas.

### 0.1 GATE FORMAT CONTRACT

Every phase exit gate uses this named-block structure:

```
PHASE N EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: [specific out-of-scope content — named by category]
  REQUIRED:
    [ ] item one
    [ ] item two
    ...
```

Rules: PROHIBITED clause appears first. A gate without a named header fails 0.1.
A gate without a PROHIBITED clause fails 0.1.

### 0.2 EVIDENCE SCHEMA CONTRACT

Every Phase 3 evidence extraction table uses these columns in this order:

```
| # | Evidence text | Signal type | Strength | Rationale | Basis | Profile relevance |
```

Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
Strength: STRONG / MODERATE / WEAK (each requires a non-blank Rationale)
Basis: verbatim / inferred / corroborated
Profile relevance values: declared in Phase 0A gate (not here)

A table that omits any column or reorders columns fails 0.2.

### 0.3 MOMENT-LABEL FORMAT CONTRACT

Every Phase 2 moment label uses one of:

```
SURPRISING (expected: [Phase 0C prediction → tier name], got: [transcript content])
CONFIRMING (validates: [Phase 0C prediction → tier name])
INCONCLUSIVE (signal: [transcript content], ambiguity: [why direction is unclear])
```

Decision rules:
- SURPRISING: moment violates the Phase 0C prediction for this tier
- CONFIRMING: moment upholds the Phase 0C prediction for this tier
- INCONCLUSIVE: signal present but directionally ambiguous

A label without the parenthetical structure fails 0.3.
A label that omits the Phase 0C source fails 0.3.

### 0.4 SUBJECT SCHEMA CONTRACT

Every Phase 1 subject card declares these fields in this order:

```
ROLE:
PRIOR KNOWLEDGE:
  - Direct experience:
  - Knowledge gaps:
BLIND SPOTS: [specific domain or perspective gap — not generic]
DISPOSITION: [INCUMBENT / CHAMPION / EVALUATOR / SKEPTIC]
PRIMARY CONCERN:
VOCABULARY SIGNATURE: [term-1] | [term-2] | [term-3]
EVIDENTIAL FUNCTION: [structural role in the evidence chain — not a disposition restatement]
```

A card missing any field fails 0.4. BLIND SPOTS generic descriptors fail 0.4.

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice declare:
  - Practice name
  - Stickiness factor: the specific mechanism sustaining this practice (not generic — name the
    structural or behavioral mechanism, e.g., "24-month audit log retention tied to existing
    toolchain" not "familiarity")
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
  REQUIRED:
    [ ] INERTIA PROFILE TABLE has at least two practice rows
    [ ] Each row has a stickiness factor naming a specific mechanism
    [ ] PROFILE RELEVANCE vocabulary declared here for Phase 3 use:
        Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
        Each Phase 3 item must carry exactly one of these tags.
        Contract authority: this gate — not any tag list reproduced elsewhere.
    [ ] Gate block structure satisfies 0.1

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — evidence types and
cross-subject pattern. A level name alone is not a definition.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure satisfies 0.1

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
                INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent
              (level names may appear; definitions must not be restated)
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Non-overlapping regions across five levels
    [ ] Completing 0B-I does not pass this gate
    [ ] Gate block structure satisfies 0.1

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if order were reversed

For each tier declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

INCUMBENT anchor: names the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] Adjacency blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier predictions with all four fields
    [ ] INCUMBENT anchor names specific Phase 0A row and stickiness factor
    [ ] Gate block structure satisfies 0.1

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

Each card follows the 0.4 subject schema.
INCUMBENT card additionally carries: INCUMBENT designation label, Inertia anchor (exact match
to Phase 0C anchor, naming the specific Phase 0A row and stickiness factor).

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent
  REQUIRED:
    [ ] Four subject cards in tier sequence
    [ ] Each card satisfies the 0.4 subject schema (all fields, BLIND SPOTS non-generic)
    [ ] EVIDENTIAL FUNCTION non-blank and not a disposition restatement for all subjects
    [ ] INCUMBENT card: designation label + inertia anchor matching Phase 0C exactly
    [ ] Gate block structure satisfies 0.1

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's PRIMARY CONCERN
  - Write answers in the subject's distinct voice; vocabulary signature terms from 0.4 should
    appear naturally in the answers
  - Mark exactly one moment per subject using the 0.3 format, citing the Phase 0C per-tier
    prediction for that subject's tier

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: hypothesis question sections and synthesis content are absent
  REQUIRED:
    [ ] All four transcripts complete
    [ ] Each subject has exactly one moment labeled per 0.3 format
    [ ] Labels cite Phase 0C predictions by tier name
    [ ] Answers in distinct subject voices
    [ ] Vocabulary signature terms from 0.4 appear in each subject's answers
    [ ] Gate block structure satisfies 0.1

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables using the 0.2 evidence schema.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent
  REQUIRED:
    [ ] Tables use 0.2 schema column order and values
    [ ] PROFILE RELEVANCE tags from Phase 0A gate only
    [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
    [ ] Basis: verbatim / inferred / corroborated only
    [ ] Gate block structure satisfies 0.1

---

## PHASE 4 — SYNTHESIS

Produce in order: CROSS-PERSONA SYNTHESIS, DISPOSITION ARC, CONTRADICTION REGISTER,
EPISTEMIC RE-WEIGHTING, INERTIA PROFILE ACCOUNTING, PREDICTION DELTA, INERTIA/ADOPTION PARTITION.

Then produce NET VERDICT with VERDICT MARGIN AUDIT table (both boundary rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [level] / [level above] | [Phase 0B-II factor] | [named item] | [placement] |
    | Lower: [level below] / [level] | [Phase 0B-II factor] | [named item] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence not in Phase 3 is absent
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] Net verdict from Phase 0B-I defined levels
    [ ] VERDICT MARGIN AUDIT table has both boundary rows populated
    [ ] Prediction delta citations name specific Phase 3 items
    [ ] Gate block structure satisfies 0.1

---

## V-02 — Downstream Sub-Schema Citation ("per 0.N schema")

**Variation axis:** Phrasing register — phase gates cite numbered sub-schemas as authorization authority
**Hypothesis:** When each phase exit gate closes relevant checklist items with explicit numbered citations ("— per 0.1 gate format", "— per 0.2 evidence schema"), the gate completion condition becomes a traceable pointer to the document-level authority declared in any head contract. This is the mechanism C-35 requires: point-of-use confirmations name an authorization authority rather than self-asserting. V-02 tests the citation pattern without SECTION 0 — the cited authority is named inline at each gate rather than at document head. The contrast with V-04 (which adds SECTION 0) isolates whether the citation alone satisfies C-35 or whether C-35 requires both a head declaration and a citation.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice declare:
  - Practice name
  - Stickiness factor: specific mechanism (not a generic descriptor)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

Declare the GATE FORMAT CONTRACT before this gate:
  All phase exit gates in this document use this structure:
  PROHIBITED clause first, then REQUIRED checklist items.
  Gate items derived from a named contract end with "— per [contract name]".

Declare the EVIDENCE SCHEMA CONTRACT before Phase 3:
  Evidence tables use: | # | Evidence text | Signal type | Strength | Rationale | Basis | Profile relevance |
  Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  Strength: STRONG / MODERATE / WEAK  |  Basis: verbatim / inferred / corroborated

Declare the MOMENT-LABEL FORMAT CONTRACT before Phase 2:
  SURPRISING (expected: [Phase 0C prediction → tier], got: [transcript content])
  CONFIRMING (validates: [Phase 0C prediction → tier])
  INCONCLUSIVE (signal: [transcript content], ambiguity: [why unclear])
  Decision rules: SURPRISING = violated; CONFIRMING = upheld; INCONCLUSIVE = ambiguous.

Declare the SUBJECT SCHEMA CONTRACT before Phase 1:
  ROLE / PRIOR KNOWLEDGE (experience, gaps) / BLIND SPOTS / DISPOSITION / PRIMARY CONCERN /
  VOCABULARY SIGNATURE (3 terms) / EVIDENTIAL FUNCTION

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
  REQUIRED:
    [ ] INERTIA PROFILE TABLE has at least two practice rows
    [ ] Each row has a stickiness factor naming a specific mechanism
    [ ] PROFILE RELEVANCE vocabulary declared here: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
        Contract authority: this gate item — per PROFILE RELEVANCE VOCABULARY CONTRACT
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
                INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive definitions from 0B-I are absent (names only, not definitions)
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Non-overlapping regions across five levels
    [ ] Completing 0B-I does not pass this gate
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair declare an ADJACENCY block.
For each tier declare: expected evidence type, expected posture, confirming signal, surprising signal.
INCUMBENT anchor: names Phase 0A row and stickiness factor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] Adjacency blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier predictions with all four fields
    [ ] INCUMBENT anchor names specific Phase 0A row and stickiness factor
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

Each card follows the SUBJECT SCHEMA CONTRACT.
INCUMBENT card: add designation label, inertia anchor (exact match to Phase 0C anchor).

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent
  REQUIRED:
    [ ] Four subject cards in tier sequence — per SUBJECT SCHEMA CONTRACT
    [ ] Each card has all declared fields with non-generic BLIND SPOTS — per SUBJECT SCHEMA CONTRACT
    [ ] INCUMBENT: designation label + inertia anchor matching Phase 0C
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence.

For each subject: 4-6 questions anchored to PRIMARY CONCERN; answers in distinct voice;
vocabulary signature terms should appear naturally; exactly one moment labeled per MOMENT-LABEL
FORMAT CONTRACT, citing Phase 0C per-tier prediction.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: hypothesis questions and synthesis content are absent
  REQUIRED:
    [ ] All four transcripts complete
    [ ] Each subject: one moment labeled — per MOMENT-LABEL FORMAT CONTRACT
    [ ] Labels cite Phase 0C tier predictions — per MOMENT-LABEL FORMAT CONTRACT
    [ ] Answers in distinct subject voices; vocabulary signatures appear naturally
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables per EVIDENCE SCHEMA CONTRACT.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent
  REQUIRED:
    [ ] Tables use column order and values — per EVIDENCE SCHEMA CONTRACT
    [ ] PROFILE RELEVANCE tags from Phase 0A gate only — per PROFILE RELEVANCE VOCABULARY CONTRACT
    [ ] All STRENGTH ratings: non-blank, non-self-referential Rationale — per EVIDENCE SCHEMA CONTRACT
    [ ] Basis: verbatim / inferred / corroborated — per EVIDENCE SCHEMA CONTRACT
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## PHASE 4 — SYNTHESIS

Produce in order: CROSS-PERSONA SYNTHESIS, DISPOSITION ARC, CONTRADICTION REGISTER,
EPISTEMIC RE-WEIGHTING, INERTIA PROFILE ACCOUNTING, PREDICTION DELTA, INERTIA/ADOPTION PARTITION.

NET VERDICT with VERDICT MARGIN AUDIT table (both boundary rows required).

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence not in Phase 3 is absent
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] Net verdict from Phase 0B-I levels
    [ ] VERDICT MARGIN AUDIT table: both boundary rows populated
    [ ] Prediction delta cites specific Phase 3 items
    [ ] Gate block structure — per GATE FORMAT CONTRACT

---

## V-03 — C-36 Framework Dimension Column

**Variation axis:** Output format — evidence table maps each item to a declared INERTIA PROFILE framework dimension
**Hypothesis:** When the INERTIA PROFILE TABLE is elevated from a vocabulary source to a named subject framework with four discrete labeled dimensions, and Phase 3's evidence extraction table adds an explicit FRAMEWORK DIMENSION column, the declaration-enforcement loop required by C-36 closes. The INERTIA PROFILE's dimensions become a structural schema contract: every evidence item must declare which dimension it engages. V-03 does not add SECTION 0 (no numbered sub-schemas) — the framework is declared inline in Phase 0A and the column contract is stated before Phase 3.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE FRAMEWORK

Before designing any subject card, map the practices being displaced as a named framework
with four discrete labeled dimensions.

INERTIA PROFILE FRAMEWORK — declared dimensions:
  - STICKINESS: the mechanism sustaining the practice despite alternatives
  - LIMITATION: the constraint that blocks or slows displacement
  - DISPLACEMENT: the active transition away from the practice
  - EXTERNAL: a force outside the team or organization

For each practice, declare:
  - Practice name
  - Framework dimension (one of the four above)
  - Specific mechanism: the concrete driver (not a generic descriptor)
  - Switching cost or structural barrier

Produce a named table: INERTIA PROFILE FRAMEWORK TABLE with columns:
  | Practice | Framework dimension | Specific mechanism | Switching cost |

This framework is the named subject framework for Phase 3's FRAMEWORK DIMENSION column.
Each Phase 3 evidence item must declare which dimension it engages.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
  REQUIRED:
    [ ] INERTIA PROFILE FRAMEWORK TABLE has at least two practice rows
    [ ] Each row has a framework dimension from the four declared labels and a specific mechanism
    [ ] Framework vocabulary gate-declared here — only valid values for Phase 3 columns:
          STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
        Contract source: this gate item
    [ ] Gate block has named header and PROHIBITED clause

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive definitions from 0B-I are absent (level names only)
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Non-overlapping regions
    [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair declare an ADJACENCY block.
For each tier declare: expected evidence type, expected posture, confirming signal, surprising signal.
INCUMBENT anchor: names the specific Phase 0A framework row and dimension.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] Adjacency blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier predictions with all four fields
    [ ] INCUMBENT anchor names specific Phase 0A framework row and dimension

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (specific domain gap — not blank, not generic)
  - Disposition
  - Primary concern
  - Vocabulary signature: 2-3 role-specific terms
  - Evidential function: structural role in the evidence chain (not a disposition restatement)

INCUMBENT card additionally: designation label, inertia anchor (exact match to Phase 0C anchor).

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent
  REQUIRED:
    [ ] Four subject cards in tier sequence
    [ ] Each card has all declared fields; BLIND SPOTS non-generic; EVIDENTIAL FUNCTION structural
    [ ] INCUMBENT: designation label + inertia anchor matching Phase 0C

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence.

For each subject: 4-6 questions anchored to PRIMARY CONCERN; answers in distinct voice;
vocabulary signature terms should appear naturally; exactly one moment labeled:
  SURPRISING (expected: [Phase 0C prediction → tier], got: [transcript content])
  CONFIRMING (validates: [Phase 0C prediction → tier])
  INCONCLUSIVE (signal: [content], ambiguity: [why unclear])

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: hypothesis questions and synthesis content are absent
  REQUIRED:
    [ ] All four transcripts complete
    [ ] Each subject: one moment labeled; label cites Phase 0C prediction by tier name
    [ ] Answers in distinct voices; vocabulary terms appear naturally

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables with this schema:

```
| # | Evidence text | Signal type | Strength | Rationale | Basis | Framework dimension | Profile relevance |
```

Column contracts:
- Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
- Strength: STRONG / MODERATE / WEAK (each requires non-blank Rationale)
- Basis: verbatim / inferred / corroborated
- Framework dimension: STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL
  (from INERTIA PROFILE FRAMEWORK TABLE declared in Phase 0A)
  Each item must declare which framework dimension it engages.
- Profile relevance: STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL
  (from Phase 0A gate)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent
  REQUIRED:
    [ ] Tables use the declared eight-column schema
    [ ] FRAMEWORK DIMENSION column populated for every row
    [ ] Framework dimension values from Phase 0A labels only
    [ ] PROFILE RELEVANCE values from Phase 0A gate only
    [ ] All STRENGTH ratings: non-blank, non-self-referential Rationale
    [ ] Basis: verbatim / inferred / corroborated only

---

## PHASE 4 — SYNTHESIS

Produce in order: CROSS-PERSONA SYNTHESIS, DISPOSITION ARC, CONTRADICTION REGISTER,
EPISTEMIC RE-WEIGHTING, INERTIA PROFILE ACCOUNTING, PREDICTION DELTA, INERTIA/ADOPTION PARTITION.

INERTIA PROFILE ACCOUNTING must address each of the four framework dimensions explicitly:
name which evidence items engaged it and whether confirmed, challenged, or unaddressed.

NET VERDICT with VERDICT MARGIN AUDIT table (both boundary rows required).

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence not in Phase 3 is absent
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] INERTIA PROFILE ACCOUNTING addresses each of the four framework dimensions
    [ ] Net verdict from Phase 0B-I levels
    [ ] VERDICT MARGIN AUDIT table: both boundary rows populated
    [ ] Prediction delta cites specific Phase 3 items

---

## V-04 — Combined: Document-Head Numbered Sub-Schemas + Downstream Citation

**Variation axis:** Format contract + phrasing register — head contract with numbered sub-schemas AND gates cite sub-schema numbers
**Hypothesis:** When SECTION 0 declares four numbered sub-schemas AND each relevant gate item closes with an explicit numbered citation ("— per 0.1", "— per 0.2 evidence schema"), two structural elements become mutually reinforcing: SECTION 0 declares what is authoritative (C-33 satisfied); gate citations prove each section derives from that authority (C-35 approached). Neither element alone achieves what both together establish: a full traceable chain from gate completion condition to document-level contract. V-04 combines V-01's head declaration with V-02's citation pattern.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## SECTION 0 — DOCUMENT-HEAD CONTRACT

This section is the format authority for the entire document. All phases derive their
structural requirements from the four numbered sub-schemas declared below. Each sub-schema
number is a citation target: a phase gate item ending "— per 0.N" is a traceable pointer
to the contract declared here.

### 0.1 GATE FORMAT CONTRACT

All phase exit gates use this named-block structure:
```
PHASE N EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: [out-of-scope content — named by category]
  REQUIRED:
    [ ] item — per 0.N [where item derives from a sub-schema]
    [ ] item [no citation tag for phase-local items]
```
A gate without a named header fails 0.1. A gate without a PROHIBITED clause fails 0.1.
Gate items that derive from this section cite "— per 0.1".

### 0.2 EVIDENCE SCHEMA CONTRACT

All Phase 3 evidence tables use these columns in this order:
```
| # | Evidence text | Signal type | Strength | Rationale | Basis | Profile relevance |
```
Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
Strength: STRONG / MODERATE / WEAK  |  Basis: verbatim / inferred / corroborated
Profile relevance: declared at Phase 0A gate (STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL)
Gate items citing this contract append "— per 0.2".

### 0.3 MOMENT-LABEL FORMAT CONTRACT

All Phase 2 moment labels:
```
SURPRISING (expected: [Phase 0C prediction → tier name], got: [transcript content])
CONFIRMING (validates: [Phase 0C prediction → tier name])
INCONCLUSIVE (signal: [transcript content], ambiguity: [why unclear])
```
Decision rules: SURPRISING = violated; CONFIRMING = upheld; INCONCLUSIVE = ambiguous.
Gate items citing this contract append "— per 0.3".

### 0.4 SUBJECT SCHEMA CONTRACT

All Phase 1 subject cards:
```
ROLE:
PRIOR KNOWLEDGE:
  - Direct experience:
  - Knowledge gaps:
BLIND SPOTS: [specific gap — not generic]
DISPOSITION: [INCUMBENT / CHAMPION / EVALUATOR / SKEPTIC]
PRIMARY CONCERN:
VOCABULARY SIGNATURE: [term-1] | [term-2] | [term-3]
EVIDENTIAL FUNCTION: [structural role — not a disposition restatement]
```
Gate items citing this contract append "— per 0.4".

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice declare:
  - Practice name
  - Stickiness factor: specific mechanism (not generic)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
  REQUIRED:
    [ ] INERTIA PROFILE TABLE has at least two practice rows — per 0.2 (evidence basis)
    [ ] Each row has a stickiness factor naming a specific mechanism
    [ ] PROFILE RELEVANCE vocabulary declared here:
        Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
        Contract authority: this gate — not any tag list reproduced elsewhere
        These tags appear in Phase 3 PROFILE RELEVANCE column — per 0.2
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive definitions from 0B-I absent (level names only allowed)
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Non-overlapping regions
    [ ] Completing 0B-I does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair declare an ADJACENCY block.
For each tier declare: expected evidence type, expected posture, confirming signal, surprising signal.
INCUMBENT anchor: names specific Phase 0A row and stickiness factor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] Adjacency blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier predictions with all four fields
    [ ] INCUMBENT anchor names specific Phase 0A row and stickiness factor
    [ ] Gate block structure — per 0.1

---

## PRE-INTERVIEW MASTER GATE

Before Phase 1 begins, confirm all pre-interview structure is collectively complete.

PRE-INTERVIEW MASTER GATE — ALL REQUIRED BEFORE PHASE 1:
  PROHIBITED: transcript content, evidence items, and synthesis content are absent
  REQUIRED:
    [ ] Phase 0A EXIT GATE: passed — INERTIA PROFILE TABLE complete, vocabulary declared — per 0.1
    [ ] Phase 0B-I EXIT GATE: passed — five verdict levels defined — per 0.1
    [ ] Phase 0B-II EXIT GATE: passed — four margin pairs declared — per 0.1
    [ ] Phase 0C EXIT GATE: passed — tier sequence and predictions complete — per 0.1
    [ ] 0.4 subject schema declared at SECTION 0 — per 0.4
    [ ] 0.3 moment-label format declared at SECTION 0 — per 0.3
    [ ] 0.2 evidence schema declared at SECTION 0 — per 0.2
    [ ] 0.1 gate format declared at SECTION 0 and applied throughout — per 0.1

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

Each card follows the 0.4 subject schema — per 0.4.
INCUMBENT: designation label + inertia anchor (exact match to Phase 0C).
PRE-INTERVIEW MASTER GATE confirmed fully satisfied before proceeding.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent
  REQUIRED:
    [ ] Four subject cards in tier sequence
    [ ] Each card satisfies 0.4 subject schema — per 0.4
    [ ] BLIND SPOTS non-generic; EVIDENTIAL FUNCTION structural — per 0.4
    [ ] INCUMBENT: designation label + inertia anchor matching Phase 0C
    [ ] Gate block structure — per 0.1

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence.

For each subject: 4-6 questions anchored to PRIMARY CONCERN; answers in distinct voice;
vocabulary signature terms appear naturally; exactly one moment labeled per 0.3 format — per 0.3,
citing Phase 0C per-tier prediction.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: hypothesis questions and synthesis content are absent
  REQUIRED:
    [ ] All four transcripts complete
    [ ] Each subject: one moment labeled — per 0.3
    [ ] Labels cite Phase 0C predictions by tier name — per 0.3
    [ ] Answers in distinct voices; vocabulary terms appear naturally — per 0.4
    [ ] Gate block structure — per 0.1

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables using the 0.2 evidence schema — per 0.2.

Evidence table format per 0.2:
```
| # | Evidence text | Signal type | Strength | Rationale | Basis | Profile relevance |
```

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent
  REQUIRED:
    [ ] Tables use 0.2 schema column order and values — per 0.2
    [ ] PROFILE RELEVANCE tags from Phase 0A gate — per 0.2
    [ ] All STRENGTH ratings: non-blank, non-self-referential Rationale — per 0.2
    [ ] Basis: verbatim / inferred / corroborated — per 0.2
    [ ] Gate block structure — per 0.1

---

## PHASE 4 — SYNTHESIS

Produce in order: CROSS-PERSONA SYNTHESIS, DISPOSITION ARC, CONTRADICTION REGISTER,
EPISTEMIC RE-WEIGHTING, INERTIA PROFILE ACCOUNTING, PREDICTION DELTA, INERTIA/ADOPTION PARTITION.
NET VERDICT with VERDICT MARGIN AUDIT table (both boundary rows required).

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence not in Phase 3 is absent
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] Net verdict from Phase 0B-I levels
    [ ] VERDICT MARGIN AUDIT table: both boundary rows populated
    [ ] Prediction delta cites specific Phase 3 items — per 0.2
    [ ] Gate block structure — per 0.1

---

## V-05 — Full R16 Apparatus

**Variation axis:** Combined — document-head numbered sub-schemas (C-33) + downstream citation (C-35 approach) + C-36 framework dimension column + C-37 dual-source moment labels + C-41 vocabulary in gate scope
**Hypothesis:** When all R16 innovations operate simultaneously — SECTION 0 declares numbered sub-schemas 0.1–0.4 making C-33 fully satisfiable; phase gates cite "per 0.N" making the head contract a live navigation target (C-35 approach); Phase 3 carries a FRAMEWORK DIMENSION column mapping items to INERTIA PROFILE dimensions (C-36); the 0.3 template names both Expectation Register and INERTIA PROFILE FRAMEWORK as valid "expected:" sources (C-37); and the Phase 0A gate block embeds framework vocabulary as a gate-interior item rather than body prose (C-41) — the four structural innovations form a chain: head declares → gates cite → evidence maps → labels trace → vocabulary enforces. Each innovation is independently auditable and the chain closes without requiring any section to carry format instructions that belong elsewhere.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## SECTION 0 — DOCUMENT-HEAD CONTRACT

This section is the single format authority for the entire document. All phases derive their
structural requirements from the four numbered sub-schemas declared below. No phase introduces
format requirements outside of this section. A phase gate item ending "— per 0.N" is a
traceable pointer to the sub-schema declared here; the citation is the audit trace from gate
to contract authority.

### 0.1 GATE FORMAT CONTRACT

All phase exit gates use this named-block structure:

```
PHASE N EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: [specific out-of-scope content — named by category]
  REQUIRED:
    [ ] item [— per 0.N where item derives from a sub-schema]
    [ ] item [no citation tag for phase-local items]
```

Rules: PROHIBITED clause appears first. Gate without named header fails 0.1.
Gate without PROHIBITED clause fails 0.1. Gate items deriving from this section cite "— per 0.1".

### 0.2 EVIDENCE SCHEMA CONTRACT

All Phase 3 evidence extraction tables use these columns in this exact order:

```
| # | Evidence text | Signal type | Strength | Rationale | Basis | Framework dimension | Profile relevance |
```

Column value contracts:
- Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
- Strength: STRONG / MODERATE / WEAK (non-blank Rationale required for each)
- Basis: verbatim / inferred / corroborated
- Framework dimension: declared at Phase 0A gate (STICKINESS / LIMITATION / DISPLACEMENT / EXTERNAL)
- Profile relevance: declared at Phase 0A gate (same four tags)

A table omitting the Framework dimension column fails 0.2. Reordered columns fail 0.2.
Gate items deriving from this section cite "— per 0.2".

### 0.3 MOMENT-LABEL FORMAT CONTRACT

All Phase 2 moment labels use one of these three forms:

```
SURPRISING (expected: [source → entry], got: [transcript content])
CONFIRMING (validates: [source → entry])
INCONCLUSIVE (signal: [transcript content], ambiguity: [why neither confirms nor surprises])
```

Named sources for "expected:" and "validates:" slots:
  1. Expectation Register — Phase 0C per-tier prediction: cite as "Expectation Register → [tier name]"
  2. INERTIA PROFILE FRAMEWORK — Phase 0A framework dimension: cite as "INERTIA PROFILE FRAMEWORK → [dimension]"

A label must name which source it cites. A label that omits the source fails 0.3.
A label without the parenthetical structure fails 0.3.

Decision rules:
- SURPRISING: moment violates a prior expectation in the named source
- CONFIRMING: moment upholds a prior expectation in the named source
- INCONCLUSIVE: signal present but cannot be assigned to either category

Gate items deriving from this section cite "— per 0.3".

### 0.4 SUBJECT SCHEMA CONTRACT

All Phase 1 subject cards declare these fields in this order:

```
ROLE:
PRIOR KNOWLEDGE:
  - Direct experience:
  - Knowledge gaps:
BLIND SPOTS: [specific domain or perspective gap — not generic]
DISPOSITION: [INCUMBENT / CHAMPION / EVALUATOR / SKEPTIC]
PRIMARY CONCERN:
VOCABULARY SIGNATURE: [term-1] | [term-2] | [term-3]
EVIDENTIAL FUNCTION: [structural role in the evidence chain — not a disposition restatement]
EXPECTATION REGISTER ENTRY: [what this subject is expected to say, from Phase 0C per-tier prediction]
```

Rules: BLIND SPOTS must name a specific domain. EVIDENTIAL FUNCTION must name the structural
contribution (not restate role or disposition). EXPECTATION REGISTER ENTRY must reference the
Phase 0C prediction for this subject's tier. A card missing any field fails 0.4.
Gate items deriving from this section cite "— per 0.4".

---

## PHASE 0A — INERTIA PROFILE FRAMEWORK

Before designing any subject card, map the practices being displaced as a named framework
with four discrete labeled dimensions.

INERTIA PROFILE FRAMEWORK — declared dimensions:
  - STICKINESS: the mechanism sustaining the practice despite alternatives
  - LIMITATION: the constraint that blocks or slows displacement
  - DISPLACEMENT: the active transition away from the practice
  - EXTERNAL: a force outside the team or organization

For each practice, declare:
  - Practice name
  - Framework dimension (one of the four above)
  - Specific mechanism: the concrete structural or behavioral driver (not a generic descriptor)
  - Switching cost or structural barrier

Produce a named table: INERTIA PROFILE FRAMEWORK TABLE with columns:
  | Practice | Framework dimension | Specific mechanism | Switching cost |

Phase 3 evidence tables must carry a FRAMEWORK DIMENSION column mapping each item to one of the
four dimensions above (per 0.2). Phase 2 moment labels may cite framework dimensions as a named
source in the "expected:" slot (per 0.3).

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
  REQUIRED:
    [ ] INERTIA PROFILE FRAMEWORK TABLE has at least two practice rows
    [ ] Each row has a specific mechanism (generic descriptors fail)
    [ ] Framework vocabulary gate-declared here as the contract source for Phase 3 columns:
          Permitted values: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
          These are the only valid values for FRAMEWORK DIMENSION and PROFILE RELEVANCE — per 0.2
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration — evidence types and cross-subject pattern.
A level name without a constitutive definition fails.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
                INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent
              (level names may appear; definitions must not be restated)
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Non-overlapping regions across five levels
    [ ] Completing 0B-I does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0C — TIER SEQUENCE, ADJACENCY, AND EXPECTATION REGISTER

Declare tier sequence rationale and per-tier predictions before any subject cards.
These per-tier predictions constitute the Expectation Register for 0.3 moment labels.

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if order were reversed

For each tier, declare the per-tier prediction block:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like (source for CONFIRMING labels — per 0.3)
  - What surprising signal would look like (source for SURPRISING labels — per 0.3)

These per-tier prediction blocks are the Expectation Register. Each subject's EXPECTATION
REGISTER ENTRY in the 0.4 schema derives from this register.

INCUMBENT anchor: names the specific Phase 0A INERTIA PROFILE FRAMEWORK TABLE row and dimension.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] Adjacency blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier prediction blocks with all four fields
    [ ] Per-tier prediction blocks designated as the Expectation Register for 0.3 labels — per 0.3
    [ ] INCUMBENT anchor names specific Phase 0A framework row and dimension
    [ ] Gate block structure — per 0.1

---

## PRE-INTERVIEW MASTER GATE

Before Phase 1 begins, confirm all pre-interview structure is collectively and fully satisfied.

PRE-INTERVIEW MASTER GATE — ALL REQUIRED BEFORE PHASE 1:
  PROHIBITED: transcript content, evidence items, and synthesis content are absent
  REQUIRED:
    [ ] Phase 0A EXIT GATE: passed — INERTIA PROFILE FRAMEWORK TABLE complete,
        vocabulary gate-declared — per 0.1
    [ ] Phase 0B-I EXIT GATE: passed — five verdict levels constitutively defined — per 0.1
    [ ] Phase 0B-II EXIT GATE: passed — four margin pairs declared — per 0.1
    [ ] Phase 0C EXIT GATE: passed — Expectation Register complete — per 0.1
    [ ] 0.4 subject schema declared at SECTION 0 — per 0.4
    [ ] 0.3 moment-label format declared at SECTION 0 with dual named sources — per 0.3
    [ ] 0.2 evidence schema declared at SECTION 0 with Framework dimension column — per 0.2
    [ ] 0.1 gate format declared at SECTION 0 and applied in all preceding gates — per 0.1

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

Each card follows the 0.4 subject schema — per 0.4. PRE-INTERVIEW MASTER GATE confirmed
FULLY SATISFIED before proceeding.

INCUMBENT card additionally: INCUMBENT designation label, Inertia anchor (exact match to
Phase 0C anchor, naming the specific Phase 0A framework row and dimension).

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent
  REQUIRED:
    [ ] Four subject cards in tier sequence
    [ ] Each card satisfies 0.4 subject schema — per 0.4
    [ ] BLIND SPOTS: specific, non-generic for all subjects — per 0.4
    [ ] EVIDENTIAL FUNCTION: structural contribution named, not disposition restatement — per 0.4
    [ ] EXPECTATION REGISTER ENTRY: references Phase 0C per-tier prediction — per 0.4
    [ ] INCUMBENT: designation label + inertia anchor matching Phase 0C exactly
    [ ] Gate block structure — per 0.1

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to PRIMARY CONCERN
  - Write answers in distinct voice; vocabulary signature terms from 0.4 appear naturally
  - Mark exactly one moment per subject using the 0.3 format, naming the source:
      - If grounded in Phase 0C prediction: "Expectation Register → [tier name]"
      - If grounded in framework dimension: "INERTIA PROFILE FRAMEWORK → [dimension]"

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: hypothesis question sections and synthesis content are absent
  REQUIRED:
    [ ] All four transcripts complete
    [ ] Each subject: one moment labeled per 0.3 format — per 0.3
    [ ] Labels name source (Expectation Register or INERTIA PROFILE FRAMEWORK) — per 0.3
    [ ] Vocabulary signature terms from 0.4 appear in each subject's answers — per 0.4
    [ ] Answers written in distinct subject voices
    [ ] Gate block structure — per 0.1

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables using the 0.2 evidence schema — per 0.2.

The FRAMEWORK DIMENSION column maps each item to the INERTIA PROFILE FRAMEWORK dimension it
engages (contract authority: Phase 0A gate) — per 0.2. The PROFILE RELEVANCE column uses the
same four tags from the same Phase 0A gate authority — per 0.2.

Evidence table format — per 0.2:
```
| # | Evidence text | Signal type | Strength | Rationale | Basis | Framework dimension | Profile relevance |
```

PRE-INTERVIEW MASTER GATE confirmed FULLY SATISFIED — per PRE-INTERVIEW MASTER GATE.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent
  REQUIRED:
    [ ] Tables use 0.2 schema: all eight columns in declared order — per 0.2
    [ ] FRAMEWORK DIMENSION column populated for every row — per 0.2
    [ ] Framework dimension values from Phase 0A gate only — per 0.2
    [ ] PROFILE RELEVANCE values from Phase 0A gate only — per 0.2
    [ ] All STRENGTH ratings: non-blank, non-self-referential Rationale — per 0.2
    [ ] Basis: verbatim / inferred / corroborated — per 0.2
    [ ] Gate block structure — per 0.1

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS
2. DISPOSITION ARC
3. CONTRADICTION REGISTER (at least one naming both subjects and both evidence items)
4. EPISTEMIC RE-WEIGHTING (per-blind-spot resolution conditions; at least one item's weight
   explicitly adjusted with named rationale based on epistemic standing)
5. INERTIA PROFILE ACCOUNTING — for each of the four Phase 0A framework dimensions:
   name which evidence items engaged it and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA — classify each Phase 0C per-tier prediction as CONFIRMED / CONTRADICTED /
   ABSENT / PARTIAL, citing specific Phase 3 items — per 0.2
7. INERTIA / ADOPTION PARTITION (two separately populated lists)

Then produce NET VERDICT:
  - Verdict level from Phase 0B-I definitions
  - Constitutive evidence configuration named
  - VERDICT MARGIN AUDIT table:

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named item] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named item] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence items not present in Phase 3 are absent
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] INERTIA PROFILE ACCOUNTING addresses each of the four Phase 0A framework dimensions
    [ ] Epistemic re-weighting: at least one explicit weight adjustment with rationale
    [ ] Net verdict from Phase 0B-I defined levels
    [ ] VERDICT MARGIN AUDIT table: both upper-boundary and lower-boundary rows populated
    [ ] Prediction delta citations name specific Phase 3 items — per 0.2
    [ ] Gate block structure — per 0.1
