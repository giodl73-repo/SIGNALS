Written to `simulations/quest/variations/discover-coherence-variations-R1-2026-03-17.md`.

---

## Summary

5 variations for `discover-coherence`, covering 4 axes:

| # | Label | Axis | Hypothesis |
|---|-------|------|------------|
| V-01 | Baseline | Baseline prose | Structured prose with `Signal A says / Signal B says` headers is the safest default for C-02 |
| V-02 | Table format | Output format | Table columns structurally enforce C-03 (severity) and C-04 (resolution) — harder to omit |
| V-03 | Inertia-first | Inertia framing | Elevating inertia contradictions to their own section keeps the most important disagreements from being buried |
| V-04 | Conversational | Phrasing register | Plain-language framing reduces ambiguity about what "contradiction" means; quoted-claims requirement is more explicit |
| V-05 | Combined | Table + inertia-first + lifecycle phases | Gate-enforced phases structurally prevent skipping C-01 (inventory check) and C-07 (verdict); table enforces C-02/C-03/C-04 |

**Key design tensions being tested:**
- V-02 vs V-01: Does table format over-constrain the output or does it reduce omission errors?
- V-03 vs V-01: Does inertia-first ordering improve actionability or just add complexity for topics with no inertia signal?
- V-04 vs V-01: Does conversational phrasing help Claude understand "side-by-side quoted claims" better than formal headers?
- V-05: Does the phase/gate structure pay for its verbosity, or does it over-specify a simple comparison task?
, and scored findings that could conflict with findings from other skills.

COHERENCE CHECK: Compare every claim that appears in more than one signal.
For each contradiction found, write an entry in this format:

### Contradiction N: {short label}
Severity: blocking | advisory
Signal A ({skill-name}, {date}): "{exact quote or close paraphrase of the claim}"
Signal B ({skill-name}, {date}): "{exact quote or close paraphrase of the conflicting claim}"
Why it matters: {one sentence on the decision impact}
Resolution: {specific action -- name a skill to run, a field to update, or a claim to amend}

SEVERITY RULES:
- blocking: the two signals cannot both be true and the decision depends on which is correct
- advisory: worth noting but does not prevent specifying

CROSS-SKILL RULE: Every contradiction must involve claims from two DIFFERENT discover skills.
Do not report version-date differences within the same skill as contradictions.

CLOSING: After all contradictions, write:
"Compared: {list of skill names} -- {N} contradiction(s) found: {M} blocking, {K} advisory."
Then: "Ready to specify." if blocking count is 0, else "Not ready to specify -- resolve
{N} blocking contradiction(s) first."

Write artifact to simulations/discover/coherence/{topic}-coherence-{date}.md with frontmatter:
  topic, date, signals_compared (list), blocking_count, advisory_count, verdict.
```

---

## V-02: Table format (output format axis)

Axis: Output format -- contradiction matrix table instead of per-entry prose blocks

Hypothesis: A table with one row per contradiction makes severity visible at a glance and
makes it harder to accidentally omit the severity or resolution columns (C-03, C-04).

```
You are running /discover-coherence for topic: {topic}.

SETUP: Find all discover artifacts for this topic.
- Glob: simulations/discover/**/{topic}-*-*.md and simulations/scout/**/{topic}-*-*.md
- List each file found: | skill | date | path |
- Minimum 2 distinct skill files required. If not met: "Fewer than 2 discover signals
  found. Run at least 2 discover skills before coherence check." Stop.

INVENTORY: Read each file. Pull out every claim that carries a rating, prediction, or
scored finding. Build an internal comparison matrix: which claims overlap across skills?

CONTRADICTION TABLE: For each pair of conflicting claims across different skills, add
one row to a markdown table:

| # | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|----------|----------------|---------|----------------|---------|------------|

Column rules:
- Severity: exactly `blocking` or `advisory` -- no other values
- Claim A / Claim B: the specific conflicting statement (quoted or close paraphrase)
- Resolution: a concrete next action -- name the skill to run or the field to amend

If no contradictions are found, write an empty table with header row and note:
"No contradictions found across {N} signals."

COMPARISON SUMMARY: Below the table, one line:
"Compared: {skill-1}, {skill-2}, ... ({N} signals) -- {M} blocking, {K} advisory."

VERDICT: "Ready to specify." if blocking = 0, else "Not ready to specify -- {M}
blocking contradiction(s) must be resolved before specifying."

Write artifact: simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter: topic, date, signals_compared, blocking_count, advisory_count, verdict.
```

---

## V-03: Inertia-first framing

Axis: Inertia framing -- contradictions involving discover-inertia or the status-quo
competitor are surfaced first, before other contradictions

Hypothesis: Since inertia is the primary competitor in Signal's philosophy, placing
inertia-related contradictions first focuses attention on the most decision-critical
disagreements and avoids burying blocking inertia conflicts in the middle of the report.

```
You are running /discover-coherence for topic: {topic}.

SIGNAL PHILOSOPHY NOTE: In Signal, the status-quo / inertia competitor is always the
primary competitor. Any contradiction involving inertia ratings or switching-cost
findings is automatically elevated -- these are listed FIRST, regardless of other
severity. If discover-competitors rates inertia MEDIUM but discover-inertia rates it
HIGH, that is a blocking contradiction by definition.

SETUP: Scan for all discover artifacts for this topic.
- Glob: simulations/discover/**/{topic}-*-*.md and simulations/scout/**/{topic}-*-*.md
- Print inventory: each file's skill name and date.
- If fewer than 2 distinct skill files found: "Fewer than 2 signals found. Coherence
  check requires 2+ discover artifacts." Stop.

EXECUTION SEQUENCE:
1. Read all artifacts. Extract key claims per skill.
2. Identify inertia-related claims in every artifact (threat level, switching cost,
   workaround viability, adoption prediction). Compare these across skills first.
3. Then compare remaining claims across skills (ratings, predictions, evidence findings).

OUTPUT STRUCTURE:

## Inertia-Related Contradictions
(List first -- these are the most important. Use the same entry format as below.)

## Other Contradictions
(All non-inertia contradictions in any order.)

Per-entry format:
### Contradiction N: {label}
Severity: blocking | advisory
{skill-A} ({date}): "{claim from A}"
{skill-B} ({date}): "{claim from B}"
Resolution: {specific action}

CROSS-SKILL RULE: Each contradiction must span two different discover skills.

CLOSING:
"Compared: {skills}. Inertia contradictions: {N} ({M} blocking). Other contradictions:
{K} ({J} blocking). Total: {T} blocking, {U} advisory."
Verdict: "Ready to specify." (0 blocking) or "Not ready to specify -- resolve {T}
blocking contradiction(s) before specifying."

Artifact: simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter: topic, date, signals_compared, inertia_contradictions, other_contradictions,
blocking_count, advisory_count, verdict.
```

---

## V-04: Conversational register (phrasing axis)

Axis: Phrasing register -- plain conversational language, direct "you" framing,
avoid bureaucratic section headers

Hypothesis: Plain-language instructions reduce ambiguity about what counts as a
contradiction and make the skill easier to execute correctly on first run -- particularly
for C-02 (the quoted claims requirement) which formal phrasing tends to obscure.

```
You are running /discover-coherence for topic: {topic}.

Your job is to find places where your discover signals disagree with each other.

First, find all the discover files for this topic:
- Glob simulations/discover/**/{topic}-*-*.md and simulations/scout/**/{topic}-*-*.md
- List every file you find and which skill produced it.
- You need at least 2 files from 2 different skills. If you don't have that, say:
  "Not enough signals yet -- found only {N} from {skill-names}. Run more discover
  skills and come back." Then stop.

Read each file. For each one, pull out the claims that have a score, rating, or
prediction attached -- things like "inertia threat: HIGH" or "adoption likely" or
"switching cost: 3 weeks." These are the claims that might contradict each other.

Now look for places where two different skills say different things about the same thing.
When you find one, write it up like this:

**Contradiction {N}: {short label}** | {blocking or advisory}

- {skill-A} on {date}: "{what it said, in its own words}"
- {skill-B} on {date}: "{what it said, in its own words}"
- Why this matters: {one sentence}
- Fix it by: {name the specific thing to do -- run a skill, update a field, amend a claim}

Only use `blocking` or `advisory` -- nothing else. Blocking means you can't spec this
until you resolve it. Advisory means you can spec it but should note the tension.

Only compare claims across different skills. Don't flag a skill disagreeing with itself.

When you're done, write one line like:
"Checked: discover-X, discover-Y, discover-Z. Found {N} contradiction(s): {M} blocking,
{K} advisory."

Then the verdict: "Good to spec." (zero blocking) or "Don't spec yet -- {M} blocking
issue(s) to resolve first."

Write the report to simulations/discover/coherence/{topic}-coherence-{date}.md.
Frontmatter: topic, date, signals_compared, blocking_count, advisory_count, verdict.
```

---

## V-05: Combined (table format + inertia-first + explicit lifecycle phases)

Axes: Output format (table) + inertia framing (elevated first) + lifecycle emphasis
(explicit phase boundaries with gates)

Hypothesis: Combining table format with inertia-first ordering and named lifecycle
phases (INVENTORY -> COMPARE -> REPORT -> GATE) produces the most rubric-complete output
because the table enforces C-02/C-03/C-04 structurally, inertia-first enforces C-05
cross-skill relevance, and explicit gates enforce C-01 (minimum signal check) and
C-07 (verdict).

```
You are running /discover-coherence for topic: {topic}.

=== PHASE 1: INVENTORY ===

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory table:
| Skill | Date | Path |
|-------|------|------|

GATE: If the table has fewer than 2 rows from 2 distinct skills, output:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop here.

=== PHASE 2: EXTRACT CLAIMS ===

Read every file in the inventory. For each skill, extract all claims that are:
- A rating: HIGH / MEDIUM / LOW on any factor
- A prediction: "likely", "unlikely", "expected to"
- A scored finding: any numeric or scale-based assessment

Build a claim map internally: {factor -> {skill: claim}}.

=== PHASE 3: COMPARE ===

For every factor that appears in 2+ skills, check whether the claims agree.
Disagreements become contradiction rows.

INERTIA PRIORITY RULE: Process all inertia-related factors first (threat level,
switching cost, workaround quality, adoption prediction). These appear in the first
section of the report regardless of when they are found.

=== PHASE 4: REPORT ===

Output two tables:

**Inertia Contradictions** (always first, even if empty)

| # | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|----------|----------------|---------|----------------|---------|------------|

Column rules:
- Severity: exactly `blocking` or `advisory`
- Claim A / Claim B: quoted or directly paraphrased -- the actual words, not just the topic
- Resolution: specific skill to run, field to update, or claim to amend -- not "investigate further"

Cross-skill rule: Both skills in a row must be different discover skills.

=== PHASE 5: GATE + VERDICT ===

Summary line:
"Compared: {skill list} ({N} signals). Inertia contradictions: {A} ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

Verdict:
- 0 blocking -> "Ready to specify."
- 1+ blocking -> "Not ready to specify -- {N} blocking contradiction(s) must be
  resolved. See rows marked `blocking` above."

=== PHASE 6: ARTIFACT ===

Write to simulations/discover/coherence/{topic}-coherence-{date}.md.
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
