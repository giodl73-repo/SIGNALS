Written to `simulations/quest/variations/topic-report-variations-R2-2026-03-14.md`.

---

## Variations: topic-report R2

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (bidirectional BLOCKERS) | R1 V-05's "used verbatim" is ambiguous for C-11's strict requirement; COMPLETENESS + EXCLUSIVITY named as separate explicit rules closes the gap without structural changes |
| V-02 | Output format (teams branch isolation) | SLOT 2's backtick notation in default format description risks C-12 contamination; sealed BRANCH A / BRANCH B execution means teams path is never polluted by default format patterns |
| V-03 | Phrasing register (declaration/contract style) | Contract framing makes G-7 bidirectionality and G-8 zero-char requirement formally precise guarantees rather than imperative instructions |
| V-04 | Combined lifecycle + output format (V-01 + V-02) | Tests whether the two structural fixes achieve 4/4 aspirational without the register change |
| V-05 | Combined all three (V-01 + V-02 + V-03) | Ceiling candidate — bidirectionality + isolation + contract register |

**R2 discriminator analysis:**

Under v2, R1 V-05 has two residual risks:

1. **C-11** — R1 V-05 says "used verbatim" and "must reference by name" but doesn't explicitly state that signal names cannot be added *or* dropped. V-01 names these as COMPLETENESS and EXCLUSIVITY sub-rules.

2. **C-12** — R1 V-05's SLOT 2 uses backtick notation (`` `namespace/skill (owner)` ``) in the default format description. If the model processes this before the teams branch rules, it may carry backtick entry patterns into teams output. V-02 seals BRANCH A and BRANCH B so neither reads the other's format descriptions.

**Recommended scoring order:** V-01 and V-02 first to isolate which gap matters more — V-04 to test structural combination — V-03 as phrasing register control — V-05 as ceiling.
emoving the contamination source before Branch B is reached.
- **V-03** reframes the entire skill as a contract of numbered guarantees (G-1 through G-8). Execution steps are labeled "to fulfill G-n." G-7 splits into G-7a (COMPLETENESS) and G-7b (EXCLUSIVITY) as separate guarantee conditions. G-8 is framed as a character-count guarantee ("zero backtick characters; zero angle-bracket characters"), making it testable rather than prohibitive.
- **V-04** combines V-01 + V-02: bidirectional BLOCKERS language in PHASE 2 + sealed branches in PHASE 3 with clean entry notation. Tests structural fixes alone.
- **V-05** combines all three: G-7 bidirectionality + sealed branches + contract register. Ceiling candidate.

**R2 discriminator analysis:** Under v2 rubric, R1 V-05's weakest points are C-11 (bidirectionality not explicit: "used verbatim" vs "cannot add / cannot drop") and C-12 (backtick notation in SLOT 2 risks output contamination). V-01 and V-02 each attack one dimension; V-04 is the combined structural fix; V-05 is the ceiling candidate. V-03 tests whether contract framing alone is sufficient without structural changes.

**Recommended scoring order:** V-01 and V-02 first to isolate which dimension matters more for C-11 vs C-12 -- then V-04 to see if structural combination achieves 4/4 aspirational -- V-03 as phrasing control -- V-05 as ceiling.

---

## V-01: Lifecycle emphasis (bidirectional BLOCKERS constraint)

Axis: Lifecycle emphasis -- PHASE 2 gets explicit COMPLETENESS + EXCLUSIVITY sub-rules replacing "used verbatim"
Hypothesis: R1 V-05's "used verbatim" instruction is sufficient for C-09 but ambiguous for C-11's strict
bidirectionality; naming both sub-constraints explicitly ("must name every signal in list; must not name any
signal outside list") closes the C-11 gap without structural changes to discovery or rendering.

```
You are running /topic:report.
This skill writes a shareable status artifact for a topic.
Execution has four phases: DISCOVER, BLOCKERS, RENDER, CONFIRM.
Complete each phase in order. Do not skip ahead.

INPUTS:
- Topic name (required). Ask once if absent.
- --format teams (optional flag).

=== PHASE 1: DISCOVER ===

1a. Glob simulations/**/{topic}-* -- collect all artifact paths.

1b. Read simulations/{topic}/strategy.md (or the topic entry in simulations/TOPICS.md).
    Extract for each planned signal: namespace, skill, priority (essential/recommended/optional), owner.

1c. Cross-reference each planned signal against the artifact paths from 1a.
    Match condition: the path contains both the namespace folder and the skill name.
    Result per signal: DONE (match found) or OPEN (no match).

1d. CHECKPOINT -- state before continuing:
    "DISCOVER: {total_done}/{total_planned} complete ({pct}%). Open: {namespace/skill for each OPEN}"

=== PHASE 2: BLOCKERS ===

2a. From PHASE 1 OPEN signals, select those with priority = essential.

2b. Emit:
    "BLOCKERS: {namespace/skill for each essential OPEN signal, comma-separated}"
    If none: "BLOCKERS: none"

2c. Bidirectional enforcement rule -- governs SLOT 3 in PHASE 3:
    COMPLETENESS: The readiness sentence must name every signal present in the BLOCKERS list.
    EXCLUSIVITY:  The readiness sentence must not name any signal absent from the BLOCKERS list.
    Both constraints hold simultaneously. Do not add signal names not in the list.
    Do not drop signal names that are in the list. Do not revise the list in PHASE 3.

=== PHASE 3: RENDER ===

--- Default format ---

Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  signals_found: {total_done}
  signals_planned: {total_planned}

### SLOT 1 -- PROGRESS TABLE
Markdown table. Columns: Namespace | Skill | Priority | Status | Owner
One row per planned signal. Values from PHASE 1 only -- do not re-derive.
Final row: **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if not specified in strategy.md.

### SLOT 2 -- OPEN SIGNALS
List every OPEN signal. Each entry on its own line:
  - namespace: {ns}  skill: {skill-type}  owner: {owner}
If total_open == 0: "None -- all planned signals gathered."

### SLOT 3 -- READINESS
Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
The sentence is governed by rule 2c (bidirectional):
  COMPLETENESS: Name every signal from the PHASE 2 BLOCKERS list.
  EXCLUSIVITY:  Name no signal outside the PHASE 2 BLOCKERS list.
  If BLOCKERS is none: "Ready -- all essential signals are present."
  Example (BLOCKERS = prove-analysis, review-design):
    "Not ready -- missing prove-analysis (prove) and review-design (review)."

### SLOT 4 -- NEXT STEP
One concrete action. Must name skill and namespace.
Source: highest-priority entry in SLOT 2.
If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."
Generic steps ("gather more signals") are not acceptable.

--- --format teams ---

Produce a single ASCII card. Write it to simulations/{topic}/status-{date}.md.
Rules:
- No backtick characters (`) anywhere in the card
- No angle-bracket characters (< or >) anywhere in the card
- No markdown headers (#, ##, ###)
- No fenced code blocks
- Max 40 lines total
- Max 80 characters per line
- Table borders: + - | characters only

Card structure:
  TOPIC REPORT: {topic}
  DATE: {date}
  (blank)
  +--namespace--+--skill--+--status--+--owner--+
  | {ns}        | {skill} | DONE     | {owner} |
  | {ns}        | {skill} | OPEN     | {owner} |
  +-------------+---------+----------+---------+
  (blank)
  OPEN ({total_open}):
    {namespace}/{skill} ({owner})
  (blank)
  READINESS: {label} -- {blocker names from PHASE 2, or "none"}
  NEXT: {concrete skill name} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-02: Output format (teams branch isolation)

Axis: Output format -- PHASE 3 restructured as two sealed rendering branches with no cross-reference;
SLOT 2 in Branch A uses dash-format entry notation instead of backtick notation.
Hypothesis: Backtick notation in SLOT 2's default format description risks C-12 contamination of the teams
card even when the teams rules explicitly prohibit backticks; sealing the branches means the model reads
only the active branch's instructions and cannot carry backtick entry patterns from Branch A into Branch B.

```
You are running /topic:report.
This skill writes a shareable status artifact for a topic.
Four phases: DISCOVER, BLOCKERS, RENDER, CONFIRM.

INPUTS:
- Topic name (required). Ask once if absent.
- --format teams (optional flag). Check before PHASE 3.

=== PHASE 1: DISCOVER ===

1a. Glob simulations/**/{topic}-* -- collect all artifact paths.

1b. Read simulations/{topic}/strategy.md (or simulations/TOPICS.md topic entry).
    For each planned signal: namespace, skill, priority (essential/recommended/optional), owner.

1c. For each planned signal: DONE if a path from 1a matches (namespace folder + skill name in path);
    OPEN otherwise.

1d. CHECKPOINT:
    "DISCOVER: {total_done}/{total_planned} ({pct}%). Open: {namespace/skill per OPEN}"

=== PHASE 2: BLOCKERS ===

2a. From OPEN signals, select priority = essential.

2b. Emit:
    "BLOCKERS: {namespace/skill for each, comma-separated}"
    Or: "BLOCKERS: none"

2c. The readiness statement in PHASE 3 must reference every name in this list and only names in
    this list. Do not revise this list in PHASE 3.

=== PHASE 3: RENDER ===

Read the --format flag. Execute ONE branch. The branches are sealed --
do not reference the other branch's format descriptions when executing.

====================================================================
BRANCH A -- DEFAULT FORMAT (execute only when --format teams NOT set)
====================================================================

Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  signals_found: {total_done}
  signals_planned: {total_planned}

## Progress
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. PHASE 1 values only -- do not re-derive.
Total row: {total_done}/{total_planned} ({pct}%)
Owner defaults to "unassigned" if not specified.

## Open Signals
One item per OPEN signal, plain text, no code fencing:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None" if total_open == 0.

## Readiness
"Readiness: {Ready | Not Ready | Conditionally Ready}"
One sentence. Must cite every name in PHASE 2 BLOCKERS list, no more and no less.
If BLOCKERS none: "Ready -- all essential signals are present."

## Next Step
One sentence. Name skill and namespace.
Highest-priority OPEN signal.
If none open: "Run /topic:story to synthesize gathered signals."

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

BRANCH B CHARACTER RULES -- enforce before writing:
  Rule 1: Zero backtick characters (`). Scan every character. Tolerate none.
  Rule 2: Zero angle-bracket characters (< and >). Scan every character. Tolerate none.
  Rule 3: No pound-sign header lines.
  Rule 4: Max 80 characters per line.
  Rule 5: Max 40 lines total.
  Rule 6: Table borders use only: + - |

BRANCH B LAYOUT (four sections required):

Section 1 -- Header:
  TOPIC REPORT: {topic}
  DATE: {date}

Section 2 -- Progress table:
  +------------+------------+--------+------------+
  | Namespace  | Skill      | Status | Owner      |
  +------------+------------+--------+------------+
  | {ns}       | {skill}    | DONE   | {owner}    |
  | {ns}       | {skill}    | OPEN   | {owner}    |
  +------------+------------+--------+------------+
  Total: {total_done}/{total_planned} ({pct}%)

Section 3 -- Open signals and readiness:
  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  READINESS: {label} -- {blocker names from PHASE 2, or "none"}

Section 4 -- Next step:
  NEXT: {concrete skill} ({namespace})

No frontmatter in Branch B output.

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-03: Phrasing register (declaration/contract style)

Axis: Phrasing register -- skill defined as a numbered contract of output guarantees; execution steps are
the mechanism to fulfill each guarantee; prohibited chars are framed as count guarantees (zero) not rules.
Hypothesis: Contract framing makes G-7's bidirectionality (completeness AND exclusivity as separate guarantee
conditions) and G-8's zero-character requirement formally precise in a way imperative instructions are not;
a model is less likely to silently violate a declared guarantee than to reinterpret an imperative command.

```
/topic:report produces a shareable status artifact for a topic.

This skill makes the following output guarantees:

  G-1. One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
  G-2. Artifact contains a progress table: one row per planned signal, accurate completion counts.
  G-3. Every open signal is listed with namespace, skill type, and owner field populated.
  G-4. Readiness statement present and consistent with the progress table counts.
  G-5. One concrete next step present, naming a specific skill and namespace.
  G-6. When --format teams is set: single ASCII card, max 40 lines, max 80 chars wide, all four sections.
  G-7. Readiness sentence fulfills two simultaneous conditions:
       G-7a COMPLETENESS: names every essential blocking signal.
       G-7b EXCLUSIVITY:  names no signal outside the essential blocking list.
  G-8. When --format teams is set: card output contains zero backtick characters (`)
       and zero angle-bracket characters (< and >), verified character by character.

INPUTS:
- Topic name (required to fulfill all guarantees). Ask once if absent.
- --format teams (optional). Activates G-6 and G-8 in addition to G-1 through G-5 and G-7.

--- EXECUTION SEQUENCE ---

STEP 1 -- DISCOVER (fulfills G-2, G-3)

Glob simulations/**/{topic}-* to collect all existing signal artifact paths.
Read simulations/{topic}/strategy.md (or simulations/TOPICS.md) to obtain the planned signal list.
Per planned signal: namespace, skill, priority (essential/recommended/optional), owner.
Cross-reference: each planned signal is DONE (matching path found) or OPEN (no match).
Matching condition: path contains both the namespace folder name and the skill name.
Emit before continuing:
  "DISCOVER: {total_done}/{total_planned} ({pct}%). Open: {namespace/skill for each OPEN}"

STEP 2 -- BLOCKERS (fulfills G-7)

List every OPEN signal with priority = essential:
  "BLOCKERS: {namespace/skill, ...}"
  Or: "BLOCKERS: none"

To fulfill G-7 (bidirectional constraint):
  G-7a COMPLETENESS: The readiness sentence in STEP 4 must name every signal in this list.
  G-7b EXCLUSIVITY:  The readiness sentence in STEP 4 must not name any signal outside this list.
Both G-7a and G-7b are required. This list is final. It cannot be revised in STEP 4.

STEP 3 -- BRANCH SELECTION

If --format teams is set, execute STEP 4B only. Skip STEP 4A.
If --format teams is not set, execute STEP 4A only. Skip STEP 4B.

STEP 4A -- DEFAULT ARTIFACT (fulfills G-1 through G-5, G-7)

Write simulations/{topic}/status-{date}.md.
Frontmatter: skill: topic-report, topic, date, signals_found, signals_planned.

## Progress (G-2)
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal from STEP 1. No re-derivation.
Total row: {total_done}/{total_planned} ({pct}%)

## Open Signals (G-3)
One item per OPEN signal: namespace, skill type, owner.
Format: namespace/skill -- owner: {owner}
"None" if total_open == 0.

## Readiness (G-4, G-7)
"Readiness: {Ready | Not Ready | Conditionally Ready}"
One sentence. Apply G-7a (completeness) and G-7b (exclusivity) simultaneously.
If BLOCKERS none: "Ready -- all essential signals are present."
Example (BLOCKERS = prove-analysis, review-design):
  "Not ready -- missing prove-analysis (prove) and review-design (review)."

## Next Step (G-5)
One sentence. Skill and namespace. Highest-priority OPEN signal.
If open list empty: "Run /topic:story to synthesize gathered signals."

STEP 4B -- TEAMS ARTIFACT (fulfills G-1 through G-8)

Write simulations/{topic}/status-{date}.md.

G-8 verification -- before writing, confirm the card output satisfies:
  Backtick count = 0. Scan character by character. Any backtick (`) is a violation.
  Angle-bracket count = 0. Scan character by character. Any < or > is a violation.
  No pound-sign header lines.
  Every line max 80 characters.
  Total lines max 40.
  Table borders composed of: + - | only.

Card content (four sections, all required):

  TOPIC REPORT: {topic}
  DATE: {date}

  +------------+------------+--------+------------+
  | Namespace  | Skill      | Status | Owner      |
  +------------+------------+--------+------------+
  | {ns}       | {skill}    | DONE   | {owner}    |
  | {ns}       | {skill}    | OPEN   | {owner}    |
  +------------+------------+--------+------------+
  Total: {total_done}/{total_planned} ({pct}%)

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  READINESS: {label} -- {blocker names, or "none"}
    (apply G-7a and G-7b: cite every BLOCKER, cite only BLOCKERs)

  NEXT: {skill} ({namespace})

STEP 5 -- CONFIRM (fulfills G-1 echo)

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-04: Combined lifecycle + output format (V-01 + V-02)

Axis: Combined -- bidirectional BLOCKERS constraint (V-01) + sealed branch isolation (V-02)
Hypothesis: The two structural gaps in R1 V-05 are independent: C-11 requires explicit bidirectionality
in PHASE 2, and C-12 requires isolation of the teams rendering path from default format descriptions.
Applying both without the register change tests whether the structural fixes alone achieve 4/4 aspirational.

```
You are running /topic:report.
This skill writes a shareable status artifact for a topic.
Execution: DISCOVER, BLOCKERS, RENDER, CONFIRM -- in order.

INPUTS:
- Topic name (required). Ask once if absent.
- --format teams (optional flag). Check before RENDER.

=== PHASE 1: DISCOVER ===

1a. Glob simulations/**/{topic}-* -- all artifact paths.

1b. Read simulations/{topic}/strategy.md (or simulations/TOPICS.md topic entry).
    Per planned signal: namespace, skill, priority (essential/recommended/optional), owner.

1c. Cross-reference: each planned signal is DONE (path matches namespace + skill) or OPEN.

1d. CHECKPOINT:
    "DISCOVER: {total_done}/{total_planned} ({pct}%). Open: {namespace/skill per OPEN}"

=== PHASE 2: BLOCKERS ===

2a. From OPEN signals, filter to priority = essential.

2b. Emit:
    "BLOCKERS: {namespace/skill for each essential OPEN, comma-separated}"
    Or: "BLOCKERS: none"

2c. Bidirectional enforcement rule -- governs the readiness sentence in PHASE 3:
    COMPLETENESS: Every name in the BLOCKERS list must appear in the readiness sentence.
    EXCLUSIVITY:  No name outside the BLOCKERS list may appear in the readiness sentence.
    Both constraints are required simultaneously. This list is closed. Do not revise in PHASE 3.

=== PHASE 3: RENDER ===

Read --format flag. Execute one branch. The branches are sealed --
do not reference the other branch's format descriptions when executing.

====================================================================
BRANCH A -- DEFAULT (execute only when --format teams NOT set)
====================================================================

Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  signals_found: {total_done}
  signals_planned: {total_planned}

### SLOT 1 -- PROGRESS TABLE
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. PHASE 1 values only -- do not re-derive.
Total row: **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if not in strategy.md.

### SLOT 2 -- OPEN SIGNALS
One line per OPEN signal, plain text:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None -- all planned signals gathered." if total_open == 0.

### SLOT 3 -- READINESS
Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
Apply rule 2c (bidirectional):
  COMPLETENESS: Name every signal from the BLOCKERS list.
  EXCLUSIVITY:  Name no signal outside the BLOCKERS list.
  If BLOCKERS none: "Ready -- all essential signals are present."
  Example (BLOCKERS = prove-analysis, review-design):
    "Not ready -- missing prove-analysis (prove) and review-design (review)."

### SLOT 4 -- NEXT STEP
One sentence. Name skill and namespace.
Source: highest-priority entry in SLOT 2.
If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."
Generic steps fail this slot.

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

CHARACTER RULES -- apply before writing; these are the only format rules for Branch B:
  1. Zero backtick characters (`). None anywhere in the card output.
  2. Zero angle-bracket characters (< and >). None anywhere in the card output.
  3. No pound-sign header lines.
  4. Max 80 characters per line.
  5. Max 40 lines total.
  6. Table borders: + - | only.

LAYOUT (four sections required):

Section 1 -- Header:
  TOPIC REPORT: {topic}
  DATE: {date}

Section 2 -- Progress table (plain ASCII):
  +--------------+------------+--------+------------+
  | Namespace    | Skill      | Status | Owner      |
  +--------------+------------+--------+------------+
  | {ns}         | {skill}    | DONE   | {owner}    |
  | {ns}         | {skill}    | OPEN   | {owner}    |
  +--------------+------------+--------+------------+
  Total: {total_done}/{total_planned} ({pct}%)

Section 3 -- Open signals and readiness:
  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  READINESS: {label} -- {blocker names from PHASE 2, or "none"}
  (apply 2c: cite every BLOCKER, cite only BLOCKERs)

Section 4 -- Next step:
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-05: Combined (bidirectionality + branch isolation + contract register)

Axis: Combined -- V-01's bidirectional BLOCKERS + V-02's sealed branches + V-03's contract register
Hypothesis: All three mechanisms together eliminate the residual C-11 and C-12 risks from R1 V-05:
bidirectionality closes the omission/addition gap in C-11; branch isolation prevents backtick notation
from default-format descriptions contaminating the teams card (C-12); contract register makes guarantees
explicit and verifiable, improving precision across all aspirational criteria.

```
/topic:report produces a shareable status artifact for a topic.

This skill makes the following output guarantees:

  G-1. One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
  G-2. Artifact contains a progress table with one row per planned signal and accurate counts.
  G-3. Every open signal is listed with namespace, skill type, and owner populated.
  G-4. Readiness statement present and consistent with progress table counts.
  G-5. One concrete next step naming a specific skill and namespace.
  G-6. When --format teams is set: single ASCII card, max 40 lines, max 80 chars wide.
  G-7. Readiness sentence fulfills two simultaneous conditions:
       G-7a COMPLETENESS: names every essential blocking signal.
       G-7b EXCLUSIVITY:  names no signal outside the essential blocking list.
  G-8. When --format teams is set: card output contains zero backtick characters (`)
       and zero angle-bracket characters (< and >), verified character by character.

INPUTS:
- Topic name (required). Ask once if absent.
- --format teams (optional). Activates G-6 and G-8.

=== PHASE 1: DISCOVER ===

1a. Glob simulations/**/{topic}-* -- all artifact paths.

1b. Read simulations/{topic}/strategy.md (or simulations/TOPICS.md topic entry).
    Per planned signal: namespace, skill, priority (essential/recommended/optional), owner.

1c. Cross-reference: each planned signal is DONE (path matches namespace + skill) or OPEN.

1d. CHECKPOINT -- emit before continuing:
    "DISCOVER: {total_done}/{total_planned} ({pct}%). Open: {namespace/skill per OPEN}"

=== PHASE 2: BLOCKERS ===

2a. From OPEN signals, select priority = essential.

2b. Emit:
    "BLOCKERS: {namespace/skill for each, comma-separated}"
    Or: "BLOCKERS: none"

2c. G-7 contract -- governs the readiness sentence in PHASE 3:
    G-7a COMPLETENESS: Every signal name in the BLOCKERS list must appear in the readiness sentence.
    G-7b EXCLUSIVITY:  No signal name outside the BLOCKERS list may appear in the readiness sentence.
    This list is closed and final. It cannot be revised in PHASE 3.
    Both G-7a and G-7b are required simultaneously.

=== PHASE 3: RENDER ===

Read --format flag. Execute one branch only. The branches are sealed --
do not reference the other branch's format descriptions when executing.

====================================================================
BRANCH A -- DEFAULT (execute only when --format teams NOT set)
====================================================================

Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  signals_found: {total_done}
  signals_planned: {total_planned}

SLOT 1 -- PROGRESS TABLE (fulfills G-2)
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. PHASE 1 values only -- do not re-derive.
Total row: **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if not in strategy.md.

SLOT 2 -- OPEN SIGNALS (fulfills G-3)
One line per OPEN signal, plain text, no code fencing:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None -- all planned signals gathered." if total_open == 0.

SLOT 3 -- READINESS (fulfills G-4, G-7)
Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
Sentence must satisfy G-7a and G-7b simultaneously (from PHASE 2 2c):
  If BLOCKERS none: "Ready -- all essential signals are present."
  Otherwise name every BLOCKER, name only BLOCKERs.
  Example (BLOCKERS = prove-analysis, review-design):
    "Not ready -- missing prove-analysis (prove) and review-design (review)."

SLOT 4 -- NEXT STEP (fulfills G-5)
One sentence. Name skill and namespace.
Highest-priority entry from SLOT 2.
If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."
Generic steps ("gather more signals") fail this slot.

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

G-8 verification -- before writing, confirm the card satisfies:
  Backtick count = 0.      Scan every character. Any backtick (`) is a violation.
  Angle-bracket count = 0. Scan every character. Any < or > is a violation.
  No pound-sign header lines.
  Max 40 lines total.
  Max 80 characters per line.
  Table borders use only: + - |

Card content (four sections required):

  TOPIC REPORT: {topic}
  DATE: {date}

  +--------------+------------+--------+------------+
  | Namespace    | Skill      | Status | Owner      |
  +--------------+------------+--------+------------+
  | {ns}         | {skill}    | DONE   | {owner}    |
  | {ns}         | {skill}    | OPEN   | {owner}    |
  +--------------+------------+--------+------------+
  Total: {total_done}/{total_planned} ({pct}%)

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  READINESS: {label} -- {blocker names, or "none"}
    (G-7a: every BLOCKER named; G-7b: only BLOCKERs named)

  NEXT: {skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```
