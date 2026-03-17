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
      This declaration is the contract source -- Phase 3 compliance is with this gate, not
      with any tag list reproduced elsewhere.
  [ ] No verdict-level classifications, margin declarations, or tier predictions appear here

---

## PHASE 0B-I -- VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels before evidence collection.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it -- what pattern of evidence types
across subjects places the finding at this level. A level name without a constitutive definition does
not satisfy this gate.

PHASE 0B-I EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: margin-boundary declarations -- the 0B-II domain -- are absent from this
      sub-section; naming the sibling sub-phase's domain by content type makes the 0B-I boundary
      auditable for 0B-II scope violations by reading only this gate without cross-inspecting 0B-II;
      a generic out-of-scope category label satisfies C-34 but does not name the sibling sub-phase's
      domain by content type and does not satisfy C-49; this contrast between C-34 (named out-of-scope
      category required) and C-49 (sibling sub-phase's specific domain required) is stated here so
      the criterion boundary is auditable from gate text without reading the rubric -- following the
      self-annotating gate pattern of C-43, C-46, and C-47; the two PROHIBITED clauses are mutually
      referential -- each names the other's domain -- making the 0B-I/0B-II scope boundary
      bidirectionally auditable from either gate alone; a PROHIBITED clause that satisfies C-51
      (C-34/C-49 contrast present in both gate blocks) but does not include this mutual-referentiality
      rationale does not satisfy C-53; the C-49/C-51/C-53 chain: C-49 requires sibling-scope naming
      (structural fact -- the 0B-II domain is named); C-51 requires the C-34/C-49 contrast (boundary
      statement -- why generic naming is insufficient); C-53 requires the mutual-referentiality
      consequence clause (architectural explanation -- why mutual referentiality produces bidirectional
      auditability, making that property observable within gate text without reading the rubric); this
      clause must appear in both 0B-I and 0B-II gate blocks -- single-block presence is structurally
      equivalent to single-direction auditability for C-53 purposes
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II -- VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor -- the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE -- ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions -- the 0B-I domain -- are absent from this
      sub-section (level names may be referenced; constitutive definitions must not be restated);
      naming the sibling sub-phase's domain by content type makes the 0B-II boundary auditable for
      0B-I scope violations by reading only this gate without cross-inspecting 0B-I; a generic
      out-of-scope category label satisfies C-34 but does not name the sibling sub-phase's domain
      by content type and does not satisfy C-49; the C-34/C-49 criterion boundary is stated here
      following the self-annotating gate pattern so it is auditable without reading the rubric;
      the two PROHIBITED clauses are mutually referential -- each names the other's domain -- making
      the 0B-I/0B-II scope boundary bidirectionally auditable from either gate alone; a PROHIBITED
      clause that satisfies C-51 (C-34/C-49 contrast present in both gate blocks) but does not
      include this mutual-referentiality rationale does not satisfy C-53; the C-49/C-51/C-53 chain:
      C-49 requires sibling-scope naming (structural fact); C-51 requires the C-34/C-49 contrast
      (boundary statement -- what generic naming fails to provide); C-53 requires the
      mutual-referentiality consequence clause (architectural explanation -- why mutual referentiality
      produces bidirectional auditability; this is the explanation of the *why* that neither C-49
      nor C-51 provides); this clause must appear in both 0B-I and 0B-II gate blocks; the symmetric
      placement is required because the bidirectional auditability property should be observable from
      either gate alone -- an asymmetric design that places the rationale in one block only is
      structurally self-contradicting: it states that mutual referentiality produces bidirectional
      auditability in a design that is not itself bidirectionally auditable for that property
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
      These obligations are declared at the source so any chain break is auditable at the phase
      that names its predecessor rather than requiring inspection of the downstream phase alone.
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
  [ ] INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording --
      this gate condition closes the Phase 1 link of the traceability chain declared at Phase 0C
      exit gate; C-48 closes the Phase 1 link; C-45 closes the Phase 2 link; naming both closure
      points makes the full two-link downstream obligation structure (exact-match at Phase 1,
      direct-question at Phase 2) readable from Phase 1 alone without inspecting the Phase 2 gate;
      a Phase 1 gate condition that satisfies C-48 (exact-match anchor present, Phase 1 chain link
      independently auditable) but names only the Phase 1 closure point does not satisfy C-50 --
      this criterion-boundary contrast makes the C-48/C-50 distinction auditable from gate text
      without reading the rubric; this is the Phase 1 parallel of C-51, which applies the same
      self-annotating gate pattern to the C-34/C-49 boundary at the 0B gate blocks: C-51 states
      that a generic out-of-scope category satisfies C-34 but not C-49; C-52 states that naming
      only the Phase 1 link satisfies C-48 but not C-50; the pattern -- each criterion encodes in
      gate text what its base criterion lacks -- is established by C-43 (C-34 base), C-46 (C-44
      base), C-47 (C-45 base), C-51 (C-49 base), and C-52 (C-50 base)
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
      reading through affirmative completion conditions; the anchor is now enforced at four structural
      points: declared at the source with both downstream obligations named (Phase 0C exit gate,
      C-41); enforced as a gate-interior exact-match condition at Phase 1 (C-48); named as the Phase 2
      sibling closure in the Phase 1 gate condition text (C-50); and the C-48/C-50 criterion boundary
      is stated in the Phase 1 gate text so the distinction is auditable without rubric reference
      (C-52); the direct-question obligation is required here as the first gate condition (C-45, C-47);
      a Phase 2 gate whose first checklist item is any condition other than this anchor requirement
      does not satisfy C-47 even when the anchor condition is present as a later gate item
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
      reading through affirmative completion conditions; naming the Phase 0A contract source without
      stating this failure condition is protection by implication only (satisfying C-40) and does
      not constitute enforcement (C-44); placing any affirmative completion item before this
      condition satisfies C-44 but fails C-46; gate-block-first is the positional parallel of C-34's
      requirement applied to the Phase 3 anti-drift enforcement clause
  [ ] Evidence extraction section separate from transcripts and synthesis
  [ ] Each item has all five fields
  [ ] PROFILE RELEVANCE tag on each item complies with the Phase 0A exit gate vocabulary contract
      (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) -- the Phase 0A exit gate is the named
      contract source; a tag list reproduced at Phase 3 does not close the mid-chain drift gap
      this condition is designed to detect; a Phase 3 gate that checks tag presence without citing
      the Phase 0A gate contract does not satisfy C-40
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
      a single-row VERDICT MARGIN AUDIT table is a gate failure by content type -- this is a
      structural failure detectable by row count without reading any cell content, not a format
      deviation; a gate that requires "completeness" without naming the single-row failure condition
      explicitly does not satisfy this criterion
  [ ] Prediction delta classifications name specific Phase 3 evidence items
  [ ] No new evidence introduced in this section