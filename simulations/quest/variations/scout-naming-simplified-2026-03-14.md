Now I have everything I need. Let me perform the analysis and produce the simplified version.

**V-05 word count** (prompt body only, lines 608–813): I'll do a precise structural pass.

---

## Analysis: What's Doing No Work

Every sentence is mapped against all 20 criteria. Phrases that serve **only** C-09 or C-20 (the `--validate` machinery) can be removed without affecting essential criteria C-01 through C-05, and also without affecting recommended C-06/C-07/C-08 or aspirational C-10 through C-19.

### Removable blocks (C-09/C-20 only, zero other criterion coverage):

| # | Text removed | Approx words |
|---|-------------|-------------|
| 1 | The entire `IF --validate <name> IS PRESENT` preamble block | 53 |
| 2 | SETUP step 3: "If --validate is present, record it: Pinned candidate..." | 13 |
| 3 | "including status-quo and pinned row" in anchor rubric header | 6 |
| 4 | GENERATE: "--validate is present, the pinned name does not count..." qualifier | 20 |
| 5 | Gate 2 tail: "(+ 1 pinned row if --validate active)" | 8 |
| 6 | SCORE: "Row 2: [PINNED] if --validate is active (score it as any other candidate)." | 14 |
| 7 | SCORE EXIT CONDITIONS item: "[ ] [PINNED] row present as Row 2..." | 12 |
| 8 | Collision check: "including pinned if present" → remove qualifier | 5 |
| 9 | TOP PICK name: "may be the pinned candidate or a fresh candidate" qualifier | 9 |
| 10 | DECIDE EXIT CONDITIONS item: "[ ] VALIDATION SUMMARY written if --validate was active" | 9 |
| 11 | Entire VALIDATION SUMMARY section | 95 |
| 12 | FINDINGS REGISTER C-09 entry: "C-09 compliance: did --validate flag handling produce..." | 32 |

### Also removable (redundancy, zero criterion coverage):

| # | Text removed | Approx words |
|---|-------------|-------------|
| 13 | "No new candidates in this phase." (SCORE opening — "Score surviving candidates only" already says it) | 6 |

**Total removed: ~282 words**

### What stays (criterion mapping):

- Preamble + phase headers → C-12
- Anchor rubric (all 5 roles) → C-17
- Status-quo identification + baseline scoring + displacement floor + `Beat SQ?` column → C-19
- Exit condition checklists (SETUP, GENERATE, SCORE, DECIDE) → C-18
- 10-15 candidates + [VOC] tags → C-01
- Scoring matrix + weights + formula → C-02
- Collision check (internal + external, top 3) → C-03
- TOP PICK with score + 3-part rationale → C-04, C-14, C-15
- Constraint parse + generation-time enforcement → C-05, C-11
- Domain vocabulary extraction → C-10
- Gate confirmation counts → C-13
- Gate 3 binary flags → C-16
- RUNNER-UP + fallback → C-07
- DISQUALIFIED SUMMARY with tally → C-06
- FINDINGS REGISTER → C-08

---

## Simplified Prompt

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

Produce 10-15 candidate names. Tag each [VOC], [EVK], [CPD], or [FNC]. At least 3 must be [VOC].

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
  "Generated: N. Below SQ threshold: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."

--- PHASE 3: SCORE ---

Score surviving candidates only.
Row 1: [STATUS QUO] pre-populated from SETUP.

| Candidate | Strategy (25%) | PM (25%) | GTM (20%) | UX (20%) | Design (10%) | Composite | Beat SQ? |
|-----------|----------------|----------|-----------|----------|--------------|-----------|----------|

Apply anchor rubric consistently to all rows.
Score floor: Strategy <= 5 or PM <= 5 --> [DISQ: low Strategy] or [DISQ: low PM] in Composite.
Beat SQ?: (Y) | (N) | (--) if no status-quo.

Collision check -- top 3 candidates (excluding [STATUS QUO]):
  Internal (repo namespace) + External (npm/PyPI + brand/domain).
  Report: [candidate] / [class] / [hit or clear]

SCORE EXIT CONDITIONS -- check each before Gate 3:
  [ ] [STATUS QUO] row present as Row 1 (if status-quo was identified)
  [ ] All Gate 2 candidates scored or labeled [DISQ]
  [ ] Score floor applied
  [ ] Collision report present covering top 3
  [ ] Both collision classes reported (internal + external)

GATE 3 -- Write after exit conditions pass:
  "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."

--- PHASE 4: DECIDE ---

TOP PICK
  Name: [winner]
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

FINDINGS REGISTER: SF-NN table. At minimum one entry on:
  - Anchor + benchmark interaction: did the rubric + benchmark row produce
    discriminating scores? Did any anchor tier feel too tight or too loose?
  - Displacement strength: fraction of candidates that beat [STATUS QUO] composite.
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

## Simplification Report

**What was removed and why:**

| Block | Words | Reason |
|-------|-------|--------|
| `IF --validate <name> IS PRESENT` preamble (lines 611-615) | ~53 | C-09/C-20 only — no essential criterion requires flag handling |
| SETUP step 3: pinned candidate recording | ~13 | C-09 only |
| Anchor rubric header qualifier: "including status-quo and pinned row" | 6 | C-09 only (all candidates already in scope) |
| GENERATE opening: "--validate, pinned name does not count toward total" | ~20 | C-09 only |
| Gate 2 tail: "(+ 1 pinned row if --validate active)" | 8 | C-09 only |
| SCORE: "Row 2: [PINNED]..." instruction | ~14 | C-09 only |
| SCORE EXIT CONDITIONS: "[PINNED] row present as Row 2" item | ~12 | C-09 only |
| Collision check: "including pinned if present" qualifier | 5 | C-09 only |
| TOP PICK: "may be the pinned candidate or a fresh candidate" | 9 | C-09 only |
| DECIDE EXIT CONDITIONS: "VALIDATION SUMMARY written" item | 9 | C-09 only |
| Entire VALIDATION SUMMARY section | ~95 | C-09 only |
| FINDINGS REGISTER C-09 entry ("did --validate flag handling produce...") | ~32 | C-09 only |
| "No new candidates in this phase." in SCORE opening | 6 | Pure redundancy — "Score surviving candidates only" already covers it |

**Total removed: ~282 words**

**Criteria verification (essential):**

| Criterion | Still passes? | Evidence in simplified prompt |
|-----------|--------------|-------------------------------|
| C-01 Candidate Volume (10-15) | YES | "Produce 10-15 candidate names" + GENERATE EXIT CONDITIONS item 1 |
| C-02 Five-Role Matrix + weights | YES | Full scoring system declared in SETUP with formula; matrix header in SCORE |
| C-03 Collision Check (both classes, top 3) | YES | Collision check block in SCORE + exit condition item 4-5 |
| C-04 Top Pick Named + Justified | YES | TOP PICK with score + (1) Dimensions rationale |
| C-05 Constraint Parsed + Applied | YES | SETUP step 2 + generation-time constraint enforcement block |

**All essential criteria: YES — all 5 pass.**

**Aspirational criteria lost by simplification:** C-09 (--validate row pin + Validation Summary) and C-20 (--validate branch diagnostics). These two were the sole criteria requiring the --validate infrastructure. Neither has a path to pass without external prior-run score storage regardless of prompt length, so they were already unachievable in a pure single-run context.

**Aspirational criteria retained:** C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19 — all 10 remain intact.

```json
{"simplified_word_count": 648, "original_word_count": 930, "all_essential_still_pass": true}
```
