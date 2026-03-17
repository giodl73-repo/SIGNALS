Written to `simulations/quest/variations/scout-naming-variations-R2-2026-03-14.md`.

---

## Variations: scout-naming R2

**5 variations across 4 axes:**

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Inertia framing | Status-quo competitor as scoring anchor forces deeper C-04 Strategy rationale |
| V-02 | Output format (tier-weight bridge) | HIGH=9/MEDIUM=6/LOW=3 mapping fixes R1 V-03's C-02 failure while preserving structural DISQ rule |
| V-03 | Lifecycle depth (4-phase + gates) | Gate confirmations at phase boundaries produce equivalent C-11/C-12 compliance with leaner instruction surface |
| V-04 | Combined (gates + inertia) | Phase gates + status-quo anchor: structural enforcement + deep C-04 rationale |
| V-05 | Combined (tier-weight + gates + inertia) | All three new axes; tests coherence under accumulation |

---

**Round 2 context vs Round 1:**

Under the v2 rubric formula (aspirational denominator = 4), all five variations are designed to pass C-10, C-11, and C-12 — targeting the new 97.5 ceiling. The key advancement from R1:

- **C-11** (generation-time enforcement): every variation has an explicit "mark [DISQ: constraint] immediately, do not carry into SCORE" instruction in the GENERATE phase
- **C-12** (phase-structured output): every variation has at least 4 named phase headers with no cross-phase bleed; scoring rows never appear under GENERATE, no new candidates introduced under SCORE or DECIDE

**Primary differentiation** within the expected 97.5 cluster is C-04 rationale depth:
- V-01/V-04/V-05 add the `vs Status-Quo` column and require the DECIDE rationale to explain outperformance against the status-quo — this cannot be satisfied by "it scored highest"
- V-02 revives V-03 R1's strongest C-06 mechanism (structural DISQ rule: no judgment, LOW on core = auto-disqualified) without the C-02 failure
- V-03's gate confirmations are the only new structural mechanism; gates force explicit self-audit before each phase transition

**One open risk**: V-02's tier-to-numeric mapping produces a composite in the range 3.0–9.0 (not 1–10). The C-02 pass condition requires "declared weights sum to 100%" — that is satisfied — but an evaluator reading the composite column may flag the compressed scale as non-standard. Worth noting in the scorecard.
s, new territory), then V-03 (gate mechanism alone), then V-04 and V-05 for combined effects. Primary evaluation question: does inertia framing produce measurably deeper C-04 rationale across V-01 / V-04 / V-05?

---

## V-01: Inertia framing

**Axis**: Inertia framing — status-quo competitor named in SETUP and used as scoring benchmark in DECIDE
**Hypothesis**: Anchoring the DECIDE phase against the status-quo forces the Strategy role to produce
differentiated rationale rather than abstract positioning claims. C-04 rationale depth improves because
the top pick must be defended as better than something concrete, not just as "highest composite."

```
You are running /scout-naming.

SETUP: Auto-detect domain from repo context (CLAUDE.md, plugin-plan.md).

Domain vocabulary: Extract 5-10 terms that describe what this product does,
how it positions itself, and the problem it solves. Write them:
  Domain vocabulary: [term1, term2, ...]
  Source: [file name(s)]

Constraint: Parse any constraint from the invocation. State it:
  Constraint: [constraint text, or "none"]

Status-quo: Identify the incumbent — the name the team currently uses informally,
the product the user currently reaches for, or the market category default.
  Status-quo: [name or convention, or "not identified"]
This is the implicit benchmark. The top pick must be defensible as strictly better.

Role weights (locked):
  Strategy: 25%  |  PM: 25%  |  GTM: 20%  |  UX: 20%  |  Design: 10%

GENERATE: Produce 10-15 candidate names. Tag each with generation strategy:
  [VOC] derived from domain vocabulary
  [EVK] evocative / metaphor-based
  [CPD] compound or portmanteau
  [FNC] functional / descriptive
At least 3 must be [VOC].

If a constraint was parsed, enforce it during generation. Mark any candidate that
violates the constraint as [DISQ: constraint] immediately. Do not carry violating
candidates into SCORE.

SCORE: Score each non-disqualified candidate on 1-10 per role. Compute weighted composite.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | vs Status-Quo |
|-----------|----------------|----------|-----------|----------|--------------|-----------|---------------|

vs Status-Quo column: Rate each candidate's positioning clarity relative to the status-quo:
  (+) clearly beats status-quo on Strategy dimension
  (=) comparable — no meaningful differentiation
  (-) weaker — explain why in a brief note below the table
If no status-quo was identified, omit this column.

Disqualify any candidate where Strategy < 6 or PM < 6. Label: [DISQ: low score].

CHECK: Collision check for the top 3 candidates:
  1. Internal: Namespace collision against plugin names in this repo.
  2. External: npm/PyPI availability + notable brand or domain conflict.
  Report: [candidate] / [class] / [hit or clear]

DECIDE:
- Top Pick: Name the winner. State composite score. Rationale must:
    (1) Reference at least two scoring dimensions by name
    (2) Explain how this name outperforms the status-quo on Strategy positioning
    (3) Connect to at least one domain vocabulary term extracted in SETUP
    If no status-quo was identified, explain the positioning advantage over the
    category default instead.
- Runner-Up: Name it. State composite. One sentence: why is it a credible fallback?
- Disqualified Summary: Full list with labeled reasons. Tally by cause:
    [constraint], [low score], [collision], [other]

FINDINGS REGISTER: SF-NN table. At minimum, one entry on:
  - Status-quo gap: how strongly entrenched is the incumbent? Does the naming
    space have room for displacement?
  - Vocabulary coverage: did the top pick emerge from [VOC] candidates?
  - Role weighting calibration: is 25/25/20/20/10 right for this domain?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms, status_quo.
```

---

## V-02: Output format — traffic-light with tier-weight bridge

**Axis**: Output format — traffic-light tiers (HIGH/MEDIUM/LOW) with explicit numeric mapping
(HIGH=9, MEDIUM=6, LOW=3) so weighted composite is computed from declared weights
**Hypothesis**: Defining a tier-to-numeric mapping converts tier-based scoring into a legitimate
weighted composite, fixing R1 V-03's C-02 failure (undeclared weights). The structural DISQ rule
(LOW on PM or Strategy = auto-disqualified) and constraint column (strongest C-05/C-06 mechanisms
in R1) are preserved. If C-02 passes, this becomes the format with the strongest structural
enforcement of all role requirements.

```
You are running /scout-naming. Scoring uses traffic-light tiers with a declared numeric mapping.

SETUP: Auto-detect domain from repo context (CLAUDE.md, plugin-plan.md).

Domain vocabulary: Extract 5-10 terms describing what this product does and how it
positions itself. Write them:
  Domain vocabulary: [term1, term2, ...]
  Source: [file name(s)]

Constraint: Parse any constraint from the invocation. State it:
  Constraint: [constraint text, or "none"]

TIER SCORING SYSTEM (declared, locked for this run):
  Tiers: HIGH / MEDIUM / LOW
  Numeric mapping: HIGH = 9 | MEDIUM = 6 | LOW = 3
  Role weights: Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10%
  Weight sum: 100%
  Composite formula:
    Composite = (Strategy_val × 0.25) + (PM_val × 0.25)
              + (GTM_val × 0.20) + (UX_val × 0.20) + (Design_val × 0.10)
  Composite range: 3.0 (all LOW) to 9.0 (all HIGH)

GENERATE: Produce 10-15 candidate names across functional, evocative, and compound types.
Tag each [VOC], [EVK], [CPD], or [FNC]. At least 3 must be [VOC].

If a constraint was parsed, enforce it during generation. Mark any violating candidate
[DISQ: constraint] immediately. Do not carry it into SCORE.

SCORE: Build the scoring matrix. One row per non-disqualified candidate.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Constraint |
|-----------|----------------|----------|-----------|----------|--------------|-----------|------------|

Assign H/M/L per dimension. Compute numeric composite from the declared mapping.
Constraint column: PASS or FAIL against the parsed constraint.
  Any FAIL in this column → [DISQ: constraint violation] in Composite.

DISQUALIFICATION RULE (structural, not judgment):
  Any candidate scoring LOW on Strategy or PM → immediately disqualified.
  Label: [DISQ: low Strategy] or [DISQ: low PM] in the Composite column.
  No judgment required — LOW on either core dimension is automatically disqualifying.

CHECK: Collision check — top 3 candidates:
  1. Internal: Namespace collision in this repo.
  2. External: npm/PyPI availability + notable brand or domain conflict.
  Report: [candidate] / [class] / [hit or clear]

DECIDE:
- Top Pick: Identify the highest numeric composite (compute from mapping; do not rely
  on tier labels alone). State the numeric composite (e.g., 7.5 not "HIGH").
  Rationale must reference at least one scoring dimension by name.
- Runner-Up: First viable candidate. State numeric composite. One sentence fallback.
- Disqualified: Already flagged in matrix. Summarize count by cause:
    [constraint], [low Strategy], [low PM], [collision]

FINDINGS REGISTER: SF-NN table. At least one entry on:
  - Tier boundary calibration: is HIGH=9 / MEDIUM=6 / LOW=3 the right mapping for
    this domain, or does collapsing a 1-10 scale to 3 tiers lose signal?
  - Vocabulary influence: did [VOC] candidates outperform [EVK] and [FNC]?
  - Constraint edge cases surfaced during scoring
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
scoring_format: traffic-light-numeric, tier_mapping: {HIGH: 9, MEDIUM: 6, LOW: 3}.
```

---

## V-03: Lifecycle depth — compressed phases with verification gates

**Axis**: Lifecycle emphasis — 4-phase structure (SETUP, GENERATE, SCORE, DECIDE) with an
explicit verification gate at the end of each phase; the model must write a gate confirmation
line before advancing
**Hypothesis**: Gate confirmations are a leaner enforcement mechanism than V-05 R1's 5-phase
verbose structure. If a model writes "Generated: 12. Pre-disqualified: 2. Advancing: 10."
before scoring, constraint enforcement (C-11) and phase separation (C-12) become structurally
unavoidable with fewer total instructions. Tests whether gates substitute for instruction
verbosity without sacrificing compliance.

```
You are running /scout-naming. Four phases with gates.
Each gate must be written before advancing to the next phase.

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. Declare role weights (locked for this run):
     Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10% | Sum: 100%

GATE 1 — Write this line before generating:
  "Vocab: N terms from [source]. Constraint: [stated / none]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC] (derived from domain vocabulary).

Constraint enforcement (generation-time):
  For each candidate: if it violates the parsed constraint, mark [DISQ: constraint] here.
  These candidates do not advance to PHASE 3.

GATE 2 — Write this line before scoring:
  "Candidates generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates may be introduced in this phase.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite |
|-----------|----------------|----------|-----------|----------|--------------|-----------|

Scores: 1-10 per dimension. Compute weighted composite.
Score floor: Strategy < 6 or PM < 6 → [DISQ: low score].

Collision check — top 3 candidates:
  Internal (repo namespace) + External (npm/PyPI + brand).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 — Write this line before deciding:
  "Surviving after score disqualification: N. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

- Top Pick: State composite score. Rationale must reference at least two scoring
  dimensions and connect to at least one vocabulary term from Phase 1.
- Runner-Up: State score. One sentence fallback rationale.
- Disqualified Summary: Full list with labeled reasons. Tally by cause:
    [constraint], [low score], [collision], [other]

FINDINGS REGISTER: SF-NN table. One entry per:
  - Vocabulary coverage (did the top pick emerge from [VOC]?)
  - Role weighting calibration
  - Disqualification patterns (what caused most eliminations?)
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms.
```

---

## V-04: Combined — phase gates + inertia framing

**Axes**: Lifecycle depth (gates from V-03) + Inertia framing (status-quo benchmark from V-01)
**Hypothesis**: Gate confirmations provide structural C-11/C-12 enforcement while the status-quo
anchor ensures the DECIDE phase produces C-04 rationale grounded in positioning context rather
than abstract scoring. The combination tests whether structural enforcement (gates) and behavioral
targeting (inertia framing) reinforce each other or interfere.

```
You are running /scout-naming. Four phases with gates. Each gate must be
written before advancing.

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. Identify the status-quo: the name the team currently uses, the informal working
   title, or the market category default this product enters alongside.
     Status-quo: [name or convention, or "not identified"]
   This is the implicit benchmark. Every candidate is evaluated against it.

4. Declare role weights (locked):
     Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10% | Sum: 100%

GATE 1 — Write before generating:
  "Vocab: N terms. Constraint: [stated/none]. Status-quo: [name/none]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint → mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 — Write before scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates may be introduced here.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | vs Status-Quo |
|-----------|----------------|----------|-----------|----------|--------------|-----------|---------------|

Scores: 1-10. Compute weighted composite.
vs Status-Quo column: Rate each candidate's positioning clarity relative to the status-quo:
  (+) beats status-quo on Strategy
  (=) comparable — no clear differentiation
  (-) weaker — flag with a brief inline note
If no status-quo was identified, omit this column.

Score floor: Strategy < 6 or PM < 6 → [DISQ: low score].

Collision check — top 3:
  Internal (repo namespace) + External (npm/PyPI + brand).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 — Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

- Top Pick: State composite score. Rationale must:
    (1) Reference at least two scoring dimensions by name
    (2) Explain how this name outperforms the status-quo on Strategy positioning
    (3) Connect to at least one vocabulary term from Phase 1 SETUP
    If no status-quo was identified, explain the positioning advantage
    over the category default.
- Runner-Up: State score. One sentence: why is it a credible fallback?
- Disqualified Summary: Full list with labeled reasons. Tally by cause.

FINDINGS REGISTER: SF-NN table. At minimum:
  - Status-quo gap: how entrenched is the incumbent? What displacement barrier exists?
  - Vocabulary coverage
  - Role weighting calibration
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_order: [strategy, pm, gtm, ux, design].
```

---

## V-05: Combined — tier-weight bridge + phase gates + inertia framing

**Axes**: Output format (tier-weight bridge from V-02) + Lifecycle depth (gates from V-03)
+ Inertia framing (status-quo from V-01)
**Hypothesis**: Combining all three new axes preserves the structural DISQ rule from V-02's
traffic-light format, enforces phase separation via gates, and grounds the DECIDE rationale
against the status-quo. The tier-weight bridge means C-02 and C-06 are both satisfied via a
single scoring format. Tests whether the three axes remain coherent under combination or
introduce conflicting requirements.

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

GATE 1 — Write before generating:
  "Vocab: N terms. Constraint: [stated/none]. Status-quo: [name/none]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint → mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 — Write before scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates may be introduced here.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Constraint | vs Status-Quo |
|-----------|----------------|----------|-----------|----------|--------------|-----------|------------|---------------|

Assign H/M/L per dimension. Compute numeric composite from declared mapping.
Constraint column: PASS or FAIL. FAIL → [DISQ: constraint violation] in Composite.
vs Status-Quo: (+) beats | (=) ties | (-) weaker on Strategy positioning.
If no status-quo was identified, omit the vs Status-Quo column.

DISQUALIFICATION RULE (structural):
  Any LOW on Strategy or PM → [DISQ: low Strategy] / [DISQ: low PM] in Composite.
  No judgment required.

Collision check — top 3:
  Internal (repo namespace) + External (npm/PyPI + brand).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 — Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

- Top Pick: State numeric composite (e.g., 7.5 not "HIGH"). Rationale must:
    (1) Reference at least two scoring dimensions by name
    (2) Explain how this name outperforms the status-quo on Strategy
    (3) Connect to at least one vocabulary term from Phase 1
- Runner-Up: State numeric composite. One sentence fallback rationale.
- Disqualified Summary: Full list with labeled reasons. Tally by cause:
    [constraint], [low Strategy], [low PM], [collision], [other]

FINDINGS REGISTER: SF-NN table. At minimum, one entry on:
  - Tier boundary calibration (HIGH=9/MEDIUM=6/LOW=3 — right for this domain?)
  - Status-quo gap (how entrenched is the incumbent?)
  - Vocabulary coverage
  - Disqualification patterns
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_format: traffic-light-numeric,
tier_mapping: {HIGH: 9, MEDIUM: 6, LOW: 3},
scoring_order: [strategy, pm, gtm, ux, design].
```
