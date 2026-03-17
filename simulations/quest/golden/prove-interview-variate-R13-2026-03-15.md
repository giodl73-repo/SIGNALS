# prove-interview — Skill Body Variations — R13

**Skill:** prove-interview
**Round:** 13
**Rubric version:** v13
**Date:** 2026-03-15

---

## R13 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|-----------|----------------|------|------------|
| V-01 | Combined | Role Sequence — INCUMBENT First (C-37 + C-39) | Anchoring the exercise on the status-quo user before any adopter establishes an inertia reference that makes every subsequent subject's signals legible as a departure from a known baseline; vocabulary declared at Phase 0A gate makes tag compliance a contract auditable at entry, not a convention checked at Phase 3 |
| V-02 | Single | Phase 4 Synthesis Gate (C-38) | A Phase 4 exit gate that explicitly names every required synthesis section and calls VERDICT MARGIN AUDIT table completeness as a gate condition makes synthesis omission detectable by gate-check alone, without reading the section content |
| V-03 | Single | INCUMBENT Traceability Chain (C-39) | When each downstream phase explicitly names the prior phase's named anchor output as its required input, a broken traceability chain is detectable at the phase that names its predecessor — Phase 1 gate fails if Phase 0C anchor was not named, Phase 2 gate fails if Phase 1 anchor was not carried forward |
| V-04 | Combined | Vocabulary Contract + Phase 4 Gate (C-37 + C-38) | C-37 and C-38 are bookend criteria: C-37 declares the vocabulary contract at Phase 0A entry, C-38 closes the loop at Phase 4 exit — making vocabulary tag compliance and synthesis completeness auditable at both endpoints without inspecting interior phases |
| V-05 | Combined | Full apparatus (C-37 + C-38 + C-39 + bidirectional C-35) | When vocabulary declaration, Phase 4 synthesis gating, and INCUMBENT anchor traceability are all present simultaneously, the skill creates a closed-loop chain from Phase 0A vocabulary contract through Phase 3 tag compliance through Phase 4 audit gate; C-39 makes the INCUMBENT anchor a cross-phase structural invariant rather than a restatement |

Single-axis variations: V-02 (Phase 4 exit gate), V-03 (INCUMBENT traceability chain)
Combined variations: V-01 (C-37 + C-39 with role-sequence framing), V-04 (C-37 + C-38 bookend), V-05 (all three new criteria + bidirectional audit table)

New R13 territory probed:
- **Vocabulary as Phase 0A gate contract** (V-01, V-04, V-05): vocabulary declared in the Phase 0A exit gate REQUIRED clause, making it a gate-checkable commitment rather than a format convention defined at Phase 3 header
- **Phase 4 synthesis exit gate** (V-02, V-04, V-05): Phase 4 has an explicit exit gate enumerating all required synthesis sections; VERDICT MARGIN AUDIT bidirectional completeness is a named gate condition
- **INCUMBENT anchor traceability chain** (V-01, V-03, V-05): Phase 0C names the anchor and declares it as a named output propagating forward; Phase 1 requires the specific Phase 0C row by name; Phase 2 requires at least one question naming the Phase 1 anchor directly

---

## V-01 — Role Sequence — INCUMBENT First (C-37 + C-39)

**Variation axis:** Role sequence + vocabulary contract
**Hypothesis:** Anchoring the exercise on the status-quo user before any adopter establishes an inertia reference that makes every subsequent subject's signals legible as a departure from a known baseline, rather than assertions in a vacuum. Adoption signals gain diagnostic weight because the incumbent resistance was already on the record. Vocabulary declared at the Phase 0A exit gate makes PROFILE RELEVANCE tag compliance a contract commitment auditable at Phase 0A, not a format convention audited only at Phase 3.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear
      in this section (those belong to 0B and 0C respectively)

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare the verdict classification levels and their constitutive definitions BEFORE evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — what pattern of evidence types across subjects places the finding at this level. A level name without a constitutive definition does not satisfy this gate.

PROHIBITED: do not include margin-boundary declarations or deciding-factor content in this section — that belongs in 0B-II.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions
  [ ] Definitions name evidence types and cross-subject patterns, not just tone or quantity
  [ ] No margin-boundary content (deciding factor at adjacent-level boundaries) is present in this sub-section
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not restate constitutive definitions from 0B-I here — reference level names only.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four margin pairs have a named deciding factor
  [ ] Margin definitions do not restate the adjacent constitutive definitions from 0B-I
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

**SEQUENCE DECLARATION — INCUMBENT FIRST:**

Subject design and interview order: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

Sequence rationale: The INCUMBENT subject is placed first because the inertia reference must be on the record before adoption signals are collected. When skeptic or evaluator resistance is encountered later, it reads against both (a) the confirmed inertia baseline from Phase 0A and (b) the incumbent's actual expressed concerns — not against a hypothetical. CHAMPION signals that follow the incumbent are readable as genuine departures from the established baseline rather than unanchored enthusiasm.

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like (the departure that would be diagnostic)

INCUMBENT anchor: Name the specific Phase 0A inertia profile row and stickiness factor
that makes this subject the baseline anchor. This named anchor propagates forward to
Phase 1 (subject card inertia anchor field) and Phase 2 (at least one question names it).

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] INCUMBENT anchor names a specific Phase 0A table row and stickiness factor
      (not a summary; not "see above"; a named row)
  [ ] Sequence rationale explains contrast logic, not just order
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN (INCUMBENT FIRST)

Design subject cards in sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate fields)
  - Blind spots (not blank, not "none")
  - Disposition
  - Primary concern
  - INCUMBENT designation label (for the INCUMBENT subject; omit for others)
  - Inertia anchor (INCUMBENT only): name the specific Phase 0A practice row
    and stickiness factor. Must match the anchor named in Phase 0C exactly.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards in sequence: INCUMBENT first
  [ ] Each card has role, prior knowledge, blind spots, disposition, primary concern
  [ ] INCUMBENT card carries an INCUMBENT designation label
  [ ] INCUMBENT inertia anchor names a specific row from the Phase 0A INERTIA PROFILE TABLE
      (not a paraphrase; the named row)
  [ ] Blind spots field is non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT (INCUMBENT FIRST)

Write transcripts in subject order: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

All four transcripts are completed before any hypothesis questions are written.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern and prior knowledge
  - INCUMBENT questions: at least one question names the declared Phase 0A inertia anchor
    directly (not a paraphrase; the named anchor from Phase 0C / Phase 1)
  - Write answers in the subject's distinct voice; answers must not be interchangeable
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to the
    Phase 0C per-tier prediction for that subject's tier

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript has at least one question naming the declared Phase 0A
      inertia anchor directly
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment, named against
      its Phase 0C prediction
  [ ] Answers are written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts
and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary:
    STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
    Name which Phase 0A profile dimension the item addresses.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section exists and is separate from transcripts
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag is one of: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content appears in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregates findings across all four subjects
2. DISPOSITION ARC — traces how each subject's disposition shifted or held
3. CONTRADICTION REGISTER — names at least one contradiction, citing both subjects
   and both specific conflicting evidence items by content
4. EPISTEMIC RE-WEIGHTING — adjusts evidence weight by subject blind spots;
   specifies resolution conditions per blind spot
5. INERTIA PROFILE ACCOUNTING — closes the loop from Phase 0A: for each
   stickiness factor in the INERTIA PROFILE TABLE, state which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether the factor was confirmed,
   challenged, or unaddressed
6. PREDICTION DELTA — iterates through each Phase 0C per-tier prediction and
   classifies actual evidence as CONFIRMED / CONTRADICTED / ABSENT / PARTIAL,
   naming specific evidence items for each classification
7. INERTIA / ADOPTION PARTITION — two separately populated lists:
   inertia signals and adoption signals

Then produce the NET VERDICT:
  - State the verdict classification from the Phase 0B levels
  - Name the constitutive evidence configuration that places the finding at this level
  - Produce the VERDICT MARGIN AUDIT table:

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper boundary ([next level] / [this level]) | | | |
    | Lower boundary ([this level] / [level below]) | | | |

    Both rows must be populated. A single-row audit does not satisfy C-35.

---

## V-02 — Phase 4 Synthesis Gate (C-38)

**Variation axis:** Phase 4 synthesis completeness gate
**Hypothesis:** Prior variations instruct synthesis sections to be produced but leave omission recoverable — an absent section is a prose failure, not a gate failure. When Phase 4 has an explicit exit gate that names all required synthesis sections and calls VERDICT MARGIN AUDIT bidirectional completeness as a gate condition, synthesis omission becomes detectable at gate-check time without reading the section content. C-38 upgrades Phase 4 from a prose checklist to a structural gate.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PROFILE RELEVANCE vocabulary for Phase 3 evidence items:
Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL

PROHIBITED: do not include tier sequence, verdict threshold, or margin content in this section.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not include margin-boundary declarations in this sub-section.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] No margin-boundary or deciding-factor content present
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

Declare the deciding margin factor for each adjacent level pair.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not restate constitutive definitions from 0B-I.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four margin pairs have a named deciding factor
  [ ] No constitutive threshold restatements present
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

For each tier, declare:
  - Expected evidence type
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared with adjacency blocks for all consecutive pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design four subject cards. For each card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate fields)
  - Blind spots (not blank, not "none")
  - Disposition
  - Primary concern

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present
  [ ] Each card has all five fields
  [ ] Blind spots field is non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential
  - PROFILE RELEVANCE: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS
2. DISPOSITION ARC
3. CONTRADICTION REGISTER (at least one contradiction, citing both subjects and both evidence items)
4. EPISTEMIC RE-WEIGHTING (adjusts by blind spots; specifies resolution conditions per blind spot)
5. INERTIA PROFILE ACCOUNTING (closes loop from Phase 0A)
6. PREDICTION DELTA (CONFIRMED / CONTRADICTED / ABSENT / PARTIAL per prediction, naming evidence items)
7. INERTIA / ADOPTION PARTITION (two separately populated lists)

Then produce the NET VERDICT:
  - State the verdict classification from Phase 0B levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table with both boundary rows populated:

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper boundary | | | |
    | Lower boundary | | | |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] CROSS-PERSONA SYNTHESIS section present
  [ ] DISPOSITION ARC section present
  [ ] CONTRADICTION REGISTER section present with at least one contradiction named
  [ ] EPISTEMIC RE-WEIGHTING section present with per-blind-spot resolution conditions
  [ ] INERTIA PROFILE ACCOUNTING section present
  [ ] PREDICTION DELTA section present with evidence item citations
  [ ] INERTIA / ADOPTION PARTITION section present
  [ ] NET VERDICT present with verdict classification from Phase 0B-I taxonomy
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated

---

## V-03 — INCUMBENT Traceability Chain (C-39)

**Variation axis:** Multi-phase INCUMBENT anchor propagation
**Hypothesis:** Prior variations declare an INCUMBENT anchor in Phase 0C but do not require downstream phases to name it as a required input. When Phase 0C declares the anchor as a named output, Phase 1's exit gate requires that named output by phase reference, and Phase 2's exit gate requires at least one question naming the Phase 1 anchor directly, a broken traceability chain becomes detectable at the phase that names its predecessor — without inspecting downstream phases.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PROFILE RELEVANCE vocabulary for Phase 3 evidence items:
Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL

PROHIBITED: do not include tier sequence, verdict threshold, or margin content in this section.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not include margin-boundary declarations in this sub-section.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] No margin-boundary or deciding-factor content present
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

Declare the deciding margin factor for each adjacent level pair.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not restate constitutive definitions from 0B-I.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four margin pairs have a named deciding factor
  [ ] No constitutive threshold restatements present
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale, per-tier predictions, and INCUMBENT anchor before any subject cards.

For each tier, declare:
  - Expected evidence type
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

INCUMBENT ANCHOR DECLARATION:
Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that anchors the INCUMBENT subject's inertia baseline. This anchor is a named output of Phase 0C.

  Named anchor: [Phase 0A row name] — [stickiness factor]

This named anchor propagates forward:
  - Phase 1: INCUMBENT subject card must name this specific row and stickiness factor in the Inertia anchor field
  - Phase 2: INCUMBENT transcript must include at least one question that names this anchor directly

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT ANCHOR DECLARATION present, naming a specific Phase 0A row and stickiness factor
  [ ] Anchor declared as a named output with explicit propagation forward to Phase 1 and Phase 2
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] Tier sequence declared with adjacency blocks
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design four subject cards. For each card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate fields)
  - Blind spots (not blank, not "none")
  - Disposition
  - Primary concern

INCUMBENT subject additionally requires:
  - INCUMBENT designation label
  - Inertia anchor: must name the specific Phase 0A row and stickiness factor declared in Phase 0C.
    The named anchor must match Phase 0C exactly — paraphrase does not satisfy this gate.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present
  [ ] Each card has role, prior knowledge, blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor names the specific Phase 0C declared row and stickiness factor
      (must match Phase 0C declaration exactly, not paraphrase)
  [ ] Blind spots field is non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING

INCUMBENT subject additionally requires:
  - At least one question must name the Phase 1 inertia anchor directly (not a paraphrase).
    The question text must include the anchor name from Phase 1.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript has at least one question naming the Phase 1 inertia anchor directly
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential
  - PROFILE RELEVANCE: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS
2. DISPOSITION ARC
3. CONTRADICTION REGISTER
4. EPISTEMIC RE-WEIGHTING
5. INERTIA PROFILE ACCOUNTING (for each Phase 0A stickiness factor, state which evidence items addressed it by PROFILE RELEVANCE tag)
6. PREDICTION DELTA
7. INERTIA / ADOPTION PARTITION

Then produce the NET VERDICT:
  - State the verdict classification from Phase 0B levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table:

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper boundary | | | |
    | Lower boundary | | | |

    Both rows must be populated.

---

## V-04 — Vocabulary Contract + Phase 4 Gate (C-37 + C-38)

**Variation axis:** Bookend criteria — Phase 0A vocabulary contract (C-37) + Phase 4 synthesis exit gate (C-38)
**Hypothesis:** C-37 and C-38 are architectural bookends: C-37 makes the PROFILE RELEVANCE vocabulary a gate commitment declared at Phase 0A entry, C-38 makes synthesis section completeness a gate failure detectable at Phase 4 exit. Together they create auditable endpoints at both the evidence-collection entry (vocabulary contract) and the synthesis exit (section completeness), without requiring the INCUMBENT traceability chain of C-39.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not include margin-boundary declarations in this sub-section.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] No margin-boundary or deciding-factor content present
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

Declare the deciding margin factor for each adjacent level pair.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not restate constitutive definitions from 0B-I.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four margin pairs have a named deciding factor
  [ ] No constitutive threshold restatements present
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

For each tier, declare:
  - Expected evidence type
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared with adjacency blocks for all consecutive pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design four subject cards. For each card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate fields)
  - Blind spots (not blank, not "none")
  - Disposition
  - Primary concern

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present
  [ ] Each card has all five fields
  [ ] Blind spots field is non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential
  - PROFILE RELEVANCE: one tag from Phase 0A exit gate vocabulary:
    STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag from Phase 0A exit gate vocabulary
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS
2. DISPOSITION ARC
3. CONTRADICTION REGISTER (at least one contradiction, citing both subjects and both evidence items)
4. EPISTEMIC RE-WEIGHTING (adjusts by blind spots; specifies resolution conditions per blind spot)
5. INERTIA PROFILE ACCOUNTING (closes loop from Phase 0A; PROFILE RELEVANCE tag accounting)
6. PREDICTION DELTA (CONFIRMED / CONTRADICTED / ABSENT / PARTIAL, naming evidence items)
7. INERTIA / ADOPTION PARTITION (two separately populated lists)

Then produce the NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table:

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper boundary | | | |
    | Lower boundary | | | |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] CROSS-PERSONA SYNTHESIS section present
  [ ] DISPOSITION ARC section present
  [ ] CONTRADICTION REGISTER present with at least one named contradiction
  [ ] EPISTEMIC RE-WEIGHTING present with per-blind-spot resolution conditions
  [ ] INERTIA PROFILE ACCOUNTING present
  [ ] PREDICTION DELTA present with evidence item citations
  [ ] INERTIA / ADOPTION PARTITION present
  [ ] NET VERDICT present with classification from Phase 0B-I taxonomy
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated

---

## V-05 — Full Apparatus (C-37 + C-38 + C-39 + bidirectional C-35)

**Variation axis:** All three new criteria combined with bidirectional audit table
**Hypothesis:** When vocabulary declaration (C-37), Phase 4 synthesis gating (C-38), and INCUMBENT anchor traceability (C-39) are present simultaneously, the skill achieves closed-loop evidence accountability: the vocabulary contract declared at Phase 0A propagates through Phase 3 tag compliance and is audited at Phase 4 exit; the INCUMBENT anchor declared at Phase 0C propagates through Phase 1 (named match) and Phase 2 (named question) creating a cross-phase structural invariant detectable by gate-check at each phase. C-35's explicit two-row template makes a single-direction audit a visible structural failure.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3 and Phase 4:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      This declaration is a gate-level contract: Phase 3 items must use these tags;
      Phase 4 INERTIA PROFILE ACCOUNTING must address each tag category represented.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not include margin-boundary declarations or deciding-factor content here.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] No margin-boundary or deciding-factor content present
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

Declare the deciding margin factor for each adjacent level pair.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not restate constitutive definitions from 0B-I — reference level names only.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four margin pairs have a named deciding factor
  [ ] No constitutive threshold restatements present
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale, per-tier predictions, and INCUMBENT anchor before any subject cards.

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

INCUMBENT ANCHOR DECLARATION:
Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that anchors the INCUMBENT subject's inertia baseline.

  Named anchor: [Phase 0A row name] — [stickiness factor]

This is a named output of Phase 0C. It propagates as follows:
  - Phase 1 INCUMBENT card: inertia anchor field must name this row and stickiness factor exactly
  - Phase 2 INCUMBENT transcript: at least one question must name this anchor directly

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT ANCHOR DECLARATION present, naming a specific Phase 0A row and stickiness factor
  [ ] Propagation chain declared explicitly: Phase 1 field + Phase 2 question
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] Tier sequence with adjacency blocks for all consecutive pairs
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design four subject cards.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate fields)
  - Blind spots (not blank, not "none")
  - Disposition
  - Primary concern

INCUMBENT subject additionally requires:
  - INCUMBENT designation label
  - Inertia anchor: must name the specific Phase 0C declared row and stickiness factor.
    Must match Phase 0C named anchor exactly — paraphrase does not satisfy this gate.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present
  [ ] Each card has role, prior knowledge, blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor matches Phase 0C named anchor exactly (named row + stickiness factor)
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, against Phase 0C prediction

INCUMBENT subject additionally requires:
  - At least one question names the Phase 1 inertia anchor directly (not a paraphrase).

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript has at least one question naming Phase 1 inertia anchor directly
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate declared vocabulary:
    STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
    (violation of Phase 0A gate contract if tag is outside this set)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag drawn from Phase 0A exit gate declared vocabulary
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregates findings across all four subjects
2. DISPOSITION ARC — traces per-subject disposition shift or hold
3. CONTRADICTION REGISTER — at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING — adjusts evidence weight by blind spots; per-blind-spot resolution conditions
5. INERTIA PROFILE ACCOUNTING — for each Phase 0A stickiness factor, state which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA — iterate Phase 0C per-tier predictions; classify as CONFIRMED / CONTRADICTED /
   ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION — two separately populated lists

Then produce the NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (TWO ROWS REQUIRED — both must be populated):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II margin factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II margin factor] | [named evidence] | [placement] |

    A table with one populated row does not satisfy C-35.
    An absent upper-boundary row or an absent lower-boundary row is a gate failure.

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] CROSS-PERSONA SYNTHESIS section present
  [ ] DISPOSITION ARC section present
  [ ] CONTRADICTION REGISTER present with at least one named contradiction citing both subjects
  [ ] EPISTEMIC RE-WEIGHTING present with per-blind-spot resolution conditions specified
  [ ] INERTIA PROFILE ACCOUNTING present, addressing each Phase 0A stickiness factor
  [ ] PREDICTION DELTA present with specific Phase 3 evidence item citations
  [ ] INERTIA / ADOPTION PARTITION present with two separately populated lists
  [ ] NET VERDICT present with classification from Phase 0B-I taxonomy
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary row AND lower-boundary row populated
      (single-row audit fails this gate regardless of row content)
