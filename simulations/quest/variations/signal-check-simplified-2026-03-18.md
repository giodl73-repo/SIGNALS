The simplified prompt looks clean. Now the full simplification report:

---

## Simplified Prompt

Written to `simulations/quest/variations/signal-check-simplified-2026-03-18.md`.

---

## Simplification Report

### What was removed and why

| Cut | Where | Words removed | Reason |
|-----|-------|---------------|--------|
| Consulting Directory block | STANDING RULES | ~55 | Reader-role mapping is meta-commentary; `Applies to:` scopes on each rule already govern who does what |
| Rule 1 middle paragraph (2 sentences → 1) | STANDING RULES | ~30 | "A committing engineer checking... consults this rule to determine..." explains how a reader uses the rule — the rule itself and its `Applies to:` scope are sufficient; kept only "Silence in any governed location constitutes absence drift." |
| Rule 2 middle paragraph (2 sentences → 1) | STANDING RULES | ~40 | "A skill-reference consumer disambiguating a reference consults this rule..." same pattern; kept only the operative definition "A bare name or imprecise format constitutes reference ambiguity -- it cannot be resolved without guessing." |
| Rule 3 philosophical elaboration (3 sentences) | STANDING RULES | ~89 | `"Not operative" understates the condition...`, `These two registers are not substitutes...`, `A constraint without explicit location scope...` all restate the existence condition in different registers; the one operative sentence was kept |
| ENFORCEMENT STACK NOTE | STANDING RULES | ~65 | All three rules already encode their failure class in their headings; the note adds no instruction |
| VERDICT `[FUNCTION:]` experimental narration | VERDICT | ~70 | "This is the live R20 axis: V-01 through V-04 carry zero to two..." documents the experimental design, not operating instructions; the operational description of the closed loop was kept |
| READINESS SUMMARY `[FUNCTION:]` trim | READINESS SUMMARY | ~15 | "Does not decide; the VERDICT section below states the decision. This section provides the narrative context." reduced to one phrase since VERDICT's existence already makes this clear |
| Standalone "Write this section last" duplicate | READINESS SUMMARY | ~10 | `[FUNCTION:]` label already says "Written last, placed first" |
| "The order is intentional:" note | PREFLIGHT CHECK | ~35 | Order is encoded in item numbering; the explanation of WHY adds no constraint |
| 4× "Why this matters:" blocks | Items 1–4 | ~60 | Explanatory context; item analysis structure is unchanged and sufficient |
| CROSS-ITEM PATTERNS `[FUNCTION:]` trim | CROSS-ITEM PATTERNS | ~30 | Dim/Quality/trajectory detection list removed from label; the `Scan:` block inside the section teaches these directly |
| ARTIFACT `[FUNCTION:]` trim | ARTIFACT | ~30 | Removed field enumeration (fields listed in frontmatter below); kept only the trajectory feed note |
| 4× "What the inventory shows:" labels | Items 1–4 | ~16 | Structural scaffolding; content that follows is self-explanatory |
| 4× "What the team can do:" labels | Items 1–4 | ~20 | `Action:` field appears directly; template at section top already names it |
| "Scan index:" explanatory suffix | PREFLIGHT CHECK | ~13 | "(absence phrases embedded at point of use per Rule 1 -- both locations required)" — kept both instances of the phrases; the explanatory note is redundant |
| "Invariant ordering" line | MISSING SIGNAL GUIDE | ~12 | Ordering stated immediately above in two explicit bullet points |
| "Do not imply signal health when none was checked." | READINESS SUMMARY | ~9 | Rule 1 already covers all governed locations; this is a restatement |

**Total removed: 553 words (17.6%)**

---

### Essential criteria verification

| Criterion | What it requires | Present in simplified? |
|-----------|-----------------|------------------------|
| **C-54** | Evidence trace in VERDICT maps each blocking dim to exact inventory row # and artifact path; `evidence_trace` in frontmatter | YES — full Evidence trace format preserved, frontmatter intact |
| **C-55** | Named VERDICT section with go/no-go, `blocking_dims`, Condition, in Rule scopes | YES — VERDICT section present, all fields present, Rule 1 and Rule 2 scopes include VERDICT |
| **C-56** | Quality column in artifact inventory (STRONG/ADEQUATE/WEAK) | YES — table column and annotation rules preserved |
| **C-57** | Prior check field in each preflight item with trajectory labels | YES — Prior check field in all 4 items, trajectory vocabulary block preserved |
| **Rule 1 scope** | Covers readiness summary, VERDICT (Evidence trace), all Finding locations, Prior check fields, cross-item patterns, MISSING SIGNAL GUIDE | YES — scope list unchanged |
| **Rule 2 scope** | Covers readiness summary, VERDICT (Condition field only), all action locations; Evidence trace explicitly excluded | YES — both clauses preserved exactly |
| **Rule 3** | Every rule must declare scope; undeclared = does not exist as active rule | YES — Obligation + Existence condition + self-application preserved; only philosophical elaboration removed |
| **Verbatim absence phrases** | 4 phrases, at scan index AND embedded at point of use in each item | YES — scan index table intact, all 4 per-item phrases intact |
| **Null-pattern block** | Required when no cross-item pattern exists | YES — null-pattern block + Rule 1 reminder preserved |
| **Row number stability** | Assigned in GATHER YOUR SIGNALS, referenced in Evidence trace | YES — instruction and FUNCTION label both preserved |
| **Prior check lookup** | Glob for prior check artifact, frontmatter STATUS fields, trajectory values | YES — lookup instructions and trajectory vocab block preserved |
| **ARTIFACT frontmatter** | `verdict`, `blocking_dims`, `evidence_trace`, `trajectory`, `quality_distribution`, `dims_coverage` all machine-readable | YES — complete frontmatter preserved |

All essential criteria: **PASS**

---

```json
{"simplified_word_count": 2590, "original_word_count": 3143, "all_essential_still_pass": true}
```
 the inventory source.
  Format per blocking dimension:
    [Dimension] ([STATUS]): Row {N} -- {artifact path} -- {one phrase explaining the gap}
    -- OR --
    [Dimension] ([STATUS]): not represented in inventory -- no artifact carries {abbrev} in Dims
  If Verdict is GO: "None -- all dimensions pass; inventory rows confirm coverage."
  Rule 1 applies: do not leave Evidence trace blank for any blocking dimension. If source
    is ambiguous, write "source ambiguous -- inspect rows {N, M} for {dimension} coverage."
  Note: Evidence trace uses row numbers from the GATHER YOUR SIGNALS table. Rule 2 does
    not apply within Evidence trace (no skill references required in this field).]

Rule 1 applies to entire VERDICT section: if no artifacts exist and check stopped:
  "Verdict: NO-GO -- no signal artifacts exist for {topic}.
   Condition: Run /discover:causal to begin signal gathering. Rule 2 applies.
   Blocking dimensions: CAUSAL GAP (OPEN), SEQUENCE (OPEN), STALENESS (OPEN), COHERENCE (OPEN)
   Evidence trace: all dimensions -- not represented in inventory -- no artifacts found."

=== THE PREFLIGHT CHECK ===
[FUNCTION: Four-dimension analysis. STATUS values feed READINESS SUMMARY and VERDICT.
 Evidence trace references row numbers from GATHER YOUR SIGNALS -- they must match.]

STATUS scale:
  OK-STRONG = 2+ independent artifacts cover this dimension, all within staleness threshold
  OK-WEAK   = 1 artifact only, or at threshold boundary; covered but thin
  FLAG      = evidence exists but raises a concern worth reviewing
  OPEN      = no artifact covers this dimension at all

Quality weight: WEAK-only coverage caps STATUS at OK-WEAK regardless of artifact count.

Trajectory vocabulary for Prior check field:
  IMPROVING = prior STATUS was worse than current
  STABLE    = prior STATUS matches current (no change)
  DEGRADING = prior STATUS was better than current
  NEW       = no prior check artifact found for this topic

Scan index:

  | Dimension  | Key check question                                         | Required absence phrase when empty                                                           |
  |------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------|
  | CAUSAL GAP | Does any artifact trace mechanism from feature to outcome? | "No mechanism evidence found -- the causal gap is open."                                    |
  | SEQUENCE   | Does a discovery artifact predate the commitment artifact? | "No discovery artifacts found -- ordering cannot be established."                            |
  | STALENESS  | Do artifacts fall within the named freshness threshold?    | "No dated artifacts found -- staleness cannot be assessed."                                  |
  | COHERENCE  | Do at least two artifacts on the same question agree?      | "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."  |

Each item uses this structure:

  Dims prediction: [inference from Dims column count for this dimension]
  Prior check: [{prior date}: {prior status}] -> [{current}: IMPROVING | STABLE | DEGRADING]
    -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: OK-STRONG | OK-WEAK | FLAG | OPEN
  Basis: [artifacts with dates and Quality; "see above" does not pass]
  Finding: [observation or required verbatim absence phrase -- Rule 1]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2; omit if OK-STRONG or OK-WEAK]

--- Item 1: CAUSAL GAP ---

Dims prediction: count rows with C in the Dims column. 0 rows predicts OPEN;
1 row predicts OK-WEAK at best; 2+ rows may support OK-STRONG if mechanism is traced.
Quality check: all WEAK C-annotated artifacts cap STATUS at OK-WEAK.

Required verbatim absence phrase:
  "No mechanism evidence found -- the causal gap is open."

  Step 1: "The claimed outcome is: [outcome]." (Or: not named -- itself a gap.)
  Step 2: Mechanism = causal chain [step 1] -> [step 2] -> [step 3]. Not correlation.
  Step 3: Scan C-annotated artifacts.
    (a) "Mechanism evidence found: [artifact, date, Quality] establishes [mechanism]
        by tracing [step 1] -> [step 2] -> [step 3]."
    (b) Required verbatim absence phrase.

  OK-STRONG: 2+ STRONG/ADEQUATE C-annotated artifacts trace mechanism independently.
  OK-WEAK: 1 artifact; or all WEAK quality.
  FLAG: artifact traces correlation not mechanism.
  OPEN: no C in Dims; or no artifact passes mechanism test.

  Dims prediction: [state count and prediction]
  Prior check: [{prior date}: {prior causal_gap_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with Quality; if none: "no artifact addresses mechanism"]
  Finding: [(a) or required absence phrase (b)]
  Action: [if FLAG or OPEN: /discover:causal -- Rule 2]

--- Item 2: SEQUENCE ---

Dims prediction: count Sq rows. 0 predicts OPEN.
Quality note: WEAK discovery counts for ordering but carries reliability caveat.

Required verbatim absence phrase:
  "No discovery artifacts found -- ordering cannot be established."

  Classify: Discovery (discover, scout, prove, research, listen) vs Commitment (draft,
  topic, program). Compare dates.

  OK-STRONG: 2+ STRONG/ADEQUATE discovery predating commitment by clear margin.
  OK-WEAK: 1 predating; or WEAK quality; or narrow margin.
  FLAG: commitment precedes discovery -- inversion.
  OPEN: no discovery artifacts.

  (a) "Discovery precedes commitment: [discovery, date, Quality] predates [commitment, date]."
  (b) "Commitment precedes discovery: inversion flagged."
  (c) Required verbatim absence phrase.

  Dims prediction: [Sq count and prediction]
  Prior check: [{prior date}: {prior sequence_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [artifacts with dates and Quality compared]
  Finding: [(a), (b), or required absence phrase (c)]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 3: STALENESS ---

Dims prediction: St annotation identifies staleness-sensitive artifacts.
Quality note: WEAK artifacts near boundary especially at risk.

Required verbatim absence phrase:
  "No dated artifacts found -- staleness cannot be assessed."

  "For {topic}'s domain: signals older than [N] days are stale because [reason]."

  OK-STRONG: all within threshold; most < half age; STRONG/ADEQUATE quality.
  OK-WEAK: within threshold but near boundary; or WEAK quality.
  FLAG: one or more exceed threshold.
  OPEN: no dated artifacts.

  Dims prediction: [St count and prediction]
  Prior check: [{prior date}: {prior staleness_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [each artifact with date and Quality]
  Finding: [fresh/stale with Quality notes; or required absence phrase]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

--- Item 4: COHERENCE ---

Dims prediction: 0-1 Co rows predicts OPEN. 2+ may support OK-WEAK or OK-STRONG.
Quality note: contradiction between WEAK artifacts is noted with lower urgency.

Required verbatim absence phrase:
  "Only one artifact exists for {topic} -- no comparable pair available to assess coherence."

  OK-STRONG: 2+ STRONG/ADEQUATE pairs agree; no latent contradictions.
  OK-WEAK: 1 pair; agree; limited scope; or both WEAK.
  FLAG: at least one pair disagrees.
  OPEN: single artifact only.

  Agreement: "[A, date, Quality] and [B, date, Quality] both say [X]."
  Contradiction: "[A, date, Quality] says [X]. [B, date, Quality] says [Y]."
  Required absence phrase when no pair.

  Dims prediction: [Co count and prediction]
  Prior check: [{prior date}: {prior coherence_status}] -> [{current}: IMPROVING |
    STABLE | DEGRADING] -- OR -- "none -- first run for {topic} [NEW]"
  STATUS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  Basis: [pairs with Quality; or "single artifact -- no comparable pair"]
  Finding: [agreement, contradiction, or required absence phrase]
  Action: [if FLAG or OPEN: /namespace:skill -- Rule 2]

=== CROSS-ITEM PATTERNS ===
[FUNCTION: Root-cause synthesis. Null-pattern block required when no pattern exists.]

Step back from all four items. Do two or more share a common root?
Scan:
  - Thin Coverage: 3+ dimensions with 1 Dims artifact each.
  - Weak Foundation: 3+ dimensions covered only by WEAK artifacts.
  - Signal Decay: 2+ dimensions showing DEGRADING in Prior check field.

  Pattern: [name -- e.g., "Premature Commitment", "Thin Coverage", "Weak Foundation",
    "Signal Decay", "Stale Signal Cascade"]
  Items implicated: [list dimensions]
  Root cause: [single sentence]
  Single action: [/namespace:skill -- Rule 2]

Common patterns:
  - CAUSAL GAP OPEN + SEQUENCE OPEN/FLAG: root = missing discovery phase;
    action = /discover:causal
  - STALENESS FLAG + COHERENCE FLAG: root = stale signal causing contradiction;
    action = refresh the stale artifact
  - Multiple OK-WEAK (Dims: 3+ dims with 1 artifact each):
    root = thin coverage; action = discovery skill for weakest dim
  - Signal Decay (2+ DEGRADING): root = signal portfolio eroding without refresh;
    action = /discover:causal or /scout:feasibility for the most degraded dim

If no pattern exists:

  Pattern: None
  Items implicated: N/A
  Root cause: N/A
  Single action: N/A

Rule 1 applies: null-pattern block required when no pattern exists.
Rule 2 applies: Single action uses /namespace:skill format.

=== MISSING SIGNAL GUIDE ===
[FUNCTION: Actionable gap map, severity-ordered. Most blocking gap appears first.
 Rule 1 and Rule 2 both apply to every line.]

Items ordered by severity: OPEN before FLAG.
Within same severity tier: CAUSAL GAP, then SEQUENCE, then STALENESS, then COHERENCE.
For every FLAG or OPEN dimension:
  [Dimension] [OPEN|FLAG]: run /[namespace]:[skill] -- produces [what it creates]

Examples (OPEN before FLAG):
  CAUSAL GAP OPEN: run /discover:causal -- produces mechanism evidence for the causal chain
  SEQUENCE OPEN: run /discover:competitors -- produces dated discovery artifact to establish order
  COHERENCE OPEN: run /scout:feasibility -- produces second feasibility signal for comparison
  STALENESS FLAG: run /discover:competitors -- refreshes competitive landscape signal

Rule 1: if a gap is present and no skill is identified, write
"no skill identified for [dimension] -- manual investigation required."

If all dimensions pass: "No missing signals -- signal health is clear."

=== ARTIFACT ===
[FUNCTION: Persist the health report. STATUS fields feed trajectory computation in the
 next run's Prior check fields.]

Write to simulations/signal/check/{topic}-check-{date}.md.

Frontmatter:
  topic: {topic}
  date: {date}
  verdict: go | conditional | no-go
  blocking_dims: [{list of FLAG or OPEN dimension names, or empty list}]
  evidence_trace:
    causal_gap: "Row {N}: {artifact path}" | "not represented in inventory"
    sequence: "Row {N}: {artifact path}" | "not represented in inventory"
    staleness: "Row {N}: {artifact path}" | "not represented in inventory"
    coherence: "Row {N}: {artifact path}" | "not represented in inventory"
  causal_gap_status: ok-strong | ok-weak | flag | open
  sequence_status: ok-strong | ok-weak | flag | open
  staleness_status: ok-strong | ok-weak | flag | open
  coherence_status: ok-strong | ok-weak | flag | open
  staleness_threshold_named: true | false
  mechanism_evidence_found: true | false
  explicit_absences_declared: true | false
  skill_format_enforced: true
  cross_dimension_pattern: true | false
  missing_signals_by_skill: true | false
  verbatim_absence_phrases_used: true | false
  artifact_count: {count}
  open_dimensions: [{list of FLAG or OPEN dimension names}]
  dims_coverage:
    causal_gap: {count of artifacts with C in Dims column}
    sequence: {count of artifacts with Sq in Dims column}
    staleness: {count of artifacts with St in Dims column}
    coherence: {count of artifacts with Co in Dims column}
  quality_distribution:
    strong: {count}
    adequate: {count}
    weak: {count}
  prior_check_date: {date or null}
  trajectory:
    causal_gap: improving | stable | degrading | new
    sequence: improving | stable | degrading | new
    staleness: improving | stable | degrading | new
    coherence: improving | stable | degrading | new
```
