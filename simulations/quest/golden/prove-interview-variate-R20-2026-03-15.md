# prove-interview — Skill Body Variations — R20

**Skill:** prove-interview
**Round:** 20
**Rubric version:** v18
**Date:** 2026-03-15

---

## R20 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|---|---|---|---|
| V-01 | Single | C-49 absent, C-50 absent, C-51 absent — gate items in arbitrary order; no downstream propagation obligations at source; no contract-source declaration at vocabulary gate | When chain-critical gate items are not ordered first, no propagation obligations are declared at source gates, and no contract-source warnings appear, three independent auditability gaps coexist: the chain link from Phase 0C to Phase 1/2 requires cross-phase inspection to verify; the Phase 0A vocabulary contract can be silently reproduced downstream without attribution; and the design intent behind vocabulary enforcement must be reconstructed from surrounding prose rather than read at gate entry |
| V-02 | Single | C-49 present, C-50 absent, C-51 absent — chain-critical items ordered first in all gate blocks with gate-block-first rationale; no downstream propagation obligations; no contract-source declaration | When chain-critical gate items are placed first in each gate block with explicit gate-block-first rationale, each chain link becomes auditable at gate entry without reading through affirmative completion conditions; propagation obligations remain undeclared at source gates, leaving the obligation chain reconstructable only by cross-phase inspection; vocabulary contract-source attribution is absent; C-49 contribution is isolated |
| V-03 | Single | C-50 present, C-49 absent, C-51 absent — downstream propagation obligations declared at Phase 0C source gate; chain-critical items not ordered first; no contract-source declaration | When Phase 0C explicitly enumerates what each downstream phase must enforce, the propagation chain is traceable from source outward; chain-critical items are not ordered first, so a scorer reading Phase 0C must pass through affirmative tier-sequence items before reaching the INCUMBENT anchor condition; vocabulary contract-source attribution absent; C-50 contribution is isolated |
| V-04 | Combined | C-49 present, C-50 present, C-51 absent — gate-block-first ordering and downstream propagation obligations both present; no contract-source declaration | When gate-block-first ordering and source-declared propagation obligations are combined, the Phase 0C exit gate makes both the chain-critical condition and its downstream obligations auditable from a single reading; the vocabulary contract in Phase 0A still lacks contract-source attribution, leaving silent parallel contract creation at Phase 3 unclosed |
| V-05 | Combined | C-49 present, C-50 present, C-51 present — full target: gate-block-first ordering, downstream propagation obligations at source, and contract-source declaration with parallel-contract warning | When all three criteria are satisfied, each gate block surfaces its chain-critical condition first with rationale; Phase 0C declares both the INCUMBENT anchor first and its propagation obligations in a single named block; Phase 0A names itself as the authoritative contract source and warns that Phase 3 reproduction without citation creates a parallel contract |

---

## V-01 — C-49 Absent, C-50 Absent, C-51 Absent

**Variation axis:** Lifecycle emphasis — gate-block-first ordering absent from all gate blocks; no downstream propagation obligations declared at any source gate; no contract-source declaration at vocabulary gate
**Hypothesis:** When chain-critical gate items are not ordered first, no propagation obligations are declared at source gates, and no contract-source warnings appear, three independent auditability gaps coexist: the chain link from Phase 0C to Phase 1/2 requires cross-phase inspection to verify; the Phase 0A vocabulary contract can be silently reproduced downstream without attribution; and the design intent behind each gate condition must be reconstructed from surrounding prose rather than read at the gate item itself. No single gate item in this variation is self-auditing for chain obligation or contract authority.

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

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of margin declarations is absent from this sub-section
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC

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
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (non-blank, non-generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): must match the Phase 0C anchor

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present in tier sequence
  [ ] Each card has all five standard fields plus INCUMBENT designation
  [ ] INCUMBENT inertia anchor is non-blank
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate
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
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag not present in the Phase 0A exit gate
      vocabulary declaration is a gate failure
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS -- aggregate findings across all subjects
2. DISPOSITION ARC -- trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER -- at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING -- adjust evidence weights by declared blind spots; per-blind-spot
   resolution conditions specified
5. INERTIA PROFILE ACCOUNTING -- for each Phase 0A stickiness factor, name which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA -- iterate Phase 0C per-tier predictions; classify each as CONFIRMED /
   CONTRADICTED / ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION -- two separately populated lists

Then produce NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table completeness: both boundary rows populated (upper and lower);
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-02 -- C-49 Present, C-50 Absent, C-51 Absent

**Variation axis:** Lifecycle emphasis -- chain-critical gate items ordered first in every gate block with explicit gate-block-first rationale (C-49 satisfied); no downstream propagation obligations declared at any source gate (C-50 absent); no contract-source declaration at vocabulary gate (C-51 absent)
**Hypothesis:** When chain-critical items are placed first in each gate block with explicit rationale naming why first-position was chosen, each gate's chain-critical condition becomes auditable at gate entry without reading through affirmative completion conditions. Propagation obligations remain undeclared at source gates: Phase 1 and Phase 2 still carry their own enforcement conditions, but the obligation chain is not visible from Phase 0C outward -- it must be reconstructed by reading both the source gate and the downstream gates. Vocabulary contract-source attribution is absent, leaving parallel contract creation at Phase 3 unwarned. C-49's contribution to gate-entry auditability is isolated; C-50 and C-51 gaps are preserved.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A -- INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
      -- this condition is the first gate item because gate-block-first placement makes vocabulary
      compliance immediately auditable at gate entry without reading through table-completeness conditions
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I -- VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it -- what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II -- VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor -- the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of margin declarations is absent from this sub-section
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C -- TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC

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

PHASE 0C EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT anchor declared as named output: names specific Phase 0A row and stickiness factor
      -- this condition is the first gate item because gate-block-first placement makes the INCUMBENT
      chain obligation immediately auditable at gate entry without reading through affirmative
      completion conditions
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 -- SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (non-blank, non-generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): must match the Phase 0C anchor exactly

PHASE 1 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording
      -- this condition is the first gate item because gate-block-first placement makes the INCUMBENT
      chain link immediately auditable at gate entry without reading through card-completeness conditions
  [ ] Four subject cards present in tier sequence
  [ ] Each card has all five standard fields plus INCUMBENT designation
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 -- TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate -- this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 -- EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure -- this condition is the first gate item because
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry without
      reading through affirmative completion conditions
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 -- SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS -- aggregate findings across all subjects
2. DISPOSITION ARC -- trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER -- at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING -- adjust evidence weights by declared blind spots; per-blind-spot
   resolution conditions specified
5. INERTIA PROFILE ACCOUNTING -- for each Phase 0A stickiness factor, name which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA -- iterate Phase 0C per-tier predictions; classify each as CONFIRMED /
   CONTRADICTED / ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION -- two separately populated lists

Then produce NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table completeness: both boundary rows populated (upper and lower);
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-03 -- C-50 Present, C-49 Absent, C-51 Absent

**Variation axis:** Inertia framing -- downstream propagation obligations declared at Phase 0C source gate naming each downstream phase and its specific enforcement constraint (C-50 satisfied); chain-critical items not ordered first in gate blocks (C-49 absent); no contract-source declaration at vocabulary gate (C-51 absent)
**Hypothesis:** When Phase 0C explicitly enumerates what Phase 1 and Phase 2 must each enforce regarding the INCUMBENT anchor, the propagation chain becomes traceable from source outward -- a scorer reading Phase 0C can see the full chain without inspecting Phase 1 or Phase 2 separately. Gate items are not ordered by chain-criticality, so reaching the INCUMBENT anchor condition in Phase 0C requires reading through affirmative tier-sequence and per-tier-prediction items first. Vocabulary contract-source attribution is absent, leaving the Phase 0A tag vocabulary reproducible at Phase 3 without attribution warning. C-50's contribution to source-declared propagation auditability is isolated; C-49 and C-51 gaps are preserved.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A -- INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I -- VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it -- what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II -- VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor -- the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of margin declarations is absent from this sub-section
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C -- TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC

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

PHASE 0C EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] INCUMBENT anchor declared as named output: names specific Phase 0A row and stickiness factor
      Downstream propagation obligations declared at this gate:
        - Phase 1: INCUMBENT subject card inertia anchor field must match this named row exactly
          (exact-match required -- a paraphrase does not satisfy the Phase 1 obligation)
        - Phase 2: at least one question in the INCUMBENT transcript must name this anchor directly
          (direct-question required -- referencing the topic without naming the anchor does not satisfy)
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 -- SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (non-blank, non-generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): must match the Phase 0C anchor exactly
    (exact-match required per Phase 0C exit gate propagation obligation)

PHASE 1 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present in tier sequence
  [ ] Each card has all five standard fields plus INCUMBENT designation
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 -- TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 -- EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag not present in Phase 0A exit gate vocabulary
      is a gate failure
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 -- SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS -- aggregate findings across all subjects
2. DISPOSITION ARC -- trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER -- at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING -- adjust evidence weights by declared blind spots; per-blind-spot
   resolution conditions specified
5. INERTIA PROFILE ACCOUNTING -- for each Phase 0A stickiness factor, name which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA -- iterate Phase 0C per-tier predictions; classify each as CONFIRMED /
   CONTRADICTED / ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION -- two separately populated lists

Then produce NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table completeness: both boundary rows populated (upper and lower);
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-04 -- C-49 Present, C-50 Present, C-51 Absent

**Variation axis:** Combined -- gate-block-first ordering (C-49) and downstream propagation obligations at source gate (C-50) are both present; no contract-source declaration at vocabulary gate (C-51 absent)
**Hypothesis:** When gate-block-first ordering and source-declared propagation obligations are combined, the Phase 0C exit gate becomes fully self-auditing for the INCUMBENT chain: the chain-critical anchor condition appears first with explicit rationale, and the obligations it propagates to Phase 1 and Phase 2 are named inline at the source -- a scorer reading only Phase 0C can verify the chain without inspecting any downstream gate. The vocabulary contract in Phase 0A still lacks contract-source attribution: Phase 3 can reproduce the tag vocabulary without citing Phase 0A, creating a silent parallel contract. A scorer detecting vocabulary drift at Phase 3 cannot confirm from Phase 3 alone whether the drift constitutes a contract violation unless they inspect Phase 0A. C-51 gap is isolated as the remaining auditability hole.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A -- INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
      -- this condition is the first gate item because gate-block-first placement makes vocabulary
      compliance immediately auditable at gate entry without reading through table-completeness conditions
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I -- VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it -- what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II -- VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor -- the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of margin declarations is absent from this sub-section
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C -- TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC

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

PHASE 0C EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT anchor declared as named output: names specific Phase 0A row and stickiness factor
      -- this condition is the first gate item because gate-block-first placement makes the INCUMBENT
      chain obligation immediately auditable at gate entry without reading through affirmative
      completion conditions
      Downstream propagation obligations declared at this gate:
        - Phase 1: INCUMBENT subject card inertia anchor field must match this named row exactly
          (exact-match required -- a paraphrase does not satisfy the Phase 1 obligation)
        - Phase 2: at least one question in the INCUMBENT transcript must name this anchor directly
          (direct-question required -- referencing the topic without naming the anchor does not satisfy)
      These obligations are declared at the source so any chain break is auditable at the phase
      that names its predecessor rather than requiring inspection of the downstream phase alone.
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 -- SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (non-blank, non-generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): must match the Phase 0C anchor exactly
    (exact-match required per Phase 0C exit gate propagation obligation)

PHASE 1 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording
      -- this condition is the first gate item because gate-block-first placement makes the INCUMBENT
      chain link immediately auditable at gate entry without reading through card-completeness conditions
  [ ] Four subject cards present in tier sequence
  [ ] Each card has all five standard fields plus INCUMBENT designation
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 -- TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate -- this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 -- EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure -- this condition is the first gate item because
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry without
      reading through affirmative completion conditions
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 -- SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS -- aggregate findings across all subjects
2. DISPOSITION ARC -- trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER -- at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING -- adjust evidence weights by declared blind spots; per-blind-spot
   resolution conditions specified
5. INERTIA PROFILE ACCOUNTING -- for each Phase 0A stickiness factor, name which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA -- iterate Phase 0C per-tier predictions; classify each as CONFIRMED /
   CONTRADICTED / ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION -- two separately populated lists

Then produce NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table completeness: both boundary rows populated (upper and lower);
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-05 -- C-49 Present, C-50 Present, C-51 Present

**Variation axis:** Combined -- full target: gate-block-first ordering at all applicable gates (C-49), downstream propagation obligations declared at source gate (C-50), and contract-source declaration at vocabulary gate with parallel-contract warning (C-51)
**Hypothesis:** When all three criteria are satisfied, each gate block surfaces its chain-critical condition first with explicit gate-block-first rationale; the Phase 0C exit gate declares both the INCUMBENT anchor (first, chain-critical) and its propagation obligations to Phase 1 and Phase 2 in a single named block at the source; the Phase 0A vocabulary gate names itself as the authoritative contract source and warns that a Phase 3 tag list not citing this gate creates a parallel contract. A scorer reading any single gate item reaches the chain-critical condition first; a scorer reading Phase 0C alone can audit the full chain without inspecting Phase 1 or Phase 2; a scorer detecting a Phase 3 vocabulary deviation can identify it as a contract violation without inspecting Phase 0A. These three properties are independently auditable -- each gate item is self-contained for its obligation.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## PHASE 0A -- INERTIA PROFILE

Before designing any subject card, enumerate the practices being displaced.

For each practice:
  - Practice name
  - Stickiness factor (the specific reason this practice persists despite alternatives)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
      This declaration is the contract source -- Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere; a tag list reproduced at Phase 3 without citing
      this gate creates a parallel contract and does not close the mid-chain drift gap.
      -- this condition is the first gate item because gate-block-first placement makes vocabulary
      compliance and contract authority immediately auditable at gate entry without reading through
      table-completeness conditions
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I -- VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it -- what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II -- VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor -- the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of margin declarations is absent from this sub-section
  [ ] All four margin pairs have a named deciding factor
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C -- TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

Tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC

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

PHASE 0C EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT anchor declared as named output: names specific Phase 0A row and stickiness factor
      -- this condition is the first gate item because gate-block-first placement makes the INCUMBENT
      chain obligation immediately auditable at gate entry without reading through affirmative
      completion conditions
      Downstream propagation obligations declared at this gate:
        - Phase 1: INCUMBENT subject card inertia anchor field must match this named row exactly
          (exact-match required -- a paraphrase does not satisfy the Phase 1 obligation)
        - Phase 2: at least one question in the INCUMBENT transcript must name this anchor directly
          (direct-question required -- referencing the topic without naming the anchor does not satisfy)
      These obligations are declared at the source so any chain break is auditable at the phase
      that names its predecessor rather than requiring inspection of the downstream phase alone.
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 -- SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots (non-blank, non-generic)
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): must match the Phase 0C anchor exactly
    (exact-match required per Phase 0C exit gate propagation obligation)

PHASE 1 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording
      -- this condition is the first gate item because gate-block-first placement makes the INCUMBENT
      chain link immediately auditable at gate entry without reading through card-completeness conditions;
      compliance is with the Phase 0C exit gate propagation obligation, not with any paraphrase of
      the anchor reproduced here without citing that gate
  [ ] Four subject cards present in tier sequence
  [ ] Each card has all five standard fields plus INCUMBENT designation
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 -- TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4-6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate -- this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions; compliance is with the Phase 0C exit gate
      propagation obligation, not with any generalized "address the incumbent" instruction
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices

---

## PHASE 3 -- EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure -- this condition is the first gate item because
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry without
      reading through affirmative completion conditions; compliance is with the Phase 0A exit gate
      contract source, not with any tag list reproduced at Phase 3 without citing that gate
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL); a tag list reproduced here without citing
      Phase 0A as contract source creates a parallel contract and does not satisfy this condition
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 -- SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS -- aggregate findings across all subjects
2. DISPOSITION ARC -- trace per-subject disposition shift or hold
3. CONTRADICTION REGISTER -- at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING -- adjust evidence weights by declared blind spots; per-blind-spot
   resolution conditions specified
5. INERTIA PROFILE ACCOUNTING -- for each Phase 0A stickiness factor, name which evidence items
   addressed it (by PROFILE RELEVANCE tag) and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA -- iterate Phase 0C per-tier predictions; classify each as CONFIRMED /
   CONTRADICTED / ABSENT / PARTIAL, naming specific Phase 3 evidence items
7. INERTIA / ADOPTION PARTITION -- two separately populated lists

Then produce NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] All seven synthesis sections present and non-empty
  [ ] Net verdict drawn from Phase 0B-I defined levels
  [ ] VERDICT MARGIN AUDIT table completeness: both boundary rows populated (upper and lower);
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section
