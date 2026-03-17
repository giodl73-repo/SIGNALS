Written to `simulations/quest/variations/discover-coherence-variations-R3-2026-03-17.md`.

---

## discover-coherence R3 — 5 variations

| # | Label | Axis | Primary targets | Key mechanism |
|---|-------|------|----------------|---------------|
| V-01 | Silent-scan | Lifecycle emphasis | C-15 only | Named PRE-SCAN phase + explicit "do not output" instruction |
| V-02 | Token-enforced | Output format | C-16 only | Severity-split rules + two wrong-example lines for BLOCKING |
| V-03 | Conversational | Phrasing register | C-04, C-12, C-16 | Explains WHY each constraint exists; embeds failure-mode negation in prose |
| V-04 | Two-phase + token | Lifecycle + format combined | C-15 + C-16 | Minimal base combining both new criteria |
| V-05 | Full stack 130 | All 16 criteria on R2 V-05 base | All criteria | Adds "do not output" silence + wrong-example negation to R2 V-05 |

---

**What's new in R3 vs R2:**

The two new criteria are C-15 (two-phase scan silence) and C-16 (token syntax for blocking resolutions). R2 V-01 already had the phase structure but lacked the explicit silence instruction; R2 V-03 had token syntax but no phase separation. R3 tests whether each mechanism is sufficient alone, whether register affects compliance, and whether the minimal combination closes both before going to full stack.

**Predicted scoring against v3 rubric (130 max, golden >= 95):**
- V-01: ~105 (C-15 pass, C-16 fail — no token; C-09, C-13, C-14 fail — no table)
- V-02: ~110 (C-16 pass, C-15 likely fail — single-pass; C-09, C-13, C-14 fail)
- V-03: ~105–115 (C-15 borderline, C-16 borderline; depends on register effect)
- V-04: ~115–120 (C-15 + C-16 pass; C-09, C-13, C-14 still fail — no table/taxonomy)
- V-05: ~130 (all criteria addressed explicitly)
inct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop here.

STEP 2: PRE-SCAN (do not output any contradiction in this step)

Read every file in the inventory. For each skill, extract all claims that carry:
- A rating: HIGH / MEDIUM / LOW on any named factor
- A prediction: "likely", "unlikely", "expected to", "will", "won't"
- A scored finding: any numeric or scale assessment

For every factor that appears in claims from 2+ different skills, compare:
- Claims agree? Skip.
- Claims disagree? Record internally: factor, skill A + claim, skill B + claim, severity.

Severity definitions:
- blocking: the two claims cannot both be true; the decision depends on which is correct
- advisory: a tension worth noting; does not prevent specifying

Count all contradictions before moving to the next step.
N = total, M = blocking, K = advisory.

You now have N, M, K. Do not write any contradiction entry yet. Move to STEP 3.

STEP 3: FINDINGS HEADER (output this before any contradiction entry)

Output this block first, then write the contradiction entries:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

STEP 4: CONTRADICTION ENTRIES

Now write each contradiction found in STEP 2:

### Contradiction {n}: {short label}
Severity: blocking | advisory
{skill-A} ({date}): "{what signal A said, in its own words}"
{skill-B} ({date}): "{what signal B said, in its own words}"
Why it matters: {one sentence on the decision impact}
Resolution: {specific skill to run, field to update, or claim to amend -- not "investigate further"}

Rules:
- Severity: exactly `blocking` or `advisory` -- no other values
- Both sides: show the specific conflicting wording from the source artifact
- Resolution: name a concrete action -- not "investigate further"
- Cross-skill: both skills must be different discover skills

STEP 5: VERDICT

"Ready to specify." if M = 0.
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

## V-02: Token-enforced (C-16 axis)

**Axis**: Output format — BLOCKING resolutions require exact `/skill-name [--focus param]`
token syntax; ADVISORY resolutions require concrete prose; both formats are enforced with
worked examples and explicit failure negation

**Hypothesis**: R1 and R2 showed that a single resolution rule for both severities allows
Claude to satisfy advisory entries with field-update language while slipping blocking entries
into vague prose ("Run the inertia skill" rather than "/discover-inertia --focus switching-cost").
C-16 requires not only a skill reference but a specific machine-parseable token format.
V-02 enforces this by: (1) naming the format as a structural rule, (2) showing a correct
and two incorrect examples for BLOCKING, (3) explicitly forbidding "investigate further"
for both severities. Tests whether worked-example + negation produces reliable token
compliance without requiring the full two-phase scan structure.

```
You are running /discover-coherence for topic: {topic}.

SETUP

Find all discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print each file found: skill name, date, path.

If fewer than 2 files from 2 distinct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop.

INVENTORY

Read every file. For each skill, extract all claims with a rating (HIGH/MEDIUM/LOW),
prediction, or scored finding.

COHERENCE CHECK

For each factor that appears in claims from 2+ different skills, check whether the claims
agree. Write an entry for each disagreement.

### Contradiction {N}: {short label}
Severity: blocking | advisory
{skill-A} ({date}): "{what it said, in its own words}"
{skill-B} ({date}): "{what it said, in its own words}"
Why it matters: {one sentence}
Resolution: {see RESOLUTION FORMAT RULES below}

RESOLUTION FORMAT RULES

Read these rules before writing any entry.

BLOCKING contradictions: the resolution MUST use this exact token format:
  Resolve with: /{skill-name} [--focus {parameter}]

  Correct:   "Resolve with: /discover-inertia --focus switching-cost"
  Wrong:     "Run discover-inertia to check switching cost"  (no /token)
  Wrong:     "Investigate the switching-cost discrepancy"    (no action, no token)

  The leading slash and skill name are required. Anything else fails this requirement.

ADVISORY contradictions: the resolution must name a concrete action in prose:
  - A field to update: "Update discover-competitors threat rating from MEDIUM to HIGH."
  - A claim to amend: "Amend discover-hypothesis adoption prediction to reflect NPS 4 result."
  - A skill to run: "Run discover-analysis --focus market-size" (prose form acceptable).
  Do not write "investigate further" -- name the specific change needed.

SEVERITY DEFINITIONS
- blocking: the two claims cannot both be true; the decision depends on which is correct
- advisory: worth noting but does not prevent specifying

CROSS-SKILL RULE: Both skills in each contradiction must be different discover skills.

CLOSING

"Compared: {skill list}. {N} contradiction(s): {M} blocking, {K} advisory."
Verdict: "Ready to specify." (0 blocking) or
         "Not ready to specify -- resolve {M} blocking contradiction(s) before specifying."

ARTIFACT

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter: topic, date, signals_compared, blocking_count, advisory_count, verdict.
```

---

## V-03: Conversational (phrasing register axis)

**Axis**: Phrasing register — explanatory / conversational framing that states the WHY
behind each structural requirement, rather than issuing bare imperatives

**Hypothesis**: Formal imperative prompts ("STEP 2: PRE-SCAN -- do not output") rely on
rule compliance. A conversational register that explains the purpose of each constraint
("you can't report the tally accurately if you haven't read all signals yet, so count
everything before outputting") engages the model's reasoning rather than its instruction-
following. This may improve yield on C-04, C-12, and C-16 because the model understands
why vague resolutions and prose skill references are insufficient, not just that they are.
Tests whether register alone shifts compliance without adding structural mechanisms.

```
You are running /discover-coherence for topic: {topic}.

The goal here is to surface contradictions between your discover signals before you commit
to a spec. If discover-competitors rated inertia MEDIUM but discover-inertia found switching
cost HIGH, those two signals disagree -- and that disagreement could derail your feature if
left unresolved. This skill finds those conflicts, tells you which ones block you from
specifying, and gives you exact next steps to resolve each one.

--- FIND YOUR SIGNALS ---

Start by locating all discover artifacts for this topic:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Show the inventory as a table: | Skill | Date | Path |

You need at least 2 artifacts from at least 2 different discover skills to run a meaningful
coherence check. With only one signal there is nothing to compare. If you don't have 2+:
  "GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop -- you cannot produce a coherence report from a single signal.

--- COUNT EVERYTHING BEFORE YOU OUTPUT ---

Before writing any contradiction entry, read all files and complete your count. This matters
because the tally in your header ("N contradictions: M blocking, K advisory") must cover
the full set -- if you output entries as you scan, the tally at the top will be wrong.

Read every file. For each skill, pull out claims with a rating (HIGH/MEDIUM/LOW), a
prediction, or a scored finding. For every factor present in 2+ skills, ask: do the claims
agree? If not, record it privately:
- blocking: the two claims can't both be true; the right answer changes the decision
- advisory: worth flagging but doesn't prevent specifying

Count N (total), M (blocking), K (advisory). Don't output yet.

--- OPEN WITH THE TALLY ---

Your report must open with this tally before any contradiction entry:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

--- ONE ENTRY PER CONTRADICTION ---

For each contradiction, write:

### Contradiction {n}: {short label}
Severity: blocking | advisory
{skill-A} ({date}): "{exact quote or close paraphrase of what this signal said}"
{skill-B} ({date}): "{exact quote or close paraphrase of what this signal said}"
Why it matters: {one sentence -- why does this disagreement affect the feature decision?}
Resolution: {what must happen to resolve this?}

Resolution guidance:
  "Investigate further" is not a resolution -- it doesn't tell anyone what to do.
  For BLOCKING contradictions, name the exact skill invocation:
    "Resolve with: /discover-inertia --focus switching-cost"
    The /skill-name token is required -- prose like "run the inertia skill" doesn't count.
  For ADVISORY contradictions, name the specific change:
    "Update discover-competitors inertia threat rating from MEDIUM to HIGH."
    Or: "Amend discover-hypothesis adoption prediction to reflect the NPS 4 finding."

Both signals in a contradiction must be from different discover skills. Severity must be
exactly `blocking` or `advisory` -- no other labels.

--- VERDICT ---

Close with a readiness statement that matches your blocking count:
  M = 0: "Ready to specify."
  M >= 1: "Not ready to specify -- resolve {M} blocking contradiction(s) before specifying."

--- ARTIFACT ---

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

## V-04: Two-phase + token (C-15 + C-16 combined, minimal base)

**Axes**: Lifecycle emphasis (C-15) + output format (C-16) — both new criteria from v3
rubric, combined in the smallest prompt that addresses them cleanly, without the full
table/taxonomy/inertia-priority apparatus of V-05

**Hypothesis**: C-15 and C-16 are orthogonal: C-15 governs when output is emitted (scan
first, emit after); C-16 governs how blocking resolutions are formatted (token syntax).
A minimal prompt that adds only these two structural rules to the solid R2 V-03 base should
score 110-120/130 — covering all essential + recommended criteria plus C-11, C-12, C-15,
C-16 from aspirational. Establishes a clean two-criterion combination before the full stack.

```
You are running /discover-coherence for topic: {topic}.

=== PHASE 1: INVENTORY ===

Glob for all discover artifacts:
- simulations/discover/**/{topic}-*-*.md
- simulations/scout/**/{topic}-*-*.md

Print the inventory:
| Skill | Date | Path |
|-------|------|------|

GATE: If fewer than 2 rows from 2 distinct skills:
"GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop.

=== PHASE 2: PRE-SCAN (no output in this phase) ===

Read every file. For each skill, extract claims with a rating (HIGH/MEDIUM/LOW),
prediction ("likely", "unlikely", "expected to"), or scored finding.

For every factor present in claims from 2+ skills, compare. For each disagreement, record:
- Factor name
- Skill A, exact claim; Skill B, exact claim
- Severity: blocking (claims cannot both be true; decision depends on which is correct)
            advisory (tension worth noting; does not prevent specifying)

Do not output any contradiction in this phase. Count: N total, M blocking, K advisory.

=== PHASE 3: FINDINGS HEADER ===

Output this block before writing any contradiction entry:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

=== PHASE 4: CONTRADICTION ENTRIES ===

For each contradiction from PHASE 2:

### Contradiction {n}: {short label}
Severity: blocking | advisory
{skill-A} ({date}): "{the specific claim in its own words}"
{skill-B} ({date}): "{the conflicting claim in its own words}"
Why it matters: {one sentence}
Resolution: {see RESOLUTION RULES below}

RESOLUTION RULES:

  BLOCKING: Required token format:
    "Resolve with: /{skill-name} [--focus {parameter}]"
    Example: "Resolve with: /discover-inertia --focus switching-cost"
    A blocking entry without the /skill-name token fails. Do not write "investigate further."

  ADVISORY: Required concrete action (prose):
    Name a specific field to update, claim to amend, or skill to run.
    Example: "Update discover-competitors inertia threat rating from MEDIUM to HIGH."
    Do not write "investigate further."

Cross-skill rule: Both skills in each contradiction must be different discover skills.
Severity rule: Exactly `blocking` or `advisory` -- no other values.

=== PHASE 5: VERDICT ===

"Ready to specify." if M = 0.
"Not ready to specify -- resolve {M} blocking contradiction(s) before specifying." otherwise.

=== PHASE 6: ARTIFACT ===

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

## V-05: Full stack 130 (all criteria on R2 V-05 base)

**Axes**: All 16 criteria from v3 rubric — C-15 (two-phase scan) and C-16 (severity-split
token syntax) added explicitly to the R2 V-05 base that already addressed C-09, C-10,
C-11, C-12, C-13, C-14

**Hypothesis**: R2 V-05 scored 120/120 on the v2 rubric. The v3 rubric adds C-15 (5 pts)
and C-16 (5 pts). R2 V-05 already has a COUNT + CLASSIFY phase (satisfies C-15) and
severity-split resolution with `/skill-name [--focus param]` token (satisfies C-16).
However, C-15 in v3 requires the phase to be explicitly labeled "do not output" during
scanning, and C-16 requires the token format to be stated as a structural rule with
failure-mode negation. V-05 makes both requirements explicit. Predicted score: 130/130.

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

For every factor that appears in 2+ skills, compare claims. For each disagreement, classify:

Type (exactly one):
- `rating-conflict`: two skills assign different ratings to the same factor
- `prediction-conflict`: one skill predicts an outcome the other contradicts
- `evidence-conflict`: two evidence findings point in opposite directions

Severity (exactly one):
- `blocking`: the two claims cannot both be true; the decision depends on which is correct
- `advisory`: tension worth noting; does not prevent specifying

Inertia priority: contradictions involving inertia-related factors (threat level, switching
cost, workaround quality, adoption prediction) are flagged for the Inertia table.

Count: N total, M blocking, K advisory.
Count by type: R rating-conflict, P prediction-conflict, E evidence-conflict.

Do not output any contradiction entry during this phase. Proceed to PHASE 4 with counts ready.

=== PHASE 4: FINDINGS HEADER ===

Before writing any contradiction table, output:

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

=== PHASE 5: REPORT ===

Output two tables. The Inertia table renders first -- render it even if empty.

**Inertia Contradictions** (inertia / switching-cost / adoption factors -- always first)

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

Column rules:

Type: exactly `rating-conflict`, `prediction-conflict`, or `evidence-conflict`

Severity: exactly `blocking` or `advisory`

Claim A / Claim B: the specific conflicting statement in its own words, not just the topic

Resolution by severity -- read before filling any cell:

  BLOCKING: required token format:
    "Resolve with: /{skill-name} [--focus {parameter}]"
    Correct:  "Resolve with: /discover-inertia --focus switching-cost"
    Wrong:    "Run discover-inertia to check switching cost"  (no /token -- fails C-16)
    Wrong:    "Investigate the inertia discrepancy"           (vague -- fails C-12, C-16)
    The /skill-name token is required. A blocking cell without it fails.

  ADVISORY: concrete action in prose:
    Name a specific field to update, claim to amend, or skill to run.
    Example: "Update discover-competitors threat rating for inertia from MEDIUM to HIGH."
    Do not write "investigate further" -- name the specific change needed.

Cross-skill rule: Both skills in each row must be different discover skills.

=== PHASE 6: VERDICT ===

Summary line:
"Compared: {skill list} ({total} signals). Inertia contradictions: {A} ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

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
  inertia_blocking: {N}
  inertia_advisory: {N}
  other_blocking: {N}
  other_advisory: {N}
  verdict: ready | not-ready
```

---

## Design notes

**Single-axis picks (V-01, V-02, V-03)**:

- V-01 isolates C-15 with the minimal change: name STEP 2 PRE-SCAN and add "do not output any contradiction in this step." No taxonomy, no table, no token rules. Tests whether the phase label + silence instruction alone closes C-15.

- V-02 isolates C-16 with worked examples and explicit failure negation. The key addition over R2 V-03: two wrong-example lines ("no /token", "no action") make the failure mode concrete rather than abstract. Tests whether failure-mode negation at the per-rule level (not just in the resolution text) produces token compliance.

- V-03 tests phrasing register: does explaining WHY each constraint exists produce better compliance than stating WHAT to do? Specifically, the resolution guidance explains that "Resolve with: /discover-inertia" counts but "run the inertia skill" does not, and explains the reasoning. If phrasing register matters, V-03 should outperform V-01 on C-04 and C-16 without adding structural mechanisms.

**Combination rationale (V-04)**:

V-04 is the minimal combination of the two new criteria. It does not add taxonomy (C-09),
table format (C-13, C-14), or inertia priority (C-13). Tests whether C-15 + C-16 are
additive without the full apparatus. Establishes the combination floor before V-05.

**Full stack rationale (V-05)**:

R2 V-05 already satisfied C-15 (COUNT + CLASSIFY phase) and C-16 (severity-split resolution
with /skill-name token) on v2 rubric runs. The v3 rubric makes both criteria explicit with
stricter pass conditions. V-05 adds: (1) "do not output any contradiction in this phase"
to PHASE 3, satisfying C-15's silence requirement; (2) explicit wrong-example lines in
the Resolution column rule, satisfying C-16's failure-mode negation requirement. No other
changes from R2 V-05.
