# prove-interview — Skill Body Variations — R18

**Skill:** prove-interview
**Round:** 18
**Rubric version:** v18
**Date:** 2026-03-15

---

## R18 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|---|---|---|---|
| V-01 | Single | C-48 absent, C-49 absent — Phase 1 gate mentions anchor but no explicit exact-match checklist condition; Phase 0B PROHIBITED clauses use generic category names | When Phase 1 gate has no dedicated checklist condition enforcing exact-match anchor citation, the Phase 1 link of the traceability chain declared at Phase 0C is auditable only by reading Phase 1 body instructions and comparing against Phase 0C output — it is not independently auditable at the Phase 1 gate boundary alone; when 0B PROHIBITED clauses name generic out-of-scope categories rather than the sibling sub-phase's specific domain, the 0B-I/0B-II boundary is not bidirectionally auditable from either gate alone |
| V-02 | Single | C-48 present, C-49 absent — Phase 1 gate has explicit exact-match anchor checklist condition; Phase 0B PROHIBITED clauses remain generic | When Phase 1 exit gate adds an explicit binary checklist condition requiring exact-match INCUMBENT anchor citation, the Phase 1 chain link becomes auditable at Phase 1 independently of Phase 0C — a scorer reading only the Phase 1 gate can determine whether the exact-match obligation was met; Phase 0B PROHIBITED clauses remain generic (C-34 satisfied, C-49 absent), isolating C-48's contribution to chain auditability |
| V-03 | Single | C-49 present, C-48 absent — Phase 0B PROHIBITED clauses are sibling-scope-named; Phase 1 gate lacks explicit exact-match anchor condition | When 0B-I PROHIBITED clause names margin-boundary declarations (the 0B-II domain) and 0B-II PROHIBITED clause names constitutive threshold definitions (the 0B-I domain), the boundary is bidirectionally auditable — a scope violation at either gate is detectable by reading only that gate; Phase 1 gate remains without an explicit exact-match anchor checklist condition (C-48 absent), isolating C-49's contribution to boundary auditability |
| V-04 | Combined | C-48 + C-49 both present — Phase 1 gate has explicit exact-match condition; Phase 0B PROHIBITED clauses are sibling-scope-named | When both C-48 and C-49 are satisfied — Phase 1 chain link enforced as a named gate condition, 0B boundary auditable from either sub-phase gate alone — the INCUMBENT traceability chain and the 0B-I/0B-II scope boundary are each independently auditable at their respective gate boundaries without cross-phase inspection; no explicit structural rationale is present in the gate text |
| V-05 | Combined | Full v18 apparatus — C-48 and C-49 present with explicit structural rationale at each new gate position | When every R18 gate condition carries an explicit rationale clause naming what it enforces and why gate-interior placement matters, the design is legible without rubric reference: 0B-I names margin-boundary declarations as the sibling's domain with cross-auditing rationale; 0B-II names constitutive threshold definitions with the same; Phase 1 names the exact-match obligation and states that it closes the Phase 1 chain link declared at Phase 0C; all v17 gate-block-first positions (C-46, C-47) retained with rationale; this is the full v18 ceiling prompt |

Single-axis variations: V-01 (both absent — baseline), V-02 (C-48 present, C-49 absent), V-03 (C-49 present, C-48 absent)
Combined variations: V-04 (C-48 + C-49 together), V-05 (full v18 apparatus)

New R18 territory probed:
- **Both absent as baseline** (V-01): Establishes what the pre-R18 gap looks like — generic PROHIBITED clauses satisfy C-34 but not C-49; Phase 1 gate mentions anchor but not as a C-48-satisfying condition
- **C-48 exact-match gate condition** (V-02, V-04, V-05): Phase 1 exit gate explicitly names exact-match requirement as a binary checklist condition, making the Phase 1 chain link independently auditable
- **C-49 sibling-scope-named** (V-03, V-04, V-05): 0B-I PROHIBITED names the 0B-II domain; 0B-II PROHIBITED names the 0B-I domain — bidirectional boundary auditability without cross-gate inspection
- **C-48 and C-49 independence** (V-04): Both satisfied simultaneously without requiring any structural reorganization beyond the content of two gate conditions and the Phase 1 gate checkbox text
- **Full structural rationale** (V-05): Each new gate condition carries an explicit rationale clause naming what it enforces, why the placement matters, and what a gate that omits it fails to provide; chain auditability and scope auditability are both self-documenting

---

## V-01 — C-48 Absent, C-49 Absent: Pre-R18 Baseline

**Variation axis:** Lifecycle emphasis — Phase 1 gate references the INCUMBENT anchor but has no dedicated binary checklist condition enforcing exact-match wording; Phase 0B PROHIBITED clauses name generic out-of-scope categories (satisfying C-34) but do not name the sibling sub-phase's specific domain (C-49 absent)
**Hypothesis:** When Phase 1 gate has no explicit exact-match anchor checklist condition, the Phase 1 obligation declared at Phase 0C is carried only in the Phase 1 body instructions — a scorer verifying Phase 1 compliance must cross-reference Phase 0C output against Phase 1 body text rather than reading a single gate condition. The Phase 1 chain link is present but not gate-enforced. When 0B PROHIBITED clauses name generic categories ("content outside threshold definition scope", "content outside margin scope") rather than the sibling sub-phase's domain by content type, a scope violation at one sub-phase gate requires reading the other gate to determine whether the boundary was crossed. Both gaps are detectable at R18 scoring: C-48 fails because no binary gate condition enforces exact-match wording; C-49 fails because generic category names do not enable bidirectional boundary auditing from a single gate.

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
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section (out-of-scope content includes margin and deciding-factor material)
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of margin declarations is absent from this sub-section
      (out-of-scope content includes constitutive threshold definitions; level names may be referenced)
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
  [ ] INCUMBENT inertia anchor declared and non-blank
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

## V-02 — C-48 Present, C-49 Absent: Phase 1 Gate Has Exact-Match Anchor Condition

**Variation axis:** Lifecycle emphasis — Phase 1 exit gate adds an explicit binary checklist condition requiring exact-match INCUMBENT anchor citation (C-48 satisfied); Phase 0B PROHIBITED clauses retain generic out-of-scope category names (C-34 satisfied, C-49 absent)
**Hypothesis:** When Phase 1 exit gate contains a named checklist condition explicitly requiring that the INCUMBENT inertia anchor cites the Phase 0C INCUMBENT ANCHOR with exact-match wording, the Phase 1 chain link becomes independently auditable at the Phase 1 gate boundary — a scorer can verify exact-match compliance by reading the gate condition and the Phase 1 subject card without inspecting Phase 0C. The three-phase chain declared at Phase 0C (Phase 1 exact-match, Phase 2 direct-question) now has gate enforcement at both receiving boundaries. Phase 0B PROHIBITED clauses use generic category names: "content outside threshold definition scope" (0B-I) and "content outside margin declaration scope" (0B-II) — these satisfy C-34 (named out-of-scope category) but do not name the sibling sub-phase's domain by content type, leaving the 0B-I/0B-II boundary auditable only by cross-inspecting both gates. C-48's contribution is isolated: Phase 1 chain auditability improves; 0B boundary auditability remains cross-gate-only.

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
  [ ] PROHIBITED: content outside the scope of constitutive threshold definitions is absent
      from this sub-section (out-of-scope content includes margin and deciding-factor material)
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: content outside the scope of margin declarations is absent from this sub-section
      (out-of-scope content includes constitutive threshold definitions; level names may be referenced)
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
      this gate condition makes the Phase 1 chain link auditable at Phase 1 independently of
      inspecting Phase 0C; the obligation declared at Phase 0C exit gate is enforced at this
      receiving boundary (C-48); a Phase 1 gate that requires only a non-blank anchor without
      naming exact-match wording does not satisfy this criterion
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

## V-03 — C-49 Present, C-48 Absent: Phase 0B PROHIBITED Clauses Are Sibling-Scope-Named

**Variation axis:** Inertia framing — Phase 0B-I PROHIBITED clause names margin-boundary declarations (the 0B-II domain) as prohibited; Phase 0B-II PROHIBITED clause names constitutive threshold definitions (the 0B-I domain) as prohibited (C-49 satisfied); Phase 1 exit gate mentions the anchor but has no explicit binary checklist condition enforcing exact-match wording (C-48 absent)
**Hypothesis:** When 0B-I PROHIBITED clause names the sibling's domain ("margin-boundary declarations — the 0B-II domain") and 0B-II PROHIBITED clause names the sibling's domain ("constitutive threshold definitions — the 0B-I domain"), the 0B-I/0B-II boundary becomes bidirectionally auditable: a scope violation at 0B-I is detectable by reading only the 0B-I gate, and a scope violation at 0B-II is detectable by reading only the 0B-II gate. Generic category names ("content outside threshold scope") satisfy C-34 but require cross-gate inspection to audit the boundary; sibling-scope naming eliminates the cross-gate dependency. Phase 1 gate retains the body instruction that the anchor must match exactly, but the gate checklist has no dedicated exact-match condition — the Phase 1 chain link is auditable by reading body instructions and Phase 0C output together but not by reading the Phase 1 gate alone. This isolates C-49's contribution to scope auditability while leaving C-48's chain auditability gap visible.

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
  [ ] PROHIBITED: margin-boundary declarations — the 0B-II domain — are absent from this
      sub-section; sibling-scope naming makes the 0B-I boundary auditable for 0B-II scope
      violations by reading only this gate, without cross-inspecting 0B-II
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions — the 0B-I domain — are absent from this
      sub-section (level names may be referenced; constitutive definitions must not be restated);
      sibling-scope naming makes the 0B-II boundary auditable for 0B-I scope violations by reading
      only this gate, without cross-inspecting 0B-I
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
  [ ] INCUMBENT inertia anchor declared and non-blank
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

## V-04 — C-48 + C-49 Combined: Both Present Without Explicit Rationale

**Variation axis:** Combined — Phase 1 gate has explicit exact-match anchor checklist condition (C-48 satisfied); Phase 0B PROHIBITED clauses name the sibling sub-phase's domain by content type (C-49 satisfied); no explicit structural rationale explaining why each new condition matters
**Hypothesis:** When both C-48 and C-49 are satisfied simultaneously — Phase 1 gate enforces exact-match anchor citation as a named binary condition, 0B-I PROHIBITED names "margin-boundary declarations" as the sibling's domain, 0B-II PROHIBITED names "constitutive threshold definitions" as the sibling's domain — the INCUMBENT traceability chain is gate-enforced at all three links (Phase 0C declares obligations, Phase 1 gate enforces exact-match, Phase 2 gate enforces direct-question as gate-block-first), and the 0B scope boundary is bidirectionally auditable from either sub-phase gate. The absence of explicit rationale means these properties are correct by structure but the design intent is not self-documenting; a scorer reading the gates can verify compliance but cannot determine from the gate text alone why sibling-scope naming is required or why the Phase 1 gate has this exact-match condition. V-05 adds that rationale layer.

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
  [ ] PROHIBITED: margin-boundary declarations — the 0B-II domain — are absent from this sub-section
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions — the 0B-I domain — are absent from this
      sub-section (level names may be referenced; constitutive definitions must not be restated)
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
      this gate condition makes the Phase 1 chain link auditable at Phase 1 independently of
      inspecting Phase 0C; the obligation declared at Phase 0C exit gate is enforced at this
      receiving boundary (C-48)
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

## V-05 — Full v18 Apparatus: C-48 + C-49 With Explicit Structural Rationale

**Variation axis:** Combined — all accumulated structural criteria with C-48 and C-49 both present and each new gate condition carrying an explicit rationale clause naming what it enforces and why the design choice matters
**Hypothesis:** When every new R18 gate condition carries explicit rationale — 0B-I PROHIBITED names the sibling's domain with cross-auditing explanation; 0B-II PROHIBITED names the sibling's domain with cross-auditing explanation; Phase 1 gate names the exact-match obligation and explains that it closes the Phase 1 chain link independently of Phase 0C — the design is self-documenting. A reader of the prompts can determine without consulting the rubric: why the PROHIBITED clauses name each other's domains, what bidirectional auditability means for the 0B scope boundary, and why the Phase 1 gate has a dedicated exact-match checklist condition. All v17 gate-block-first positions (C-46, C-47) retained with their rationale clauses. The pattern: PROHIBITED clauses open 0B sub-phase gates with sibling-scope naming and rationale (C-34, C-43, C-49); anti-drift enforcement clause opens Phase 3 gate with rationale (C-46); INCUMBENT anchor opens Phase 2 gate with rationale (C-47); Phase 1 gate closes the exact-match chain link with rationale (C-48). Each failure condition is evaluable by reading only the gate block it inhabits; each rationale explains the audit consequence of the placement. This is the full v18 ceiling prompt.

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
  [ ] PROHIBITED: margin-boundary declarations — the 0B-II domain — are absent from this
      sub-section; naming the sibling sub-phase's domain by content type (not by sub-phase label
      alone) makes the 0B-I boundary auditable for 0B-II scope violations by reading only this
      gate without cross-inspecting 0B-II; a PROHIBITED clause that names a generic category
      ("out-of-scope content") satisfies C-34 but does not enable bidirectional boundary auditing
      and does not satisfy C-49
  [ ] All five levels have constitutive definitions naming evidence types and cross-subject patterns
  [ ] Completing 0B-II does not pass this gate

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor — the specific evidence property that
tips the verdict from one level to the other.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION | INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  [ ] PROHIBITED: constitutive threshold definitions — the 0B-I domain — are absent from this
      sub-section (level names may be referenced; constitutive definitions must not be restated);
      naming the sibling sub-phase's domain by content type makes the 0B-II boundary auditable for
      0B-I scope violations by reading only this gate without cross-inspecting 0B-I; the two
      PROHIBITED clauses are mutually referential — each names the other's domain — making the
      0B-I/0B-II scope boundary bidirectionally auditable from either gate alone (C-49)
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
      this gate condition closes the Phase 1 link of the traceability chain declared at Phase 0C
      exit gate (where both downstream obligations are declared: exact-match at Phase 1, direct-
      question at Phase 2); placing the exact-match obligation as a named gate condition makes it
      auditable at Phase 1 independently of Phase 0C — a scorer reading this gate item and the
      Phase 1 subject card can verify compliance without inspecting Phase 0C; a Phase 1 gate that
      requires a non-blank anchor without naming exact-match wording carries the chain obligation
      in body instructions only and does not satisfy C-48; this criterion is the Phase 1 parallel
      of C-45 (Phase 2 gate enforces direct-question anchor) — C-41 declared both obligations;
      C-48 closes the Phase 1 link; C-45 closes the Phase 2 link
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
      reading through affirmative completion conditions; the anchor is triply enforced: declared at
      the source with downstream obligations named (Phase 0C exit gate, C-41), enforced as a
      gate-interior exact-match condition at Phase 1 (C-48), and required as a direct-question gate
      condition here at Phase 2 as the first gate item (C-45, C-47); a Phase 2 gate whose first
      checklist item is any condition other than this anchor requirement does not satisfy C-47 even
      when the anchor condition is present as a later gate item; gate-block-first placement makes
      the chain enforcement immediately auditable at Phase 2 gate entry
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
      condition satisfies C-44 but fails C-46; gate-block-first is the positional parallel of C-34's
      requirement applied to the Phase 3 anti-drift enforcement clause
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
| C-32 | PASS | PASS | PASS | PASS | PASS |
| C-33 | PASS | PASS | PASS | PASS | PASS |
| C-34 | PASS | PASS | PASS | PASS | PASS |
| C-39 | PASS | PASS | PASS | PASS | PASS |
| C-40 | PASS | PASS | PASS | PASS | PASS |
| C-41 | PASS | PASS | PASS | PASS | PASS |
| C-43 | PASS | PASS | PASS | PASS | PASS |
| C-44 | PASS | PASS | PASS | PASS | PASS |
| C-45 | PASS | PASS | PASS | PASS | PASS |
| C-46 | PASS | PASS | PASS | PASS | PASS |
| C-47 | PASS | PASS | PASS | PASS | PASS |
| **C-48** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-49** | **FAIL** | **FAIL** | **PASS** | **PASS** | **PASS** |

**Distinguishing pattern:**
- V-01: Both C-48 and C-49 fail — establishes the pre-R18 gap; all v17 criteria satisfied; the two new R18 obligations are absent
- V-02: C-48 passes, C-49 fails — Phase 1 chain link gate-enforced; 0B scope boundary requires cross-gate inspection
- V-03: C-48 fails, C-49 passes — 0B scope boundary bidirectionally auditable from either gate; Phase 1 chain link not gate-enforced
- V-04: Both C-48 and C-49 pass — chain enforced at all three downstream boundaries; 0B boundary bidirectionally auditable; no structural rationale in gate text
- V-05: Both C-48 and C-49 pass with explicit rationale — design is self-documenting; each gate condition names what it enforces and what a gate that omits it fails to provide

**New R18 ceiling:** V-04 and V-05 both satisfy C-48 + C-49. V-05 adds self-documenting rationale at each new gate position, making the structural intent legible without rubric reference.
