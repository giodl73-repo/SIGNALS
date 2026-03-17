INTERVIEW MASTER GATE (item: Schema 0.2 declared)` — C-45 is satisfied: the dual authority is transparent in a single gate item without requiring a reader to cross-reference two separate checklist items. When sub-schemas are still declared with handles at their respective phases (0.4 at Phase 1, 0.3 in the master gate, 0.2 in the master gate) rather than consolidated in a FORMAT CONTRACT registry section with populated example rows, C-44 fails independently. V-03 isolates C-45's structural contribution: co-declared pairs make dual authority transparent; the absence of a registry makes individual schemas searchable only by document body inspection.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## SECTION 0 — DOCUMENT-HEAD CONTRACT

This section assigns numbered handles to all sub-schemas. All phases derive their format
requirements from these declarations. Each sub-schema number is a citation target.

### 0.1 GATE FORMAT CONTRACT

All phase exit gates use this named-block structure:
```
PHASE N [NAME] EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: [out-of-scope content named by category]
  REQUIRED:
    [ ] item
```
A gate missing a named header or a PROHIBITED clause fails 0.1.

### 0.2 EVIDENCE TABLE SCHEMA

All Phase 3 evidence tables use these columns in this order:
`| # | Evidence text | Signal type | Strength | Rationale | Basis | Profile relevance |`

Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION
Strength: STRONG / MODERATE / WEAK (Rationale required per item)
Basis: verbatim / inferred / corroborated

### 0.3 MOMENT-LABEL FORMAT

All Phase 2 moment labels use one of:
```
SURPRISING (expected: [Phase 0C prediction → tier name], got: [transcript content])
CONFIRMING (validates: [Phase 0C prediction → tier name])
INCONCLUSIVE (signal: [transcript content], ambiguity: [why direction is unclear])
```
Decision rules: SURPRISING = expectation violated; CONFIRMING = expectation upheld;
INCONCLUSIVE = signal present but directionally ambiguous.

### 0.4 SUBJECT CARD SCHEMA

All Phase 1 subject cards declare these fields:
ROLE / PRIOR KNOWLEDGE (direct experience + knowledge gaps) / BLIND SPOTS /
DISPOSITION / PRIMARY CONCERN / VOCABULARY SIGNATURE (3 terms) / EVIDENTIAL FUNCTION

INCUMBENT adds: DESIGNATION: INCUMBENT + INERTIA ANCHOR (exact Phase 0C match).

---

## PHASE 0A — INERTIA PROFILE TABLE CONSTRUCTION

Before designing any subject card, map the practices being displaced.

For each practice declare:
  - Practice name
  - Stickiness factor: specific mechanism sustaining this practice (not generic)
  - Switching cost or structural limitation

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
  REQUIRED:
    [ ] INERTIA PROFILE TABLE has at least two rows with non-generic stickiness factors
    [ ] PROFILE RELEVANCE vocabulary declared here as gate-scope contract for Phase 3:
        Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
        Contract source: this gate item — not any reproduced tag list elsewhere.
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
               INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent
              (level names may appear; definitions must not be restated)
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Margin factors create non-overlapping level regions
    [ ] Completing 0B-I does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if order were reversed

For each tier declare: expected evidence type / expected posture / confirming signal /
surprising signal.

INCUMBENT anchor: names the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] ADJACENCY blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier predictions with all four fields
    [ ] INCUMBENT anchor declared: names specific Phase 0A row and stickiness factor
        Downstream propagation obligations:
          - Phase 1: INCUMBENT inertia anchor must match this row exactly (exact-match required)
          - Phase 2: INCUMBENT transcript must contain a question directly naming this anchor
    [ ] Gate block structure — per 0.1

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence per Schema 0.4 field structure declared in Section 0.

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent
  REQUIRED:
    [ ] Four subject cards in tier sequence, each following 0.4 field structure — per 0.4
    [ ] All cards have non-generic BLIND SPOTS and structural EVIDENTIAL FUNCTION entries
    [ ] INCUMBENT: designation label + INERTIA ANCHOR exactly matching Phase 0C row
    [ ] Subject card schema and master gate authorization co-declared:
        Schema 0.4 field compliance confirmed — per 0.4 | auth: PRE-INTERVIEW MASTER GATE
        (item: subject card schema declared)
    [ ] Gate block structure — per 0.1

---

## PRE-INTERVIEW MASTER GATE — ALL SETUP PREREQUISITES CONFIRMED

PRE-INTERVIEW MASTER GATE — ALL REQUIRED BEFORE PHASE 2 MAY BEGIN:
  PROHIBITED: interview transcripts and evidence extraction content are absent
  REQUIRED:
    [ ] Phase 0A EXIT GATE: passed — INERTIA PROFILE TABLE complete, PROFILE RELEVANCE
        vocabulary declared at gate scope
    [ ] Phase 0B-I EXIT GATE: passed — all five verdict levels have constitutive definitions
    [ ] Phase 0B-II EXIT GATE: passed — all four margin pairs have named deciding factors
    [ ] Phase 0C EXIT GATE: passed — tier sequence, adjacency blocks, predictions, INCUMBENT
        anchor and propagation obligations declared
    [ ] Phase 1 EXIT GATE: passed — four subject cards complete, INCUMBENT designation and
        exact-match anchor confirmed
    [ ] Schema 0.3 moment-label format fully specified in Section 0 (three-form decision taxonomy)
    [ ] Schema 0.2 evidence table fully specified in Section 0 (column order declared)
    [ ] Gate block structure — per 0.1

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence.

For each subject:
  - Write 4-6 questions anchored to declared PRIMARY CONCERN
  - INCUMBENT transcript: at least one question directly names the Phase 0C INCUMBENT anchor
  - Answers in subject's distinct voice; vocabulary signature terms appear naturally
  - Mark exactly one moment per subject using Schema 0.3 format, citing Phase 0C prediction

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: evidence extraction and synthesis content are absent
  REQUIRED:
    [ ] All four transcripts complete before any hypothesis questions
    [ ] INCUMBENT transcript contains a question directly naming the INCUMBENT ANCHOR
        (direct-question required per Phase 0C propagation obligation)
    [ ] Each subject has exactly one moment labeled per 0.3 format, citing Phase 0C prediction —
        per 0.3 | auth: PRE-INTERVIEW MASTER GATE (item: Schema 0.3 declared)
    [ ] Answers in distinct voices; vocabulary signature terms appear naturally
    [ ] Gate block structure — per 0.1

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables using Schema 0.2 column order declared in Section 0.

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent
  REQUIRED:
    [ ] Evidence section separate from transcripts and synthesis
    [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag not in the Phase 0A exit gate
        vocabulary declaration (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) is a gate
        failure — detectable by reading this condition against evidence items without inspecting
        Phase 0A body text
    [ ] Each item uses Schema 0.2 column order and all columns populated —
        per 0.2 | auth: PRE-INTERVIEW MASTER GATE (item: Schema 0.2 declared)
    [ ] PROFILE RELEVANCE tags comply with Phase 0A exit gate vocabulary contract —
        Phase 0A exit gate is the named source; a reproduced tag list does not close this gap
    [ ] All STRENGTH ratings have non-blank, non-self-referential rationale sentences
    [ ] Gate block structure — per 0.1

---

## PHASE 4 — SYNTHESIS

Produce in order: CROSS-PERSONA SYNTHESIS, DISPOSITION ARC, CONTRADICTION REGISTER,
EPISTEMIC RE-WEIGHTING, INERTIA PROFILE ACCOUNTING, PREDICTION DELTA, INERTIA/ADOPTION PARTITION.

NET VERDICT with VERDICT MARGIN AUDIT table (both boundary rows required).

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence not present in Phase 3 is absent
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] Net verdict from Phase 0B-I levels; constitutive configuration named
    [ ] VERDICT MARGIN AUDIT table: both boundary rows populated; single-row table is gate
        failure by content type detectable by row count
    [ ] Prediction delta names specific Phase 3 evidence items
    [ ] Gate block structure — per 0.1

---

## V-04 — Combined: C-44 + C-45 Together

**Variation axis:** Combined output format + lifecycle emphasis — FORMAT CONTRACT — SCHEMA REGISTRY with populated example rows (C-44) AND gate items with dual obligations carry co-declared pairs (C-45)
**Hypothesis:** When both innovations operate simultaneously, each criterion is independently auditable: C-44 is verifiable by navigating to the FORMAT CONTRACT — SCHEMA REGISTRY section and confirming each schema has a populated example row; C-45 is verifiable by locating any gate item with dual citation obligations and confirming both citation types appear in the same item. Neither verification requires the other: a scorer can confirm C-44 without reading any gate items, and can confirm C-45 without checking whether the registry exists. Their combined satisfaction creates a layered citation chain — schemas are browsable at the registry (C-44), and at every gate item that derives from a schema AND requires master gate authorization, both authorities are co-cited (C-45).

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## FORMAT CONTRACT — SCHEMA REGISTRY

This section is the single named authority for all format contracts in this document.
All sub-schemas are listed here with handles, definitions, and populated example rows.
Navigate to this section to inspect any schema without searching the document body.

---

### Schema 0.1 — Gate Block Format

Structure:
```
PHASE N [NAME] EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: [out-of-scope content named by category]
  REQUIRED:
    [ ] item — per 0.N [for schema-derived items]
    [ ] item   [for phase-local items]
```

**Populated example:**
```
PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure — per 0.1
```

---

### Schema 0.2 — Evidence Table

Columns in order: `| # | Evidence text | Signal type | Strength | Rationale | Basis | Profile relevance |`

Permitted values: Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION |
Strength: STRONG / MODERATE / WEAK | Basis: verbatim / inferred / corroborated

**Populated example row:**
| 1 | "Retraining the team on observable state took four sprints — I have the retro notes." | CONSTRAINT | STRONG | Subject names a specific timeline from direct experience; claim is verifiable against documented artifacts | verbatim | LIMITATION |

A table omitting any column or leaving Rationale blank fails 0.2.

---

### Schema 0.3 — Moment-Label Format

Three-form decision taxonomy (all three forms declared; all three decision rules stated):
```
SURPRISING (expected: [Phase 0C prediction → tier name], got: [transcript content])
CONFIRMING (validates: [Phase 0C prediction → tier name])
INCONCLUSIVE (signal: [transcript content], ambiguity: [why direction is unclear])
```
Decision rules:
- SURPRISING: labeled moment violates the Phase 0C prediction for this tier
- CONFIRMING: labeled moment upholds the Phase 0C prediction for this tier
- INCONCLUSIVE: signal present but cannot be assigned to either prior-expectation category

**Populated example:**
```
CONFIRMING (validates: [Phase 0C prediction → SKEPTIC: expected INVALIDATION posture on
            operational readiness grounds])
```

A label missing the parenthetical structure or the Phase 0C source citation fails 0.3.

---

### Schema 0.4 — Subject Card

Fields in order: ROLE / PRIOR KNOWLEDGE (direct experience + knowledge gaps) / BLIND SPOTS /
DISPOSITION / PRIMARY CONCERN / VOCABULARY SIGNATURE / EVIDENTIAL FUNCTION

INCUMBENT adds: DESIGNATION: INCUMBENT / INERTIA ANCHOR: [exact Phase 0C row + stickiness factor]

**Populated example:**
```
ROLE: Staff Engineer, Developer Experience
PRIOR KNOWLEDGE:
  - Direct experience: Led three SDK adoption programs across platform teams; owns onboarding metrics
  - Knowledge gaps: Has not operated the current signal-routing stack in production
BLIND SPOTS: Adoption curve optimism — prior programs were voluntary; this migration is mandated
DISPOSITION: CHAMPION
PRIMARY CONCERN: Reducing time-to-first-signal for new service owners
VOCABULARY SIGNATURE: adoption curve | onboarding friction | time-to-first-signal
EVIDENTIAL FUNCTION: Provides the affirmative case that subsequent skeptic objections are measured against
```

---

## PHASE 0A — INERTIA PROFILE TABLE CONSTRUCTION

Before designing any subject card, map the practices being displaced.

For each practice declare: practice name / stickiness factor (specific mechanism, not generic) /
switching cost or structural limitation.

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
  REQUIRED:
    [ ] INERTIA PROFILE TABLE has at least two rows with non-generic stickiness factors
    [ ] PROFILE RELEVANCE vocabulary declared here as gate-scope contract for Phase 3:
        Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
        Contract source: this gate item — not any tag list reproduced elsewhere.
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
               INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent
              (level names may appear; definitions must not be restated)
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Margin factors create non-overlapping level regions
    [ ] Completing 0B-I does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if order were reversed

For each tier declare: expected evidence type / expected posture / confirming signal /
surprising signal.

INCUMBENT anchor: names the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] ADJACENCY blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier predictions with all four fields
    [ ] INCUMBENT anchor declared: names specific Phase 0A row and stickiness factor
        Downstream propagation obligations:
          - Phase 1: INCUMBENT inertia anchor must match this row exactly (exact-match required)
          - Phase 2: INCUMBENT transcript must contain a question directly naming this anchor
    [ ] Gate block structure — per 0.1

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence per Schema 0.4 (FORMAT CONTRACT — SCHEMA REGISTRY).

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent
  REQUIRED:
    [ ] Four subject cards in tier sequence; each field complete and non-generic per 0.4 —
        per 0.4 | auth: PRE-INTERVIEW MASTER GATE (item: subject card schema declared)
    [ ] INCUMBENT: designation label + INERTIA ANCHOR exactly matching Phase 0C row
    [ ] Gate block structure — per 0.1

---

## PRE-INTERVIEW MASTER GATE — ALL SETUP PREREQUISITES CONFIRMED

PRE-INTERVIEW MASTER GATE — ALL REQUIRED BEFORE PHASE 2 MAY BEGIN:
  PROHIBITED: interview transcripts and evidence extraction content are absent
  REQUIRED:
    [ ] Phase 0A EXIT GATE: passed — INERTIA PROFILE TABLE complete, PROFILE RELEVANCE
        vocabulary declared at gate scope
    [ ] Phase 0B-I EXIT GATE: passed — all five verdict levels have constitutive definitions
    [ ] Phase 0B-II EXIT GATE: passed — all four margin pairs have named deciding factors
    [ ] Phase 0C EXIT GATE: passed — tier sequence, adjacency blocks, predictions, INCUMBENT
        anchor and propagation obligations declared
    [ ] Phase 1 EXIT GATE: passed — four subject cards complete, INCUMBENT designation and
        exact-match anchor confirmed; 0.4 compliance co-declared at Phase 1 gate
    [ ] Schema 0.3: fully specified with populated example in FORMAT CONTRACT — SCHEMA REGISTRY
    [ ] Schema 0.2: fully specified with populated example row in FORMAT CONTRACT — SCHEMA REGISTRY
    [ ] Gate block structure — per 0.1

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence.

For each subject:
  - Write 4-6 questions anchored to declared PRIMARY CONCERN
  - INCUMBENT transcript: at least one question directly names the Phase 0C INCUMBENT anchor
  - Answers in subject's distinct voice; vocabulary signature terms appear naturally
  - Mark exactly one moment per subject using Schema 0.3 format, citing Phase 0C prediction

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: evidence extraction and synthesis content are absent
  REQUIRED:
    [ ] All four transcripts complete before any hypothesis questions
    [ ] INCUMBENT transcript contains a question directly naming the INCUMBENT ANCHOR
        (direct-question required per Phase 0C propagation obligation)
    [ ] Each subject has exactly one moment labeled per 0.3 format, citing Phase 0C prediction —
        per 0.3 | auth: PRE-INTERVIEW MASTER GATE (item: Schema 0.3 declared)
    [ ] Answers in distinct voices; vocabulary signature terms appear naturally
    [ ] Gate block structure — per 0.1

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables using Schema 0.2 (FORMAT CONTRACT — SCHEMA REGISTRY).

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent
  REQUIRED:
    [ ] Evidence section separate from transcripts and synthesis
    [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag not in the Phase 0A exit gate
        vocabulary declaration is a gate failure — detectable by reading this condition
        against evidence items without inspecting Phase 0A body text
    [ ] Each item uses Schema 0.2 column order, all columns populated —
        per 0.2 | auth: PRE-INTERVIEW MASTER GATE (item: Schema 0.2 declared)
    [ ] PROFILE RELEVANCE tags comply with Phase 0A exit gate vocabulary contract;
        Phase 0A exit gate is the named source
    [ ] All STRENGTH ratings have non-blank, non-self-referential rationale sentences
    [ ] Gate block structure — per 0.1

---

## PHASE 4 — SYNTHESIS

Produce in order: CROSS-PERSONA SYNTHESIS, DISPOSITION ARC, CONTRADICTION REGISTER,
EPISTEMIC RE-WEIGHTING, INERTIA PROFILE ACCOUNTING, PREDICTION DELTA, INERTIA/ADOPTION PARTITION.

NET VERDICT with VERDICT MARGIN AUDIT table (both boundary rows required).

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence not present in Phase 3 is absent
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] Net verdict from Phase 0B-I levels; constitutive configuration named
    [ ] VERDICT MARGIN AUDIT table: both boundary rows populated; single-row is gate failure
        detectable by row count
    [ ] Prediction delta names specific Phase 3 evidence items
    [ ] Gate block structure — per 0.1

---

## V-05 — Full v16 Apparatus: C-44 + C-45 + C-46 + C-47 With Structural Rationale

**Variation axis:** Combined — FORMAT CONTRACT — SCHEMA REGISTRY with populated example rows (C-44), co-declared dual citations (C-45), ANTI-DRIFT enforcement clause gate-block-first at Phase 3 (C-46), INCUMBENT anchor gate-block-first at Phase 2 (C-47), with explicit structural rationale at each positional and co-declaration requirement
**Hypothesis:** When all four v16 innovations operate simultaneously with explicit rationale at each structural requirement, the prompt is fully self-documenting: C-44 is satisfied and named at the registry section; C-45 is satisfied and named at each co-declared gate item with an explanation of why co-declaration is required; C-46 is satisfied by placing the ANTI-DRIFT clause first in Phase 3 with a rationale naming what a gate that buries it fails to provide; C-47 is satisfied by placing the INCUMBENT anchor condition first in Phase 2 with the same rationale logic. A scorer working from this prompt can verify each criterion by reading the structural rationale embedded in the gate text itself, without consulting the rubric. This is the v16 ceiling prompt.

---

You are executing the prove-interview skill for Signal.

Topic: {{Topic}}
Signal: {{Signal}}
Date: {{Date}}
Output path: simulations/prove/investigations/{{topic}}-interview-{{date}}.md

---

## FORMAT CONTRACT — SCHEMA REGISTRY

This section is the single named authority for all format contracts in this document.
All sub-schemas are listed here — centralized as a browsable reference so that any schema
definition can be located by navigating to this section without searching the document body.
This satisfies C-44: each schema has its handle, column or field definitions, and a populated
example row. Schemas not in this registry have no authority in downstream phases.

---

### Schema 0.1 — Gate Block Format

Structure:
```
PHASE N [NAME] EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: [out-of-scope content named by category — gate-block-first placement makes
              scope restriction auditable at gate entry without reading affirmative items]
  REQUIRED:
    [ ] item — per 0.N | auth: PRE-INTERVIEW MASTER GATE (item: N) [dual-obligation items]
    [ ] item — per 0.N [schema-derived items without master gate authorization obligation]
    [ ] item   [phase-local items]
```

**Populated example:**
```
PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent from this section
  REQUIRED:
    [ ] Four subject cards complete per field structure — per 0.4 | auth: PRE-INTERVIEW MASTER GATE
        (item: subject card schema declared)
    [ ] Gate block structure — per 0.1
```

Rules: PROHIBITED clause is always first. Gate items with both sub-schema and master gate
obligations carry both citations co-declared in the same item — `per 0.N | auth: MASTER GATE
(item N)`. Items with only one obligation carry one citation. This is the C-45 contract:
when both apply, both must appear; splitting them into separate items satisfies C-42 and C-35
independently but fails C-45.

---

### Schema 0.2 — Evidence Table

Columns in order: `| # | Evidence text | Signal type | Strength | Rationale | Basis | Profile relevance |`

Permitted values: Signal type: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION |
Strength: STRONG / MODERATE / WEAK | Basis: verbatim / inferred / corroborated |
Profile relevance: from Phase 0A exit gate vocabulary only

**Populated example row:**
| 2 | "We've tried two observability migrations — both stalled at month four when incidents spiked and we reverted." | RISK | STRONG | Subject names a specific recurring failure pattern from direct operational experience with prior migrations at this organization | verbatim | STICKINESS |

---

### Schema 0.3 — Moment-Label Format

Three-form decision taxonomy — all three forms and all three decision rules declared here:

```
SURPRISING (expected: [Phase 0C prediction → tier name], got: [transcript content])
CONFIRMING (validates: [Phase 0C prediction → tier name])
INCONCLUSIVE (signal: [transcript content], ambiguity: [why direction is unclear])
```

Decision rules:
- SURPRISING: labeled moment violates the Phase 0C prediction declared for this tier
- CONFIRMING: labeled moment upholds the Phase 0C prediction declared for this tier
- INCONCLUSIVE: signal present but directionally ambiguous — cannot be assigned to either
  prior-expectation category. Outputs that apply SURPRISING or CONFIRMING to every labeled moment
  without acknowledging any INCONCLUSIVE possibility fail C-14 unless explicitly noting all
  labeled moments were unambiguously one or the other.

**Populated example:**
```
SURPRISING (expected: [Phase 0C prediction → CHAMPION: expected VALIDATION posture on team
            readiness], got: [flagged a prerequisite skill gap that would delay adoption by
            at least one sprint])
```

---

### Schema 0.4 — Subject Card

Fields in order:
```
ROLE:
PRIOR KNOWLEDGE:
  - Direct experience:
  - Knowledge gaps:
BLIND SPOTS: [specific domain or perspective gap — not blank, not generic]
DISPOSITION: [INCUMBENT / CHAMPION / EVALUATOR / SKEPTIC]
PRIMARY CONCERN:
VOCABULARY SIGNATURE: [term-1] | [term-2] | [term-3]
EVIDENTIAL FUNCTION: [structural role in the evidence chain — not a role or disposition restatement]
```
INCUMBENT adds: `DESIGNATION: INCUMBENT` / `INERTIA ANCHOR: [exact Phase 0C row + stickiness factor]`

**Populated example:**
```
ROLE: Engineering Manager, Core Services
PRIOR KNOWLEDGE:
  - Direct experience: Managed two platform migrations from roadmap approval through team adoption
  - Knowledge gaps: No hands-on implementation exposure; relies on team leads for technical depth
BLIND SPOTS: Underweights implementation friction that doesn't surface in sprint reports
DISPOSITION: EVALUATOR
PRIMARY CONCERN: Timeline predictability for dependent team commitments
VOCABULARY SIGNATURE: milestone commitment | dependency freeze | adoption readiness
EVIDENTIAL FUNCTION: Calibration surface — validates Champion claims and surfaces timeline risks
    the INCUMBENT hasn't articulated as blockers
```

---

## PHASE 0A — INERTIA PROFILE TABLE CONSTRUCTION

Before designing any subject card, map the practices being displaced.

For each practice declare: practice name / stickiness factor (specific mechanism, not generic) /
switching cost or structural limitation.

Produce a named table: INERTIA PROFILE TABLE.

PHASE 0A EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict-level classifications, margin declarations, and tier predictions are absent
              from this section — gate-block-first placement makes this scope restriction auditable
              at gate entry without reading affirmative items
  REQUIRED:
    [ ] INERTIA PROFILE TABLE has at least two rows with non-generic stickiness factors
    [ ] PROFILE RELEVANCE vocabulary declared here as gate-scope enforcement contract for Phase 3:
        Permitted tags: STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL
        Each Phase 3 evidence item must carry exactly one of these tags.
        Contract source: this gate item. A tag list reproduced at Phase 3 does not replace this
        declaration. A Phase 3 gate that cites this vocabulary without naming this gate as the
        contract source does not close the mid-chain drift gap.
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-I — VERDICT THRESHOLD DEFINITIONS

Declare constitutive definitions for all five verdict levels.

Required levels: STRONG VALIDATION / VALIDATION / MIXED / INVALIDATION / STRONG INVALIDATION

For each level, state the evidence configuration that constitutes it — evidence types and
cross-subject pattern. A level name alone is not a constitutive definition.

PHASE 0B-I EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: margin-boundary declarations and deciding-factor content are absent from this
              sub-section — gate-block-first placement makes this scope restriction immediately
              auditable at gate entry; a gate that opens with affirmative content checks before
              this prohibition cannot be verified by reading only the first gate item
  REQUIRED:
    [ ] All five levels have constitutive definitions naming evidence types and patterns
    [ ] Completing 0B-II does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0B-II — VERDICT MARGIN DEFINITIONS

For each adjacent level pair, declare the deciding margin factor.

Required pairs: STRONG VALIDATION / VALIDATION | VALIDATION / MIXED | MIXED / INVALIDATION |
               INVALIDATION / STRONG INVALIDATION

PHASE 0B-II EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: constitutive threshold definitions from Phase 0B-I are absent from this sub-section
              (level names may appear; constitutive definitions must not be restated) —
              gate-block-first placement makes this scope restriction auditable at gate entry;
              a gate that opens with affirmative checks before this prohibition cannot be verified
              by reading only the first gate item
  REQUIRED:
    [ ] All four margin pairs have a named deciding factor
    [ ] Margin factors create non-overlapping level regions
    [ ] Completing 0B-I does not pass this gate
    [ ] Gate block structure — per 0.1

---

## PHASE 0C — TIER SEQUENCE AND PREDICTIONS

Tier sequence: INCUMBENT → CHAMPION → EVALUATOR → SKEPTIC

For each consecutive tier pair, declare an ADJACENCY block:
  - What the preceding tier establishes
  - What the following tier's departure is measured against
  - Contrast lost if order were reversed

For each tier declare: expected evidence type / expected posture / confirming signal /
surprising signal.

INCUMBENT anchor: names the specific Phase 0A INERTIA PROFILE TABLE row and stickiness factor.

PHASE 0C EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: verdict threshold and margin content are absent
  REQUIRED:
    [ ] ADJACENCY blocks for all three consecutive tier pairs
    [ ] All four tiers have per-tier predictions with all four fields
    [ ] INCUMBENT anchor declared: names specific Phase 0A row and stickiness factor
        Downstream propagation obligations declared at this gate so any chain break is auditable
        at the phase that names its predecessor:
          - Phase 1: INCUMBENT inertia anchor must match this row exactly (exact-match required —
            a paraphrase does not satisfy)
          - Phase 2: INCUMBENT transcript must contain a question directly naming this anchor
            (direct-question required — referencing the topic without naming the anchor fails)
    [ ] Gate block structure — per 0.1

---

## PHASE 1 — SUBJECT DESIGN

Design subject cards in tier sequence per Schema 0.4 (FORMAT CONTRACT — SCHEMA REGISTRY).

PHASE 1 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: transcript lines are absent from this section
  REQUIRED:
    [ ] Four subject cards in tier sequence; each field complete and non-generic per 0.4 —
        per 0.4 | auth: PRE-INTERVIEW MASTER GATE (item: subject card schema declared)
        [C-45: this item has both sub-schema authority (0.4) and master gate authorization
        obligations — co-declaration is required; splitting into two separate items satisfies
        each independently but fails C-45 because the dual authority is not transparent in
        a single gate item]
    [ ] INCUMBENT: designation label + INERTIA ANCHOR exactly matching Phase 0C row
    [ ] Gate block structure — per 0.1

---

## PRE-INTERVIEW MASTER GATE — ALL SETUP PREREQUISITES CONFIRMED

Before Phase 2 begins, confirm that all structural prerequisites for the interview phase are
collectively and fully satisfied. This gate cross-references named phase-gate completions rather
than re-asserting readiness — evidenced closure (C-34) requires pointing to completed sub-gates,
not re-verifying their content here.

PRE-INTERVIEW MASTER GATE — ALL REQUIRED BEFORE PHASE 2 MAY BEGIN:
  PROHIBITED: interview transcripts and evidence extraction content are absent from this section
  REQUIRED:
    [ ] Phase 0A EXIT GATE: passed — INERTIA PROFILE TABLE complete, PROFILE RELEVANCE
        vocabulary declared at gate scope as enforcement contract
    [ ] Phase 0B-I EXIT GATE: passed — all five verdict levels have constitutive definitions
    [ ] Phase 0B-II EXIT GATE: passed — all four margin pairs have named deciding factors
    [ ] Phase 0C EXIT GATE: passed — tier sequence, adjacency blocks, predictions,
        INCUMBENT anchor and downstream propagation obligations declared
    [ ] Phase 1 EXIT GATE: passed — four subject cards complete in tier sequence; INCUMBENT
        designation and exact-match anchor confirmed; 0.4 co-declared at Phase 1 gate
    [ ] Schema 0.3: fully specified with decision taxonomy and populated example in
        FORMAT CONTRACT — SCHEMA REGISTRY
    [ ] Schema 0.2: fully specified with populated example row in FORMAT CONTRACT — SCHEMA REGISTRY
    [ ] Gate block structure — per 0.1

---

## PHASE 2 — TRANSCRIPT

Write all four subject transcripts in tier sequence.

For each subject:
  - Write 4-6 questions anchored to declared PRIMARY CONCERN
  - INCUMBENT transcript: at least one question directly names the Phase 0C INCUMBENT anchor
  - Answers in subject's distinct voice; vocabulary signature terms appear naturally
  - Mark exactly one moment per subject using Schema 0.3 format, citing Phase 0C prediction

PHASE 2 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: evidence extraction and synthesis content are absent from this section
  REQUIRED:
    [ ] INCUMBENT transcript contains a question directly naming the INCUMBENT ANCHOR declared
        in Phase 0C exit gate — this condition is the first gate item because gate-block-first
        placement makes the INCUMBENT chain obligation immediately auditable at gate entry without
        reading through affirmative completion conditions; the anchor is doubly enforced at the
        source (Phase 0C exit gate, satisfying C-41) and required at this receiving phase boundary
        as the first gate condition (satisfying C-47); a Phase 2 gate whose first checklist item
        is any condition other than this anchor requirement satisfies C-45 but fails C-47
    [ ] All four transcripts complete before any hypothesis questions
    [ ] Each subject has exactly one moment labeled per 0.3 format, citing Phase 0C prediction —
        per 0.3 | auth: PRE-INTERVIEW MASTER GATE (item: Schema 0.3 declared)
        [C-45: both sub-schema authority (0.3) and master gate authorization apply to this item;
        co-declaration makes both authorities visible in a single gate item]
    [ ] Answers in distinct voices; vocabulary signature terms appear naturally
    [ ] Gate block structure — per 0.1

---

## PHASE 3 — EVIDENCE EXTRACTION

Produce per-subject evidence tables using Schema 0.2 (FORMAT CONTRACT — SCHEMA REGISTRY).

PHASE 3 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: synthesis content is absent from this section
  REQUIRED:
    [ ] ANTI-DRIFT ENFORCEMENT: any PROFILE RELEVANCE tag not present in the Phase 0A exit gate
        vocabulary declaration (STICKINESS | LIMITATION | DISPLACEMENT | EXTERNAL) is a gate
        failure — this condition is the first gate item because gate-block-first placement makes
        vocabulary drift immediately auditable at gate entry without reading through affirmative
        conditions; naming the Phase 0A contract source without stating this failure condition is
        protection by implication only (C-40) and does not constitute enforcement (C-46); placing
        any affirmative item before this condition satisfies C-40 but fails C-46
    [ ] Evidence section separate from transcripts and synthesis
    [ ] Each item uses Schema 0.2 column order, all columns populated —
        per 0.2 | auth: PRE-INTERVIEW MASTER GATE (item: Schema 0.2 declared)
        [C-45: both sub-schema authority (0.2) and master gate authorization apply; co-declaration
        makes both authorities transparent in a single gate item]
    [ ] PROFILE RELEVANCE tags comply with Phase 0A exit gate vocabulary — Phase 0A exit gate
        is the named contract source; a reproduced tag list does not close the mid-chain drift gap
    [ ] All STRENGTH ratings have non-blank, non-self-referential rationale sentences
    [ ] Gate block structure — per 0.1

---

## PHASE 4 — SYNTHESIS

Produce in order: CROSS-PERSONA SYNTHESIS, DISPOSITION ARC, CONTRADICTION REGISTER,
EPISTEMIC RE-WEIGHTING, INERTIA PROFILE ACCOUNTING, PREDICTION DELTA, INERTIA/ADOPTION PARTITION.

NET VERDICT:
  - Verdict classification from Phase 0B-I levels; constitutive configuration named
  - VERDICT MARGIN AUDIT table (both boundary rows required):

    | Boundary | Margin factor | Actual evidence | Placement |
    |----------|---------------|-----------------|-----------|
    | Upper: [level] / [level above] | [Phase 0B-II factor] | [named evidence] | [placement] |
    | Lower: [level below] / [level] | [Phase 0B-II factor] | [named evidence] | [placement] |

PHASE 4 EXIT GATE — ALL REQUIRED BEFORE PROCEEDING:
  PROHIBITED: new evidence not present in Phase 3 is absent from this section
  REQUIRED:
    [ ] All seven synthesis sections present and non-empty
    [ ] Net verdict from Phase 0B-I levels; constitutive configuration named
    [ ] VERDICT MARGIN AUDIT table: both boundary rows populated — a single-row table is a gate
        failure by content type detectable by row count without reading any cell content; a gate
        that requires "completeness" without naming this specific failure condition does not satisfy
        this item
    [ ] Prediction delta names specific Phase 3 evidence items
    [ ] Gate block structure — per 0.1

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
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-28 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-31 | PASS | PASS | PASS | PASS | PASS |
| C-32 | PASS | PASS | PASS | PASS | PASS |
| C-33 | PASS | PASS | PASS | PASS | PASS |
| C-34 | PASS | PASS | PASS | PASS | PASS |
| C-35 | PASS | PASS | PASS | PASS | PASS |
| C-39 | PASS | PASS | PASS | PASS | PASS |
| C-40 | PASS | PASS | PASS | PASS | PASS |
| C-41 | PASS | PASS | PASS | PASS | PASS |
| C-42 | PASS | PASS | PASS | PASS | PASS |
| C-43 | PASS | PASS | PASS | PASS | PASS |
| **C-44** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-45** | **FAIL** | **FAIL** | **PASS** | **PASS** | **PASS** |
| C-46 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-47 | FAIL | FAIL | FAIL | FAIL | PASS |

**Distinguishing pattern:**
- V-01: C-44 FAIL (schemas declared inline at respective phases, no populated-row registry) + C-45 FAIL (dual-obligation gate items split into separate checklist items) — establishes that C-33, C-35, and C-42 can all be satisfied while C-44 and C-45 independently fail
- V-02: C-44 PASS (FORMAT CONTRACT — SCHEMA REGISTRY with populated example rows) + C-45 FAIL (gate items still carry single citation per item despite registry) — isolates C-44's structural contribution: registry navigability is independent of gate item co-declaration
- V-03: C-44 FAIL (schemas in SECTION 0 without populated example rows — no centralized registry) + C-45 PASS (gate items at Phase 1, Phase 2, Phase 3 carry co-declared dual citations) — isolates C-45's structural contribution: dual-obligation transparency does not require a registry to be present
- V-04: C-44 PASS + C-45 PASS — both satisfied simultaneously; neither requires the other; each is independently verifiable
- V-05: All four (C-44, C-45, C-46, C-47) pass with explicit structural rationale — the v16 ceiling prompt

**New R18 ceiling:** V-04 satisfies C-44 + C-45 without the positional requirements. V-05 adds C-46 + C-47 gate-block-first ordering with rationale, constituting the full v16 apparatus.
