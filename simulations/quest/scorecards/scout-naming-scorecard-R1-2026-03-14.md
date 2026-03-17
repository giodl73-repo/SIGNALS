## Round 1 Scorecard — scout-naming

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-02 Strategy-first | **95** | YES |
| 1 | V-04 Conversational | **95** | YES |
| 1 | V-05 Combined | **95** | YES |
| 4 | V-01 Baseline | **90** | YES |
| 5 | V-03 Traffic-light | **73** | NO |

```json
{"top_score": 95, "all_essential_pass": false, "new_patterns": ["Generation-time disqualification (V-05 GENERATE phase) prevents contaminated candidates from entering scoring, eliminating a class of false-positive score inflation not addressed by post-hoc filtering instructions", "Traffic-light tier scoring and declared percentage weights are structurally incompatible — the format axis directly sacrifices the C-02 pass condition; a tier-based format requires either a relaxed C-02 or an explicit tier-to-weight mapping"]}
```

**Key findings:**

- **C-09 is the ceiling.** The `--validate` flag doesn't exist in the current skill — no variation can clear 95. It's a design gap, not a phrasing problem.
- **V-03 fails C-02 by design.** Traffic-light (HIGH/MEDIUM/LOW) never declares percentage weights. The format axis and the weight-declaration requirement are structurally incompatible. V-03 still has the round's strongest C-05 mechanism (dedicated constraint column) and strongest C-06 mechanism (structural DISQ rule), but pays with an essential failure.
- **`all_essential_pass: false`** because V-03 is in the set.
- **V-05 leads within the 95 cluster**: phase headers prevent phase-bleeding, generation-time constraint marking is the most rigorous C-05/C-06 mechanism, collision covers top 3, C-08 requires minimum 3 findings entries.
- **Vocab extraction (C-10)** is the single highest-value addition to the baseline — all three variations that add it jump from 90 → 95.
 | PASS | "Top Pick: Name the highest composite score candidate. State the score. Give a rationale grounded in at least one scoring dimension." Pass condition met; rationale depth is thin (one dimension minimum, no requirement to reference Strategy specifically) |
| C-05 | Constraint Parsed + Applied | PASS | Constraint in frontmatter + disqualified section explicitly labels constraint violation as a removal reason |
| C-06 | Disqualification Logic labeled | PASS | "Disqualified: List any candidates removed for constraint violation, namespace collision, or brand conflict. Label each with the specific reason." |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: Name the second-best available candidate. State the score. Give one sentence explaining why it is a viable fallback." All three elements explicit. |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: Conclude with a findings table in SF-NN format. Each entry: ID, description, severity (P1/P2/P3)." |
| C-09 | `--validate` flag behavior | FAIL | No --validate flag mechanism. Design gap, not phrasing gap. |
| C-10 | Domain Vocabulary Extraction logged | FAIL | No explicit vocab extraction step. Candidates generated without visible seed vocabulary. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 0/2

```
composite = (5/5 * 60) + (3/3 * 30) + (0/2 * 10)
          = 60 + 30 + 0
          = 90
```

**Score: 90 / 100 — GOLDEN** (all essential pass, composite >= 80)

---

### V-02: Strategy-first role sequence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names drawn from or contrasting with the domain terms." |
| C-02 | Five-Role Scoring Matrix + weights | PASS | All 5 roles with percentages summing to 100%; "Compute weighted composite. Show the per-role scores and composite in a table." |
| C-03 | Collision Check (namespace + external) | PASS | Internal + external classes named; "State result (hit or clear) for each class. Cover at least the top candidate." |
| C-04 | Top Pick Named + Justified | PASS | "Rationale must reference Strategy and at least one other dimension (not just 'highest score')." Strongest C-04 requirement in the round — two named dimensions guaranteed. |
| C-05 | Constraint Parsed + Applied | PASS | "Parse any constraint in the invocation. State it explicitly. If none, note that." Explicit state-before-generate requirement. |
| C-06 | Disqualification Logic labeled | PASS | "Any candidate removed must be listed with a labeled reason (constraint violation / namespace collision / brand conflict / scoring floor)." |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: Name it. Score it. One sentence on why it is a viable fallback if the top pick is taken." All three elements explicit. |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At least one entry on role weighting, vocabulary influence, or constraint gap." |
| C-09 | `--validate` flag behavior | FAIL | No --validate flag mechanism. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "DOMAIN VOCABULARY: Before generating candidates, extract 5-8 terms from CLAUDE.md or plugin-plan.md... List them as 'Domain terms: [...]'." Named source files + explicit term count. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/2

```
composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10)
          = 60 + 30 + 5
          = 95
```

**Score: 95 / 100 — GOLDEN**

---

### V-03: Traffic-light output format

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names across functional, evocative, and compound types." |
| C-02 | Five-Role Scoring Matrix + weights | **FAIL** | All 5 role columns present but percentage weights never declared. Format uses HIGH/MEDIUM/LOW tiers; composite derived from tier count, not from weighted arithmetic. C-02 pass condition requires "Declared weights sum to 100%." Structural incompatibility: the format axis and the weight-declaration requirement cannot coexist. |
| C-03 | Collision Check (namespace + external) | PASS | "Internal: Namespace collision in this repo. External: npm/PyPI availability + brand/domain conflict check. Report result (hit or clear) for both classes on the top candidate." |
| C-04 | Top Pick Named + Justified | PASS | "Top Pick: Named from the 'strong' composite tier. State which dimensions are HIGH. Rationale must reference at least one dimension beyond composite tier." |
| C-05 | Constraint Parsed + Applied | PASS | "Parse any constraint in the invocation. State it before generation." + dedicated constraint column (PASS/FAIL per candidate) — strongest C-05 mechanism in the round. |
| C-06 | Disqualification Logic labeled | PASS | "DISQUALIFICATION RULE: Any candidate scoring LOW on PM or Strategy is immediately disqualified. Label it 'DISQ: low [dimension]' in the composite column." Structural rule is the clearest C-06 mechanism in the round — no judgment required. |
| C-07 | Runner-Up + Fallback Rationale | PASS* | Runner-up named from "viable" tier + one sentence rationale present. *No numeric score; "viable" tier is the score. Strict reading borderline; tier is an explicit composite label. |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table with at least one entry on scoring gaps or traffic-light boundary calibration." |
| C-09 | `--validate` flag behavior | FAIL | No --validate flag mechanism. |
| C-10 | Domain Vocabulary Extraction logged | FAIL | No domain vocabulary extraction step. |

**Essential**: 4/5 (C-02 fails) | **Recommended**: 3/3 | **Aspirational**: 0/2

```
composite = (4/5 * 60) + (3/3 * 30) + (0/2 * 10)
          = 48 + 30 + 0
          = 78
```

**Score: 78 / 100 — NOT GOLDEN** (C-02 fails essential; composite < 80)

Note: V-03's C-05 and C-06 mechanisms are structurally the strongest in the round. The traffic-light format hypothesis works for C-06 but is incompatible with C-02. This is a rubric-format tension that cannot be resolved by phrasing.

---

### V-04: Conversational phrasing register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "generate 10-15 candidate names" |
| C-02 | Five-Role Scoring Matrix + weights | PASS | "Build a table. One row per candidate. Five role columns. One weighted composite column. Weights must sum to 100%." Explicit sum-to-100 requirement. |
| C-03 | Collision Check (namespace + external) | PASS | "check collisions: 1. Does the name collide with another namespace already in this repo? 2. Does it collide with an existing npm package, PyPI module, or notable brand? Note what you found (hit or clear) for at least the top candidate." |
| C-04 | Top Pick Named + Justified | PASS | "explain why -- in terms of the scoring dimensions, not just 'it scored highest.'" Pass condition met. |
| C-05 | Constraint Parsed + Applied | PASS | "Did the user pass a constraint? ... say what it is before you generate anything... Every candidate decision should trace back to whether it meets that constraint." Strongest C-05 instruction: decision-tracing requirement is explicit. |
| C-06 | Disqualification Logic labeled | PASS | "For any candidate you dropped, say why in one phrase. Silently omitting names is not allowed -- label the reason (constraint violation, collision, scoring floor, etc.)." |
| C-07 | Runner-Up + Fallback Rationale | PASS | "name the runner-up and explain why it is a credible fallback." Score present in scoring table; runner-up named + rationale sentence required. Score not restated in the DECIDE section but is visible in output table. |
| C-08 | Findings Register (SF-NN) | PASS | "Close with a short findings register: use SF-NN IDs, note any design gaps, weighting questions, or constraint edge cases that came up during scoring." |
| C-09 | `--validate` flag behavior | FAIL | No --validate flag mechanism. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Read CLAUDE.md and plugin-plan.md in the repo. Pull out the vocabulary -- the 5-8 words that best describe what this thing does... Write them down before you start generating names." Named source files meet the pass condition. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/2

```
composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10)
          = 60 + 30 + 5
          = 95
```

**Score: 95 / 100 — GOLDEN**

---

### V-05: Combined (lifecycle phases + domain vocab + Strategy-first)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." Tagged by generation strategy [VOC/EVK/CPD/FNC]. |
| C-02 | Five-Role Scoring Matrix + weights | PASS | All 5 roles listed with percentages summing to 100%; "Show scores on a 1-10 scale. Compute weighted composite." Strongest C-02 mechanism: scoring order is explicit (Strategy, PM, GTM, UX, Design). |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check for the top 3 candidates: 1. Internal... 2. External..." Coverage extends to top 3 — strongest C-03 depth in the round. |
| C-04 | Top Pick Named + Justified | PASS | "Rationale must reference at least two scoring dimensions (not just composite). Address how it relates to the domain vocabulary extracted in Phase 1." Strongest C-04 requirement: two dimensions + vocabulary connection mandatory. |
| C-05 | Constraint Parsed + Applied | PASS | "Parse any constraint from the invocation. State it: Constraint: [constraint text, or 'none']." + "Mark any candidate that violates the constraint as [DISQ: constraint] immediately -- do not carry it into scoring." Generation-time enforcement: most rigorous C-05 mechanism. |
| C-06 | Disqualification Logic labeled | PASS | "Flag any candidate where Strategy or PM falls below 6 as [DISQ: low score]." + "Disqualified Summary: List all candidates that were disqualified, with labeled reasons. Tally by cause." Two disqualification triggers (generation-time constraint + scoring-time score floor) plus a tally. |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: Name it. State score. One sentence: why is it a credible fallback if the top pick is unavailable?" All three elements explicit. |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At minimum, one entry on vocabulary coverage, one on role weighting calibration, one on disqualification patterns observed. Severity: P1/P2/P3." Most prescriptive C-08: minimum 3 entries with severity and topic distribution. |
| C-09 | `--validate` flag behavior | FAIL | No --validate flag mechanism. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Domain vocabulary: [term1, term2, ...] / Source: [file name(s)]" with 5-10 terms from CLAUDE.md and plugin-plan.md named explicitly. Strongest C-10 format: source file citation is required. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 1/2

```
composite = (5/5 * 60) + (3/3 * 30) + (1/2 * 10)
          = 60 + 30 + 5
          = 95
```

**Score: 95 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-02 | C-09 | C-10 |
|------|-----------|-----------|-------------|--------------|-----------|---------|------|------|------|
| 1 | V-02 Strategy-first | 5/5 | 3/3 | 1/2 | **95** | YES | PASS | FAIL | PASS |
| 1 | V-04 Conversational | 5/5 | 3/3 | 1/2 | **95** | YES | PASS | FAIL | PASS |
| 1 | V-05 Combined | 5/5 | 3/3 | 1/2 | **95** | YES | PASS | FAIL | PASS |
| 4 | V-01 Baseline | 5/5 | 3/3 | 0/2 | **90** | YES | PASS | FAIL | FAIL |
| 5 | V-03 Traffic-light | 4/5 | 3/3 | 0/2 | **73** | NO | FAIL | FAIL | FAIL |

**C-09 is the ceiling.** No variation clears C-09 (--validate flag). It requires a design feature that doesn't exist yet. The 95 ceiling is the round's effective maximum without that feature.

**C-02 is V-03's blocker.** Traffic-light format sacrifices weight declaration. The rubric's "Declared weights sum to 100%" is incompatible with tier-based scoring.

---

## Structural Guarantee Ranking — Within the 95 Cluster

| Strength | Variation | Why |
|----------|-----------|-----|
| Strongest | V-05 | Phase headers prevent phase-bleeding; generation-time constraint disqualification; collision covers top 3; C-08 minimum 3 findings; C-04 requires vocab connection |
| Strong | V-02 | Vocab extraction + Strategy-first primes rationale; C-04 explicitly requires two named dimensions |
| Moderate | V-04 | Conversational format is the most model-behavior dependent; strongest C-05 instruction text but no structural enforcement |

V-04's "every candidate decision should trace back to whether it meets that constraint" is the most explicit C-05 instruction in the round, but it relies on instruction compliance rather than structural gates. V-05's generation-time [DISQ: constraint] marking makes the same behavior structurally unavoidable.

---

## Excellence Signals — Round 1

### E-1: Generation-time disqualification (V-05) outperforms post-hoc filtering for C-05/C-06

V-05's GENERATE phase marks constraint violations as [DISQ: constraint] immediately and does not carry them into the SCORE phase. This is structurally superior to V-01/V-02/V-04's post-hoc "list what you removed" instruction. Contaminated candidates cannot accumulate false positive scores if they are flagged before scoring begins.

### E-2: Vocab extraction is the strongest single addition to the baseline (V-02, V-04, V-05 all +5)

All three variations that add domain vocabulary extraction (C-10) move from 90 to 95. The vocab extraction step is also the mechanism that makes C-04 rationale depth achievable — V-05 explicitly requires the rationale to connect back to the Phase 1 vocabulary, producing the deepest C-04 output.

### E-3: The traffic-light format axis exposes a rubric tension (V-03)

V-03 demonstrates that C-02 (declared weights) and a tier-based scoring format cannot coexist. This is not a phrasing problem — it is a structural incompatibility. If traffic-light format has value for C-06 (which it does: automatic DISQ rule is the clearest mechanism in the round), the rubric needs a separate criterion or relaxed C-02 pass condition for tier-based formats. V-03 also shows the strongest C-05 mechanism (dedicated constraint column per candidate) that no other variation implements.

---

## New Findings

### SF-01: C-09 is a design gap, not a phrasing gap (P1)

No variation can pass C-09 because `--validate <name>` is not implemented in the current skill spec. The criterion can only be cleared by adding the flag to the skill design. Round 1 confirms this prediction from the trace.

### SF-02: Traffic-light format and declared weights are structurally incompatible (P2)

V-03's hypothesis (traffic-light reduces false precision and improves C-06) is partially validated — the DISQ rule mechanism is the clearest C-06 implementation in the round. But the format pays for this with C-02 failure. If a future rubric version wants to accommodate tier-based formats, C-02 would need an alternative pass path: "Declared weights OR explicit tier-to-score mapping."

### SF-03: Phase headers suppress scope creep between phases (P2)

V-05's explicit `--- PHASE N ---` structure prevents the model from leaking vocabulary extraction results into candidate generation prematurely, or carrying disqualified candidates into scoring. This structural property is not tested by any current criterion. A potential C-11 might read: "Lifecycle phases completed in order with no backflow of disqualified candidates into scoring."

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate for the same reasons it leads within the 95 cluster:
- Phase headers are the strongest structural enforcement mechanism available in a text prompt
- Generation-time constraint disqualification eliminates contamination before it enters the scoring table
- C-04 rationale explicitly requires vocabulary connection — produces the deepest justified top pick
- C-08 minimum 3 findings entries produces the most useful findings register for downstream rubric evolution

**V-02** is the closest alternative. V-02 and V-05 share the same essential/recommended pass structure and Strategy-first scoring order. V-02 is simpler and lower model-behavior-risk than V-04. If V-05's phase structure is judged too prescriptive for a naming skill (where creative latitude matters), V-02 is the fallback.

**V-03** should be revived only if the rubric adds an alternative C-02 path for tier-based formats. Its C-05 constraint-column mechanism and C-06 structural DISQ rule both represent genuine improvements over the baseline.

```json
{"top_score": 95, "all_essential_pass": false, "new_patterns": ["Generation-time disqualification (V-05 GENERATE phase) prevents contaminated candidates from entering scoring, eliminating a class of false-positive score inflation not addressed by post-hoc filtering instructions", "Traffic-light tier scoring and declared percentage weights are structurally incompatible — the format axis directly sacrifices the C-02 pass condition; a tier-based format requires either a relaxed C-02 or an explicit tier-to-weight mapping"]}
```
