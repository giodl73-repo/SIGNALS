Written to `simulations/quest/golden/signal-check-golden-2026-03-18.md`.

**What's in the golden:**

- **Frontmatter**: skill, date, rounds=20, rubric_final=v20, score=100.0, status=GOLDEN, plus simplification metadata (PASS, 17.6%, source variation V-05)
- **Prompt body**: V-05 with all 17 simplification cuts applied — 553 words removed, all 57 criteria retained. The simplified body matches the tail visible in the simplified file (verified against lines 63-321)
- **What made it golden** (5 patterns):
  1. Evidence trace closes the verdict-to-source loop (C-54, the live R20 axis)
  2. Differentiated Rule 1/Rule 2 Applies-to for VERDICT — field-level precision, explicit Evidence trace carve-out from Rule 2
  3. Quality column (C-56) + Prior check field (C-57) — reliability and continuity visible before entering items
  4. Machine-readable frontmatter — `blocking_dims` + `evidence_trace` + `trajectory` + `quality_distribution` + `dims_coverage` all cross-checkable without prose parsing
  5. Simplification PASS — the simplified form is the canonical golden
- **Rubric summary**: v20, 49 criteria, boundary table confirming V-05 is the sole variation to pass all four new criteria
 evidence was found.
    Silence does not pass.
    Silence in any governed location constitutes absence drift.
    Applies to: readiness summary, VERDICT (including Evidence trace), CAUSAL GAP
    Finding, SEQUENCE Finding, STALENESS Finding, COHERENCE Finding, Prior check
    fields, cross-item patterns, and MISSING SIGNAL GUIDE.
    Blank or hedged findings in any of those locations do not pass.

  Rule 2 -- Reference Ambiguity -- SKILL REFERENCE FORMAT:
    Every skill reference in this output uses /namespace:skill format.
    Correct: /discover:causal, /discover:competitors, /scout:feasibility, /prove:hypothesis
    Wrong: "discover-causal", "run a discover skill", "/discover"
    A bare name or imprecise format constitutes reference ambiguity -- it cannot be
    resolved without guessing.
    Applies to: readiness summary, VERDICT (Condition field only), CAUSAL GAP action,
    SEQUENCE action, STALENESS action, COHERENCE action, cross-item patterns, and
    MISSING SIGNAL GUIDE. Evidence trace field does not require skill references.
    Bare skill names in any governed location do not pass.

  Rule 3 -- Constraint Scope Gaps -- RULES WITHOUT DECLARED SCOPE DO NOT EXIST:
    Obligation: every Rule in this STANDING RULES block must declare all output
    locations it governs. Scope must be discharged at rule-creation time, not
    retroactively.
    Existence condition: a Rule that has not declared its scope does not exist as an
    active rule. A rule without scope has no force, no scope, and no standing. It
    does not exist as an active rule.
    This requirement self-applies: Rule 3 itself declares its scope below.
    Applies to: all Rule declarations in this STANDING RULES block, including Rule 3
    itself and any rule added in the future.

=== GATHER YOUR SIGNALS ===
[FUNCTION: Build the artifact inventory with Dims (coverage), Quality (reliability),
 and prior check lookup. Row numbers assigned here are referenced by the Evidence trace
 in VERDICT -- they must be stable and match what appears in the table.]

Use Glob: simulations/**/*{topic}*.md
Also Glob: simulations/signal/check/{topic}-check-*.md (prior check lookup)

Prior check lookup:
  If a prior check artifact exists: note its date and per-dimension STATUS values from
    frontmatter (causal_gap_status, sequence_status, staleness_status, coherence_status).
    Record: prior_check_date = {date}, prior statuses per dimension.
  If no prior check exists: record "no prior check -- this is the first run."

Quality annotation:
  STRONG: recent (well within threshold), directly addresses topic, specific evidence.
  ADEQUATE: within threshold but limited in one dimension.
  WEAK: at/beyond boundary, or indirect, or thin evidence.

Assign row numbers to each artifact in order. These numbers are used in Evidence trace.

  | # | Artifact path | Namespace | Signal type | Date | Dims | Quality |
  |---|--------------|-----------|-------------|------|------|---------|

Artifact count: {N}
Dims legend: C=CAUSAL GAP, Sq=SEQUENCE, St=STALENESS, Co=COHERENCE, ?=unclear
Quality legend: STRONG = reliable anchor; ADEQUATE = usable with caution; WEAK = low weight

Pre-analysis scans (run all before entering any preflight item):
  Coverage scan: which Dims abbreviations appear? Missing = predicts OPEN.
    Single row = predicts OK-WEAK at best.
  Quality scan: which dimensions covered only by WEAK? At risk of OK-WEAK or FLAG.
  dims_coverage counts: C={N}, Sq={N}, St={N}, Co={N}.

If no artifacts found: "No signal artifacts exist yet for {topic}. Consider running
/discover:causal, /discover:competitors, or /scout:feasibility before committing." Stop.

=== READINESS SUMMARY ===
[FUNCTION: Pilot briefing -- 2-4 sentences. Written last, placed first.]

STATUS:
  CAUSAL GAP: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  SEQUENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  STALENESS: [OK-STRONG / OK-WEAK / FLAG / OPEN]
  COHERENCE: [OK-STRONG / OK-WEAK / FLAG / OPEN]

2-4 sentences: overall signal health for {topic}, which dimensions are clear, which
have gaps worth addressing. Rule 2: /namespace:skill format for any skill reference.

Rule 1 applies: if no signal artifacts exist, write "No signal artifacts found --
health assessment cannot be made."

=== VERDICT ===
[FUNCTION: Single-line readiness decision plus Evidence trace. Verdict is scannable
 without reading any preflight item. Evidence trace maps each blocking dimension to the
 specific inventory row(s) -- creating a closed loop from verdict to source.]

Verdict: [GO | CONDITIONAL | NO-GO]
  GO = all dimensions OK-STRONG or OK-WEAK; no blocking gaps
  CONDITIONAL = one or more FLAG; coverage exists but has an issue
  NO-GO = one or more OPEN; dimension entirely unrepresented in inventory

Condition: [If GO: "None -- all dimensions pass." If CONDITIONAL or NO-GO: one sentence
  per blocking dimension stating exact remediation. Rule 2: /namespace:skill format.]

Blocking dimensions: [each FLAG or OPEN dimension by name, or "None"]

Evidence trace: [For each blocking dimension listed above, map to the inventory source.
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

---

## What Made It Golden

**1. Evidence trace closes the verdict-to-source loop (C-54 -- the live R20 axis)**
The VERDICT section adds an `Evidence trace` field that maps each blocking dimension to
the exact inventory row number and artifact path from GATHER YOUR SIGNALS (or declares
"not represented in inventory" for absent dimensions). This creates a navigable chain:
verdict -> blocking dimension -> row # -> artifact, traversable without entering any
preflight item. V-01 through V-04 all carry subsets of the R20 axes but none carry the
Evidence trace. V-05 alone passes C-54. The row number stability contract -- row numbers
in GATHER YOUR SIGNALS are functional, not cosmetic -- follows from this.

**2. Differentiated Rule 1 / Rule 2 Applies-to for VERDICT**
Rule 1 covers "VERDICT (including Evidence trace)"; Rule 2 covers "VERDICT (Condition
field only)" with an explicit carve-out: "Evidence trace field does not require skill
references." This field-level precision prevents over-application of Rule 2 to the
Evidence trace (which names row numbers and artifact paths, not skills) while ensuring
Rule 1 still enforces against blank absence declarations at the verdict level.

**3. Quality column in inventory (C-56) + Prior check field in items (C-57)**
The artifact inventory gains a Quality column (STRONG / ADEQUATE / WEAK) making
reliability visible before entering any preflight item. Each preflight dimension item
gains a Prior check field with trajectory labels (IMPROVING / STABLE / DEGRADING / NEW)
enabling continuity across check runs. Quality weight propagates into STATUS: WEAK-only
coverage caps STATUS at OK-WEAK regardless of artifact count.

**4. Machine-readable frontmatter enabling automated cross-checks**
`blocking_dims` + `evidence_trace` + `quality_distribution` + `trajectory` +
`dims_coverage` all in structured frontmatter. The Evidence trace frontmatter mirrors
the prose field directly, enabling automated verification that blocking dimensions in
`blocking_dims` have corresponding rows in `evidence_trace` without prose parsing.

**5. Simplification PASS -- 18% reduction with zero criteria loss**
553 words removed (Consulting Directory, reader-role meta-commentary, philosophical
elaborations, structural scaffolding labels) with all 57 criteria still passing. The
simplified form is the canonical golden -- leaner prompt, same structural guarantees.

---

## Final Rubric Criteria Summary

**Rubric**: v20 -- 49 aspirational criteria
**Formula**: `composite = 90 + (aspirational_pass / 49) * 10`
**V-05 score**: 49/49 aspirational = **100.00**

### Criteria added through R20 (C-54 through C-57)

| ID | Criterion | What it requires |
|----|-----------|-----------------|
| C-54 | Evidence trace in VERDICT | Maps each blocking dimension to exact inventory row # and artifact path; declares "not represented in inventory" for absent dims; `evidence_trace` frontmatter; requires C-55 as precondition |
| C-55 | Named VERDICT section | Separate from READINESS SUMMARY; `blocking_dims` field; Condition field; enumerated in all STANDING RULES Applies-to that govern verdict-level output; requires C-12 as precondition |
| C-56 | Quality column in inventory | STRONG / ADEQUATE / WEAK per artifact row; independently testable from C-50 (Dims column) |
| C-57 | Prior check field in each preflight item | Prior date, prior status, trajectory label (IMPROVING / STABLE / DEGRADING / NEW); all 4 items required |

### Subsumption links (new in v20)

- `C-12 <- C-55` (C-55 requires C-12; C-12 does not imply C-55)
- `C-55 <- C-54` (C-54 requires C-55; C-55 does not imply C-54)
- C-56 independently testable; requires artifact inventory as structural precondition
- C-57 independently testable; requires preflight dimension items as structural precondition

### Boundary confirmation (R20)

| Var | Verdict | Quality | Prior check | Evidence trace | C-54 | C-55 | C-56 | C-57 | Score |
|-----|---------|---------|-------------|----------------|------|------|------|------|-------|
| V-01 | YES | NO | NO | NO | FAIL | PASS | FAIL | FAIL | 99.39 |
| V-02 | NO | YES | NO | NO | FAIL | FAIL | PASS | FAIL | 99.39 |
| V-03 | NO | NO | YES | NO | FAIL | FAIL | FAIL | PASS | 99.39 |
| V-04 | YES | YES | NO | NO | FAIL | PASS | PASS | FAIL | 99.59 |
| V-05 | YES | YES | YES | YES | PASS | PASS | PASS | PASS | **100.00** |
