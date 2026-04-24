# prove-interview — Skill Body Variations — R19

**Skill:** prove-interview
**Round:** 19
**Rubric version:** v17
**Date:** 2026-03-15

---

## R19 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|---|---|---|---|
| V-01 | Single | C-46 absent, C-47 absent, C-48 absent — gate conditions for anchored content require only non-blank; PROHIBITED clauses use generic category names; no inline failure-mode rationales at gate items | When Phase 1 gate requires only a non-blank anchor, Phase 0B PROHIBITED clauses name generic out-of-scope categories, and gate items carry no embedded rationale, three independent auditability gaps coexist: the Phase 1 chain link is verifiable only by cross-inspecting Phase 0C; the 0B-I/0B-II scope boundary requires reading both gates to detect contamination; and the design intent behind each gate condition must be reconstructed from surrounding prose rather than read at the gate item itself |
| V-02 | Single | C-46 present, C-47 absent, C-48 absent — Phase 1 gate has explicit exact-match condition; PROHIBITED clauses generic; no inline rationales | When Phase 1 exit gate adds a checklist condition explicitly requiring exact-match wording for the INCUMBENT anchor, the Phase 1 chain link becomes auditable at Phase 1 without inspecting Phase 0C; PROHIBITED clauses remain generic, leaving the 0B-I/0B-II scope boundary cross-gate-dependent; no gate item carries an inline failure-mode rationale; C-46 contribution is isolated |
| V-03 | Single | C-47 present, C-46 absent, C-48 absent — Phase 0B PROHIBITED clauses name sibling sub-phase domain by content type; Phase 1 gate non-blank only; no inline rationales | When 0B-I PROHIBITED clause names the 0B-II domain by content type and 0B-II PROHIBITED clause names the 0B-I domain by content type, the 0B-I/0B-II boundary becomes bidirectionally auditable at each gate independently; Phase 1 gate retains non-blank-only anchor condition, leaving the Phase 1 chain link cross-gate-dependent; no inline rationales; C-47 contribution is isolated |
| V-04 | Combined | C-46 present, C-47 present, C-48 absent — exact-match anchor conditions and sibling-domain PROHIBITED clauses both present; no inline failure-mode rationales | When exact-match anchor conditions (C-46) and sibling-domain PROHIBITED clauses (C-47) are both present, the Phase 1 chain link and the 0B-I/0B-II scope boundary are each independently auditable; the absence of inline rationales means design intent must be reconstructed from surrounding prose — compliance is auditable; intent is not |
| V-05 | Combined | C-46 present, C-47 present, C-48 present — full target: exact-match anchor, sibling-domain PROHIBITED clauses, and inline failure-mode rationale at every gate item | When all three criteria are satisfied, each gate item names the condition, how to verify it, and why it exists; a scorer reading any single gate item can determine what is required, how to verify it, and what failure mode the condition prevents; design intent is auditable without contextual reconstruction |

---

## V-01 — C-46 Absent, C-47 Absent, C-48 Absent

**Variation axis:** Lifecycle emphasis — gate conditions for anchored content require only non-blank; PROHIBITED clauses use generic category names; gate items carry no embedded failure-mode rationale
**Hypothesis:** When Phase 1 gate requires only a non-blank anchor, Phase 0B PROHIBITED clauses name generic out-of-scope categories, and gate items carry no inline rationale, three auditability gaps coexist: the Phase 1 chain link requires cross-phase inspection to verify; the 0B-I/0B-II scope boundary requires reading both gates to detect contamination; and the design intent behind each gate condition must be reconstructed from surrounding prose. No single gate item in this variation is self-auditing for intent.

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
        - Phase 2: at least one question in the INCUMBENT transcript must name this anchor directly
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
  - Write 4–6 questions anchored to the subject's declared primary concern
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
  [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag appearing in a Phase 3 evidence item
      that is not present in the Phase 0A exit gate vocabulary declaration (STICKINESS | LIMITATION |
      DISPLACEMENT | EXTERNAL) is a gate failure — this condition is the first gate item because
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
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
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-02 — C-46 Present, C-47 Absent, C-48 Absent

**Variation axis:** Lifecycle emphasis — Phase 1 exit gate adds an explicit binary checklist condition requiring exact-match INCUMBENT anchor citation (C-46 satisfied); PROHIBITED clauses in 0B-I and 0B-II retain generic category names (C-47 absent); gate items carry no embedded failure-mode rationale (C-48 absent)
**Hypothesis:** When Phase 1 exit gate contains a named checklist condition explicitly requiring that the INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording, the Phase 1 chain link becomes independently auditable at the Phase 1 gate boundary — a scorer reading only the Phase 1 gate and the subject card can verify exact-match compliance without inspecting Phase 0C. Phase 0B PROHIBITED clauses remain generic, leaving the 0B-I/0B-II scope boundary auditable only by cross-reading both gates. Gate items carry no inline rationale, so design intent is present in body prose but not embedded at gate item level. C-46's contribution to chain auditability is isolated; the remaining two gaps are preserved.

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
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording —
      a paraphrase does not satisfy this condition; the exact-match obligation declared at Phase 0C
      is enforced here as a named gate condition (C-46); a Phase 1 gate that requires only a
      non-blank anchor without naming exact-match wording does not satisfy C-46 even when the
      anchor is present
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4–6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions
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
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
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
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-03 — C-47 Present, C-46 Absent, C-48 Absent

**Variation axis:** Inertia framing — Phase 0B-I PROHIBITED clause names the 0B-II domain by content type; Phase 0B-II PROHIBITED clause names the 0B-I domain by content type (C-47 satisfied); Phase 1 exit gate requires only a non-blank anchor (C-46 absent); gate items carry no embedded failure-mode rationale (C-48 absent)
**Hypothesis:** When 0B-I PROHIBITED clause names the sibling's content domain ("margin declarations — Phase 0B-II domain") and 0B-II PROHIBITED clause names the sibling's content domain ("constitutive threshold definitions — Phase 0B-I domain"), the 0B-I/0B-II boundary becomes bidirectionally auditable at each gate independently — a scope violation at either gate is detectable without cross-inspecting its sibling. Generic PROHIBITED clauses satisfy C-34 but require cross-gate inspection to audit the boundary. Phase 1 gate retains non-blank-only anchor condition, leaving the Phase 1 chain link cross-gate-dependent. Gate items carry no inline rationale. C-47's contribution to scope boundary auditability is isolated.

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

For each level, state the evidence configuration that constitutes it — what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin declarations (Phase 0B-II domain) are absent from this sub-section —
      level names may be referenced but margin-boundary content belongs to 0B-II, not here
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions (Phase 0B-I domain) are absent from this
      sub-section — level names may be referenced but constitutive-definition content belongs
      to 0B-I, not here
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
  - Write 4–6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions
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
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
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
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-04 — C-46 Present, C-47 Present, C-48 Absent

**Variation axes:** Lifecycle emphasis + Inertia framing — Phase 1 exit gate has explicit exact-match anchor condition (C-46 satisfied); Phase 0B PROHIBITED clauses name the sibling sub-phase domain by content type (C-47 satisfied); gate items carry no embedded failure-mode rationale (C-48 absent)
**Hypothesis:** When exact-match anchor conditions (C-46) and sibling-domain PROHIBITED clauses (C-47) are both present, the Phase 1 chain link and the 0B-I/0B-II scope boundary are each independently auditable at their respective gate positions — a scorer can verify both structural properties without cross-phase inspection. The absence of inline rationales means the design intent behind these choices must be reconstructed from body instructions or surrounding prose. Structural auditability of compliance is satisfied; auditability of intent is not. This is the minimum combination required before C-48 can be distinguished as an independent contribution.

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

For each level, state the evidence configuration that constitutes it — what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin declarations (Phase 0B-II domain) are absent from this sub-section —
      level names may be referenced but margin-boundary content belongs to 0B-II, not here
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions (Phase 0B-I domain) are absent from this
      sub-section — level names may be referenced but constitutive-definition content belongs
      to 0B-I, not here
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
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording —
      a paraphrase does not satisfy this condition; the exact-match obligation declared at Phase 0C
      is enforced here as a named gate condition
  [ ] Blind spots non-blank and non-generic for all subjects
  [ ] No transcript lines appear in this section

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4–6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions
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
      gate-block-first placement makes vocabulary drift immediately auditable at gate entry
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
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
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type — structural
      failure detectable by row count without reading cell content
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section

---

## V-05 — C-46 Present, C-47 Present, C-48 Present (Full Target)

**Variation axes:** Lifecycle emphasis + Inertia framing + Phrasing register — exact-match anchor conditions (C-46), sibling-domain PROHIBITED clauses (C-47), and inline failure-mode rationale at every gate item (C-48) all present
**Hypothesis:** When all three criteria are satisfied, each gate item is fully self-auditing: it names the condition (what is required), how to verify it (exact-match wording or domain-named PROHIBITED clause), and why it exists (the failure mode the condition prevents, stated inline). A scorer reading any single gate item can determine what is required, how to verify compliance, and why the condition exists — without reading body instructions, surrounding prose, or any other phase. Design intent is auditable without contextual reconstruction. The full target produces gate items that function as self-contained audit contracts rather than references to external rationale.

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
  [ ] INERTIA PROFILE TABLE has at least two practice rows — fewer rows may miss a dominant
      stickiness factor and bias Phase 3 PROFILE RELEVANCE tagging toward the single named
      practice, collapsing the multi-factor inertia model into a single-variable account
  [ ] Each row has a stickiness factor that is not blank, not generic — a generic factor
      (e.g., "habit") does not name the mechanism of persistence and cannot be matched by
      Phase 3 PROFILE RELEVANCE tags in a way that tests whether specific factors were addressed
  [ ] PROFILE RELEVANCE vocabulary declared here for use in Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Each Phase 3 evidence item must carry exactly one of these tags.
      This declaration is the contract source — Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere; a tag list reproduced at Phase 3 without citing
      this gate creates a parallel contract and does not close the mid-chain drift gap
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here —
      their presence here pre-loads evidence-collection phases with conclusions the phase
      separation structure is specifically designed to prevent

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — what pattern of evidence
types across subjects places the finding at this level. A level name without a constitutive
definition does not satisfy this gate.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin declarations (Phase 0B-II domain) are absent from this sub-section —
      margin-boundary content belongs to 0B-II; its presence here collapses the threshold /
      margin distinction and makes 0B-I completion dependent on 0B-II output, breaking the
      independent-auditability property this sub-phase separation is designed to maintain;
      level names may be referenced (C-47)
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject
      patterns — a level name without a definition cannot anchor Phase 4 verdict classification;
      the Net Verdict step requires drawing the verdict from these definitions, not from implicit
      understanding of level names
  [ ] Completing 0B-II does not pass this gate — the two sub-phases serve different structural
      functions (threshold vs. margin); satisfying 0B-II does not verify that constitutive
      definitions are present

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property
that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions (Phase 0B-I domain) are absent from this
      sub-section — constitutive-definition content belongs to 0B-I; its presence here collapses
      the threshold / margin distinction and makes 0B-II completion dependent on 0B-I output,
      breaking the independent-auditability property this sub-phase separation is designed to
      maintain; level names may be referenced (C-47)
  [ ] All four margin pairs have a named deciding factor — a pair without a named factor leaves
      the VERDICT MARGIN AUDIT table in Phase 4 unable to populate the "Margin factor" column
      for that boundary, producing a structural gap in the audit trail detectable by row inspection
  [ ] The margin column creates non-overlapping regions across all five levels — overlapping
      regions make the VERDICT MARGIN AUDIT table ambiguous: the same evidence pattern could
      place the verdict at two levels simultaneously, defeating the audit function
  [ ] Completing 0B-I does not pass this gate — the two sub-phases serve different structural
      functions; satisfying 0B-I does not verify that margin factors are present

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
  [ ] Tier sequence declared with adjacency blocks for all three consecutive tier pairs — a
      missing adjacency block leaves the ordering rationale partially asserted; the contrast
      lost if reversed cannot be evaluated for that pair
  [ ] All four tiers have per-tier predictions with all four fields — a prediction without all
      four fields cannot be fully classified at PREDICTION DELTA in Phase 4; partial predictions
      produce partial delta classifications
  [ ] INCUMBENT anchor declared as named output naming specific Phase 0A row and stickiness
      factor — a generic anchor declaration does not name a specific row and cannot be matched
      by exact-match verification at Phase 1 or direct-question verification at Phase 2; the
      chain is unverifiable if the anchor is unspecific
      Downstream propagation obligations declared at this gate:
        - Phase 1: INCUMBENT subject card inertia anchor field must match this named row exactly
          (exact-match required — a paraphrase breaks the chain; the break is detectable at Phase 1
          gate only when Phase 1 gate condition names exact-match wording as the requirement,
          not merely non-blank presence)
        - Phase 2: at least one question in the INCUMBENT transcript must name this anchor directly
          (direct-question required — referencing the topic without naming the anchor makes chain
          enforcement dependent on content judgment rather than structure)
      These obligations are declared at the source so any chain break is auditable at the phase
      that names its predecessor rather than requiring inspection of the downstream phase alone.
  [ ] No verdict threshold or margin content appears here — its presence here pre-loads the
      tier prediction phase with verdict-level framing, biasing the prediction register toward
      a pre-declared verdict rather than genuine uncertainty

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
  [ ] Four subject cards present in tier sequence — fewer than four collapses the
      INCUMBENT-CHAMPION-EVALUATOR-SKEPTIC coverage structure; the tier sequence's
      evidential logic depends on all four roles being represented
  [ ] Each card has all five standard fields plus INCUMBENT designation — a missing field
      leaves the corresponding Phase 3 or Phase 4 step without a subject-level anchor
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording —
      a paraphrase does not satisfy this condition; a non-blank anchor that restates the anchor
      in different words makes the Phase 1-to-Phase 0C chain auditable only by comparing both
      documents and judging semantic equivalence rather than by reading the Phase 1 gate alone;
      exact-match wording closes this cross-phase dependency (C-46)
  [ ] Blind spots non-blank and non-generic for all subjects — a generic blind spot does not
      identify a specific knowledge gap that can be used in the EPISTEMIC RE-WEIGHTING section
      of Phase 4
  [ ] No transcript lines appear in this section — transcripts in the subject design section
      collapse the setup/interview phase boundary; Phase 4 DISPOSITION ARC depends on having
      a clean separation between the pre-interview subject profile and the interview itself

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence before any hypothesis questions.

For each subject:
  - Write 4–6 questions anchored to the subject's declared primary concern
  - INCUMBENT transcript: at least one question names the Phase 0C INCUMBENT anchor directly
    (direct-question required per Phase 0C exit gate propagation obligation)
  - Write answers in the subject's distinct voice
  - Mark exactly one moment per subject as SURPRISING or CONFIRMING, tied to Phase 0C prediction

All four transcripts must be complete before any hypothesis question section begins.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT transcript contains at least one question directly addressing the INCUMBENT ANCHOR
      declared in Phase 0C exit gate — this condition is the first gate item because gate-block-first
      placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
      reading through affirmative completion conditions; placing this condition after affirmative
      items requires reading past irrelevant checks before reaching the chain-critical item (C-47
      for Phase 2 gate-block-first requirement)
  [ ] All four transcripts complete before any hypothesis questions — a partial transcript set
      leaves the tier sequence incomplete; PREDICTION DELTA in Phase 4 cannot evaluate predictions
      for subjects whose transcripts were not written before synthesis began
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment named against Phase 0C
      prediction — zero moments leaves the prediction register unevaluated for that subject;
      more than one per subject dilutes the signal by implying the prediction register was not
      specific enough to produce a single decisive test
  [ ] Answers written in distinct subject voices — generic voice means the simulation is not
      grounded in the declared persona profiles; the DISPOSITION ARC and CROSS-PERSONA SYNTHESIS
      sections cannot detect real divergence if voices are indistinguishable

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
      reading through affirmative completion conditions; a tag introduced at Phase 3 not declared
      at Phase 0A breaks the contract chain; detecting this break at Phase 3 requires only reading
      the first gate item and checking the tag against the Phase 0A declaration
  [ ] Evidence extraction section separate from transcripts and synthesis — evidence items embedded
      in transcripts or synthesis cannot be independently enumerated for Phase 4 INERTIA PROFILE
      ACCOUNTING; the separation is a structural precondition for PROFILE RELEVANCE accounting
      to function as designed
  [ ] Each item has all five fields — a missing RATIONALE means the STRENGTH rating is asserted
      without justification; a missing PROFILE RELEVANCE tag means INERTIA PROFILE ACCOUNTING
      in Phase 4 cannot attribute the item to a specific stickiness factor
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; compliance is against the Phase 0A declaration, not
      against any locally reproduced list
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales — a self-referential
      rationale does not explain why the evidence was rated at this strength and cannot be used
      to challenge or validate the rating
  [ ] No synthesis content in this section — synthesis in the evidence section collapses the
      Phase 3 / Phase 4 boundary; Phase 4 CROSS-PERSONA SYNTHESIS depends on a clean evidence
      base to aggregate from, not pre-synthesized conclusions

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
  [ ] All seven synthesis sections present and non-empty — a missing section leaves its
      analytical dimension unaddressed; the NET VERDICT draws on evidence patterns that only
      become visible when all seven perspectives are completed
  [ ] Net verdict drawn from Phase 0B-I defined levels — a verdict that uses an undefined level
      name cannot be placed on the Phase 0B-II margin map and the VERDICT MARGIN AUDIT table
      cannot be populated for undefined levels
  [ ] VERDICT MARGIN AUDIT table completeness: both boundary rows populated (upper and lower) —
      a single-row table leaves one boundary unaudited; this is a structural failure detectable
      by row count without reading any cell content, not a format deviation
  [ ] Prediction delta classifications name specific Phase 3 evidence items — a classification
      without a named evidence item cannot be verified; CONFIRMED without citation means
      confirmation is asserted, not evidenced
  [ ] No new evidence introduced in this section — new evidence in Phase 4 not captured in Phase 3
      is outside the evidence accounting perimeter; it cannot carry a PROFILE RELEVANCE tag and
      is not subject to Phase 3 gate validation; its presence means the Phase 3 evidence set
      is incomplete
