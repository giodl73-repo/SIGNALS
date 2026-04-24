# prove-interview — Skill Body Variations — R14

**Skill:** prove-interview
**Round:** 14
**Rubric version:** v14
**Date:** 2026-03-15

---

## R14 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|-----------|----------------|------|------------|
| V-01 | Single | Phase 3 Reference Gate (C-40) | Phase 3 gate can detect mid-chain vocabulary drift independently if it cites Phase 0A by name rather than reproducing the tag list — a reproduced list allows Phase 0A and Phase 3 to diverge without detection; a named reference makes Phase 0A the auditable contract source at Phase 3 exit |
| V-02 | Single | Phase 0C Source Obligations (C-41) | When Phase 0C names the exact downstream destinations of the INCUMBENT anchor (Phase 1: exact-match field; Phase 2: direct question), any chain break is auditable at the source — the break origin is identifiable at Phase 0C without inspecting Phase 1 or Phase 2 |
| V-03 | Single | Gate Failure by Content Type (C-42) | Naming a single-row VERDICT MARGIN AUDIT table as a gate failure by content type (structural, row-count detectable) upgrades it from a substantive-completeness check to a structural audit — the failure is visible without reading any cell |
| V-04 | Combined | Dual Source Declaration (C-40 + C-41) | C-40 and C-41 are parallel source-declaration patterns: C-40 makes Phase 0A the named contract source for Phase 3 compliance; C-41 makes Phase 0C the named obligation source for INCUMBENT anchor propagation; together they create two independent auditable origins without requiring Phase 4 gate upgrades |
| V-05 | Combined | Full R14 Apparatus (C-40 + C-41 + C-42) | When vocabulary chain reference (C-40), INCUMBENT anchor obligation declaration (C-41), and content-type gate failure naming (C-42) are all present simultaneously, the skill achieves three independent structural audit points: Phase 0A vocabulary contract cited at Phase 3, Phase 0C obligations named at source, Phase 4 VERDICT MARGIN AUDIT structurally typed as gate failure |

Single-axis variations: V-01 (C-40 Phase 3 reference gate), V-02 (C-41 Phase 0C source obligations), V-03 (C-42 content-type gate failure)
Combined variations: V-04 (C-40 + C-41 dual source declaration), V-05 (C-40 + C-41 + C-42 full R14 apparatus)

New R14 territory probed:
- **Phase 3 gate names Phase 0A vocabulary contract by reference** (V-01, V-04, V-05): upgrades C-37's vocabulary declaration to be auditable at Phase 3 exit by citing Phase 0A as the named contract source, not just re-listing permitted tag values
- **Phase 0C source gate declares downstream propagation obligations** (V-02, V-04, V-05): upgrades C-39's INCUMBENT anchor declaration to name the exact form required at Phase 1 (exact-match) and Phase 2 (direct question), making chain-break origin auditable at the source without inspecting downstream gates
- **Phase 4 gate failure by content type for single-row audit** (V-03, V-05): upgrades C-38's VERDICT MARGIN AUDIT completeness condition to name the single-row failure as a gate failure by content type (structural, detectable by row count, not cell reading)

---

## V-01 — Phase 3 Gate Names Phase 0A Contract by Reference (C-40)

**Variation axis:** Phase 3 reference gate (single-axis C-40)
**Hypothesis:** Prior variations instruct Phase 3 to use PROFILE RELEVANCE tags "from Phase 0A" but the gate condition checks tag presence against a reproduced list — if Phase 0A is later revised, Phase 3 could pass with stale tags. When the Phase 3 exit gate cites the Phase 0A exit gate vocabulary contract by name as the compliance source, mid-chain vocabulary drift is detectable at Phase 3 exit independently of whether Phase 0A was inspected. The gate becomes an auditable link, not a format check.

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

For each level, state the evidence configuration that constitutes it — what pattern of evidence types across subjects places the finding at this level. A level name without a constitutive definition does not satisfy this gate.

PROHIBITED: do not include margin-boundary declarations or deciding-factor content in this sub-section.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] No margin-boundary or deciding-factor content present
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PROHIBITED: do not restate constitutive definitions from 0B-I — reference level names only.

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four margin pairs have a named deciding factor
  [ ] No constitutive threshold restatements present
  [ ] The margin column creates non-overlapping regions across all five levels
  [ ] Completing 0B-I does not pass this gate

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Declare tier sequence rationale and per-tier predictions before any subject cards.

For each tier, declare:
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
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

Design four subject cards.

For each subject card declare:
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
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: one tag drawn from the Phase 0A exit gate vocabulary contract
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
    Compliance is with the Phase 0A exit gate contract, not with this instruction line.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary
      contract (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — Phase 0A exit gate is
      the named contract source; checking tag presence without citing Phase 0A does not
      close the mid-chain traceability gap this gate condition is designed to detect
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregates findings across all subjects
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
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II margin factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II margin factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] CROSS-PERSONA SYNTHESIS section present
  [ ] DISPOSITION ARC section present
  [ ] CONTRADICTION REGISTER present with at least one named contradiction citing both subjects
  [ ] EPISTEMIC RE-WEIGHTING present with per-blind-spot resolution conditions
  [ ] INERTIA PROFILE ACCOUNTING present addressing each Phase 0A stickiness factor
  [ ] PREDICTION DELTA present with specific Phase 3 evidence item citations
  [ ] INERTIA / ADOPTION PARTITION present with two separately populated lists
  [ ] NET VERDICT present with classification from Phase 0B-I taxonomy
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated

---

## V-02 — Phase 0C Declares INCUMBENT ANCHOR with Downstream Obligations (C-41)

**Variation axis:** Phase 0C source obligations (single-axis C-41)
**Hypothesis:** Prior variations declare the INCUMBENT anchor in Phase 0C and instruct downstream phases to reference it — but the Phase 0C exit gate does not name the specific form required at each destination. A Phase 0C gate that names both downstream obligations (Phase 1: exact-match in inertia anchor field; Phase 2: at least one direct question) at the source makes the chain-break origin auditable at Phase 0C itself: if Phase 1 or Phase 2 deviates, the Phase 0C gate can be cited as the violated obligation without inspecting the downstream phase gates.

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
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
  - Expected posture
  - What confirming signal would look like
  - What surprising signal would look like

INCUMBENT ANCHOR DECLARATION:
Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that anchors the
INCUMBENT subject's inertia baseline. This anchor is a named output of Phase 0C.

  Named anchor: [Phase 0A row name] — [stickiness factor]

Downstream propagation obligations declared at this source gate:
  - Phase 1 INCUMBENT card: exact-match required in the inertia anchor field (same row name
    and stickiness factor; paraphrase does not satisfy the Phase 1 obligation)
  - Phase 2 INCUMBENT transcript: at least one direct question naming this anchor is required
    (the question text must include the anchor name as declared here; indirect reference
    does not satisfy the Phase 2 obligation)

These obligations are declared here so that any chain break is auditable at this source gate
without inspecting Phase 1 or Phase 2.

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT ANCHOR DECLARATION present, naming a specific Phase 0A row and stickiness factor
  [ ] Downstream obligations declared at this gate by phase:
      Phase 1 INCUMBENT card: exact-match required in inertia anchor field
      Phase 2 INCUMBENT transcript: at least one direct question naming this anchor required
      (A Phase 0C gate that declares the anchor without naming these downstream obligations
      does not make chain-break origin auditable at the source)
  [ ] All four tiers have per-tier predictions with all four fields
  [ ] Tier sequence declared with adjacency blocks for all consecutive pairs
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
  - Inertia anchor: must name the specific Phase 0A row and stickiness factor declared in Phase 0C.
    Must match Phase 0C named anchor exactly — paraphrase fails the Phase 0C propagation obligation.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present
  [ ] Each card has role, prior knowledge, blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor names the Phase 0C declared row and stickiness factor exactly
      (exact-match required per Phase 0C obligation; paraphrase fails this gate)
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
  - At least one question must name the Phase 0C declared anchor directly (not a paraphrase).
    Direct-question obligation declared at Phase 0C; the question text must include the anchor name.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript has at least one question naming the Phase 0C anchor directly
      (direct-question obligation per Phase 0C; paraphrase or indirect reference fails this gate)
  [ ] Each subject has exactly one SURPRISING or CONFIRMING moment
  [ ] Answers written in distinct subject voices

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence items in a dedicated section, separate from transcripts and synthesis.

For each evidence item:
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag is one of: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregates findings across all subjects
2. DISPOSITION ARC — traces per-subject disposition shift or hold
3. CONTRADICTION REGISTER — at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING — adjusts evidence weight by blind spots; per-blind-spot resolution conditions
5. INERTIA PROFILE ACCOUNTING — for each Phase 0A stickiness factor, state which evidence items
   addressed it and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA — iterate Phase 0C per-tier predictions; classify as CONFIRMED / CONTRADICTED /
   ABSENT / PARTIAL, naming specific evidence items
7. INERTIA / ADOPTION PARTITION — two separately populated lists

Then produce the NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table:

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper boundary | | | |
    | Lower boundary | | | |

    Both rows must be populated.

---

## V-03 — Single-Row VERDICT MARGIN AUDIT Named as Gate Failure by Content Type (C-42)

**Variation axis:** Phase 4 gate failure by content type (single-axis C-42)
**Hypothesis:** Prior variations require both audit table rows to be populated and note that a single-row audit "fails regardless of row content" — but the gate condition is still framed as a completeness requirement, which an evaluator might interpret as a substantive check (are the cells filled?). When the Phase 4 gate names a single-row table as a gate failure by content type, the audit is structural: you count rows, not read cells. The failure is detectable without opening the table contents, making it an auditable structural property rather than a substantive quality condition.

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
  - Expected evidence type (RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION)
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

Design four subject cards.

For each subject card declare:
  - Role
  - Prior knowledge (direct experience and knowledge gaps as separate fields)
  - Blind spots (not blank, not "none")
  - Disposition
  - Primary concern

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present with all five fields
  [ ] Blind spots non-blank and non-generic for all subjects
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
  - Evidence text (quote or paraphrase from transcript)
  - SIGNAL TYPE: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
  - STRENGTH: STRONG / MODERATE / WEAK
  - RATIONALE: non-blank, non-self-referential explanation for the strength rating
  - PROFILE RELEVANCE: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregates findings across all subjects
2. DISPOSITION ARC — traces per-subject disposition shift or hold
3. CONTRADICTION REGISTER — at least one contradiction naming both subjects and both evidence items
4. EPISTEMIC RE-WEIGHTING — adjusts evidence weight by blind spots; per-blind-spot resolution conditions
5. INERTIA PROFILE ACCOUNTING — for each Phase 0A stickiness factor, state which evidence items
   addressed it and whether confirmed, challenged, or unaddressed
6. PREDICTION DELTA — iterate Phase 0C per-tier predictions; classify as CONFIRMED / CONTRADICTED /
   ABSENT / PARTIAL, naming specific evidence items
7. INERTIA / ADOPTION PARTITION — two separately populated lists

Then produce the NET VERDICT:
  - State the verdict classification from Phase 0B-I levels
  - Name the constitutive evidence configuration
  - Produce the VERDICT MARGIN AUDIT table:

    The table requires two named boundary rows. A table with only one boundary row is a gate
    failure by content type — the failure is structural (row count), not substantive (cell
    content); it is detectable without reading the cells.

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II margin factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II margin factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] CROSS-PERSONA SYNTHESIS section present
  [ ] DISPOSITION ARC section present
  [ ] CONTRADICTION REGISTER present with at least one named contradiction citing both subjects
  [ ] EPISTEMIC RE-WEIGHTING present with per-blind-spot resolution conditions
  [ ] INERTIA PROFILE ACCOUNTING present
  [ ] PREDICTION DELTA present with evidence item citations
  [ ] INERTIA / ADOPTION PARTITION present
  [ ] NET VERDICT present with classification from Phase 0B-I taxonomy
  [ ] VERDICT MARGIN AUDIT table: a single-row table is a gate failure by content type —
      the failure is structural (one boundary row instead of two) and detectable without
      reading the cell content; both upper-boundary and lower-boundary rows must be present
      as named rows; "both rows populated" is a necessary but not sufficient description —
      the single-row failure is a content-type failure, not a completeness deviation

---

## V-04 — Dual Source Declaration: Vocabulary Chain + INCUMBENT Obligations (C-40 + C-41)

**Variation axis:** C-40 + C-41 combined (no C-42)
**Hypothesis:** C-40 and C-41 are structurally parallel patterns applied to different chains: C-40 makes Phase 0A the named contract source that Phase 3 cites by reference (vocabulary chain); C-41 makes Phase 0C the named obligation source that downstream phases must satisfy by form (INCUMBENT anchor chain). Together they establish two independent origin-auditable chains without requiring a Phase 4 gate upgrade. A Phase 3 drift or a Phase 1/2 anchor deviation is each auditable at the source gate that declared the obligation, not at the phase where the deviation occurs.

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
  [ ] PROFILE RELEVANCE vocabulary declared here as a gate-level contract for Phase 3:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      Phase 3 evidence items must carry one of these tags; compliance is with this Phase 0A
      gate contract, not with any tag list reproduced at Phase 3. Phase 3 exit gate must
      cite this contract by reference to Phase 0A — reproducing the list at Phase 3 without
      citing Phase 0A does not satisfy the mid-chain reference requirement.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it. A level name without
a constitutive definition does not satisfy this gate.

PROHIBITED: do not include margin-boundary or deciding-factor content in this sub-section.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] No margin-boundary or deciding-factor content present
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

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
Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that anchors the
INCUMBENT subject's inertia baseline.

  Named anchor: [Phase 0A row name] — [stickiness factor]

Downstream propagation obligations declared at this source gate:
  - Phase 1 INCUMBENT card: exact-match required in the inertia anchor field (same named row
    and stickiness factor; paraphrase does not satisfy this obligation)
  - Phase 2 INCUMBENT transcript: at least one direct question naming this anchor is required
    (the question text must include the anchor name as declared here)

The above obligations are declared at this source gate so that chain-break origin is auditable
at Phase 0C without inspecting Phase 1 or Phase 2.

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT ANCHOR DECLARATION present, naming a specific Phase 0A row and stickiness factor
  [ ] Downstream obligations declared by phase at this source gate:
      Phase 1: exact-match required in INCUMBENT inertia anchor field
      Phase 2: at least one direct question naming the anchor required
      (A Phase 0C gate that declares the anchor without naming these downstream obligations
      does not make chain-break origin auditable at the source)
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
  - Inertia anchor: must name the specific Phase 0A row and stickiness factor declared in Phase 0C.
    Must match Phase 0C named anchor exactly — paraphrase fails the Phase 0C source obligation.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present
  [ ] Each card has role, prior knowledge, blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor matches Phase 0C named anchor exactly (exact-match per Phase 0C
      obligation; paraphrase fails this gate)
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
  - At least one question names the Phase 0C anchor directly (not a paraphrase).
    Direct-question obligation per Phase 0C; the question text must include the anchor name.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript has at least one question naming Phase 0C anchor directly
      (direct-question obligation per Phase 0C; paraphrase or indirect reference fails)
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
  - PROFILE RELEVANCE: one tag drawn from the Phase 0A exit gate vocabulary contract
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
    Phase 0A exit gate is the named contract source.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary
      contract (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) — Phase 0A exit gate is
      the contract source; a Phase 3 gate that checks tag presence without citing Phase 0A
      does not satisfy the mid-chain reference requirement
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregates findings across all subjects
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
  - Produce the VERDICT MARGIN AUDIT table (both rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II margin factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II margin factor] | [named evidence] | [placement] |

    A single-row audit does not satisfy C-35 regardless of row content.

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] CROSS-PERSONA SYNTHESIS section present
  [ ] DISPOSITION ARC section present
  [ ] CONTRADICTION REGISTER present with at least one named contradiction citing both subjects
  [ ] EPISTEMIC RE-WEIGHTING present with per-blind-spot resolution conditions
  [ ] INERTIA PROFILE ACCOUNTING present addressing each Phase 0A stickiness factor
  [ ] PREDICTION DELTA present with specific Phase 3 evidence item citations
  [ ] INERTIA / ADOPTION PARTITION present with two separately populated lists
  [ ] NET VERDICT present with classification from Phase 0B-I taxonomy
  [ ] VERDICT MARGIN AUDIT table has both upper-boundary and lower-boundary rows populated

---

## V-05 — Full R14 Apparatus (C-40 + C-41 + C-42)

**Variation axis:** All three R14 criteria combined
**Hypothesis:** C-40, C-41, and C-42 each upgrade a corresponding R13 criterion by adding an auditable structural property that was previously a substantive check: C-40 upgrades C-37's vocabulary list into a named-reference audit at Phase 3; C-41 upgrades C-39's propagation declaration into a source-gate obligation with downstream specificity; C-42 upgrades C-38's completeness condition into a content-type gate failure detectable by row count. When all three are present simultaneously, every chain in the skill has a structural audit point: vocabulary drift detectable at Phase 3 by Phase 0A citation, INCUMBENT anchor chain-break auditable at Phase 0C, VERDICT MARGIN AUDIT failure auditable by structure without reading cells.

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
  [ ] PROFILE RELEVANCE vocabulary declared here as a gate-level contract for Phase 3 and Phase 4:
      Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
      This is the named contract source. Phase 3 items must carry one of these tags; Phase 3
      exit gate must cite this Phase 0A gate contract by reference — checking tag presence
      without naming Phase 0A as the contract source does not close the mid-chain audit gap.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — what pattern of evidence
types and cross-subject patterns places the finding at this level.

PROHIBITED: do not include margin-boundary or deciding-factor content in this sub-section.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] No margin-boundary or deciding-factor content present
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property
that tips the verdict from one level to the other.

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
Name the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor that anchors the
INCUMBENT subject's inertia baseline. This is a named output of Phase 0C.

  Named anchor: [Phase 0A row name] — [stickiness factor]

Downstream propagation obligations declared at this source gate:
  - Phase 1 INCUMBENT card: exact-match required in the inertia anchor field (same named row
    and stickiness factor declared here; paraphrase does not satisfy this obligation)
  - Phase 2 INCUMBENT transcript: at least one direct question naming this anchor is required
    (the question text must include the anchor name as declared here; indirect reference
    does not satisfy this obligation)

These obligations are declared at this source gate so that any chain break is auditable at
Phase 0C without inspecting Phase 1 or Phase 2.

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if reversed

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] INCUMBENT ANCHOR DECLARATION present, naming a specific Phase 0A row and stickiness factor
  [ ] Downstream obligations declared by phase at this source gate:
      Phase 1 INCUMBENT card: exact-match required in inertia anchor field
      Phase 2 INCUMBENT transcript: at least one direct question naming the anchor required
      (Declaring the anchor without naming these obligations does not make chain-break origin
      auditable at this source gate)
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
  - Inertia anchor: must name the specific Phase 0A row and stickiness factor declared in Phase 0C.
    Must match Phase 0C named anchor exactly — paraphrase fails the Phase 0C source obligation.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Four subject cards present
  [ ] Each card has role, prior knowledge, blind spots, disposition, primary concern
  [ ] INCUMBENT card carries INCUMBENT designation label
  [ ] INCUMBENT inertia anchor matches Phase 0C named anchor exactly (exact-match per Phase 0C
      obligation; paraphrase fails this gate)
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
  - At least one question names the Phase 0C anchor directly (not a paraphrase).
    Direct-question obligation per Phase 0C; the question text must include the anchor name.

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] All four transcripts complete before any hypothesis questions
  [ ] INCUMBENT transcript has at least one question naming Phase 0C anchor directly
      (direct-question obligation per Phase 0C; paraphrase fails this gate)
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
  - PROFILE RELEVANCE: one tag from the Phase 0A exit gate vocabulary contract
    (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL)
    Phase 0A exit gate is the named contract source; compliance is with Phase 0A, not
    with this instruction line.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] Evidence extraction section separate from transcripts
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary
      contract (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL); Phase 0A exit gate is
      the named contract source — a Phase 3 gate that checks tag presence without citing
      Phase 0A does not satisfy the mid-chain reference audit this gate is designed to close
  [ ] All STRENGTH ratings have non-blank, non-self-referential rationales
  [ ] No synthesis content in this section

---

## PHASE 4 — SYNTHESIS

Produce the following named sections in order:

1. CROSS-PERSONA SYNTHESIS — aggregates findings across all subjects
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
  - Name the constitutive evidence configuration that places the finding at this level
  - Produce the VERDICT MARGIN AUDIT table:

    The table requires two named boundary rows. A single-row VERDICT MARGIN AUDIT table is a
    gate failure by content type — the failure is structural (one boundary row instead of two)
    and is detectable without reading the cell content. The row count, not the cell values, is
    the auditable condition. A gate that requires "completeness" or "both rows populated"
    without naming the single-row failure by content type does not satisfy C-42.

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [this level] / [level above] | [Phase 0B-II margin factor] | [named evidence] | [placement] |
    | Lower: [level below] / [this level] | [Phase 0B-II margin factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] CROSS-PERSONA SYNTHESIS section present
  [ ] DISPOSITION ARC section present
  [ ] CONTRADICTION REGISTER present with at least one named contradiction citing both subjects
      and both specific conflicting evidence items
  [ ] EPISTEMIC RE-WEIGHTING present with per-blind-spot resolution conditions specified
  [ ] INERTIA PROFILE ACCOUNTING present, addressing each Phase 0A stickiness factor by
      PROFILE RELEVANCE tag accounting
  [ ] PREDICTION DELTA present with specific Phase 3 evidence item citations per prediction
  [ ] INERTIA / ADOPTION PARTITION present with two separately populated lists
  [ ] NET VERDICT present with classification from Phase 0B-I taxonomy and constitutive
      evidence configuration named
  [ ] VERDICT MARGIN AUDIT table: a single-row table is a gate failure by content type —
      the failure is structural (one boundary row instead of two), detectable without reading
      the cell content; both upper-boundary and lower-boundary rows must be present as named
      rows regardless of cell content; a gate condition stating only "both rows populated"
      without naming the single-row content-type failure does not satisfy this criterion
