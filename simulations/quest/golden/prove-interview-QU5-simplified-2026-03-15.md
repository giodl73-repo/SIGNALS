# prove-interview — QU5 Simplified Golden
**Date:** 2026-03-15
**Source:** prove-interview-variate-R20-2026-03-15.md V-05
**Rubric target:** v19 (C-01 through C-54)

---

## Simplification report

| Item | Removed or compressed | Words |
|------|-----------------------|-------|
| Phase 0A EXIT GATE item 1 rationale tail | compressed "because gate-block-first placement makes vocabulary compliance and contract authority immediately auditable at gate entry without reading through table-completeness conditions" → "first gate item: gate-block-first placement makes vocabulary compliance and contract authority auditable at gate entry" | ~13 |
| Phase 0A EXIT GATE parallel-contract tail | removed "and does not close the mid-chain drift gap" | ~8 |
| Phase 0B-I body description clause | removed "-- what pattern of evidence types across subjects places the finding at this level. A level name without a constitutive definition does not satisfy this gate." | ~28 |
| Phase 0B-II body descriptor | removed " -- the specific evidence property that tips the verdict from one level to the other" | ~16 |
| Phase 0C EXIT GATE item 1 rationale tail | compressed "immediately auditable at gate entry without reading through affirmative completion conditions" → "auditable at gate entry" | ~16 |
| Phase 0C EXIT GATE Phase 1 propagation clarification | "(exact-match required -- a paraphrase does not satisfy the Phase 1 obligation)" → "(exact-match required)" | ~10 |
| Phase 0C EXIT GATE Phase 2 propagation clarification | "(direct-question required -- referencing the topic without naming the anchor does not satisfy)" → "(direct-question required)" | ~12 |
| Phase 0C EXIT GATE explanatory tail sentence | removed "These obligations are declared at the source so any chain break is auditable at the phase that names its predecessor rather than requiring inspection of the downstream phase alone." | ~33 |
| Phase 1 body exact-match parenthetical | removed "(exact-match required per Phase 0C exit gate propagation obligation)" from Inertia anchor line | ~10 |
| Phase 1 body blind spots qualifier | removed "(non-blank, non-generic)" — enforced at gate | ~4 |
| Phase 1 EXIT GATE item 1 rationale tail | compressed → "-- first gate item: gate-block-first placement makes the INCUMBENT chain link auditable at gate entry" | ~15 |
| Phase 2 body direct-question parenthetical | removed "(direct-question required per Phase 0C exit gate propagation obligation)" | ~10 |
| Phase 2 body duplicate ordering statement | removed "All four transcripts must be complete before any hypothesis question section begins." (duplicate of opening line) | ~14 |
| Phase 2 EXIT GATE item 1 rationale tail | compressed → "-- first gate item: gate-block-first placement makes the INCUMBENT chain obligation auditable at gate entry" | ~15 |
| Phase 3 body tag list | removed "(STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)" — already declared in Phase 0A gate | ~6 |
| Phase 3 EXIT GATE item 1 rationale tail | compressed → "-- first gate item: gate-block-first placement makes vocabulary drift auditable at gate entry" | ~18 |
| Phase 3 EXIT GATE item 4 tag list | removed "(STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)" — already in item 1 | ~6 |

**What was NOT removed:** all five gate-block-first rationale statements (C-52), all propagation obligation bullets with phase-specific constraints (C-53), contract-source declaration with parallel-contract warning at Phase 0A (C-51), receiving-gate citations with anti-parallel-contract items at Phase 1/Phase 2/Phase 3 (C-54), all structural instruction content (phase bodies, field lists, tier sequence, adjacency block format, synthesis sections, verdict table template).

**Criteria preserved:** C-49 (gate-block-first ordering at all applicable gates), C-50 (propagation obligations declared at source), C-51 (contract source declaration at Phase 0A), C-52 (inline ordering rationale at each gate-critical item), C-53 (phase-differentiated obligations: exact-match vs direct-question), C-54 (bidirectional contract closure: Phase 3 cites Phase 0A and adds anti-parallel gate item).

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
      this gate creates a parallel contract.
      -- first gate item: gate-block-first placement makes vocabulary compliance and contract
      authority auditable at gate entry
  [ ] INERTIA PROFILE TABLE has at least two practice rows
  [ ] Each row has a stickiness factor that is not blank, not generic
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I -- VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it.

PHASE 0B-I EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II -- VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

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
      -- first gate item: gate-block-first placement makes the INCUMBENT chain obligation auditable
      at gate entry
      Downstream propagation obligations declared at this gate:
        - Phase 1: INCUMBENT subject card inertia anchor field must match this named row exactly
          (exact-match required)
        - Phase 2: at least one question in the INCUMBENT transcript must name this anchor directly
          (direct-question required)
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] No verdict threshold or margin content appears here

---

## PHASE 1 -- SUBJECT DESIGN

Design subject cards in tier sequence: INCUMBENT -> CHAMPION -> EVALUATOR -> SKEPTIC.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate sub-fields)
  - Blind spots
  - Disposition
  - Primary concern
  - INCUMBENT designation label (INCUMBENT subject only)
  - Inertia anchor (INCUMBENT only): must match the Phase 0C anchor exactly

PHASE 1 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording
      -- first gate item: gate-block-first placement makes the INCUMBENT chain link auditable at
      gate entry; compliance is with the Phase 0C exit gate propagation obligation, not with any
      paraphrase of the anchor reproduced here without citing that gate
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

PHASE 2 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate -- first gate item: gate-block-first placement makes the
      INCUMBENT chain obligation auditable at gate entry; compliance is with the Phase 0C exit gate
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

PHASE 3 EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag in a Phase 3 evidence item not in the
      Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
      is a gate failure -- first gate item: gate-block-first placement makes vocabulary drift
      auditable at gate entry; compliance is with the Phase 0A exit gate contract source, not with
      any tag list reproduced at Phase 3 without citing that gate
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract;
      a tag list reproduced here without citing Phase 0A as contract source creates a parallel
      contract and does not satisfy this condition
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
