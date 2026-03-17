Done. `simulations/quest/variations/scout-naming-variations-R4-2026-03-14.md` written.

---

## Variations: scout-naming R4

| # | Axis | Hypothesis | Target |
|---|------|------------|--------|
| V-01 | Output format — anchored 1-10 scale | Per-role rubric descriptions (1-3/4-6/7-9/10) reduce cross-role scoring variance without losing fine-grained differentiation | 98.75 |
| V-02 | Lifecycle emphasis — phase exit conditions | Exit condition checklists enforce artifact presence before advancing (prescriptive) vs gate counters that confirm cardinality only (confirmatory) | 98.75 |
| V-03 | Inertia framing — status-quo as scored benchmark row | Full scored row exposes the incumbent's absolute profile; candidates can't score 7 on Strategy if the status-quo already occupies 8 without a differentiated story | 98.75 |
| V-04 | Combined (output format + inertia framing) | Anchored scale + benchmark row: interpretive consistency meets visible comparison — displacement case emerges from rubric language, not DECIDE prose | 98.75 |
| V-05 | Combined (all three + C-09 `--validate`) | First inline `--validate` implementation attempt; pins named candidate as Row 2, adds Validation Summary with score profile + tier + verdict | **100.0** if C-09 passes |

**Key design decisions:**

- **Baseline is R3 V-05** — C-15 (labeled sub-parts) and C-16 (Gate 3 binary flags) are structural constants in all R4 variations, not axes.
- **Three fresh single axes** — output format, lifecycle emphasis, and inertia framing were each partially explored in prior rounds but never as the primary single-axis variable with everything else held constant.
- **V-05 targets C-09** — the score ceiling blocker since R1. The `--validate` branch pins Row 2, skips GENERATE for the named candidate, and produces a `Validation Summary` with anchor-tier score profile + rank + CONFIRMED/CONDITIONAL/AT RISK verdict.
- **V-01/V-03 compose cleanly in V-04** — anchored rubric + benchmark row are orthogonal changes; V-04 tests that they do not interfere before V-05 layers on the third axis and C-09.
 without losing fine-grained differentiation.
- **Lifecycle emphasis (V-02)**: Prior rounds used phase headers (R1) and gate counters
  (R2+). V-02 adds phase exit condition checklists -- a phase may not close unless named
  output artifacts are explicitly checked off. Tests whether exit conditions (prescriptive)
  produce higher completeness than counters alone (confirmatory).
- **Inertia framing (V-03)**: R2/R3 used a `vs Status-Quo` column (relative +/=/-). V-03
  gives the status-quo a full scored row in the matrix with all 5 role dimensions -- so
  the delta is directly computable column-by-column. Tests whether a visible benchmark
  row shifts scoring behavior toward relative comparison and raises the bar for strong scores.

**C-09 attempt in V-05**: The `--validate` flag has been the sole score ceiling blocker
since R1. V-05 attempts a complete inline implementation: `--validate <name>` pins that name
as Row 2 (after [STATUS QUO]), skips GENERATE for it, and produces a Validation Summary after
DECIDE with delta notation. If C-09 is satisfied, V-05 targets 100.0.

**Target scores:**
- V-01, V-02, V-03: 98.75 (C-15 + C-16 baseline, new axes do not affect aspirational criteria)
- V-04: 98.75
- V-05: 100.0 if C-09 is satisfied; 98.75 if not

**Axis lineage** (what R4 does NOT re-explore from prior rounds):
- Role sequence: explored R3 V-01 (UX-first) and V-04 (UX-first + labeled C-14)
- Phrasing register: explored R3 V-02 (conversational)
- C-14 labeled sub-parts: explored R3 V-03/V-04/V-05 -- now baseline for all R4

---

## V-01: Output Format -- Anchored 1-10 Scale

**Axis**: Output format -- 1-10 scoring scale with explicit anchor rubric per role (1-3/4-6/7-9/10)
**Hypothesis**: R3 V-01 used 1-10 with no description of what scores mean across roles.
Traffic-light (H/M/L) in R2 V-05 reduced variance by collapsing to three buckets. Anchored
1-10 combines the discrimination of a wide scale with the interpretive consistency of named
tiers -- per-role rubrics tell the model what earns a 3 vs. a 7 on Strategy vs. UX. If
scoring interpretation variance is causing inconsistent composite separation, anchors should
fix it without losing fine-grained differentiation.

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

4. SCORING SYSTEM (declared, locked):
   Role weights: Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10%
   Weight sum: 100%
   Scale: 1-10 per dimension (integer)
   Composite = (Strategy x 0.25) + (PM x 0.25) + (GTM x 0.20)
             + (UX x 0.20) + (Design x 0.10)

   ANCHOR RUBRIC (apply consistently across all candidates):

   Strategy (positioning fit):
     1-3  = off-positioning or generic; could belong to any product in the category
     4-6  = adequate; names the domain but does not differentiate
     7-9  = strong; signals what this product uniquely does or whom it serves
     10   = exceptional; own-able term that creates or defines a category

   PM (memorability):
     1-3  = forgettable; no distinctive phoneme or structure
     4-6  = adequate; retainable but not sticky
     7-9  = strong; short, distinct, survives spoken relay
     10   = exceptional; one-word recall, no disambiguation needed

   GTM (searchability):
     1-3  = buried; collides with high-volume common terms
     4-6  = findable; some competition in search landscape
     7-9  = strong; niche-dominant or brand-distinct search profile
     10   = exceptional; zero-conflict indexable identifier

   UX (speakability):
     1-3  = awkward; unusual stress pattern, ambiguous pronunciation
     4-6  = adequate; speakable but forgettable in conversation
     7-9  = strong; flows naturally in "using [name]" and "run /[name]"
     10   = exceptional; instinctive phonetics, no spelling hesitation

   Design (visual weight):
     1-3  = visually heavy or character-dense; poor in small UI contexts
     4-6  = neutral; fine in standard contexts
     7-9  = strong; clean, compact, works as icon label or namespace prefix
     10   = exceptional; 4-6 characters, natural as monogram or glyph

GATE 1 -- Write before generating:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC]:
  [VOC] derived from domain vocabulary
  [EVK] evocative / metaphor-based
  [CPD] compound or portmanteau
  [FNC] functional / descriptive
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint --> mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 -- Write before scoring:
  "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates in this phase.
Apply the anchor rubric from SETUP -- cite the rubric tier that applies.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | vs Status-Quo |
|-----------|----------------|----------|-----------|----------|--------------|-----------|---------------|

Score floor: Strategy <= 5 or PM <= 5 --> [DISQ: low Strategy] or [DISQ: low PM] in Composite.
vs Status-Quo: (+) beats | (=) ties | (-) weaker than status-quo on Strategy.
If no status-quo was identified, omit the vs Status-Quo column.

Collision check -- top 3 candidates:
  Internal (repo namespace) + External (npm/PyPI + brand/domain).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 -- Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [composite value] / 10.0
  (1) Dimensions: [Name at least two scoring dimensions. For each, state the integer score
      and the anchor-rubric tier that applies. E.g., "Strategy: 8 -- strong; signals X
      clearly, niche-dominant positioning. PM: 9 -- strong; short, survives spoken relay."]
  (2) vs. Status-quo: [State the status-quo from SETUP. Name the specific dimensions where
      this candidate's anchor-rubric tier is higher than the status-quo's estimated tier.
      If no status-quo was identified, compare against the market category default.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain the specific
      connection between this candidate and that term -- why the term is activated or implied.]

RUNNER-UP
  Name: [candidate]
  Score: [composite value] / 10.0
  Fallback rationale: [One sentence -- when or why this is the preferred alternative.]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally by cause:
    [constraint]: N | [low Strategy]: N | [low PM]: N | [collision]: N | [other]: N

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Anchor calibration: did the rubric descriptions produce expected score distributions,
    or did any role's anchor descriptions feel too tight or too loose for this domain?
  - Status-quo gap: how entrenched is the incumbent based on estimated Strategy anchor tier?
  - Vocabulary coverage: did [VOC] candidates outscore [EVK] and [FNC]?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_scale: 1-10-anchored,
weights: {strategy: 0.25, pm: 0.25, gtm: 0.20, ux: 0.20, design: 0.10}.
```

---

## V-02: Lifecycle Emphasis -- Phase Exit Conditions

**Axis**: Lifecycle emphasis -- each phase has an explicit exit condition checklist that must
be satisfied before the gate line is written and the next phase begins
**Hypothesis**: Gate counters (R2+) confirm cardinality -- how many candidates advanced.
Phase exit conditions confirm completeness -- every required artifact for the phase is present.
The difference: a gate line can be written even if the collision check was skipped (the counter
just reports fewer survivors). An exit condition for SCORE includes "Collision report present:
top 3" -- making the check a precondition for advancing rather than a retrospective observation.
Tests whether prescriptive exit conditions produce higher C-03/C-10/C-11 compliance than
confirmatory gate lines alone.

```
You are running /scout-naming. Four phases with gates. A phase may not close
until its exit conditions are met. Write each exit condition check before the gate.

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
     Composite = (Strategy x 0.25) + (PM x 0.25) + (GTM x 0.20)
               + (UX x 0.20) + (Design x 0.10)

SETUP EXIT CONDITIONS -- check each before Gate 1:
  [ ] Domain vocabulary list present (5-10 terms, source named)
  [ ] Constraint acknowledged (or "none" recorded)
  [ ] Status-quo identified (or "not identified" recorded)
  [ ] Role weights declared and sum to 100%

GATE 1 -- Write after exit conditions pass:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint --> mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GENERATE EXIT CONDITIONS -- check each before Gate 2:
  [ ] Candidate count is between 10 and 15 (inclusive)
  [ ] At least 3 [VOC] candidates present
  [ ] Constraint enforcement applied at generation time (not post-hoc filter)
  [ ] All constraint-violating candidates labeled [DISQ: constraint] here

GATE 2 -- Write after exit conditions pass:
  "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates may be introduced.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | vs Status-Quo |
|-----------|----------------|----------|-----------|----------|--------------|-----------|---------------|

Scores: 1-10 per dimension. Compute weighted composite.
Score floor: Strategy <= 5 or PM <= 5 --> [DISQ: low Strategy] or [DISQ: low PM] in Composite.
vs Status-Quo: (+) beats | (=) ties | (-) weaker than status-quo on Strategy.
If no status-quo was identified, omit the vs Status-Quo column.

Collision check -- top 3 candidates:
  Internal (repo namespace) + External (npm/PyPI + brand/domain).
  Report: [candidate] / [class] / [hit or clear]

SCORE EXIT CONDITIONS -- check each before Gate 3:
  [ ] All candidates from Gate 2 appear in the scoring matrix (or carry a [DISQ] label)
  [ ] Score floor applied: all low-scoring candidates labeled [DISQ: low Strategy/PM]
  [ ] vs Status-Quo column populated (or "not identified" noted)
  [ ] Collision report present covering top 3 candidates
  [ ] Both collision classes reported (internal namespace + external registry)

GATE 3 -- Write after exit conditions pass:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [composite value] / 10.0
  (1) Dimensions: [Name at least two scoring dimensions (Strategy, PM, GTM, UX, Design)
      and state the specific reason this candidate scored well on each. E.g.,
      "Strategy: 8 -- signals X clearly. PM: 9 -- memorable and domain-distinct."]
  (2) vs. Status-quo: [State the status-quo from SETUP. Explain what this name
      communicates on Strategy positioning that the status-quo does not. If no
      status-quo was identified, compare against the market category default.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain
      the specific connection between this candidate and that term.]

RUNNER-UP
  Name: [candidate]
  Score: [composite value] / 10.0
  Fallback rationale: [One sentence -- when or why this is the preferred alternative.]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally by cause:
    [constraint]: N | [low Strategy]: N | [low PM]: N | [collision]: N | [other]: N

DECIDE EXIT CONDITIONS -- check each before writing artifact:
  [ ] TOP PICK named with composite score
  [ ] All three labeled sub-parts present: (1) Dimensions / (2) vs. Status-quo / (3) Vocabulary
  [ ] RUNNER-UP named with fallback rationale
  [ ] DISQUALIFIED SUMMARY complete with tally

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Exit condition effect: did any exit condition catch a missing artifact that a gate
    counter alone would have passed? What was the artifact?
  - Status-quo gap: how entrenched is the incumbent?
  - Vocabulary coverage: did [VOC] candidates outscore [EVK] and [FNC]?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, lifecycle_enforcement: exit-conditions.
```

---

## V-03: Inertia Framing -- Status-Quo as Scored Benchmark Row

**Axis**: Inertia framing -- the status-quo competitor receives a full scored row in the matrix
(all 5 role dimensions scored) rather than appearing only as a relative column
**Hypothesis**: R3 V-04/V-05 used a `vs Status-Quo` column showing (+/=/-) relative to the
incumbent on Strategy. This makes the comparison explicit but keeps the incumbent's actual scores
invisible. A full scored benchmark row exposes the status-quo's absolute profile -- candidates
see whether they are beating a strong incumbent (8/7/9/8/7) or a weak one (5/4/6/5/5). The
visibility of the incumbent's actual scores may shift scoring behavior: a candidate cannot score
7 on Strategy if the incumbent already occupies 8 unless it has a clearly differentiated
positioning story. Tests whether visible benchmark raises the scoring bar relative to +/=/-
column alone.

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
   default this product enters alongside. This name will receive a full scored row
   in the matrix labeled [STATUS QUO] -- score it now, before generating candidates.
     Status-quo: [name, or "not identified"]

4. Declare role weights (locked):
     Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10% | Sum: 100%
     Composite = (Strategy x 0.25) + (PM x 0.25) + (GTM x 0.20)
               + (UX x 0.20) + (Design x 0.10)

   If status-quo was identified, score it now (scores 1-10 per dimension):
     [STATUS QUO] baseline:
       Strategy: __  PM: __  GTM: __  UX: __  Design: __  Composite: __

GATE 1 -- Write before generating:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified].
   SQ composite: [value or N/A]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

The status-quo composite is now visible as a displacement floor. Generate candidates
that you expect to outscore the status-quo on Strategy. If a candidate clearly cannot
beat the status-quo on Strategy, mark it [BELOW-SQ: Strategy] here and exclude from SCORE.

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint --> mark [DISQ: constraint] here.
  Do not carry violating candidates into PHASE 3.

GATE 2 -- Write before scoring:
  "Generated: N. Below SQ threshold: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates in this phase.
Insert [STATUS QUO] as Row 1 with scores pre-populated from SETUP.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Beat SQ? |
|-----------|----------------|----------|-----------|----------|--------------|-----------|----------|

Row 1 is always [STATUS QUO] with SETUP scores. Remaining rows are candidates.
Beat SQ?: (Y) composite beats status-quo | (N) does not | (--) no status-quo identified.
Score floor: Strategy <= 5 or PM <= 5 --> [DISQ: low Strategy] or [DISQ: low PM] in Composite.

Collision check -- top 3 candidates (excluding [STATUS QUO]):
  Internal (repo namespace) + External (npm/PyPI + brand/domain).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 -- Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [composite value] / 10.0
  (1) Dimensions: [Name at least two scoring dimensions (Strategy, PM, GTM, UX, Design)
      and state the specific reason this candidate scored well on each. Reference
      actual dimension scores from the matrix.]
  (2) vs. Status-quo: [Compare directly to the [STATUS QUO] row scores. Name the specific
      dimensions where this candidate's score leads the status-quo (e.g., "Strategy: 8
      vs. SQ 6") and any dimensions where it concedes. Conclude: strong displacement /
      conditional / narrow advantage.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain the
      specific connection between this candidate and that term.]

RUNNER-UP
  Name: [candidate]
  Score: [composite value] / 10.0
  Fallback rationale: [One sentence. Note Beat SQ? status.]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally by cause:
    [constraint]: N | [low Strategy]: N | [low PM]: N | [below SQ threshold]: N
    [collision]: N | [other]: N

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Benchmark effect: did scoring the status-quo first change what candidates were
    generated or how dimension scores were assigned? Compare to what would likely
    have emerged without the benchmark row.
  - Displacement strength: what fraction of candidates beat the [STATUS QUO] composite?
    Is the incumbency barrier high or low?
  - Vocabulary coverage: did [VOC] candidates outscore [EVK] and [FNC]?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, inertia_framing: benchmark-row,
status_quo_scores: {strategy: N, pm: N, gtm: N, ux: N, design: N, composite: N}.
```

---

## V-04: Combined -- Output Format + Inertia Framing

**Axes**: Anchored 1-10 scale (V-01) + status-quo as scored benchmark row (V-03)
**Hypothesis**: V-01 reduces per-role scoring variance via anchor rubrics. V-03 makes the
displacement argument computable column-by-column. Combined: the anchor rubric defines what
each role score means in absolute terms, and the benchmark row shows how the status-quo scores
on the same rubric -- so the comparison is apples-to-apples. A candidate that earns "Strategy:
8 -- strong; niche-dominant positioning" must beat a status-quo that earned "Strategy: 6 --
adequate; names the domain but does not differentiate." The displacement case emerges directly
from the rubric language, not from DECIDE prose alone. Tests whether combining interpretive
consistency (anchors) with visible comparison (benchmark row) produces the most auditable
scoring output yet.

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
   default this product enters alongside. Score it now using the anchor rubric below.
     Status-quo: [name, or "not identified"]

4. SCORING SYSTEM (declared, locked):
   Role weights: Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10%
   Weight sum: 100%
   Scale: 1-10 per dimension (integer)
   Composite = (Strategy x 0.25) + (PM x 0.25) + (GTM x 0.20)
             + (UX x 0.20) + (Design x 0.10)

   ANCHOR RUBRIC (apply consistently to all candidates including status-quo):

   Strategy (positioning fit):
     1-3  = off-positioning or generic; could belong to any product in the category
     4-6  = adequate; names the domain but does not differentiate
     7-9  = strong; signals what this product uniquely does or whom it serves
     10   = exceptional; own-able term that creates or defines a category

   PM (memorability):
     1-3  = forgettable; no distinctive phoneme or structure
     4-6  = adequate; retainable but not sticky
     7-9  = strong; short, distinct, survives spoken relay
     10   = exceptional; one-word recall, no disambiguation needed

   GTM (searchability):
     1-3  = buried; collides with high-volume common terms
     4-6  = findable; some competition in search landscape
     7-9  = strong; niche-dominant or brand-distinct search profile
     10   = exceptional; zero-conflict indexable identifier

   UX (speakability):
     1-3  = awkward; unusual stress pattern, ambiguous pronunciation
     4-6  = adequate; speakable but forgettable in conversation
     7-9  = strong; flows naturally in "using [name]" and "run /[name]"
     10   = exceptional; instinctive phonetics, no spelling hesitation

   Design (visual weight):
     1-3  = visually heavy or character-dense; poor in small UI contexts
     4-6  = neutral; fine in standard contexts
     7-9  = strong; clean, compact, works as icon label or namespace prefix
     10   = exceptional; 4-6 characters, natural as monogram or glyph

   [STATUS QUO] baseline scores (using anchor rubric):
     Strategy: __  PM: __  GTM: __  UX: __  Design: __  Composite: __
     Brief rationale: [One phrase per dimension citing the anchor tier that applies]

GATE 1 -- Write before generating:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Status-quo: [name/not identified].
   SQ composite: [value or N/A]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC].
At least 3 must be [VOC].

Use the status-quo composite as the displacement floor. The anchor rubric is now declared --
only generate candidates that you expect to reach a higher anchor tier on Strategy than
the status-quo. If a candidate clearly falls to the same or lower anchor tier on Strategy,
mark it [BELOW-SQ: Strategy] here and do not carry it to SCORE.

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint --> mark [DISQ: constraint] here.

GATE 2 -- Write before scoring:
  "Generated: N. Below SQ threshold: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates in this phase.
Row 1 is always [STATUS QUO] with scores pre-populated from SETUP.
Apply the anchor rubric consistently across all rows including [STATUS QUO].

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Beat SQ? |
|-----------|----------------|----------|-----------|----------|--------------|-----------|----------|

Score floor: Strategy <= 5 or PM <= 5 --> [DISQ: low Strategy] or [DISQ: low PM] in Composite.
Beat SQ?: (Y) composite beats status-quo | (N) does not | (--) no status-quo.

Collision check -- top 3 candidates (excluding [STATUS QUO]):
  Internal (repo namespace) + External (npm/PyPI + brand/domain).
  Report: [candidate] / [class] / [hit or clear]

GATE 3 -- Write before deciding:
  "Surviving after score: N. Status-quo benchmarked: yes. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [composite value] / 10.0
  (1) Dimensions: [Name at least two dimensions. For each, state the integer score and
      the anchor-rubric tier that applies. E.g., "Strategy: 8 -- strong; niche-dominant
      positioning. PM: 9 -- strong; short, survives spoken relay."]
  (2) vs. Status-quo: [Name the [STATUS QUO] composite. State the specific dimensions
      where this candidate's anchor-rubric tier is higher than the status-quo's. Conclude:
      strong displacement / conditional / narrow advantage.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain the
      specific connection between this candidate and that term.]

RUNNER-UP
  Name: [candidate]
  Score: [composite value] / 10.0
  Fallback rationale: [One sentence. Note Beat SQ? status.]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally by cause:
    [constraint]: N | [low Strategy]: N | [low PM]: N | [below SQ threshold]: N
    [collision]: N | [other]: N

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Anchor + benchmark interaction: did the rubric descriptions make the benchmark row
    more or less strict than an implicit scale? Did rubric language for Strategy produce
    expected displacement results?
  - Displacement strength: what fraction of candidates beat [STATUS QUO] composite?
  - Vocabulary coverage: did [VOC] candidates outscore [EVK] and [FNC]?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_scale: 1-10-anchored, inertia_framing: benchmark-row,
status_quo_scores: {strategy: N, pm: N, gtm: N, ux: N, design: N, composite: N},
weights: {strategy: 0.25, pm: 0.25, gtm: 0.20, ux: 0.20, design: 0.10}.
```

---

## V-05: Combined -- All Three + C-09 (--validate)

**Axes**: Anchored 1-10 scale (V-01) + phase exit conditions (V-02) + status-quo benchmark
row (V-03) + `--validate <name>` implementation (C-09 attempt)
**Hypothesis**: R4 ceiling candidate. Combines all three single-axis improvements and attempts
the first inline implementation of `--validate` -- the sole criterion blocking the score
ceiling since R1. If `--validate <name>` can be satisfied by an inline instruction pattern
(pin the named candidate as Row 2 after [STATUS QUO], skip GENERATE for it, produce a
Validation Summary after DECIDE with current scores + rank + verdict), this variation targets
100.0. The combination also tests whether three simultaneous structural additions (anchors +
exit conditions + benchmark row) produce any interference -- a clean run at 98.75+ confirms
they compose without conflict.

```
You are running /scout-naming. Four phases with gates. Phase exit conditions
must be satisfied before each gate is written.

IF --validate <name> IS PRESENT IN THE INVOCATION:
  Pin the given name as Row 2 of the scoring matrix (after [STATUS QUO], before
  all other candidates). Do not include it in the 10-15 GENERATE count.
  Generate 10-15 additional fresh candidates normally.
  After DECIDE, write a VALIDATION SUMMARY section (see PHASE 4).

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. If --validate <name> is present, record it:
     Pinned candidate: [name, or "none"]

4. Identify the status-quo: the incumbent name, working title, or market category
   default this product enters alongside. Score it using the anchor rubric below.
     Status-quo: [name, or "not identified"]

5. SCORING SYSTEM (declared, locked):
   Role weights: Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10%
   Weight sum: 100%
   Scale: 1-10 per dimension (integer)
   Composite = (Strategy x 0.25) + (PM x 0.25) + (GTM x 0.20)
             + (UX x 0.20) + (Design x 0.10)

   ANCHOR RUBRIC (apply consistently to all candidates including status-quo and pinned row):

   Strategy (positioning fit):
     1-3  = off-positioning or generic; could belong to any product in the category
     4-6  = adequate; names the domain but does not differentiate
     7-9  = strong; signals what this product uniquely does or whom it serves
     10   = exceptional; own-able term that creates or defines a category

   PM (memorability):
     1-3  = forgettable; no distinctive phoneme or structure
     4-6  = adequate; retainable but not sticky
     7-9  = strong; short, distinct, survives spoken relay
     10   = exceptional; one-word recall, no disambiguation needed

   GTM (searchability):
     1-3  = buried; collides with high-volume common terms
     4-6  = findable; some competition in search landscape
     7-9  = strong; niche-dominant or brand-distinct search profile
     10   = exceptional; zero-conflict indexable identifier

   UX (speakability):
     1-3  = awkward; unusual stress pattern, ambiguous pronunciation
     4-6  = adequate; speakable but forgettable in conversation
     7-9  = strong; flows naturally in "using [name]" and "run /[name]"
     10   = exceptional; instinctive phonetics, no spelling hesitation

   Design (visual weight):
     1-3  = visually heavy or character-dense; poor in small UI contexts
     4-6  = neutral; fine in standard contexts
     7-9  = strong; clean, compact, works as icon label or namespace prefix
     10   = exceptional; 4-6 characters, natural as monogram or glyph

   [STATUS QUO] baseline scores:
     Strategy: __  PM: __  GTM: __  UX: __  Design: __  Composite: __

SETUP EXIT CONDITIONS -- check each before Gate 1:
  [ ] Domain vocabulary list present (5-10 terms, source named)
  [ ] Constraint acknowledged (or "none" recorded)
  [ ] --validate name recorded (or "none")
  [ ] Status-quo identified and scored with anchor rubric (or "not identified")
  [ ] Role weights declared and sum to 100%

GATE 1 -- Write after exit conditions pass:
  "Vocab: N terms from [source]. Constraint: [stated/none]. Pinned: [name/none].
   Status-quo: [name/not identified]. SQ composite: [value/N/A]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. If --validate is present, the pinned name does not
count toward this total -- generate 10-15 fresh candidates beyond it.
Tag each [VOC], [EVK], [CPD], or [FNC]. At least 3 must be [VOC].

Use the status-quo composite as the displacement floor. Mark [BELOW-SQ: Strategy]
and exclude from SCORE any candidate that clearly cannot reach a higher anchor tier
on Strategy than the status-quo.

Constraint enforcement (generation-time):
  Any candidate violating the parsed constraint --> mark [DISQ: constraint] here.

GENERATE EXIT CONDITIONS -- check each before Gate 2:
  [ ] Fresh candidate count is between 10 and 15
  [ ] At least 3 [VOC] candidates present
  [ ] Constraint enforcement applied at generation time (not post-hoc filter)
  [ ] Below-SQ candidates labeled and excluded here

GATE 2 -- Write after exit conditions pass:
  "Generated: N (fresh). Below SQ threshold: N. Pre-disqualified (constraint): N.
   Advancing to SCORE: N (+ 1 pinned row if --validate active)."

--- PHASE 3: SCORE ---

Score surviving candidates only. No new candidates in this phase.
Row 1: [STATUS QUO] pre-populated from SETUP.
Row 2: [PINNED] if --validate is active (score it as any other candidate).
Remaining rows: candidates from GENERATE.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Beat SQ? |
|-----------|----------------|----------|-----------|----------|--------------|-----------|----------|

Apply anchor rubric consistently to all rows.
Score floor: Strategy <= 5 or PM <= 5 --> [DISQ: low Strategy] or [DISQ: low PM] in Composite.
Beat SQ?: (Y) | (N) | (--) if no status-quo.

Collision check -- top 3 candidates (excluding [STATUS QUO], including pinned if present):
  Internal (repo namespace) + External (npm/PyPI + brand/domain).
  Report: [candidate] / [class] / [hit or clear]

SCORE EXIT CONDITIONS -- check each before Gate 3:
  [ ] [STATUS QUO] row present as Row 1 (if status-quo was identified)
  [ ] [PINNED] row present as Row 2 (if --validate is active)
  [ ] All Gate 2 candidates scored or labeled [DISQ]
  [ ] Score floor applied
  [ ] Collision report present covering top 3 (including pinned candidate)
  [ ] Both collision classes reported (internal + external)

GATE 3 -- Write after exit conditions pass:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner -- may be the pinned candidate or a fresh candidate]
  Score: [composite value] / 10.0
  (1) Dimensions: [Name at least two dimensions. State integer score and anchor-rubric
      tier for each. E.g., "Strategy: 8 -- strong; niche-dominant positioning.
      PM: 9 -- strong; short, survives spoken relay."]
  (2) vs. Status-quo: [Name [STATUS QUO] composite. State specific dimensions where
      this candidate's anchor tier is higher. Conclude: strong displacement / conditional /
      narrow advantage.]
  (3) Vocabulary: [Name at least one domain vocabulary term from SETUP. Explain the
      specific connection between this candidate and that term.]

RUNNER-UP
  Name: [candidate]
  Score: [composite value] / 10.0
  Fallback rationale: [One sentence. Note Beat SQ? status.]

DISQUALIFIED SUMMARY
  Full list with labeled reasons. Tally by cause:
    [constraint]: N | [low Strategy]: N | [low PM]: N | [below SQ threshold]: N
    [collision]: N | [other]: N

DECIDE EXIT CONDITIONS -- check each before writing artifact:
  [ ] TOP PICK named with composite score
  [ ] All three labeled sub-parts present: (1) Dimensions / (2) vs. Status-quo / (3) Vocabulary
  [ ] RUNNER-UP named with fallback rationale
  [ ] DISQUALIFIED SUMMARY complete with tally
  [ ] VALIDATION SUMMARY written if --validate was active

---

VALIDATION SUMMARY (write only if --validate <name> was active):

  Pinned candidate: [name]
  Current composite: [value] / 10.0
  Rank in current run: [1 = top pick | N = displaced by N-1 candidates]

  Score profile (anchor tier in parentheses):
    | Dimension | Score | Tier |
    |-----------|-------|------|
    | Strategy  |       |      |
    | PM        |       |      |
    | GTM       |       |      |
    | UX        |       |      |
    | Design    |       |      |

  Strengths: [top 2 dimensions by score -- cite anchor tier language]
  Risks: [bottom 1-2 dimensions or any collision findings]
  vs Status-quo: [does pinned candidate beat [STATUS QUO] composite? By how much?]

  Verdict: [CONFIRMED | CONDITIONAL | AT RISK]
  Rationale: [One sentence.
    CONFIRMED = still top pick, beats SQ composite, no blocking collisions.
    CONDITIONAL = top pick but specific risks noted above.
    AT RISK = displaced by one or more fresh candidates, or blocking collision found.]

---

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - C-09 compliance: did --validate flag handling produce the expected pinned row and
    Validation Summary? Any edge cases (tie scores, collision on pinned name, pinned
    name beats all fresh candidates)?
  - Anchor + benchmark interaction: did the rubric + benchmark row produce more
    discriminating scores than prior rounds?
  - Displacement strength: fraction of candidates that beat [STATUS QUO] composite.
  - Exit condition value: did any exit condition catch a missing artifact?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_scale: 1-10-anchored, inertia_framing: benchmark-row,
lifecycle_enforcement: exit-conditions, validate_flag: [name or null],
status_quo_scores: {strategy: N, pm: N, gtm: N, ux: N, design: N, composite: N},
weights: {strategy: 0.25, pm: 0.25, gtm: 0.20, ux: 0.20, design: 0.10}.
```
