Written to `simulations/quest/variations/discover-coherence-variations-R2-2026-03-17.md`.

---

## Summary

5 complete variations for `discover-coherence` Round 2.

| # | Label | Axis | Target criteria |
|---|-------|------|-----------------|
| V-01 | Tally-first | C-06 only | Pre-scan step forces tally before contradiction #1 |
| V-02 | Taxonomy-defined | C-09 only | Vocabulary block with 3 conflict types defined before comparison |
| V-03 | Skill-token | C-10 only | Severity-split resolution rules; blocking requires `/skill-name [params]` |
| V-04 | Tally + taxonomy | C-06 + C-09 | FINDINGS HEADER with count AND per-type breakdown |
| V-05 | Full stack | C-06 + C-09 + C-10 + all aspirationals | All gaps closed on R1 V-05 base |

---

### Design rationale

**Three single-axis variations, one combination, one full stack** — same structure as R1.

**C-06 (V-01):** R1 analysis showed this is architecturally incompatible with single-pass generation. V-01 adds an explicit `STEP 2: PRE-SCAN` phase that instructs Claude to count contradictions before outputting any of them, then a `STEP 3: FINDINGS HEADER` that must appear before the first entry. Tests whether the mandatory counting step breaks the deferred-tally pattern.

**C-09 (V-02):** Zero passes in R1 because no variation defined the taxonomy before asking for it. V-02 places a `TYPE VOCABULARY` block with all three labels, definitions, and worked examples immediately after inventory — before any comparison work. The vocabulary is in working context exactly when it is needed.

**C-10 (V-03):** Zero passes because all R1 variations used a single resolution rule for both severities. Claude satisfied it for advisory (field-update language) but not for blocking (no skill reference). V-03 explicitly splits the rule: blocking entries require `"Resolve with: /skill-name [--focus param]"` token syntax; advisory entries require any concrete action. A blocking row with no `/` is visibly non-compliant.

**C-06 + C-09 (V-04):** Tests whether the two individual fixes are additive. The FINDINGS HEADER now shows counts AND the per-type breakdown (`{R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict`), satisfying C-06 while pre-loading the taxonomy the entries must match.

**Full stack (V-05):** Extends R1 V-05 (phases + GATE FAILED + dual inertia/other tables) with all three gap fixes. Adds a `PHASE 3: COUNT + CLASSIFY` step, `PHASE 4: FINDINGS HEADER`, a Type column to both tables, and severity-split resolution rules. Predicted score: **100** if all three gaps close cleanly.
showed that all single-pass variations defer the tally to the end because Claude outputs each contradiction as it finds it. An explicit counting step breaks that pattern.

```
You are running /discover-coherence for topic: {topic}.

STEP 1: INVENTORY

Find all discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory:
| Skill | Date | Path |
|-------|------|------|

GATE: If fewer than 2 rows from 2 distinct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run at least 2 discover skills before coherence check."
Stop here.

STEP 2: PRE-SCAN (do not output contradictions yet)

Read every file in the inventory. For each, extract all claims that carry a rating
(HIGH / MEDIUM / LOW), a prediction ("likely", "unlikely", "expected to"), or a scored
finding. Build an internal claim map: {factor -> {skill: claim}}.

For every factor that appears in 2+ skills, decide: do the claims agree or disagree?
Count them:
- Total contradictions found: N
- Blocking (signals cannot both be true; decision depends on which is correct): M
- Advisory (tension worth noting; does not prevent specifying): K

STEP 3: FINDINGS HEADER

Before writing any contradiction, output this block:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

STEP 4: CONTRADICTIONS

Now write each contradiction found in STEP 2. For every contradiction:

### Contradiction {n}: {short label}
Severity: blocking | advisory
{skill-A} ({date}): "{what signal A said, in its own words}"
{skill-B} ({date}): "{what signal B said, in its own words}"
Why it matters: {one sentence on the decision impact}
Resolution: {specific skill to run, field to update, or claim to amend -- not "investigate further"}

RULES:
- Severity must be exactly `blocking` or `advisory` -- no other values
- Each entry must show both conflicting claims with their specific wording
- Resolution must name a specific action -- not "investigate further"
- Each contradiction must span two DIFFERENT discover skills

STEP 5: VERDICT

"Ready to specify." if blocking count from STEP 2 is 0.
"Not ready to specify -- resolve {M} blocking contradiction(s) before specifying." otherwise.

STEP 6: ARTIFACT

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

## V-02: Taxonomy-defined (C-09 axis)

Axis: Taxonomy framing -- the three conflict types are defined as a named vocabulary block before any comparison work begins

Hypothesis: R1 produced zero C-09 passes across all 5 variations because no variation defined the three conflict types before asking Claude to apply them. Claude defaulted to prose descriptions or omitted type labels entirely. Placing a TYPE VOCABULARY block with definitions and examples immediately after inventory and before comparison forces the taxonomy into working context at the moment it is needed.

```
You are running /discover-coherence for topic: {topic}.

INVENTORY

Scan for all discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

List each file: | Skill | Date | Path |

Minimum 2 files from 2 distinct skills required. If not met:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop.

TYPE VOCABULARY

Every contradiction you find must be labeled with exactly one of these types:

- `rating-conflict`: two skills assign different ratings to the same factor
  Example: discover-competitors rates inertia threat MEDIUM; discover-inertia rates it HIGH
- `prediction-conflict`: one skill predicts an outcome the other contradicts
  Example: discover-hypothesis predicts 60% adoption; validate-customers finds NPS 4/10
- `evidence-conflict`: two evidence findings point in opposite directions
  Example: discover-websearch finds 3 active competitors; discover-analysis finds market "nascent"

Use exactly these labels -- no other values.

COMPARISON

Read all files. Extract claims with ratings, predictions, or scored findings.
Compare claims on the same factor across different skills.

For each disagreement, write:

### Contradiction {N}: {short label}
Type: rating-conflict | prediction-conflict | evidence-conflict
Severity: blocking | advisory
{skill-A} ({date}): "{the specific claim, in its own words}"
{skill-B} ({date}): "{the conflicting claim, in its own words}"
Why it matters: {one sentence}
Resolution: {specific skill to run, field to update, or claim to amend -- not "investigate further"}

RULES:
- Type: must use one of the three vocabulary labels above -- no other values
- Severity: exactly `blocking` or `advisory`
- Both claim sides must quote or directly paraphrase the specific wording from the artifact
- Resolution must name a concrete action -- not "investigate further"
- Cross-skill only: both skills must be different discover skills

CLOSING

"Compared: {skill-1}, {skill-2}, ... ({N} signals) -- {total} contradiction(s): {M} blocking, {K} advisory."

Verdict: "Ready to specify." (0 blocking) or "Not ready to specify -- resolve {M} blocking contradiction(s) before specifying."

ARTIFACT

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter: topic, date, signals_compared, blocking_count, advisory_count, verdict.
```

---

## V-03: Skill-token (C-10 axis)

Axis: Severity-split resolution rules -- blocking entries require a /skill-name [params] token; advisory entries require any concrete action

Hypothesis: R1 produced zero C-10 passes because all variations treated resolution as a single rule applying equally to blocking and advisory entries. Claude satisfied the rule for advisory entries with field-update language but failed to include skill references for blocking entries. Splitting the rule by severity -- and requiring a specific token syntax only for blocking -- creates a scannable compliance signal: if a blocking entry has no `/` in its resolution, the requirement is visibly unmet.

```
You are running /discover-coherence for topic: {topic}.

SETUP: Find all discover artifacts for this topic.
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md
- Print each file found: skill name, date, path.
- If fewer than 2 files from 2 distinct skills found:
  "GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
  Stop.

INVENTORY: Read every file. Pull out all claims that carry a rating (HIGH / MEDIUM / LOW),
a prediction, or a scored finding.

COHERENCE CHECK: For each factor that appears in claims from 2+ different skills,
check whether those claims agree. Write an entry for each disagreement.

### Contradiction {N}: {short label}
Severity: blocking | advisory
{skill-A} ({date}): "{what it said, in its own words}"
{skill-B} ({date}): "{what it said, in its own words}"
Resolution: {see resolution rules below}

RESOLUTION RULES -- read these before writing any entry:

For BLOCKING contradictions:
  The resolution MUST include a named skill reference in the form:
  "Resolve with: /{skill-name} [--focus {parameter}]"
  Example: "Resolve with: /discover-inertia --focus switching-cost"
  A resolution without a /skill-name token fails this requirement.
  Do NOT write "investigate further" -- name a specific skill.

For ADVISORY contradictions:
  The resolution must name a concrete action: a field to update, a claim to amend,
  or a skill to run. Generic guidance without a named action fails.
  "Investigate further" alone fails.

CROSS-SKILL RULE: Both skills in a contradiction must be different discover skills.
Do not flag version-date differences within the same skill.

SEVERITY RULES:
- blocking: the two claims cannot both be true and the decision depends on which is correct
- advisory: worth noting but does not block specifying

CLOSING:
"Compared: {skills}. {N} contradiction(s): {M} blocking, {K} advisory."
Verdict: "Ready to specify." (0 blocking) or "Not ready to specify -- resolve {M}
blocking contradiction(s) before specifying."

ARTIFACT: Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter: topic, date, signals_compared, blocking_count, advisory_count, verdict.
```

---

## V-04: Tally + taxonomy (C-06 + C-09 combined)

Axes: Tally positioning (C-06) + taxonomy vocabulary (C-09) -- a FINDINGS HEADER block that shows counts AND per-type breakdown before the first contradiction entry

Hypothesis: Combining the two individual gap fixes into a single FINDINGS HEADER that includes both the total/blocking/advisory count AND a per-type breakdown tests whether the two criteria are additive. A header like "COHERENCE FINDINGS: 3 contradictions -- 2 blocking, 1 advisory | by type: 1 rating-conflict, 1 prediction-conflict, 1 evidence-conflict" satisfies C-06 and creates a type-reference the subsequent entries must match.

```
You are running /discover-coherence for topic: {topic}.

=== PHASE 1: INVENTORY ===

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory:
| Skill | Date | Path |
|-------|------|------|

GATE: Fewer than 2 rows from 2 distinct skills?
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop.

=== PHASE 2: EXTRACT + COUNT ===

Read every file. For each skill, extract all claims with a rating (HIGH/MEDIUM/LOW),
prediction, or scored finding. Build an internal claim map.

For every factor that appears in 2+ skills, compare claims:
- Agree? Skip.
- Disagree? Record a contradiction.

For each contradiction, classify it internally using exactly one type:
- `rating-conflict`: different ratings on the same factor
- `prediction-conflict`: one predicts an outcome the other contradicts
- `evidence-conflict`: two evidence findings point in opposite directions

Count: total contradictions N, blocking M, advisory K.
Count by type: rating-conflict R, prediction-conflict P, evidence-conflict E.

=== PHASE 3: FINDINGS HEADER ===

Before writing any contradiction, output:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

=== PHASE 4: CONTRADICTIONS ===

For each contradiction identified in PHASE 2:

### Contradiction {n}: {short label}
Type: rating-conflict | prediction-conflict | evidence-conflict
Severity: blocking | advisory
{skill-A} ({date}): "{the specific claim, in its own words}"
{skill-B} ({date}): "{the conflicting claim, in its own words}"
Why it matters: {one sentence}
Resolution: {specific skill to run, field to update, or claim to amend -- not "investigate further"}

RULES:
- Type: must be one of the three values above
- Severity: exactly `blocking` or `advisory`
- Both claim sides must show the specific wording from the source artifact
- Resolution: concrete named action -- not "investigate further"
- Cross-skill: both skills must be different discover skills

=== PHASE 5: VERDICT ===

"Ready to specify." if M = 0.
"Not ready to specify -- resolve {M} blocking contradiction(s) before specifying." otherwise.

=== PHASE 6: ARTIFACT ===

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter:
  topic: {topic}
  date: {date}
  signals_compared: [{skill-1}, ...]
  blocking_count: {M}
  advisory_count: {K}
  verdict: ready | not-ready
```

---

## V-05: Full stack (C-06 + C-09 + C-10 + all aspirationals on V-05 base)

Axes: All three R1 gaps closed + all aspirational criteria from v2 rubric, built on the R1 V-05 phase/gate structure

Hypothesis: Adding the three gap fixes (C-06 tally at top, C-09 taxonomy column, C-10 skill-per-blocking token) to the already-highest-scoring R1 V-05 structure should close the remaining 20 pts and reach 100. The table format hosts the Type column naturally (extending the existing table). The FINDINGS HEADER phase is inserted between EXTRACT and REPORT. The resolution column rule is split by severity. All 14 criteria from the v2 rubric are addressed.

```
You are running /discover-coherence for topic: {topic}.

=== PHASE 1: INVENTORY ===

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory table:
| Skill | Date | Path |
|-------|------|------|

GATE: If the table has fewer than 2 rows from 2 distinct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop here.

=== PHASE 2: EXTRACT CLAIMS ===

Read every file in the inventory. For each skill, extract all claims that are:
- A rating: HIGH / MEDIUM / LOW on any factor
- A prediction: "likely", "unlikely", "expected to"
- A scored finding: any numeric or scale-based assessment

Build an internal claim map: {factor -> {skill: claim}}.

=== PHASE 3: COUNT + CLASSIFY (do not output contradictions yet) ===

For every factor that appears in 2+ skills, compare claims. For each disagreement,
classify it using exactly one type:
- `rating-conflict`: two skills assign different ratings to the same factor
- `prediction-conflict`: one skill predicts an outcome the other contradicts
- `evidence-conflict`: two evidence findings point in opposite directions

Count: total N, blocking M, advisory K.
Count by type: rating-conflict R, prediction-conflict P, evidence-conflict E.

INERTIA PRIORITY RULE: All contradictions involving inertia-related factors (threat
level, switching cost, workaround quality, adoption prediction) are placed in the
Inertia table regardless of when they are found.

=== PHASE 4: FINDINGS HEADER ===

Before writing any contradiction table, output:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

=== PHASE 5: REPORT ===

Output two tables. The Inertia table renders first -- even if empty.

**Inertia Contradictions** (status-quo / switching-cost factors -- always rendered first)

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

Column rules:
- Type: exactly `rating-conflict`, `prediction-conflict`, or `evidence-conflict`
- Severity: exactly `blocking` or `advisory`
- Claim A / Claim B: the specific conflicting statement in its own words -- not just the topic
- Resolution by severity:
  - BLOCKING: "Resolve with: /{skill-name} [--focus {parameter}]" -- must name a specific
    discover skill. Do NOT write "investigate further."
  - ADVISORY: a concrete action -- a field to update, a claim to amend, or a skill to run.
    Do NOT write "investigate further."

Cross-skill rule: Both skills in each row must be different discover skills.

=== PHASE 6: VERDICT ===

Summary line:
"Compared: {skill list} ({N} signals). Inertia contradictions: {A} ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

Verdict:
- 0 blocking -> "Ready to specify."
- 1+ blocking -> "Not ready to specify -- {M} blocking contradiction(s) must be
  resolved. See rows marked `blocking` above."

=== PHASE 7: ARTIFACT ===

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
