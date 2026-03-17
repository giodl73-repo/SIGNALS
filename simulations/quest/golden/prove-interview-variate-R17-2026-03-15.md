# prove-interview — Skill Body Variations — R17

**Skill:** prove-interview
**Round:** 17
**Rubric version:** v17
**Date:** 2026-03-15

---

## R17 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|---|---|---|---|
| V-01 | Single | C-46 absent, C-47 absent — anti-drift clause and INCUMBENT anchor both gate-interior but not first | When Phase 3 has C-44 (anti-drift clause as gate condition) but an affirmative item opens the gate block, and Phase 2 has C-45 (INCUMBENT anchor as gate condition) but an affirmative item opens that gate block, both audit points require reading past the first gate item to locate the failure condition — the gate-block-first ordering requirement fails at both positions independently |
| V-02 | Single | C-46 present, C-47 absent — Phase 3 anti-drift clause is gate-block-first; Phase 2 INCUMBENT anchor is interior but not first | When Phase 3 gate opens with the anti-drift enforcement clause (C-46 satisfied), vocabulary drift is immediately auditable at gate entry; Phase 2 gate has INCUMBENT anchor as gate-interior condition (C-45 satisfied) but an affirmative completion item opens the Phase 2 gate block before the anchor condition, requiring the scorer to read past the first item to verify chain enforcement |
| V-03 | Single | C-47 present, C-46 absent — Phase 2 INCUMBENT anchor is gate-block-first; Phase 3 anti-drift clause is interior but not first | When Phase 2 gate opens with the INCUMBENT anchor condition (C-47 satisfied), chain enforcement is immediately auditable at Phase 2 gate entry; Phase 3 gate has anti-drift enforcement clause (C-44 satisfied) but an affirmative item opens the Phase 3 gate block before the clause, requiring the scorer to read past the first item to detect vocabulary drift |
| V-04 | Combined | C-46 + C-47 both gate-block-first | When both Phase 3 and Phase 2 gates open with their respective failure conditions — anti-drift enforcement clause first in Phase 3 (C-46), INCUMBENT anchor condition first in Phase 2 (C-47) — both audit points are immediately visible at gate entry without reading through affirmative conditions; the positional parallel of C-34's prohibition-first requirement operates at two downstream gates simultaneously |
| V-05 | Combined | Full v17 apparatus (all accumulated criteria with explicit ordering rationale at each gate-block-first position) | When every gate-block-first ordering requirement is satisfied with explicit rationale — PROHIBITED clauses open 0B sub-phase gates (C-34/C-43), anti-drift enforcement clause opens Phase 3 gate (C-46), INCUMBENT anchor opens Phase 2 gate (C-47) — the failure condition at each gate is evaluable by reading only the first checklist item; the full apparatus closes the last positional gap: C-44 and C-45 can be satisfied with the failure conditions buried after affirmative items; C-46 and C-47 require them at position one |

Single-axis variations: V-01 (both absent — interior but not first), V-02 (C-46 present, C-47 absent), V-03 (C-47 present, C-46 absent)
Combined variations: V-04 (C-46 + C-47 together), V-05 (full v17 apparatus)

New R17 territory probed:
- **Affirmative-first as isolation control** (V-01): Phase 3 and Phase 2 gates both satisfy their predecessor criteria (C-44 and C-45) but open with affirmative completion items, placing the failure conditions in interior positions; C-46 and C-47 both fail
- **C-46 gate-block-first** (V-02, V-04, V-05): Phase 3 gate opens with the anti-drift enforcement clause; vocabulary drift detectable by reading only the first gate item
- **C-47 gate-block-first** (V-03, V-04, V-05): Phase 2 gate opens with the INCUMBENT anchor condition; chain enforcement detectable by reading only the first gate item
- **C-46 and C-47 independence** (V-04): Both positional criteria satisfied simultaneously without requiring any structural change beyond gate item ordering; predecessor criteria (C-44, C-45) still satisfied
- **Full ordering rationale** (V-05): Each gate-block-first position carries an explicit rationale clause naming why the first-position placement is required, making the ordering auditable as intent rather than coincidence

---

## V-01 — C-46 Absent, C-47 Absent: Affirmative-First at Both Positions

**Variation axis:** Lifecycle emphasis — Phase 3 gate has anti-drift enforcement clause (C-44 satisfied) but an affirmative item opens the gate block before it; Phase 2 gate has INCUMBENT anchor condition (C-45 satisfied) but an affirmative item opens the gate block before it
**Hypothesis:** When both C-44 and C-45 are satisfied — the anti-drift clause exists as a Phase 3 gate condition and the INCUMBENT anchor exists as a Phase 2 gate condition — but affirmative completion items open both gate blocks before the failure conditions appear, a scorer reading only the first gate item at either phase encounters a completion check rather than a failure condition. Both audit points require reading through affirmative items to locate the failure condition. This is the structural gap that C-46 and C-47 are designed to close: the clause or condition is present but its positional placement does not make it immediately auditable at gate entry.

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

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — this condition is verifiable by reading the Phase 2 transcript
      and this gate item without inspecting Phase 0C; the anchor is doubly enforced: declared at
      the source (Phase 0C exit gate, satisfying C-41) and required at this receiving phase boundary
      (this gate item, satisfying C-45)

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
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; a Phase 3 gate that checks tag presence without citing
      the Phase 0A gate contract does not satisfy C-40
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure — non-conforming tags are detectable by reading
      only this gate condition against the evidence items without inspecting Phase 0A body text;
      naming the Phase 0A contract source (C-40) without stating this failure condition is protection
      by implication only and does not constitute enforcement (C-44)
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

---

## V-02 — C-46 Present, C-47 Absent: Phase 3 Anti-Drift Clause is Gate-Block-First

**Variation axis:** Lifecycle emphasis — Phase 3 gate opens with anti-drift enforcement clause (C-46 satisfied); Phase 2 gate has INCUMBENT anchor condition (C-45 satisfied) but an affirmative item opens the Phase 2 gate block before the anchor condition
**Hypothesis:** When Phase 3 gate opens with the anti-drift enforcement clause, vocabulary drift is detectable by reading only the first gate item without scanning through affirmative conditions. The Phase 3 audit point is maximally auditable: a scorer can determine whether a non-conforming PROFILE RELEVANCE tag is a gate failure at gate entry. Phase 2 retains the INCUMBENT anchor as a gate-interior condition (C-45 satisfied) but affirmative items open the gate block before it — chain enforcement at Phase 2 requires the scorer to read past the completion checks to locate the anchor requirement. This isolates C-46's positional contribution: Phase 3 audit is gate-entry-auditable; Phase 2 audit is gate-interior-only.

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

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C prediction
  [ ] Answers written in distinct subject voices
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — this condition is verifiable by reading the Phase 2 transcript
      and this gate item without inspecting Phase 0C; the anchor is doubly enforced: declared at
      the source (Phase 0C exit gate, satisfying C-41) and required at this receiving phase boundary
      (this gate item, satisfying C-45)

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
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure — gate-block-first placement makes this failure
      condition immediately auditable at gate entry without reading through affirmative completion
      conditions; naming the Phase 0A contract source without stating this failure condition is
      protection by implication only and does not constitute enforcement
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; a Phase 3 gate that checks tag presence without citing
      the Phase 0A gate contract does not satisfy C-40
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

---

## V-03 — C-47 Present, C-46 Absent: Phase 2 INCUMBENT Anchor is Gate-Block-First

**Variation axis:** Inertia framing — Phase 2 gate opens with INCUMBENT anchor condition (C-47 satisfied); Phase 3 gate has anti-drift enforcement clause (C-44 satisfied) but an affirmative item opens the Phase 3 gate block before the clause
**Hypothesis:** When Phase 2 gate opens with the INCUMBENT anchor condition, the chain obligation declared at Phase 0C is doubly enforced and verifiable at Phase 2 gate entry — reading the first gate item tells the scorer whether INCUMBENT chain enforcement is required. The Phase 3 audit point retains the anti-drift enforcement clause (C-44 satisfied) but affirmative items open the gate block before it — vocabulary drift requires reading past the first gate item to locate the failure condition. This isolates C-47's positional contribution: Phase 2 INCUMBENT chain is gate-entry-auditable; Phase 3 drift detection requires gate-interior reading.

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

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — gate-block-first placement makes this obligation immediately
      auditable at gate entry without reading through affirmative completion conditions; the anchor
      is doubly enforced: declared at the source (Phase 0C exit gate, satisfying C-41) and required
      at this receiving phase boundary as the first gate condition (satisfying C-45 and C-47)
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
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; a Phase 3 gate that checks tag presence without citing
      the Phase 0A gate contract does not satisfy C-40
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure — non-conforming tags are detectable by reading
      only this gate condition against the evidence items without inspecting Phase 0A body text;
      naming the Phase 0A contract source (C-40) without stating this failure condition is protection
      by implication only and does not constitute enforcement (C-44)
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

---

## V-04 — C-46 + C-47 Combined: Both Gates Open With Failure Condition First

**Variation axis:** Combined lifecycle emphasis + inertia framing — Phase 3 gate opens with anti-drift enforcement clause (C-46); Phase 2 gate opens with INCUMBENT anchor condition (C-47)
**Hypothesis:** When both Phase 3 and Phase 2 gates are configured failure-condition-first — anti-drift enforcement opens Phase 3, INCUMBENT anchor opens Phase 2 — both audit points are evaluable by reading only the first gate item at each phase. The positional parallel of C-34's prohibition-first requirement operates simultaneously at two downstream gates. A scorer auditing Phase 3 compliance encounters the vocabulary failure condition before any affirmative check; a scorer auditing Phase 2 INCUMBENT chain enforcement encounters the anchor requirement before any completion check. Neither gate requires reading through affirmative items to locate the critical condition. This tests whether both positional requirements can coexist without structural conflict.

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

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — gate-block-first placement makes this obligation immediately
      auditable at gate entry without reading through affirmative completion conditions; the anchor
      is doubly enforced: declared at the source (Phase 0C exit gate, satisfying C-41) and required
      at this receiving phase boundary as the first gate condition (satisfying C-45 and C-47)
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
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure — gate-block-first placement makes this failure
      condition immediately auditable at gate entry without reading through affirmative completion
      conditions; naming the Phase 0A contract source without stating this failure condition is
      protection by implication only and does not constitute enforcement
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; a Phase 3 gate that checks tag presence without citing
      the Phase 0A gate contract does not satisfy C-40
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

---

## V-05 — Full v17 Apparatus: All Gate-Block-First Ordering Requirements With Explicit Rationale

**Variation axis:** Combined — all accumulated structural criteria including C-46 and C-47 with explicit ordering rationale at each gate-block-first position
**Hypothesis:** When every gate-block-first ordering requirement carries an explicit rationale clause naming why the first-position placement is required, the ordering is auditable as structural intent rather than coincidence. V-04 satisfies C-46 and C-47 by positioning alone; V-05 names the positional requirement and its audit consequence inside the gate item text itself, making the design legible without reading the rubric. The pattern: PROHIBITED clauses open 0B sub-phase gates (C-34/C-43, with rationale); anti-drift enforcement clause opens Phase 3 gate (C-46, with rationale); INCUMBENT anchor opens Phase 2 gate (C-47, with rationale). Each first-position condition states: what it requires, why first-position placement matters, and what a gate that buries it after affirmative items fails to provide. This is the full v17 ceiling prompt.

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
  [ ] PROHIBITED: margin-boundary declarations or deciding-factor content is absent from this
      sub-section — gate-block-first placement makes this scope restriction immediately auditable
      at gate entry; a gate that opens with affirmative content checks before stating this
      prohibition cannot be verified by reading only the first gate item
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent from this
      sub-section (level names may be referenced; constitutive definitions must not be restated) —
      gate-block-first placement makes this scope restriction immediately auditable at gate entry;
      a gate that opens with affirmative content checks before stating this prohibition cannot be
      verified by reading only the first gate item
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
      These obligations are declared at the source so any chain break is auditable at the phase
      that names its predecessor rather than requiring inspection of the downstream phase alone.
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

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions; the anchor is doubly enforced at the source
      (Phase 0C exit gate, satisfying C-41) and required at this receiving phase boundary as the
      first gate condition (satisfying C-45 and C-47); a Phase 2 gate whose first checklist item
      is any condition other than this anchor requirement does not satisfy C-47 even when the
      anchor condition is present as a later gate item
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
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure — this condition is the first gate item because
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry without
      reading through affirmative completion conditions; naming the Phase 0A contract source without
      stating this failure condition is protection by implication only (satisfying C-40) and does
      not constitute enforcement (C-44); placing any affirmative completion item before this
      condition satisfies C-44 but fails C-46
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; a Phase 3 gate that checks tag presence without citing
      the Phase 0A gate contract does not satisfy C-40
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

---

## Predicted Criterion Matrix

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-34 | PASS | PASS | PASS | PASS | PASS |
| C-40 | PASS | PASS | PASS | PASS | PASS |
| C-41 | PASS | PASS | PASS | PASS | PASS |
| C-42 | PASS | PASS | PASS | PASS | PASS |
| C-43 | PASS | PASS | PASS | PASS | PASS |
| C-44 | PASS | PASS | PASS | PASS | PASS |
| C-45 | PASS | PASS | PASS | PASS | PASS |
| **C-46** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-47** | **FAIL** | **FAIL** | **PASS** | **PASS** | **PASS** |

**Distinguishing pattern:**
- V-01: Both C-46 and C-47 fail — establishes that C-44 and C-45 can be satisfied while C-46 and C-47 fail independently
- V-02: C-46 passes, C-47 fails — Phase 3 anti-drift is gate-entry-auditable; Phase 2 INCUMBENT anchor requires interior reading
- V-03: C-46 fails, C-47 passes — Phase 2 INCUMBENT chain is gate-entry-auditable; Phase 3 drift detection requires interior reading
- V-04: Both C-46 and C-47 pass — both audit points gate-entry-auditable; no explicit rationale in gate text
- V-05: Both C-46 and C-47 pass with explicit ordering rationale — gate text names why first-position placement is required

**New R17 ceiling:** V-04 and V-05 both satisfy C-46 + C-47. V-05 adds self-documenting rationale, making the design legible without rubric reference.
