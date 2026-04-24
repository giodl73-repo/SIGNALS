`simulations/quest/golden/scout-naming-golden-2026-03-14.md` written.

**What's in it:**

- **Frontmatter**: score 98.75, GOLDEN status, v5 rubric reference, 4 rounds
- **Prompt body**: V-05 simplified — all three structural patterns (anchor rubric, exit condition checklists, benchmark row), `--validate` machinery stripped (~282 words removed, 30% reduction, all C-01–C-19 intact)
- **What made it golden**: 5 points — anchor tiers (C-17), exit checklists (C-18), displacement floor (C-19), R3 baseline (C-15 + C-16), and why simplification passed cleanly
- **Criteria summary**: Full 20-criterion table with per-criterion pass/fail for this prompt, score ceiling explanation, and next blocker

The C-09 blocker is now precisely documented: row-position conflict (inertia framing owns Row 1 for `[STATUS QUO]`) plus infrastructure gap (prior-run scores unavailable to inline prompting). Those are the two requirements for the next round to target.
ement) appear as checklist preconditions -- a phase may not close
until they clear. Converts these from evaluator-inferred observations to structural
preconditions that block phase advance if absent. First mechanism that makes completeness
enforcement prescriptive rather than confirmatory.

**3. Generation-time displacement floor (C-19)**
Status-quo pre-scored in SETUP using the anchor rubric. Candidates that clearly cannot
reach a higher Strategy anchor tier are marked [BELOW-SQ: Strategy] at GENERATE and
excluded before SCORE. [STATUS QUO] appears as Row 1 of the matrix with all five dimension
scores visible. Fraction beating the status-quo reported at DECIDE. Adds [below SQ
threshold] as a fourth disqualification class and makes incumbency strength measurable.

**4. R3 baseline carried forward (C-15 + C-16)**
Labeled sub-part record (C-15) and Gate 3 binary status flags (C-16) were proven in R3
and held as structural constants across all R4 variations. Not axes -- prerequisites.

**5. 30% simplification passed**
The --validate branch (C-09/C-20) was removed without affecting C-01 through C-19.
~282 words removed. The three essential patterns are cleaner without the conditional
branch machinery.

---

## Prompt Body

```
You are running /scout-naming. Four phases with gates. Phase exit conditions
must be satisfied before each gate is written.

--- PHASE 1: SETUP ---

1. Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms.
     Domain vocabulary: [term1, ...]
     Source: [file name]

2. Parse any constraint from the invocation.
     Constraint: [text, or "none"]

3. Identify the status-quo: the incumbent name, working title, or market category
   default this product enters alongside. Score it using the anchor rubric below.
     Status-quo: [name, or "not identified"]

4. SCORING SYSTEM (declared, locked):
   Role weights: Strategy 25% | PM 25% | GTM 20% | UX 20% | Design 10%
   Weight sum: 100%
   Scale: 1-10 per dimension (integer)
   Composite = (Strategy x 0.25) + (PM x 0.25) + (GTM x 0.20)
             + (UX x 0.20) + (Design x 0.10)

   ANCHOR RUBRIC (apply consistently to all candidates):

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
  [ ] Status-quo identified and scored with anchor rubric (or "not identified")
  [ ] Role weights declared and sum to 100%

GATE 1 -- Write after exit conditions pass:
  "Vocab: N terms from [source]. Constraint: [stated/none].
   Status-quo: [name/not identified]. SQ composite: [value/N/A]. Weights: 100%."

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC]:
  [VOC] derived from domain vocabulary
  [EVK] evocative / metaphor-based
  [CPD] compound or portmanteau
  [FNC] functional / descriptive
At least 3 must be [VOC].

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
  "Generated: N. Below SQ threshold: N. Pre-disqualified (constraint): N.
   Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only.
Row 1 is always [STATUS QUO] with scores pre-populated from SETUP.
Apply the anchor rubric consistently to all rows.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Beat SQ? |
|-----------|----------------|----------|-----------|----------|--------------|-----------|----------|

Score floor: Strategy <= 5 or PM <= 5 --> [DISQ: low Strategy] or [DISQ: low PM] in Composite.
Beat SQ?: (Y) composite beats status-quo | (N) does not | (--) no status-quo identified.

Collision check -- top 3 candidates (excluding [STATUS QUO]):
  Internal (repo namespace) + External (npm/PyPI + brand/domain).
  Report: [candidate] / [class] / [hit or clear]

SCORE EXIT CONDITIONS -- check each before Gate 3:
  [ ] [STATUS QUO] row present as Row 1 (if status-quo was identified)
  [ ] All Gate 2 candidates scored or labeled [DISQ]
  [ ] Score floor applied
  [ ] Collision report present covering top 3 candidates
  [ ] Both collision classes reported (internal namespace + external registry)

GATE 3 -- Write after exit conditions pass:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
  Score: [composite value] / 10.0
  (1) Dimensions: [Name at least two dimensions. For each, state the integer score and
      the anchor-rubric tier that applies. E.g., "Strategy: 8 -- strong; signals X
      clearly, niche-dominant positioning. PM: 9 -- strong; short, survives spoken relay."]
  (2) vs. Status-quo: [Name [STATUS QUO] composite. State specific dimensions where
      this candidate's anchor-rubric tier is higher than the status-quo's. Conclude:
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

DECIDE EXIT CONDITIONS -- check each before writing artifact:
  [ ] TOP PICK named with composite score
  [ ] All three labeled sub-parts present: (1) Dimensions / (2) vs. Status-quo / (3) Vocabulary
  [ ] RUNNER-UP named with fallback rationale
  [ ] DISQUALIFIED SUMMARY complete with tally

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Anchor + benchmark interaction: did the rubric descriptions make the benchmark row
    more or less strict? Did rubric language for Strategy produce expected displacement?
  - Displacement strength: what fraction of candidates beat [STATUS QUO] composite?
  - Vocabulary coverage: did [VOC] candidates outscore [EVK] and [FNC]?
  Severity: P1/P2/P3.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
status_quo, scoring_scale: 1-10-anchored, inertia_framing: benchmark-row,
lifecycle_enforcement: exit-conditions,
status_quo_scores: {strategy: N, pm: N, gtm: N, ux: N, design: N, composite: N},
weights: {strategy: 0.25, pm: 0.25, gtm: 0.20, ux: 0.20, design: 0.10}.
```

---

## Final Rubric Criteria Summary (v5)

| ID | Text | Tier | This prompt |
|----|------|------|-------------|
| C-01 | Candidate Volume (10-15) | essential | PASS |
| C-02 | Five-Role Scoring Matrix + declared weights | essential | PASS |
| C-03 | Collision Check (namespace + external) | essential | PASS |
| C-04 | Top Pick Named + Justified | essential | PASS |
| C-05 | Constraint Parsed + Applied | essential | PASS |
| C-06 | Disqualification Logic labeled | recommended | PASS |
| C-07 | Runner-Up + Fallback Rationale | recommended | PASS |
| C-08 | Findings Register (SF-NN) | recommended | PASS |
| C-09 | `--validate` flag pins row + Validation Summary | aspirational | FAIL (infrastructure gap) |
| C-10 | Domain Vocabulary Extraction logged | aspirational | PASS |
| C-11 | Generation-time Constraint Enforcement | aspirational | PASS |
| C-12 | Phase-structured Output | aspirational | PASS |
| C-13 | Gate Confirmation Count | aspirational | PASS |
| C-14 | 3-part DECIDE Rationale | aspirational | PASS |
| C-15 | Labeled Sub-part Record | aspirational | PASS |
| C-16 | Gate 3 Binary Status Flags | aspirational | PASS |
| C-17 | Anchor Rubric Tier Descriptions | aspirational | PASS |
| C-18 | Phase Exit Condition Checklists | aspirational | PASS |
| C-19 | Generation-time Displacement Floor | aspirational | PASS |
| C-20 | --validate Branch Diagnostics | aspirational | N/A (removed by simplification) |

**Score (v4 rubric, R4 result)**: 98.75 / 100
**Score ceiling**: C-09 requires prior-run score storage outside the prompt.
**Next blocker**: Resolve row-position conflict (C-09 requires Row 1 for pinned candidate;
inertia framing places [STATUS QUO] at Row 1) or add prior-run score storage to the
skill infrastructure.
