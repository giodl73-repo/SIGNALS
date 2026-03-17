Written to `simulations/quest/golden/prove-interview-golden-2026-03-15.md`.

The golden document contains:

1. **Frontmatter** — skill, target, date, rounds: 20, rubric v19, score: 90, status: GOLDEN

2. **Prompt body** — simplified V-05 (1425 words, 13.2% reduction, all essential criteria preserved)

3. **What made it golden** — 5 patterns:
   - Chain-critical gate items first with inline rationale (C-49 + C-52)
   - Propagation obligations at source with phase-differentiated constraints (C-50 + C-53)
   - Bidirectional contract closure: source warns, receiver cites and adds anti-parallel gate item (C-51 + C-54)
   - Five-phase gated chain: INCUMBENT anchor traced from 0A through 0C → 1 → 2 by name
   - Verdict system pre-declared before any evidence (Phase 0B-I + 0B-II)

4. **Rubric summary** — essential (5/5 PASS), recommended (2.5/3), aspirational passing criteria, and 11 open gaps for future rounds
 the
ordering decision is declared in the text, not inferred from sequence.

**2. Propagation obligations declared at source with phase-specific constraints (C-50 + C-53)**
The Phase 0C EXIT GATE names both downstream obligations in a single block at the source -- with
*differentiated* constraints: Phase 1 gets "exact-match required" and Phase 2 gets "direct-question
required." Each downstream phase receives a distinct enforcement mechanism, making the chain auditable
at each phase transition rather than requiring reconstruction across phases.

**3. Contract source named at declaration with bidirectional closure (C-51 + C-54)**
Phase 0A declares itself the authoritative contract source and warns against parallel contracts
downstream ("a tag list reproduced at Phase 3 without citing this gate creates a parallel contract").
Phase 3 closes the chain in both directions: its first gate item cites the Phase 0A contract source
and adds its own anti-parallel-contract enforcement. The chain cannot silently split.

**4. Five-phase gated structure with cross-phase evidence chain**
The INCUMBENT anchor is declared in Phase 0A (INERTIA PROFILE TABLE), named in Phase 0C (chain
obligation), exact-matched in Phase 1 (subject card), and directly questioned in Phase 2 (transcript).
Each phase commits to the prior phase's output by name -- making any break auditable at the phase
that names its predecessor.

**5. Verdict system pre-declared before evidence (Phase 0B-I + 0B-II)**
Constitutive definitions for all five verdict levels and all four margin pairs are declared before any
subject card is designed. The verdict classification at Phase 4 is not post-hoc framing -- it is
measured against definitions established before the evidence was collected.

---

## Prompt Body

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
  [ ] No new evidence introduced in this section

---

## Final Rubric Criteria Summary

**Rubric version:** v19 | **Denominator:** 49

### Essential (60 pts) -- 5/5 PASS

| ID | Criterion | Status |
|----|-----------|--------|
| C-01 | Persona identity declared before interview | PASS |
| C-02 | Prior knowledge scoped (experience + gaps) | PASS |
| C-03 | Answers in persona voice | PASS |
| C-04 | Evidence explicitly extracted in dedicated phase | PASS |
| C-05 | SURPRISING/CONFIRMING labeled with prior expectation | PASS |

### Recommended (30 pts) -- 2.5/3

| ID | Criterion | Status |
|----|-----------|--------|
| C-06 | Questions probe declared concerns; at least one follow-up anchored to prior answer | PARTIAL |
| C-07 | Multiple distinct personas (INCUMBENT/CHAMPION/EVALUATOR/SKEPTIC) | PASS |
| C-08 | Evidence signal-typed (RISK/PREFERENCE/CONSTRAINT/VALIDATION/INVALIDATION) | PASS |

### Aspirational (10 pts) -- key passing criteria on v19 axis

| ID | Criterion | Status |
|----|-----------|--------|
| C-09 | Cross-interview synthesis section | PASS |
| C-13 | Expectation register pre-populated (Phase 0C per-tier predictions) | PASS |
| C-15 | Phase-criterion ownership explicit (numbered + gated phases) | PASS |
| C-17 | Evidence strength-rated with rationale | PASS |
| C-19 | Subject sequence justified (ADJACENCY blocks) | PASS |
| C-20 | Phase completion gated (explicit EXIT GATE at each phase) | PASS |
| C-21 | Objection lifecycle tracked (DISPOSITION ARC) | PARTIAL |
| C-23 | Subject evidential function declared (ADJACENCY blocks) | PARTIAL |
| C-24 | Epistemic standing adjusts synthesis weight | PARTIAL |
| C-49 | Chain-critical gate items ordered first | PASS |
| C-50 | Propagating gate declares downstream obligations at source | PASS |
| C-51 | Contract source named at declaration | PASS |
| C-52 | Gate-item ordering rationale declared at item | PASS |
| C-53 | Propagation obligations phase-differentiated with distinct per-phase constraint | PASS |
| C-54 | Contract closure bidirectional -- receiving gate cites source + anti-parallel item | PASS |

### Open gaps (targets for future rounds)

| ID | Criterion | Gap |
|----|-----------|-----|
| C-10 | Simulation fidelity annotated | No meta-note distinguishing grounded from constructed claims |
| C-11 | Voice divergence acknowledged | No explicit voice contrast observation |
| C-12 | Follow-up origin visible | Follow-ups not anchored to specific prior answer moments |
| C-14 | INCONCLUSIVE label used where applicable | No three-label decision taxonomy declared |
| C-16 | Format templates embedded | No SURPRISING (expected: X, got: Y) template in body |
| C-18 | Evidence basis declared (verbatim/inferred/corroborated) | No origin-of-claim taxonomy |
| C-22 | Vocabulary signature declared as auditable contract | No 2-3 role-specific terms per subject |
| C-25 | Format template bridged to expectation register | No structural link between Phase 0C register and C-05 template |
| C-27 | Dual evidence taxonomy kept distinct | Only signal type + strength; no experience-proximity axis |
| C-28 | Moment-label decision taxonomy declared | No three-label decision rules declared before transcripts |
| C-29 | Schema-level template instantiated by example | No populated example row in gate structures |
