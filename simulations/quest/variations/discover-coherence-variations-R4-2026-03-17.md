---

## discover-coherence R4 — 5 variations

| # | Label | Axis | Predicted score |
|---|-------|------|----------------|
| V-01 | Minimized phases | Lifecycle — Ph2+Ph3 collapsed into one silent scan (6 phases) | 130 |
| V-02 | Blocking-priority table | Output format — blocking-first instead of inertia-first | 125 (C-13 fail) |
| V-03 | Conversational full-stack | Phrasing register — V-03 WHY-register + dual-table apparatus | 130 |
| V-04 | Minimized + inertia-motivated | Lifecycle + Inertia framing — 6-phase + motivation sentence | 130 |
| V-05 | Production candidate | All axes — 5 steps, merged verdict+artifact, leanest 130-scoring candidate | 130 |

**R4 framing**: This is the convergence round. R3 confirmed no new patterns; the only path to 130 is the dual-table apparatus (C-09/C-13/C-14). R4 answers two questions:

1. **Can V-05 be shorter?** V-01/V-04/V-05 all collapse phases — if they score 130, the answer is yes and R3-V-05's 7-phase structure was overhead.

2. **Is C-13 specifically about inertia?** V-02 substitutes "Blocking Contradictions" for "Inertia Contradictions." If it fails C-13 (predicted), it confirms the inertia label is structurally required by the pass condition — not just the priority-first concept.

The production candidate (V-05) merges verdict + artifact into a single final step and cuts 7 phases to 5. If it scores 130, it becomes the recommended skill body.
readable prompt while maintaining 130/130?
2. Does C-13's "inertia-first" requirement survive a "blocking-first" alternative? (diagnostic)

Three single-axis experiments first (V-01, V-02, V-03), then two combinations (V-04, V-05).

**Predicted scoring against v3 rubric (130 max, golden >= 95):**
- V-01: 130 (same structure as R3-V-05, fewer phases — all criteria intact)
- V-02: 125 (C-13 fails — blocking-priority does not satisfy the inertia-specific requirement)
- V-03: 130 (WHY-register + table = all 16 criteria pass)
- V-04: 130 (6-phase + motivated inertia-first)
- V-05: 130 (production candidate — leanest 130-scoring prompt in the series)

---

## V-01: Minimized phases (Lifecycle emphasis axis)

**Axis**: Lifecycle emphasis — collapse PHASE 2 (EXTRACT CLAIMS) and PHASE 3 (COUNT + CLASSIFY)
into a single SILENT SCAN phase, reducing V-05 from 7 phases to 6 without changing any
structural guarantee.

**Hypothesis**: R3-V-05's PHASE 2 builds an internal claim map ({factor → {skill: claim}})
before PHASE 3 classifies. This two-step extraction is the only structural difference from V-01's
merged approach. If the claim map is a writing aid for humans rather than a functional separator,
collapsing it should not affect scoring: all criteria depend on (a) scanning before outputting
(C-15), (b) tally-before-first-entry (C-06), (c) inertia-first table (C-13), (d) taxonomy column
(C-09), (e) token format for blocking (C-16). None of these require a separate claim-extraction
phase. Predicted: 130/130. If correct, V-01 is a shorter production candidate.

```
You are running /discover-coherence for topic: {topic}.

=== PHASE 1: INVENTORY ===

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory table:
| Skill | Date | Path |
|-------|------|------|

GATE: If fewer than 2 rows from 2 distinct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop here.

=== PHASE 2: SILENT SCAN (do not output any contradiction in this phase) ===

Read every file in the inventory. For each factor that carries a rating (HIGH / MEDIUM / LOW),
prediction ("likely", "unlikely", "expected to"), or scored finding, compare claims across skills.

For each factor where 2+ skills disagree, record internally:
  Factor name
  Skill A + exact claim; Skill B + exact claim
  Type (exactly one):
    rating-conflict      two skills assign different ratings to the same factor
    prediction-conflict  one skill predicts an outcome the other contradicts
    evidence-conflict    two evidence findings point in opposite directions
  Severity (exactly one):
    blocking    claims cannot both be true; decision depends on which is correct
    advisory    tension worth noting; does not prevent specifying
  Inertia flag: does this factor touch inertia, switching cost, workaround quality,
                or adoption prediction? These entries go in the Inertia table.

Do not emit any output in this phase.
Count: N total, M blocking, K advisory.
Count by type: R rating-conflict, P prediction-conflict, E evidence-conflict.

=== PHASE 3: FINDINGS HEADER ===

Before writing any table, output:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

=== PHASE 4: REPORT ===

Output two tables. The Inertia table renders first -- render it even if empty.

**Inertia Contradictions** (inertia / switching-cost / workaround-quality / adoption -- always first)

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

Column rules:

Type: exactly `rating-conflict`, `prediction-conflict`, or `evidence-conflict`

Severity: exactly `blocking` or `advisory`

Claim A / Claim B: the specific conflicting statement in its own words, not just the topic

Resolution by severity:

  BLOCKING: required token format:
    "Resolve with: /{skill-name} [--focus {parameter}]"
    Correct:  "Resolve with: /discover-inertia --focus switching-cost"
    Wrong:    "Run discover-inertia to check switching cost"  (no /token -- fails C-16)
    Wrong:    "Investigate the inertia discrepancy"           (vague -- fails C-12, C-16)
    The /skill-name token is required. A blocking cell without it fails.

  ADVISORY: concrete action in prose:
    Name a specific field to update, claim to amend, or skill to run.
    Example: "Update discover-competitors threat rating for inertia from MEDIUM to HIGH."
    Do not write "investigate further."

Cross-skill rule: Both skills in each row must be different discover skills.

=== PHASE 5: VERDICT ===

Summary line:
"Compared: {skill list} ({total} signals). Inertia contradictions: {A} ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

Verdict:
- M = 0 -> "Ready to specify."
- M >= 1 -> "Not ready to specify -- {M} blocking contradiction(s) must be resolved.
  See rows marked `blocking` above."

=== PHASE 6: ARTIFACT ===

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter:
  topic: {topic}
  date: {date}
  signals_compared: [{skill-1}, {skill-2}, ...]
  inertia_blocking: {N}
  inertia_advisory: {N}
  other_blocking: {N}
  other_advisory: {N}
  verdict: ready | not-ready
```

---

## V-02: Blocking-priority table (Output format axis)

**Axis**: Output format — replace inertia-first table ordering with blocking-first table ordering.
Two tables: "Blocking Contradictions" then "Advisory Contradictions." The factor column names
the contested factor for each entry.

**Hypothesis**: C-13 requires "a dedicated 'Inertia Contradictions' section or equivalent
priority-first table before any general contradictions section." Blocking-first ordering satisfies
the spirit of C-13 (highest-criticality category first) but not its letter (inertia-specific label
required). This is a diagnostic test: does the C-13 pass condition require the exact "Inertia"
label, or does any priority-first section satisfy it? If V-02 fails C-13 (predicted), it confirms
that inertia-specific labeling is structurally required — not just priority ordering. Predicted:
125/130 (C-13 fail only).

```
You are running /discover-coherence for topic: {topic}.

=== PHASE 1: INVENTORY ===

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory table:
| Skill | Date | Path |
|-------|------|------|

GATE: If fewer than 2 rows from 2 distinct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop here.

=== PHASE 2: EXTRACT CLAIMS ===

Read every file in the inventory. For each skill, extract all claims that are:
- A rating: HIGH / MEDIUM / LOW on any named factor
- A prediction: "likely", "unlikely", "expected to"
- A scored finding: any numeric or scale assessment

Build an internal claim map: {factor -> {skill: claim}}.

=== PHASE 3: COUNT + CLASSIFY (do not output any contradiction in this phase) ===

For every factor appearing in 2+ skills where claims disagree, classify:

Type (exactly one):
- `rating-conflict`: two skills assign different ratings to the same factor
- `prediction-conflict`: one skill predicts an outcome the other contradicts
- `evidence-conflict`: two evidence findings point in opposite directions

Severity (exactly one):
- `blocking`: claims cannot both be true; decision depends on which is correct
- `advisory`: tension worth noting; does not prevent specifying

Count: N total, M blocking, K advisory.
Count by type: R rating-conflict, P prediction-conflict, E evidence-conflict.

Do not output any contradiction entry during this phase.

=== PHASE 4: FINDINGS HEADER ===

Before writing any table, output:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

=== PHASE 5: REPORT ===

Output two tables. The Blocking table renders first -- render it even if empty.

**Blocking Contradictions** (must resolve before specifying -- always render first)

| # | Type | Factor | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|--------|----------------|---------|----------------|---------|------------|

**Advisory Contradictions** (notable tensions that do not block specifying)

| # | Type | Factor | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|--------|----------------|---------|----------------|---------|------------|

Column rules:

Type: exactly `rating-conflict`, `prediction-conflict`, or `evidence-conflict`

Factor: the contested factor name (e.g., "switching-cost", "adoption-likelihood",
"inertia-threat-level") — naming the factor makes each row self-explanatory

Claim A / Claim B: the specific conflicting statement in its own words

Resolution by table:

  BLOCKING entries: required token format:
    "Resolve with: /{skill-name} [--focus {parameter}]"
    Correct:  "Resolve with: /discover-inertia --focus switching-cost"
    Wrong:    "Run discover-inertia to check switching cost"  (no /token -- fails C-16)
    Wrong:    "Investigate the discrepancy"                   (vague -- fails C-12, C-16)

  ADVISORY entries: concrete action in prose:
    Name a specific field to update, claim to amend, or skill to run.
    Do not write "investigate further."

Cross-skill rule: Both skills in each row must be different discover skills.

=== PHASE 6: VERDICT ===

Summary line:
"Compared: {skill list} ({total} signals). {M} blocking, {K} advisory."

Verdict:
- M = 0 -> "Ready to specify."
- M >= 1 -> "Not ready to specify -- {M} blocking contradiction(s) must be resolved.
  See rows marked `blocking` above."

=== PHASE 7: ARTIFACT ===

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter:
  topic: {topic}
  date: {date}
  signals_compared: [{skill-1}, {skill-2}, ...]
  blocking_count: {M}
  advisory_count: {K}
  verdict: ready | not-ready
```

---

## V-03: Conversational full-stack (Phrasing register axis)

**Axis**: Phrasing register — V-03's conversational WHY-first register applied to the full-stack
dual-table apparatus from R3-V-05. Every structural rule is explained before it is stated;
every constraint includes its purpose. R3-V-03 scored 115/130 with conversational register + no
table; this variation adds the table apparatus.

**Hypothesis**: R3 confirmed register parity: V-03 (conversational, 115) tied V-04 (structural,
115) — both pass C-15 and C-16 regardless of register. The gap at 115 was C-09/C-13/C-14 (table
apparatus). Adding the dual table to V-03's register should close all three. If conversational
register + table = 130, this is the most human-readable production candidate in the series.
Predicted: 130/130.

```
You are running /discover-coherence for topic: {topic}.

The goal here is to catch signal disagreements before you commit to a spec. If discover-competitors
rated inertia MEDIUM but discover-inertia found switching cost HIGH, those two signals disagree --
and that disagreement could derail your feature if left unresolved. This skill finds those
conflicts, classifies each by type and severity, and gives you exact next steps to resolve them.

--- FIND YOUR SIGNALS ---

Start by locating all discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Show the inventory as a table:
| Skill | Date | Path |
|-------|------|------|

You need at least 2 artifacts from at least 2 different discover skills to run a meaningful
coherence check. With only one signal there is nothing to compare. If you don't have 2+:
  "GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop here -- you cannot produce a coherence report from a single signal.

--- COUNT EVERYTHING BEFORE YOU OUTPUT ---

Before writing any table, read all files and finish your count. The reason: the tally in your
header must cover the full set of contradictions. If you output entries as you scan, the tally
at the top will be wrong -- it will only reflect what you've seen so far. Completing the scan
first makes the tally accurate.

Read every file. For each factor that carries a rating (HIGH/MEDIUM/LOW), a prediction, or a
scored finding, compare the claims across skills. For every factor where 2+ skills disagree, note:

- Type (name the nature of the disagreement exactly):
    rating-conflict      two skills assign different ratings to the same factor
    prediction-conflict  one signal predicts an outcome the other contradicts
    evidence-conflict    two evidence findings point in opposite directions

- Severity (ask: can both claims be true, and does it change the decision?):
    blocking  no -- and the decision hinges on which is right
    advisory  yes, or close enough -- worth flagging but doesn't block specifying

- Inertia flag: does this factor touch inertia threat level, switching cost, workaround quality,
  or adoption prediction? These go in the Inertia table. They render first because inertia
  contradictions directly determine whether the product strategy is viable against the status quo
  -- they are the highest-priority category regardless of how many there are.

Count N (total), M (blocking), K (advisory).
Count by type: R (rating-conflict), P (prediction-conflict), E (evidence-conflict).
Don't output anything yet.

--- OPEN WITH THE TALLY ---

Your report must open with this tally block before any table entry:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

--- TWO TABLES: INERTIA FIRST ---

Inertia contradictions carry the highest decision weight -- they determine whether the feature
strategy is viable against the status quo competitor. Render the Inertia table first, even if it
is empty. Rendering an empty table is correct; omitting it is not.

**Inertia Contradictions** (inertia / switching-cost / workaround-quality / adoption)

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

For each column:

Type: `rating-conflict` | `prediction-conflict` | `evidence-conflict` -- no other values.
  Using a different label, or leaving this blank, fails C-09.

Severity: `blocking` | `advisory` -- no other values.
  "unclear", "high-priority", or any other label fails C-03.

Claim A / Claim B: quote or closely paraphrase the specific conflicting statement. The reader
must see exactly what each signal said without opening the source files. "discover-competitors
and discover-inertia disagree" with no quoted claim fails C-02.

Resolution -- the format is how you communicate what kind of action is needed:
  For BLOCKING rows (claims cannot both be true -- must run evidence to resolve):
    Use the exact token format: "Resolve with: /{skill-name} [--focus {parameter}]"
    This format is machine-parseable and directly runnable. The leading slash is required.
    Correct:  "Resolve with: /discover-inertia --focus switching-cost"
    Wrong:    "Run discover-inertia to check switching cost"  (no leading slash -- not a token)
    Wrong:    "Investigate the switching-cost discrepancy"    (no action -- fails C-12, C-16)

  For ADVISORY rows (tension worth noting -- amend existing findings, do not rerun):
    Name a concrete change in prose. No token required, but "investigate further" fails.
    Example:  "Update discover-competitors inertia threat rating from MEDIUM to HIGH."
    Example:  "Amend discover-hypothesis adoption prediction to reflect NPS 4 result."

Cross-skill: Both skills in each row must be different discover skills. A row where Skill A and
Skill B are the same artifact (different versions) does not count as a cross-skill comparison.

--- VERDICT ---

Summary line first:
"Compared: {skill list} ({total} signals). Inertia contradictions: {A} ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

Readiness verdict -- match exactly to blocking count:
  M = 0   -> "Ready to specify."
  M >= 1  -> "Not ready to specify -- {M} blocking contradiction(s) must be resolved.
    See rows marked `blocking` above."

--- ARTIFACT ---

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter:
  topic: {topic}
  date: {date}
  signals_compared: [{skill-1}, {skill-2}, ...]
  inertia_blocking: {N}
  inertia_advisory: {N}
  other_blocking: {N}
  other_advisory: {N}
  verdict: ready | not-ready
```

---

## V-04: Minimized + inertia-motivated (Lifecycle + Inertia framing combined)

**Axes**: Lifecycle emphasis (6-phase collapse from V-01) + Inertia framing (motivational
explanation of WHY inertia renders first, not just that it does).

**Hypothesis**: V-01 tests whether the phase collapse maintains 130; V-03 tests whether
conversational register + table maintains 130. V-04 combines the minimization from V-01 with
the inertia motivation from V-03 (but not the full WHY-explanation register). The inertia
motivation is a single sentence explaining the causal relationship between inertia contradictions
and product strategy viability — placed in PHASE 2 (where the inertia flag is assigned) and
PHASE 4 (where the table renders). This adds 2 sentences to V-01. If V-04 = 130, it establishes
the inertia motivation as additive rather than substitutional. Predicted: 130/130.

```
You are running /discover-coherence for topic: {topic}.

=== PHASE 1: INVENTORY ===

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory:
| Skill | Date | Path |
|-------|------|------|

GATE: If fewer than 2 rows from 2 distinct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop here.

=== PHASE 2: SILENT SCAN (do not emit any output in this phase) ===

Read every file. For each factor that carries a rating (HIGH / MEDIUM / LOW), prediction
("likely", "unlikely", "expected to"), or scored finding, compare claims across skills.

For each factor where 2+ skills disagree, record internally:
  Factor; Skill A + exact claim; Skill B + exact claim
  Type: rating-conflict | prediction-conflict | evidence-conflict
  Severity: blocking (claims cannot both be true; decision depends on which is correct)
             advisory (tension worth noting; does not prevent specifying)
  Inertia flag: does this factor touch inertia threat level, switching cost, workaround
    quality, or adoption prediction? Inertia contradictions directly determine whether
    the product strategy is viable against the status quo -- they are the highest-priority
    category and render first regardless of count.

Do not emit any output in this phase.
Count: N total, M blocking, K advisory.
Count by type: R rating-conflict, P prediction-conflict, E evidence-conflict.

=== PHASE 3: FINDINGS HEADER ===

Output this block before any table:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

=== PHASE 4: REPORT ===

Two tables. Inertia contradictions render first -- they affect product strategy viability
directly, making them the highest-priority category. Render the Inertia table even if empty.

**Inertia Contradictions** (inertia / switching-cost / workaround-quality / adoption)

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

Column rules:

  Type: exactly `rating-conflict`, `prediction-conflict`, or `evidence-conflict`
  Severity: exactly `blocking` or `advisory`
  Claim A / Claim B: the specific conflicting statement in its own words

  Resolution:
    BLOCKING -- required token format:
      "Resolve with: /{skill-name} [--focus {parameter}]"
      Correct:  "Resolve with: /discover-inertia --focus switching-cost"
      Wrong:    "Run discover-inertia to check switching cost"  (no /token -- fails C-16)
      Wrong:    "Investigate the discrepancy"                   (vague -- fails C-12, C-16)

    ADVISORY -- concrete prose action:
      Name a field to update, claim to amend, or skill to run.
      Do not write "investigate further."

  Cross-skill: Both skills in each row must be different discover skills.

=== PHASE 5: VERDICT ===

"Compared: {skill list} ({total} signals). Inertia: {A} contradiction(s) ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

- M = 0   -> "Ready to specify."
- M >= 1  -> "Not ready to specify -- {M} blocking contradiction(s) must be resolved.
  See rows marked `blocking` above."

=== PHASE 6: ARTIFACT ===

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter:
  topic: {topic}
  date: {date}
  signals_compared: [{skill-1}, {skill-2}, ...]
  inertia_blocking: {N}
  inertia_advisory: {N}
  other_blocking: {N}
  other_advisory: {N}
  verdict: ready | not-ready
```

---

## V-05: Production candidate (All axes optimized)

**Axes**: All axes — lifecycle minimized (5 steps), phrasing concise, inertia-first with inline
motivation, token format with correct/wrong examples, table-structured output. The leanest prompt
in the series that addresses all 16 criteria. Built by taking V-04, merging verdict + artifact
into STEP 5, and tightening all column-rule prose.

**Hypothesis**: The R3-V-05 prompt achieves 130/130 but uses 7 phases and verbose column rules.
V-04 (6 phases) should also reach 130. This variation tests the floor: what is the minimum
well-formed prompt that scores 130? If V-05 achieves 130 at 5 steps, it becomes the recommended
production candidate — short enough to read in one pass, structured enough to enforce all criteria.
Predicted: 130/130.

```
You are running /discover-coherence for topic: {topic}.

Before you commit to a spec, surface every place your discover signals disagree. This skill
classifies each contradiction by type (what kind of disagreement), severity (does it block you),
and resolution (exactly what to run or amend to close it).

--- STEP 1: INVENTORY ---

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory:
| Skill | Date | Path |
|-------|------|------|

If fewer than 2 rows from 2 distinct skills:
  "GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop.

--- STEP 2: SILENT SCAN (read everything -- emit nothing) ---

Read every file. For each factor carrying a rating (HIGH/MEDIUM/LOW), prediction ("likely",
"unlikely", "expected to"), or scored finding, compare claims across skills.

For each factor where 2+ skills disagree, record:
  Factor; Skill A + exact claim; Skill B + exact claim
  Type:     rating-conflict | prediction-conflict | evidence-conflict
  Severity: blocking (cannot both be true; decision depends on which is right)
             advisory (tension worth noting; does not block specifying)
  Inertia:  does this factor touch inertia, switching cost, workaround quality, or
    adoption prediction? Inertia contradictions determine product strategy viability
    against the status quo -- they render first regardless of count.

Do not emit any output. Count N total, M blocking, K advisory; R/P/E by type.

--- STEP 3: TALLY HEADER (output before any table) ---

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

--- STEP 4: TABLES ---

Two tables. Inertia table renders first, even if empty.

**Inertia Contradictions** (inertia / switching-cost / workaround-quality / adoption)

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

Filling each column:

  Type: `rating-conflict` | `prediction-conflict` | `evidence-conflict` -- no other values

  Severity: `blocking` | `advisory` -- no other values

  Claim A / Claim B: the specific conflicting statement in its own words -- reader must see
    what each signal said without opening the source files

  Resolution:
    BLOCKING -- required token (machine-parseable, directly runnable):
      "Resolve with: /{skill-name} [--focus {parameter}]"
      Correct:  "Resolve with: /discover-inertia --focus switching-cost"
      Wrong:    "Run discover-inertia to check switching cost"  (no slash token -- fails C-16)
      Wrong:    "Investigate the discrepancy"                   (no action -- fails C-12)

    ADVISORY -- concrete prose action (no token required):
      Name a field to update, claim to amend, or skill to run.
      Example:  "Update discover-competitors inertia threat rating from MEDIUM to HIGH."
      Not acceptable: "investigate further"

  Cross-skill: Skill A and Skill B must be different discover skills.

--- STEP 5: VERDICT + ARTIFACT ---

Summary: "Compared: {skill list} ({total} signals). Inertia: {A} ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

Readiness:
  M = 0   -> "Ready to specify."
  M >= 1  -> "Not ready to specify -- {M} blocking contradiction(s) must be resolved.
    See rows marked `blocking` above."

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter:
  topic: {topic}
  date: {date}
  signals_compared: [{skill-1}, {skill-2}, ...]
  inertia_blocking: {N}
  inertia_advisory: {N}
  other_blocking: {N}
  other_advisory: {N}
  verdict: ready | not-ready
```

---

## Design notes

**Single-axis picks (V-01, V-02, V-03)**:

- V-01 isolates the phase-collapse question: does EXTRACT CLAIMS (Ph2) need to be a separate
  phase from COUNT + CLASSIFY (Ph3) in R3-V-05, or is a single silent scan sufficient? If V-01
  scores 130, the separation was redundant overhead. If it fails, the explicit claim-map step
  contributes something (perhaps structural scaffolding that keeps claims from being lost).

- V-02 is a deliberate diagnostic: it tests whether C-13's "Inertia Contradictions" requirement
  survives substitution with "Blocking Contradictions." The rubric text says "typically inertia
  contradictions" but the pass condition says "dedicated Inertia Contradictions section." If V-02
  scores 125 (C-13 fail), it confirms that the inertia-specific label is structurally required --
  not just the priority-first concept. This is the cleanest experimental test C-13 has had.

- V-03 tests whether conversational WHY-register + table apparatus reaches 130. R3 confirmed
  register parity at 115 (V-03 conversational = V-04 structural, both 115). Adding the table
  should close C-09/C-13/C-14 regardless of register. If V-03 = 130, the conversational format
  is a viable production candidate alongside V-05.

**Combination rationale (V-04, V-05)**:

- V-04 combines the 6-phase collapse (V-01) with the inertia motivation framing (V-03). This is
  the smallest prompt that adds motivational context without going to full conversational register.
  Tests whether motivation + minimization are independently additive.

- V-05 is the minimization target: 5 steps instead of 7 (verdict + artifact merged; extract
  claims merged into silent scan). If V-05 = 130, it becomes the recommended production candidate
  -- the leanest prompt in the series that addresses all 16 criteria with a single read-through.
