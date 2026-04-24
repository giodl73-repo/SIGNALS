Written to `simulations/quest/variations/scout-naming-variations-R1-2026-03-14.md`.

---

## Variations: scout-naming R1

**5 variations across 4 axes:**

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Baseline | Spec as written satisfies essentials but underperforms on C-04 rationale depth |
| V-02 | Role sequence (Strategy-first) | Positioning context before memorability judgment produces deeper C-04 rationale |
| V-03 | Output format (traffic-light) | HIGH/MEDIUM/LOW tiers make disqualification logic (C-06) more natural to surface |
| V-04 | Phrasing register (conversational) | Question-framed sections force constraint reasoning rather than pattern-matching |
| V-05 | Combined (lifecycle phases + vocab extraction + Strategy-first) | Explicit phase headers + visible domain vocabulary produces strongest C-10 + C-04 together |

**Key design decisions:**
- V-02 and V-05 both lead with domain vocabulary extraction — the strongest lever for C-10 and C-04 quality
- V-03 uses disqualification-by-rule (LOW on PM or Strategy = auto-DISQ) rather than post-hoc labeling — tests whether structural rules outperform judgment-based filtering for C-06
- V-05 uses explicit phase headers (`EXTRACT > GENERATE > SCORE > CHECK > DECIDE`) which mirrors the lifecycle emphasis axis and forces commit-before-proceed discipline
- V-04 is the only conversational register — the odd-one-out test for whether phrasing affects behavioral compliance on C-05

**Recommended scoring order:** Run V-01 as baseline, then V-05 (most likely to hit C-08/C-10 aspirational), then compare V-02 vs V-03 for the C-04 rationale quality difference.
%, GTM 20%, UX 20%, Design 10%.
Compute a weighted composite score for each candidate.

COLLISION CHECK:
1. Internal: Check the candidate against known plugin namespaces in this repo.
2. External: Check for npm/PyPI package name overlap and notable brand/domain conflict.
State the result (hit or clear) for each class for the top candidate.

FINDINGS:
- Top Pick: Name the highest composite score candidate. State the score.
  Give a rationale grounded in at least one scoring dimension.
- Runner-Up: Name the second-best available candidate. State the score.
  Give one sentence explaining why it is a viable fallback.
- Disqualified: List any candidates removed for constraint violation, namespace
  collision, or brand conflict. Label each with the specific reason.

FINDINGS REGISTER: Conclude with a findings table in SF-NN format. Each entry:
ID, description, severity (P1/P2/P3). Include any design gaps, weight concerns,
or constraint relaxations surfaced during scoring.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Include frontmatter: skill, topic, date, skill_version, input, constraint.
```

---

## V-02: Strategy-first role sequence

Axis: Role sequence -- Strategy scores first, PM last; positioning context precedes memorability judgment
Hypothesis: Running Strategy before PM primes the model to evaluate candidates against positioning fit
before memorability, producing deeper C-04 rationale and reducing generic "it sounds good" top picks.

```
You are running /scout-naming. Name generation follows a positioning-first sequence:
strategy context is established before memorability is judged.

SETUP: Auto-detect domain from repo context (README, CLAUDE.md, plugin-plan.md).
Parse any constraint in the invocation. State it explicitly. If none, note that.

DOMAIN VOCABULARY: Before generating candidates, extract 5-8 terms from CLAUDE.md or
plugin-plan.md that describe what this product does. These terms seed candidate generation.
List them as "Domain terms: [...]".

GENERATE: Produce 10-15 candidate names drawn from or contrasting with the domain terms.

SCORE: For each candidate, run roles in this order:
1. Strategy (25%): Positioning fit -- does the name own a clear category? Does it
   signal differentiation without requiring explanation?
2. GTM (20%): Searchability -- clean web presence, no dominant brand collision.
3. UX (20%): Speakability -- natural to say aloud, no awkward phoneme clusters.
4. Design (10%): Visual weight -- works in a logotype, UI label, or command prefix.
5. PM (25%): Memorability -- recalled correctly after one exposure.

Weights: Strategy 25%, PM 25%, GTM 20%, UX 20%, Design 10%.
Compute weighted composite. Show the per-role scores and composite in a table.

COLLISION CHECK:
1. Internal: Namespace collision against known plugin names in this repo.
2. External: npm/PyPI name availability + notable brand/domain conflict.
State result (hit or clear) for each class. Cover at least the top candidate.

FINDINGS:
- Top Pick: Name the winner. State composite score. Rationale must reference Strategy
  and at least one other dimension (not just "highest score").
- Runner-Up: Name it. Score it. One sentence on why it is a viable fallback if
  the top pick is taken.
- Disqualified: Any candidate removed must be listed with a labeled reason
  (constraint violation / namespace collision / brand conflict / scoring floor).

FINDINGS REGISTER: SF-NN table. At least one entry on role weighting, vocabulary
influence, or constraint gap.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms.
```

---

## V-03: Traffic-light output format

Axis: Output format -- replace 1-10 numeric scores with HIGH/MEDIUM/LOW per dimension; composite derived from tier count
Hypothesis: Traffic-light format lowers the false precision of numeric scoring and forces the model to
commit to clear tier judgments per dimension, making disqualification logic (C-06) more natural to surface.

```
You are running /scout-naming. Use traffic-light scoring, not numeric scores.

SETUP: Auto-detect domain from repo context. Parse any constraint in the invocation.
State it before generation. If none, note that.

GENERATE: Produce 10-15 candidate names across functional, evocative, and compound types.

SCORE: For each candidate, assign a tier per dimension:

| Candidate | PM (memorability) | Design (visual weight) | UX (speakability) | GTM (searchability) | Strategy (positioning fit) | Composite |
|-----------|-------------------|------------------------|-------------------|---------------------|----------------------------|-----------|

Tiers: HIGH / MEDIUM / LOW.
Composite: 3+ HIGH = strong; 2 HIGH + rest MEDIUM = viable; 1 HIGH or LOW in PM/Strategy = weak.
Apply weights directionally: PM and Strategy failures are disqualifying; Design LOW alone is not.

DISQUALIFICATION RULE: Any candidate scoring LOW on PM or Strategy is immediately disqualified.
Label it "DISQ: low [dimension]" in the composite column. Do not silently omit it.

COLLISION CHECK:
1. Internal: Namespace collision in this repo.
2. External: npm/PyPI availability + brand/domain conflict check.
Report result (hit or clear) for both classes on the top candidate.

CONSTRAINT: If a constraint was parsed, mark each candidate PASS or FAIL against it
in a dedicated constraint column.

FINDINGS:
- Top Pick: Named from the "strong" composite tier. State which dimensions are HIGH.
  Rationale must reference at least one dimension beyond composite tier.
- Runner-Up: First "viable" candidate. One sentence fallback rationale.
- Disqualified: Already flagged in matrix. Summarize count and predominant cause.

FINDINGS REGISTER: SF-NN table with at least one entry on scoring gaps or
traffic-light boundary calibration.

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, scoring_format: traffic-light.
```

---

## V-04: Conversational phrasing register

Axis: Phrasing register -- descriptive/conversational tone, not imperative commands; sections framed as questions
Hypothesis: A conversational register produces richer constraint parsing (C-05) because framing as
questions forces the model to reason through the constraint rather than pattern-match to a rule.

```
You are running /scout-naming. Your job is to find the best name for what the user is building.
Walk through this as a naming workshop, not a checklist.

First, figure out what you're naming. Read CLAUDE.md and plugin-plan.md in the repo.
Pull out the vocabulary -- the 5-8 words that best describe what this thing does and how
it positions itself. Write them down before you start generating names. This vocabulary
is your seed list.

Did the user pass a constraint? (Something like "one word only", "no verbs", "must
rhyme with X".) If yes, say what it is before you generate anything. If no constraint
was given, say so. Every candidate decision should trace back to whether it meets
that constraint.

Now generate 10-15 candidate names. Mix functional names (what it does), evocative
names (how it feels), and compound or short-form options. Let the seed vocabulary
influence at least a few candidates directly.

Score each candidate from the perspective of five people who care about different things:

- The PM cares whether people remember the name correctly the first time they hear it.
  Weight: 25%.
- The Strategist cares whether the name stakes out clear positioning -- whether it
  signals the right category without needing a tagline to explain it. Weight: 25%.
- The GTM lead cares whether the name is findable -- no dominant brand collision,
  reasonable search signal. Weight: 20%.
- The UX designer cares whether the name is easy to say out loud, in a meeting,
  to someone who has never seen it written. Weight: 20%.
- The visual designer cares whether the name has good visual weight -- it works as
  a logotype or a short UI label. Weight: 10%.

Build a table. One row per candidate. Five role columns. One weighted composite column.
Weights must sum to 100%.

Before declaring a winner, check collisions:
1. Does the name collide with another namespace already in this repo?
2. Does it collide with an existing npm package, PyPI module, or notable brand?
Note what you found (hit or clear) for at least the top candidate.

Who wins? Name one candidate as the top pick, state its composite score, and explain
why -- in terms of the scoring dimensions, not just "it scored highest." Then name the
runner-up and explain why it is a credible fallback.

For any candidate you dropped, say why in one phrase. Silently omitting names is not
allowed -- label the reason (constraint violation, collision, scoring floor, etc.).

Close with a short findings register: use SF-NN IDs, note any design gaps, weighting
questions, or constraint edge cases that came up during scoring.

Write the artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms.
```

---

## V-05: Combined (lifecycle phases explicit + domain vocabulary extraction + Strategy-first)

Axis: Combined -- explicit lifecycle phase headers + domain vocabulary surfaced as setup step + Strategy-first scoring order
Hypothesis: Making lifecycle phases explicit (EXTRACT > GENERATE > SCORE > CHECK > DECIDE) combined with
visible vocabulary extraction produces stronger C-10 and tighter C-04 rationale by ensuring the model
commits to its domain understanding before generating any candidates.

```
You are running /scout-naming. The naming lifecycle runs in five phases: EXTRACT,
GENERATE, SCORE, CHECK, DECIDE. Each phase completes before the next begins.

--- PHASE 1: EXTRACT ---

Read CLAUDE.md and plugin-plan.md. Extract the domain vocabulary: the 5-10 terms that
most precisely describe what this product does, how it positions itself, and what
problem it solves. Write them as:

  Domain vocabulary: [term1, term2, ...]
  Source: [file name(s)]

Parse any constraint from the invocation. State it:

  Constraint: [constraint text, or "none"]

This vocabulary seeds candidate generation. At least 3 candidates must be directly
derived from or contrasting with vocabulary terms.

--- PHASE 2: GENERATE ---

Produce 10-15 candidate names. Tag each with its generation strategy:
  [VOC] derived from domain vocabulary
  [EVK] evocative / metaphor-based
  [CPD] compound or portmanteau
  [FNC] purely functional / descriptive

If a constraint was parsed, apply it during generation. Mark any candidate that
violates the constraint as [DISQ: constraint] immediately -- do not carry it into scoring.

--- PHASE 3: SCORE ---

Score each non-disqualified candidate across 5 roles in this order:

1. Strategy (25%): Does the name own a category? Does it signal the product's
   differentiation without requiring explanation?
2. PM (25%): Will people remember it correctly after hearing it once?
3. GTM (20%): Is the search presence clean? No dominant brand collision?
4. UX (20%): Is it easy to say aloud in a meeting or a voice command?
5. Design (10%): Does it have good visual weight as a logotype or label?

Show scores on a 1-10 scale. Compute weighted composite.
Flag any candidate where Strategy or PM falls below 6 as [DISQ: low score].

--- PHASE 4: CHECK ---

Collision check for the top 3 candidates:
1. Internal: Namespace collision against plugin names in this repo.
2. External: npm/PyPI availability + notable brand or domain conflict.

Report each check as: [candidate] / [class] / [result: hit or clear].

--- PHASE 5: DECIDE ---

Top Pick: Name the winner. State composite score. Rationale must reference at least
two scoring dimensions (not just composite). Address how it relates to the domain
vocabulary extracted in Phase 1.

Runner-Up: Name it. State score. One sentence: why is it a credible fallback if
the top pick is unavailable?

Disqualified Summary: List all candidates that were disqualified, with labeled reasons.
Tally by cause: [constraint], [low score], [collision], [other].

FINDINGS REGISTER: SF-NN table. At minimum, one entry on vocabulary coverage,
one on role weighting calibration, one on disqualification patterns observed.
Severity: P1 (blocks a correct top pick), P2 (affects depth), P3 (nice to have).

Write artifact to simulations/scout/naming/{topic}-naming-{date}.md.
Frontmatter: skill, topic, date, skill_version, input, constraint, domain_terms,
scoring_order: [strategy, pm, gtm, ux, design].
```
