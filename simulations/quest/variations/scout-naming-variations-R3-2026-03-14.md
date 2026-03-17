Written to `simulations/quest/variations/scout-naming-variations-R3-2026-03-14.md`.

---

## Variations: scout-naming R3

**5 variations across 3 new single axes, then combinations:**

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Role sequence (UX-first) | Scoring UX before Strategy surfaces speakability/positioning tension not visible under Strategy-first ordering |
| V-02 | Phrasing register (conversational) | Conversational framing preserves structural enforcement; tests whether instructional voice affects compliance independent of structural gates |
| V-03 | C-14 labeled sub-parts | Explicit (1)/(2)/(3) lines under TOP PICK make C-14 verifiable by inspection — a missing sub-part is a visible gap, not an omitted clause in prose |
| V-04 | Combined (role sequence + labeled C-14) | UX-first scoring + structured rationale; the Dimensions sub-part must address the UX/Strategy tension surfaced by column order |
| V-05 | Combined (all R2 axes + labeled C-14) | V-05 R2 body (tier-weight + gates + inertia) upgraded with explicit C-14 sub-part labeling; R3 ceiling candidate |

---

**Key design decisions for R3:**

**What's new vs R2:** Role sequence and phrasing register are both unexplored axes — R1 and R2 never touched either. C-14 labeled sub-parts target a specific verifiability gap: R2 V-05 had the 3-part DECIDE requirement embedded in a single inline instruction, which passes C-14 as written but may produce run-on prose that technically satisfies all three elements without isolating them. V-03/V-04/V-05 impose a structured record format that forces each sub-part to be a distinct labeled line.

**Target**: 98.3 (5/6 aspirational, skipping C-09). V-01 should reach 98.3 via the proven R2 V-04 inline 3-part pattern. V-02 should reach 98.3 if phrasing register is neutral on compliance. V-03/V-04/V-05 should reach 98.3 via labeled sub-parts — and if sub-part labeling produces better C-14 evidence than inline text, they may anchor the recommended golden candidate.

**The score ceiling stays at 98.3** until `--validate` (C-09) is implemented. R3's contribution is showing which structural form of C-14 produces the most verifiable and useful rationale within that ceiling.
"Produce 10-15...").
  V-02 tests "You will produce..." — conversational framing, unchanged structural requirements.
- **C-14 labeled sub-parts** (V-03, V-04, V-05): R2 embedded the 3-part requirement as inline
  instructions within the DECIDE paragraph. R3 structures DECIDE as a labeled record with explicit
  (1) Dimensions, (2) vs. Status-quo, (3) Vocabulary sub-lines. A missing sub-part is a visible
  gap in the record, not an omitted clause inside prose.

**Primary differentiation** within the expected 98.3 cluster is C-14 verifiability mechanism:
- V-03/V-04/V-05: explicit labeled sub-parts — pass/fail visible by inspection
- V-01: inline 3-part requirement from R2 V-04 (proven to satisfy C-14 as written)
- V-02: inline 3-part in conversational framing — tests whether register change degrades C-14

**One structural bet**: V-03 introduces TOP PICK / RUNNER-UP / DISQUALIFIED SUMMARY as a structured
record rather than a bulleted prose section. This may also improve C-07 compliance (Runner-Up is now
a labeled section with explicit score + rationale lines, not an embedded sentence).

---

## V-01: Role sequence — UX-first column order

**Axis**: Role sequence — UX column appears first in scoring matrix; weights and formula unchanged
**Hypothesis**: Column order in the scoring matrix anchors the evaluation frame. When UX
(speakability, memorability) is scored first, the model encounters the user-experience lens before
the positioning and strategic lenses. This may produce higher variance between UX and Strategy
scores — surfacing candidates where there is genuine tension between "says well" and "positions well."
Prior rounds always led with Strategy, which may have primed positioning as the dominant frame.

```
You are running /scout-naming. Four phases with gates. Each gate must be
written before advancing.

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. Identify the status-quo: the incumbent name, working title, or market category
   default this product enters alongside.
     Status-quo: [name, or "not identified"]

4. Declare role weights (locked). UX column appears first in the scoring matrix —
   name adoption begins with whether users can say it and remember it. Weights unchanged.
     UX: 20%  |  PM: 25%  |  GTM: 20%  |  Strategy: 25%  |  Design: 10%
     Sum: 100%
     Composite = (UX_score × 0.20) + (PM_score × 0.25) + (GTM_score × 0.20)
               + (Strategy_score × 0.25) + (Design_score × 0.10)

GATE 1 — Write before generating:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC]:
  [VOC] derived from domain vocabulary
  [EVK] evocative / metaphor-based
  [CPD] compound or portmanteau
  [FNC] functional / descriptive
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  For each candidate: if it violates the parsed constraint, mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 — Write before scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates in this phase.

| Candidate | UX (20%) | PM (25%) | GTM (20%) | Strategy (25%) | Design (10%) | Composite |
|-----------|----------|----------|-----------|----------------|--------------|-----------|

Scores: 1-10 per dimension. Compute weighted composite from the declared formula above.
Score floor: Strategy < 6 or PM < 6 → [DISQ: low score]. Label in Composite column.

vs Status-Quo column (optional): if status-quo was identified, add a final column:
  (+) beats status-quo on Strategy | (=) comparable | (-) weaker

Collision check — top 3 candidates:
  1. Internal: Namespace collision against plugin names in this repo.
  2. External: npm/PyPI availability + notable brand or domain conflict.
  Report: [candidate] / [class] / [hit or clear]

GATE 3 — Write before deciding:
  "Surviving after score disqualification: N. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

- Top Pick: Name the winner. State composite score. Rationale must:
    (1) Reference at least two scoring dimensions by name
    (2) Explain how this name outperforms the status-quo on Strategy positioning
    (3) Connect to at least one domain vocabulary term extracted in SETUP
    If no status-quo was identified, explain the positioning advantage over the
    category default instead.
- Runner-Up: Name it. State composite. One sentence: why is it a credible fallback?
- Disqualified Summary: Full list with labeled reasons. Tally by cause:
    [constraint], [low score], [collision], [other]

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - UX-first scoring effect: did scoring speakability before positioning surface
    any UX-vs-Strategy tension not visible under Strategy-first column order?
  - Status-quo gap: how entrenched is the incumbent?
  - Vocabulary coverage: did the top pick emerge from [VOC] candidates?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_order: [ux, pm, gtm, strategy, design].
```

---

## V-02: Phrasing register — conversational/descriptive

**Axis**: Phrasing register — "you will" descriptive framing rather than imperative ("do this")
**Hypothesis**: Imperative register signals compliance-as-rule-following; conversational register
signals compliance-as-understanding. All structural requirements (gates, phase headers, DISQ labels,
3-part DECIDE rationale) are preserved unchanged. If compliance rates differ between this variation
and the imperative-register variations, the difference is attributable to phrasing register alone —
isolating whether the instructional voice affects model behavior independent of structural enforcement.

```
You are running /scout-naming. This is how it works.

--- PHASE 1: SETUP ---

You will read CLAUDE.md and plugin-plan.md to understand the product domain.
From those sources, extract 5-10 vocabulary terms that describe what this product
does, how it positions itself, and the problem it solves.

  Domain vocabulary: [term1, term2, ...]
  Source: [file name(s)]

You will also check whether the invocation contains a constraint (e.g., "must be
two words," "no trademarked terms"):
  Constraint: [constraint text, or "none"]

Then identify the status-quo: the informal name the team uses, the product this
one would replace, or the market category it enters alongside.
  Status-quo: [name or convention, or "not identified"]

Role weights are fixed for this run:
  Strategy: 25%  |  PM: 25%  |  GTM: 20%  |  UX: 20%  |  Design: 10%
  Sum: 100%
  Composite = (Strategy × 0.25) + (PM × 0.25) + (GTM × 0.20)
            + (UX × 0.20) + (Design × 0.10)

GATE 1: Write this line before moving to generation:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified]. Weights: 100%."

--- PHASE 2: GENERATE ---

You will produce 10-15 candidate names. For each, tag it with how it was derived:
  [VOC] — came from domain vocabulary
  [EVK] — evocative or metaphor-based
  [CPD] — compound or portmanteau
  [FNC] — functional / descriptive
At least 3 should be [VOC] — names that emerge from the product's own vocabulary.

If you parsed a constraint above, check each candidate against it during generation.
Any candidate that violates the constraint gets labeled [DISQ: constraint] here and
does not advance to scoring.

GATE 2: Write this line before moving to scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

You will score each candidate that cleared GATE 2. Do not introduce new candidates
in this phase.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite |
|-----------|----------------|----------|-----------|----------|--------------|-----------|

Assign a score of 1-10 per dimension and compute the weighted composite.

If a candidate scores below 6 on Strategy or PM, label it [DISQ: low score] in the
Composite column — this is a structural rule, not a judgment call.

After scoring, run a collision check on the top 3 candidates:
  Internal: any namespace conflict with existing plugin names in this repo.
  External: npm/PyPI availability and notable brand or domain conflicts.
  Report: [candidate] / [class] / [hit or clear]

GATE 3: Write this line before moving to the decision:
  "Surviving after score disqualification: N. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

Here is where you make the recommendation.

- Top Pick: Name the winner and state its composite score. Your rationale should cover:
    (1) At least two scoring dimensions — name them and explain why this candidate
        scored well on each
    (2) How this name beats the status-quo on positioning — what it communicates that
        the status-quo does not. If no status-quo was identified, compare against the
        market category default instead.
    (3) A connection to at least one vocabulary term extracted in SETUP — the name
        should be grounded in the product's own language
- Runner-Up: Name it and state its composite score. One sentence on why it is the fallback.
- Disqualified Summary: List everything disqualified, with its labeled reason. Tally:
    [constraint], [low score], [collision], [other]

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Status-quo gap: how entrenched is the incumbent, and does naming have room to displace it?
  - Vocabulary coverage: did [VOC] candidates outperform [EVK] and [FNC]?
  - Role weighting calibration: is 25/25/20/20/10 the right balance for this domain?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms, status_quo.
```

---

## V-03: C-14 labeled rationale — explicit sub-part structure

**Axis**: C-14 structure — DECIDE phase uses a structured record with labeled sub-parts
(1) Dimensions, (2) vs. Status-quo, (3) Vocabulary as explicit named lines under TOP PICK
**Hypothesis**: Embedding the 3 C-14 requirements as inline instructions within a prose paragraph
(R2 approach) allows the model to satisfy C-14 via a run-on sentence that technically mentions
all three elements. Structuring DECIDE as labeled sub-parts removes that failure mode: a missing
sub-part is a visible gap in the output record, not an omitted clause inside a paragraph. This
makes C-14 pass/fail unambiguously verifiable by inspection — and may improve output usefulness
by forcing the rationale into a parallel structure that is easier to compare across candidates.

```
You are running /scout-naming. Four phases with gates. Each gate must be
written before advancing.

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. Identify the status-quo: the incumbent name, working title, or market category
   default this product enters alongside.
     Status-quo: [name, or "not identified"]

4. Declare role weights (locked):
     Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10% | Sum: 100%
     Composite = (Strategy × 0.25) + (PM × 0.25) + (GTM × 0.20)
               + (UX × 0.20) + (Design × 0.10)

GATE 1 — Write before generating:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint → mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 — Write before scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates may be introduced here.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite |
|-----------|----------------|----------|-----------|----------|--------------|-----------|

Scores: 1-10. Compute weighted composite.
Score floor: Strategy < 6 or PM < 6 → [DISQ: low score]. Label in Composite column.

Collision check — top 3:
  Internal (repo namespace) + External (npm/PyPI + brand).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 — Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [composite value]
  (1) Dimensions: [Name at least two scoring dimensions and state the specific reason
      this candidate scored well on each. E.g., "Strategy: 8 — signals X clearly.
      PM: 9 — memorable and domain-distinct."]
  (2) vs. Status-quo: [State the status-quo from SETUP. Explain what this name
      communicates on Strategy positioning that the status-quo does not. If no
      status-quo was identified, compare against the market category default.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain
      the specific connection between this candidate and that term.]

RUNNER-UP
  Name: [candidate]
  Score: [composite value]
  Fallback rationale: [One sentence — why is this a credible alternative?]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally by cause:
    [constraint]: N
    [low score]: N
    [collision]: N
    [other]: N

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Status-quo gap: how entrenched is the incumbent? What displacement barrier exists?
  - Vocabulary coverage: did the top pick emerge from [VOC] candidates?
  - Role weighting calibration: is 25/25/20/20/10 right for this domain?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms, status_quo.
```

---

## V-04: Combined — role sequence + labeled C-14

**Axes**: Role sequence (UX-first from V-01) + C-14 labeled rationale (structured sub-parts from V-03)
**Hypothesis**: UX-first column order surfaces speakability-vs-positioning tension in the scoring matrix.
Labeled C-14 sub-parts in DECIDE ensure that tension is resolved explicitly in the rationale — the
Dimensions sub-part must name UX and/or Strategy scores, and the vs. Status-quo sub-part must show
which trade-off the team should accept. Tests whether a different scoring frame (UX-first) plus
structured rationale format produce a more useful decision artifact than Standard Strategy-first ordering.

```
You are running /scout-naming. Four phases with gates. Each gate must be
written before advancing.

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. Identify the status-quo: the incumbent name, working title, or market category
   default this product enters alongside.
     Status-quo: [name, or "not identified"]

4. Declare role weights (locked). UX column appears first in the scoring matrix —
   name adoption begins with whether users can say and remember it. Weights unchanged.
     UX: 20%  |  PM: 25%  |  GTM: 20%  |  Strategy: 25%  |  Design: 10%
     Sum: 100%
     Composite = (UX_score × 0.20) + (PM_score × 0.25) + (GTM_score × 0.20)
               + (Strategy_score × 0.25) + (Design_score × 0.10)

GATE 1 — Write before generating:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint → mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 — Write before scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates in this phase.

| Candidate | UX (20%) | PM (25%) | GTM (20%) | Strategy (25%) | Design (10%) | Composite |
|-----------|----------|----------|-----------|----------------|--------------|-----------|

Scores: 1-10. Compute weighted composite.
Score floor: Strategy < 6 or PM < 6 → [DISQ: low score]. Label in Composite column.

Collision check — top 3:
  Internal (repo namespace) + External (npm/PyPI + brand).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 — Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [composite value]
  (1) Dimensions: [Name at least two scoring dimensions (UX, PM, GTM, Strategy,
      or Design) and state the specific reason this candidate scored well on each.
      If UX and Strategy scores diverged, address that tension explicitly.]
  (2) vs. Status-quo: [State the status-quo from SETUP. Explain what positioning
      gap this name fills that the status-quo leaves open. If no status-quo was
      identified, compare against the market category default.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain
      the specific connection between this candidate and that term.]

RUNNER-UP
  Name: [candidate]
  Score: [composite value]
  Fallback rationale: [One sentence.]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally:
    [constraint]: N | [low score]: N | [collision]: N | [other]: N

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - UX-first scoring effect: did evaluating speakability before positioning surface
    any UX-vs-Strategy tension? How was that tension resolved in DECIDE?
  - Status-quo gap: how entrenched is the incumbent?
  - Vocabulary coverage: did the top pick emerge from [VOC] candidates?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_order: [ux, pm, gtm, strategy, design].
```

---

## V-05: Combined — all R2 axes + labeled C-14

**Axes**: Output format (tier-weight bridge from R2 V-02) + Lifecycle depth (gates from R2 V-03)
+ Inertia framing (status-quo from R2 V-01) + C-14 labeled rationale (sub-parts from V-03 R3)
**Hypothesis**: R2 V-05 already cleared C-10, C-11, C-12, C-13 and had a 3-part inline DECIDE
requirement that satisfies C-14 as written under v2. This variation upgrades only the DECIDE
output format to labeled sub-parts — converting C-14 from an inline instruction to a verifiable
output record. If R2 V-05 was the R2 ceiling candidate, this should be the R3 ceiling candidate:
same structural enforcement floor (structural DISQ, gate-confirmed C-13) plus explicit labeled C-14.
The test: does sub-part labeling produce any conflict with the tier-weight bridge format or the
vs. Status-quo column already in the scoring matrix?

```
You are running /scout-naming. Four phases with gates. Scoring uses traffic-light
tiers with a declared numeric mapping for weighted composite.

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. Identify the status-quo: the incumbent name, working title, or market category
   default this product enters alongside.
     Status-quo: [name, or "not identified"]

4. TIER SCORING SYSTEM (declared, locked):
     Tiers: HIGH / MEDIUM / LOW
     Numeric mapping: HIGH = 9 | MEDIUM = 6 | LOW = 3
     Role weights: Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10%
     Weight sum: 100%
     Composite = (Strategy_val × 0.25) + (PM_val × 0.25)
               + (GTM_val × 0.20) + (UX_val × 0.20) + (Design_val × 0.10)
     Range: 3.0 (all LOW) to 9.0 (all HIGH)

GATE 1 — Write before generating:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint → mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 — Write before scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates may be introduced here.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Constraint | vs Status-Quo |
|-----------|----------------|----------|-----------|----------|--------------|-----------|------------|---------------|

Assign H/M/L per dimension. Compute numeric composite from declared mapping.
Constraint column: PASS or FAIL. FAIL → [DISQ: constraint violation] in Composite.
vs Status-Quo: (+) beats | (=) ties | (-) weaker on Strategy positioning.
If no status-quo was identified, omit the vs Status-Quo column.

DISQUALIFICATION RULE (structural, not judgment):
  Any LOW on Strategy or PM → [DISQ: low Strategy] or [DISQ: low PM] in Composite.
  No judgment required.

Collision check — top 3:
  Internal (repo namespace) + External (npm/PyPI + brand).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 — Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [numeric composite, e.g., 7.5 — not "HIGH"]
  (1) Dimensions: [Name at least two scoring dimensions (Strategy, PM, GTM, UX,
      Design) and state the specific rationale for each tier assigned. E.g.,
      "Strategy: HIGH — signals X clearly. PM: HIGH — memorable, short enough for
      spoken use."]
  (2) vs. Status-quo: [State the status-quo from SETUP. Explain what this name
      communicates on Strategy positioning that the status-quo does not. If no
      status-quo was identified, compare against the market category default.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain
      the specific connection between this candidate and that term.]

RUNNER-UP
  Name: [candidate]
  Score: [numeric composite]
  Fallback rationale: [One sentence.]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally by cause:
    [constraint]: N | [low Strategy]: N | [low PM]: N | [collision]: N | [other]: N

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Tier boundary calibration: is HIGH=9/MEDIUM=6/LOW=3 the right mapping for this domain?
  - Status-quo gap: how entrenched is the incumbent?
  - Vocabulary coverage: did [VOC] candidates outperform [EVK] and [FNC]?
  - Disqualification patterns: what caused most eliminations?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_format: traffic-light-numeric,
tier_mapping: {HIGH: 9, MEDIUM: 6, LOW: 3},
scoring_order: [strategy, pm, gtm, ux, design].
```
