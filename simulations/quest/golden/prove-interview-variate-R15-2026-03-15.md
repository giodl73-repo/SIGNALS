# prove-interview — Skill Body Variations — R15

**Skill:** prove-interview
**Round:** 15
**Rubric version:** v15
**Date:** 2026-03-15

---

## R15 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|---|---|---|---|
| V-01 | Single | Gate-block-interior PROHIBITED — Phase 0B-I only (C-43 partial) | When Phase 0B-I gate block opens with PROHIBITED as its first checklist item but Phase 0B-II retains body-adjacent PROHIBITED (C-34-failing), Phase 0B-I's scope constraint is auditable at its gate exit independently; the asymmetry isolates the per-gate effect — C-43 activates per-gate, not per-phase, so Phase 0B-I compliance is not contingent on Phase 0B-II |
| V-02 | Single | Gate-block-interior PROHIBITED — symmetric both 0B sub-phases (C-43 full) | When both Phase 0B-I and Phase 0B-II gate blocks open with PROHIBITED as their first checklist item, each sub-phase scope constraint is independently auditable at its own gate exit; no body-adjacent PROHIBITED language is needed because the gate block itself carries the prohibition as an evaluable exit condition |
| V-03 | Single | C-43 symmetric + INCUMBENT-first inertia framing | Gate-block-interior PROHIBITED is role-sequence-independent; testing C-43 alongside INCUMBENT-first ordering with expanded inertia profile specificity demonstrates the structural gate-interior invariant holds regardless of subject sequencing choices, and the inertia framing does not interfere with C-43's per-gate audit structure |
| V-04 | Combined | C-43 symmetric + Phase 3 gate cites Phase 0A by reference (C-43 + C-40) | C-43 and C-40 are independent audit chain upgrades at different structural positions: C-43 creates auditable scope constraints at each 0B sub-phase gate; C-40 creates an auditable vocabulary compliance point at Phase 3 exit by naming Phase 0A as the contract source rather than reproducing the tag list — together they provide three independent audit points (0B-I, 0B-II, Phase 3) without requiring Phase 4 gate changes |
| V-05 | Combined | Full R15 apparatus (C-43 + C-40 + C-41 + C-42) | When gate-block-interior PROHIBITED (C-43), Phase 3 vocabulary contract reference (C-40), Phase 0C INCUMBENT anchor propagation obligations (C-41), and Phase 4 single-row audit table named as gate failure by content type (C-42) are all present simultaneously, the skill achieves four independent structural audit points — 0B-I and 0B-II scope constraints, Phase 3 vocabulary compliance, Phase 0C chain-break origin, and Phase 4 synthesis completeness — each auditable at its own gate without inspecting any other phase |

Single-axis variations: V-01 (C-43 partial — Phase 0B-I only), V-02 (C-43 full — both 0B sub-phases), V-03 (C-43 full + inertia framing axis)
Combined variations: V-04 (C-43 + C-40), V-05 (C-43 + C-40 + C-41 + C-42)

New R15 territory probed:
- **Gate-block-interior PROHIBITED as first item in Phase 0B-I gate block** (V-01, V-02, V-03, V-04, V-05): PROHIBITED clause is the first checklist item inside the Phase 0B-I gate block boundary; body text preceding the gate contains no standalone PROHIBITED statement
- **Gate-block-interior PROHIBITED as first item in Phase 0B-II gate block** (V-02, V-03, V-04, V-05): symmetric C-43 implementation; both sub-phase scope constraints are auditable at their own gate exits
- **C-43 asymmetry as isolation control** (V-01): Phase 0B-I is C-43-compliant; Phase 0B-II retains body-adjacent PROHIBITED (C-34-failing and C-43-N/A), demonstrating that the criterion activates per-gate

---

## V-01 — Gate-block-interior PROHIBITED, Phase 0B-I Only (C-43 partial)

**Variation axis:** Lifecycle emphasis — gate block as scope boundary document, Phase 0B-I only
**Hypothesis:** When Phase 0B-I gate block opens with PROHIBITED as its first checklist item, the sub-phase scope constraint is auditable at Phase 0B-I exit without reading body text. Phase 0B-II retaining body-adjacent PROHIBITED (C-34-failing, C-43-N/A) provides an asymmetric control: the auditor encounters the structural difference by inspecting both sub-phase gates in sequence. The partial implementation isolates C-43 to one sub-phase to verify the criterion activates per-gate independently of whether the sibling sub-phase also satisfies it.

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
      This declaration is the contract source — Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — what pattern of evidence types
across subjects places the finding at this level. A level name without a constitutive definition does
not satisfy this gate.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin-boundary declarations or deciding-factor content is absent from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not restate constitutive definitions from Phase 0B-I — reference level names only.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four margin pairs have a named deciding factor
  [ ] No constitutive threshold restatements from Phase 0B-I present
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if order were reversed

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

INCUMBENT anchor: Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that
designates this subject as the inertia baseline anchor for the exercise.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] INCUMBENT anchor names a specific Phase 0A table row and stickiness factor
      (not a summary; not "see above"; a named row)
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (not blank, not "none", not generic — name the specific domain or perspective gap)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): name the specific Phase 0A practice row and stickiness factor;
    must match the Phase 0C anchor declaration exactly

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present in tier sequence
  [ ] Each card has role, prior knowledge (two sub-fields), blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor names the specific Phase 0A row (exact match to Phase 0C anchor)
  [ ] Blind spots field is non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to the Phase 0C
    per-tier prediction for that subject's tier

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices (not interchangeable across subjects)

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tags use Phase 0A vocabulary (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregate findings across all subjects
2. DISPOSITION ARC — trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER — at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING — adjust evidence weights by declared blind spots; per-blind-spot
   resolution conditions specified
5. INERTIA PROFILE ACCOUNTING — for each Phase 0A stickiness factor, name which evidence items
   addressed it and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA — iterate Phase 0C per-tier predictions; classify each as CONFIRMED /
   CONTRADICTED / ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION — two separately populated lists

Then produce NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-02 — Gate-block-interior PROHIBITED, Symmetric Both 0B Sub-phases (C-43 full)

**Variation axis:** Lifecycle emphasis — gate block as symmetric scope boundary document in both 0B sub-phases
**Hypothesis:** When both Phase 0B-I and Phase 0B-II gate blocks open with PROHIBITED as their respective first checklist items, each sub-phase scope constraint is independently auditable at its own gate exit. No body-text PROHIBITED is needed because the gate block itself carries the prohibition as an auditable exit condition. Symmetric placement removes the asymmetry present in V-01 — an auditor encounters the same structural pattern at both sub-phase gates.

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
      This declaration is the contract source — Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — what pattern of evidence types
across subjects places the finding at this level. A level name without a constitutive definition does
not satisfy this gate.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin-boundary declarations or deciding-factor content is absent from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent from this sub-section
      (level names may be referenced; constitutive definitions must not be restated)
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if order were reversed

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

INCUMBENT anchor: Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that
designates this subject as the inertia baseline anchor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] INCUMBENT anchor names a specific Phase 0A table row and stickiness factor
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (not blank, not "none", not generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): specific Phase 0A practice row — exact match to Phase 0C anchor

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present in tier sequence
  [ ] Each card has role, prior knowledge (two sub-fields), blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor names the specific Phase 0A row (exact match to Phase 0C anchor)
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to the Phase 0C
    per-tier prediction for that subject's tier

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tags use Phase 0A vocabulary (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS
2. DISPOSITION ARC
3. CONTRADICTION REGISTER (at least one contradiction naming both subjects and both evidence items)
4. EPISTEMIC RE-WEIGHTING (per-blind-spot resolution conditions)
5. INERTIA PROFILE ACCOUNTING (each Phase 0A stickiness factor addressed)
6. PREDICTION DELTA (Phase 0C predictions classified with Phase 3 evidence citations)
7. INERTIA / ADOPTION PARTITION (two separately populated lists)

Then produce NET VERDICT with VERDICT MARGIN AUDIT table (upper and lower boundary rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-03 — C-43 Symmetric + INCUMBENT-First Inertia Framing

**Variation axis:** C-43 symmetric (both 0B sub-phases) + inertia framing axis (INCUMBENT-first with expanded stickiness specificity)
**Hypothesis:** Gate-block-interior PROHIBITED placement is role-sequence-independent. Pairing full C-43 implementation with INCUMBENT-FIRST ordering and expanded Phase 0A stickiness specificity requirements verifies that the structural gate-interior invariant holds when the inertia reference is the primary organizing frame. The inertia framing deepens Phase 0A and Phase 0C without interfering with C-43's per-gate audit structure.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A — INERTIA PROFILE

The incumbent ecosystem is the primary object of study. Before designing any subject card, map the
full stickiness structure of the practices being displaced.

For each practice, declare:
  - Practice name
  - Stickiness factor: the specific mechanism sustaining this practice despite available alternatives —
    not a generic descriptor like "familiarity" or "existing tooling" but the structural or behavioral
    mechanism (e.g., "24-month audit log retention tied to existing toolchain" or "approval workflow
    embedded in IDE plugin")
  - Switching cost or structural limitation: what a team would have to undo, retrain, or rebuild

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor naming a specific mechanism (generic descriptors do not satisfy)
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
      This declaration is the contract source — Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it. A level name is not a definition.
A description of tone or quantity is not a definition. A constitutive definition names evidence types
and the cross-subject pattern that produces them.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin-boundary declarations or deciding-factor content is absent from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent from this sub-section
      (level names may be referenced; constitutive definitions must not be restated)
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

**SEQUENCE: INCUMBENT FIRST**

Subject design and interview order: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

Sequence rationale: The INCUMBENT subject is placed first because the inertia reference must be on
the record before adoption signals are collected. Every subsequent subject's signals read as departures
from a documented baseline rather than assertions against a hypothetical. CHAMPION enthusiasm is legible
as a genuine departure from the INCUMBENT's confirmed stickiness — not unanchored optimism.

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - What contrast would be lost if the order were reversed

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like for this tier
  - What surprising signal would look like for this tier

INCUMBENT anchor: Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that
designates this subject as the inertia baseline anchor. The named anchor must be traceable to a
specific Phase 0A table row — not a paraphrase, not a summary.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC
  [ ] Adjacency blocks present for all three consecutive tier pairs with contrast-lost rationale
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] INCUMBENT anchor names a specific Phase 0A table row and stickiness factor (not a summary)
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN (INCUMBENT FIRST)

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge: direct experience (sub-field) and knowledge gaps (sub-field) as separate
    declarations — the distinction between what the subject has done and what they cannot see must
    be explicit
  - Blind spots: non-blank, non-generic — name the specific domain, organizational vantage, or
    structural constraint the subject cannot see from their position
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): name the Phase 0A practice row and stickiness factor;
    must match the Phase 0C anchor declaration exactly

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present in sequence: INCUMBENT first
  [ ] Each card has role, prior knowledge (two sub-fields), blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor names the specific Phase 0A row (exact match to Phase 0C anchor)
  [ ] Blind spots field is non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - For the INCUMBENT subject: at least one question names the Phase 0A inertia anchor directly
  - Write answers in the subject's distinct voice (not interchangeable across subjects)
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to the Phase 0C
    per-tier prediction for that subject's tier

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript includes at least one question naming the Phase 0A inertia anchor directly
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tags use Phase 0A exit gate vocabulary
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregate findings across all subjects
2. DISPOSITION ARC — trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER (at least one contradiction naming both subjects and both evidence items)
4. EPISTEMIC RE-WEIGHTING (per-blind-spot resolution conditions)
5. INERTIA PROFILE ACCOUNTING (each Phase 0A stickiness factor addressed by evidence)
6. PREDICTION DELTA (Phase 0C predictions classified CONFIRMED / CONTRADICTED / ABSENT / PARTIAL
   with Phase 3 evidence citations)
7. INERTIA / ADOPTION PARTITION (two separately populated lists)

Then produce NET VERDICT with VERDICT MARGIN AUDIT table (upper and lower boundary rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-04 — C-43 Symmetric + Phase 3 Gate Cites Phase 0A by Reference (C-43 + C-40)

**Variation axis:** C-43 symmetric (both 0B sub-phases) + Phase 3 vocabulary contract reference (C-40)
**Hypothesis:** C-43 and C-40 are independent audit chain upgrades at different structural positions. C-43 makes each sub-phase scope constraint auditable at its own gate exit without inspecting body text. C-40 makes vocabulary tag compliance at Phase 3 auditable by citing Phase 0A as the named contract source — a tag list reproduced at Phase 3 would allow Phase 0A and Phase 3 to diverge without detection; a named reference makes Phase 0A the single source of truth detectable at Phase 3 exit. Together they provide three independent audit points (0B-I, 0B-II, Phase 3) without requiring Phase 4 gate changes.

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
  - Stickiness factor (specific mechanism sustaining the practice)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
      This declaration is the contract source — Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin-boundary declarations or deciding-factor content is absent from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent from this sub-section
      (level names may be referenced; constitutive definitions must not be restated)
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - Confirming signal
  - Surprising signal

INCUMBENT anchor: Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] INCUMBENT anchor names a specific Phase 0A table row and stickiness factor
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (non-blank, non-generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): exact match to Phase 0C anchor

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present in tier sequence
  [ ] Each card has all five standard fields plus INCUMBENT designation
  [ ] INCUMBENT inertia anchor names the specific Phase 0A row (exact match to Phase 0C anchor)
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; compliance is with the Phase 0A exit gate, not with
      any tag list restated here
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS
2. DISPOSITION ARC
3. CONTRADICTION REGISTER (at least one contradiction naming both subjects and both evidence items)
4. EPISTEMIC RE-WEIGHTING (per-blind-spot resolution conditions)
5. INERTIA PROFILE ACCOUNTING (each Phase 0A stickiness factor addressed)
6. PREDICTION DELTA (Phase 0C predictions classified with Phase 3 evidence citations)
7. INERTIA / ADOPTION PARTITION (two separately populated lists)

Then produce NET VERDICT with VERDICT MARGIN AUDIT table (upper and lower boundary rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-05 — Full R15 Apparatus (C-43 + C-40 + C-41 + C-42)

**Variation axis:** Combined — all R15 and accumulated R14 structural criteria
**Hypothesis:** When gate-block-interior PROHIBITED (C-43), Phase 3 vocabulary contract reference (C-40), Phase 0C INCUMBENT anchor propagation obligations declared at source (C-41), and Phase 4 single-row VERDICT MARGIN AUDIT named as gate failure by content type (C-42) are all present simultaneously, the skill achieves four independent structural audit points: each 0B sub-phase gate audits its own scope constraint; Phase 3 gate audits vocabulary compliance by naming Phase 0A as the contract source; Phase 0C gate audits INCUMBENT chain-break origin by declaring both downstream obligations at the source; Phase 4 gate audits VERDICT MARGIN AUDIT completeness by structural type. No audit point requires inspecting any other phase to verify its condition.

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
  - Stickiness factor (specific mechanism sustaining the practice despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
      This declaration is the contract source — Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — what pattern of evidence types
across subjects places the finding at this level. A level name without a constitutive definition does
not satisfy this gate.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin-boundary declarations or deciding-factor content is absent from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent from this sub-section
      (level names may be referenced; constitutive definitions must not be restated)
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - Confirming signal
  - Surprising signal

INCUMBENT anchor: Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that
designates this subject as the inertia baseline anchor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] INCUMBENT anchor declared as named output: names specific Phase 0A row and stickiness factor
      Downstream propagation obligations declared at this gate:
        - Phase 1: INCUMBENT subject card inertia anchor field must match this named row exactly
          (exact-match required — a paraphrase does not satisfy the Phase 1 obligation)
        - Phase 2: at least one question in the INCUMBENT transcript must name this anchor directly
          (direct-question required — referencing the topic without naming the anchor does not satisfy)
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (non-blank, non-generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): must match the Phase 0C anchor exactly
    (exact-match required per Phase 0C exit gate propagation obligation)

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present in tier sequence
  [ ] Each card has all five standard fields plus INCUMBENT designation
  [ ] INCUMBENT inertia anchor names the specific Phase 0A row declared in Phase 0C (exact match)
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript includes at least one question naming the Phase 0C anchor directly
      (satisfies Phase 0C exit gate downstream propagation obligation for Phase 2)
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; a Phase 3 gate that checks tag presence without citing
      the Phase 0A gate contract does not satisfy this criterion
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregate findings across all subjects
2. DISPOSITION ARC — trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER — at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING — adjust evidence weights by declared blind spots; per-blind-spot
   resolution conditions specified
5. INERTIA PROFILE ACCOUNTING — for each Phase 0A stickiness factor, name which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA — iterate Phase 0C per-tier predictions; classify each as CONFIRMED /
   CONTRADICTED / ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION — two separately populated lists

Then produce NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table completeness: both boundary rows populated (upper and lower);
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type — this is a
      structural failure detectable by row count without reading any cell content, not a format
      deviation; a gate that requires "completeness" without naming the single-row failure condition
      explicitly does not satisfy this criterion
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section
