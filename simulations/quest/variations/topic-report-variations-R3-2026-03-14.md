Written to `simulations/quest/variations/topic-report-variations-R3-2026-03-14.md`.

---

## Variations: topic-report R3

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Lifecycle emphasis (BLOCKERS LOCK) | Named sub-rules define *what* the sentence must satisfy but don't prevent a model from quietly revising the BLOCKERS list itself; LOCK makes list immutability a first-class named obligation separate from the bidirectionality rule |
| V-02 | Output format (in-render verification scan) | Declarative rules in PHASE 2 require recall at PHASE 3; explicit COMPLETENESS CHECK / EXCLUSIVITY CHECK scan at the write point substitutes *action* for *recall*, catching violations before they land |
| V-03 | Phrasing register (inline annotation style) | When constraints are defined in PHASE 2 but applied in PHASE 3, recall distance grows with prompt length; [RULE: COMPLETENESS] / [RULE: EXCLUSIVITY] markers proximate to their governed template elements make compliance a local obligation |
| V-04 | Combined lifecycle + output format (LOCK + scan) | LOCK + named sub-rules + verification scan creates three enforcement layers for C-11/C-13 — tests whether triple-layer enforcement outperforms the double-layer design (named sub-rules + "list is closed") from R2 in live runs |
| V-05 | Combined ceiling (contract register + LOCK + scan) | All proven mechanisms stacked: G-n framing, G-7a/G-7b named conditions, sealed branches, BLOCKERS LOCK, in-render verification scan — every known compliance failure mode covered |

---

**R3 discriminator analysis:**

Under v3 rubric, all five R3 variations are expected to score **100/100** — each has named COMPLETENESS/EXCLUSIVITY sub-rules (C-13) and sealed-branches language (C-14). The R3 gap is not rubric scoring but **live execution robustness**.

R2's four 100/100 variations leave three open questions:

1. **Can a model quietly revise the BLOCKERS list before writing the readiness sentence?** R2 designs say "do not revise this list" but embed it as a clause inside the bidirectionality rule. V-01 elevates it to a named LOCK directive — independently prominent.

2. **Does declaring COMPLETENESS/EXCLUSIVITY produce compliance, or must compliance be verified?** V-02 adds an explicit scan at the write point: "list each BLOCKER name, confirm it appears; list each sentence name, confirm it is in BLOCKERS." Substitutes action for recall.

3. **Does proximity of constraint to governed element improve compliance?** V-03 tests inline annotation placement — [RULE] markers at the exact template position each rule governs, eliminating the cross-phase recall distance entirely.

**Ceiling candidate: V-05** — contract register + G-7a/G-7b named guarantee conditions + sealed branches + BLOCKERS LOCK + in-render verification scan.

**Minimal R3 increment: V-04** — takes V-04 R2 (the minimal structural fix that hit 100/100 under v2) and adds the two new R3 enforcement layers without contract register overhead.
emember* C-13's constraints when writing SLOT 3, several hundred tokens after PHASE 2. A scan instruction in SLOT 3 — "list each BLOCKER name, confirm it appears in the draft sentence" — substitutes an *action* (verify) for a *recall* (remember the rule). Tests whether active verification catches violations that rule-based recall misses.

3. **Inline annotation style** — R2 designs forward-reference: the rule is in PHASE 2, the application is in PHASE 3. Inline [RULE] markers at the output template location eliminate the forward-reference gap. Tests whether proximity of constraint to governed element improves compliance independently of the constraint's content.

Under v3, all five R3 variations are expected to score 100/100. The discriminators are live-run performance, not rubric criteria.

**Recommended scoring order:** V-01 and V-02 to isolate which enforcement layer matters more for live C-11 compliance — V-03 as phrasing register control — V-04 to test triple-layer combination — V-05 as full ceiling.

---

## V-01: Lifecycle emphasis (BLOCKERS LOCK directive)

Axis: Lifecycle emphasis -- after emitting the BLOCKERS list in PHASE 2, emit an explicit LOCK
directive that names list immutability as a separate first-class obligation.
Hypothesis: R2 designs include "do not revise this list in PHASE 3" as a clause embedded in the
bidirectionality rule; elevating immutability to a named LOCK directive makes it independently
salient -- a model encountering the LOCK cannot confuse it with the bidirectionality rule itself.
Base: V-04 R2 structure (COMPLETENESS/EXCLUSIVITY named sub-rules + sealed branches).

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
    Both constraints are required simultaneously.

2d. LOCK: The BLOCKERS list from 2b is now frozen.
    No additions, removals, or revisions to this list are permitted in PHASE 3 or PHASE 4.
    The readiness sentence must comply with rule 2c using this list exactly as emitted in 2b.

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
Apply rule 2c (bidirectional) using the LOCKED list from 2b:
  COMPLETENESS: Name every signal from the BLOCKERS list.
  EXCLUSIVITY:  Name no signal outside the BLOCKERS list.
Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
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

  READINESS: {label} -- {blocker names from LOCKED list (2b), or "none"}
  (COMPLETENESS: every name in LOCKED list appears; EXCLUSIVITY: no name outside LOCKED list)

Section 4 -- Next step:
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-02: Output format (in-render verification scan)

Axis: Output format -- before finalizing SLOT 3 / READINESS in both rendering branches, require
an explicit two-step COMPLETENESS/EXCLUSIVITY verification scan against the BLOCKERS list.
Hypothesis: Declaring COMPLETENESS/EXCLUSIVITY as named rules in PHASE 2 is necessary but
declarative; inserting a scan instruction at the exact write point ("list each BLOCKER name,
confirm it appears in draft sentence; list each name in draft sentence, confirm it is in BLOCKERS")
substitutes an active verification action for a recall obligation, catching violations before they
are written rather than relying on the model to remember cross-phase constraints.

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
Before writing the readiness sentence, run the verification scan:

  COMPLETENESS CHECK: List each name from the PHASE 2 BLOCKERS list.
  For each: confirm the name appears in the draft readiness sentence.
  Any missing name is a COMPLETENESS violation. Revise the draft before proceeding.

  EXCLUSIVITY CHECK: List each signal name in the draft readiness sentence.
  For each: confirm it is present in the PHASE 2 BLOCKERS list.
  Any extra name is an EXCLUSIVITY violation. Revise the draft before proceeding.

After both checks pass, write:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence -- verified against both checks}"
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
  Before writing the READINESS line, run:
  COMPLETENESS CHECK: list each BLOCKER name, confirm each appears in the draft line.
  EXCLUSIVITY CHECK: list each name in the draft line, confirm none are outside BLOCKERS.
  Any violation: revise the draft until both checks pass.

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  READINESS: {label} -- {blocker names, or "none"}

Section 4 -- Next step:
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-03: Phrasing register (inline annotation style)

Axis: Phrasing register -- COMPLETENESS, EXCLUSIVITY, and branch-sealing constraints expressed
as [RULE: ...] inline annotations embedded directly in the output template definitions, rather
than as forward-reference rules established in PHASE 2 and recalled in PHASE 3.
Hypothesis: When constraints are defined in PHASE 2 but applied in PHASE 3, recall distance grows
with prompt length; placing [RULE: COMPLETENESS] and [RULE: EXCLUSIVITY] as inline markers at the
exact template position they govern makes compliance a local obligation rather than a cross-phase
recall task, improving reliability independently of the constraint's content or naming.

```
You are running /topic:report.
Write a shareable status artifact for a topic.

INPUTS:
- Topic name (required). Ask once if absent.
- --format teams (optional flag).

=== DISCOVER ===

Glob simulations/**/{topic}-* -- all artifact paths.
Read simulations/{topic}/strategy.md (or simulations/TOPICS.md) for planned signals.
Per planned signal: namespace, skill, priority (essential/recommended/optional), owner.
Cross-reference: DONE if an artifact path matches (namespace folder + skill name); OPEN otherwise.
CHECKPOINT: "DISCOVER: {total_done}/{total_planned} ({pct}%). Open: {namespace/skill per OPEN}"

=== BLOCKERS ===

Filter OPEN signals to priority = essential.
Emit: "BLOCKERS: {namespace/skill, ...}" or "BLOCKERS: none"

[RULE BLOCKERS-COMPLETENESS: The readiness sentence must name every signal in the list above.]
[RULE BLOCKERS-EXCLUSIVITY: The readiness sentence must not name any signal outside the list above.]
[RULE BLOCKERS-FREEZE: This list is now fixed. It cannot be modified in any phase that follows.]

=== RENDER ===

[RULE BRANCH-SEAL: Read the --format flag. Execute ONE branch only.
Do not reference the other branch's format descriptions while executing the active branch.]

--- BRANCH A: DEFAULT (active when --format teams NOT set) ---

Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  signals_found: {total_done}
  signals_planned: {total_planned}

PROGRESS TABLE
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal; DISCOVER values only, do not re-derive.
Total row: {total_done}/{total_planned} ({pct}%)
Owner = "unassigned" if not specified.

OPEN SIGNALS
One line per OPEN signal:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None -- all planned signals gathered." if total_open == 0.

READINESS
[RULE COMPLETENESS: The sentence below must name every signal from the BLOCKERS list.]
[RULE EXCLUSIVITY: The sentence below must not name any signal outside the BLOCKERS list.]
Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence -- complies with COMPLETENESS and EXCLUSIVITY}"
  If BLOCKERS none: "Ready -- all essential signals are present."
  Example (BLOCKERS = prove-analysis, review-design):
    "Not ready -- missing prove-analysis (prove) and review-design (review)."

NEXT STEP
One sentence. Name skill and namespace.
Highest-priority entry from OPEN SIGNALS.
If open list empty: "Run /topic:story to synthesize all gathered signals."

--- BRANCH B: TEAMS FORMAT (active when --format teams IS set) ---

[RULE BRANCH-B-SEAL: This branch is self-contained.
Do not reference Branch A's format descriptions while executing this branch.]

Write simulations/{topic}/status-{date}.md.

[RULE CHAR-SCAN: Before writing, verify:
  Zero backtick characters (`). Scan every character. None tolerated.
  Zero angle-bracket characters (< and >). Scan every character. None tolerated.
  No pound-sign header lines.
  Max 80 characters per line.
  Max 40 lines total.
  Table borders: + - | only.]

Four sections required:

SECTION 1:
  TOPIC REPORT: {topic}
  DATE: {date}

SECTION 2:
  +--------------+------------+--------+------------+
  | Namespace    | Skill      | Status | Owner      |
  +--------------+------------+--------+------------+
  | {ns}         | {skill}    | DONE   | {owner}    |
  | {ns}         | {skill}    | OPEN   | {owner}    |
  +--------------+------------+--------+------------+
  Total: {total_done}/{total_planned} ({pct}%)

SECTION 3:
  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  [RULE COMPLETENESS: READINESS line must name every signal in the BLOCKERS list.]
  [RULE EXCLUSIVITY: READINESS line must not name any signal outside the BLOCKERS list.]
  READINESS: {label} -- {blocker names, or "none"}

SECTION 4:
  NEXT: {concrete skill} ({namespace})

=== CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-04: Combined lifecycle + output format (LOCK + verification scan)

Axis: Combined -- V-01's BLOCKERS LOCK directive + V-02's in-render COMPLETENESS/EXCLUSIVITY
verification scan.
Hypothesis: LOCK makes the BLOCKERS list immutable as a first-class directive; the verification
scan makes compliance active at the write point; together they create three enforcement layers for
C-11/C-13: the named sub-rules (what the sentence must satisfy), the LOCK (list cannot change),
and the scan (active check before writing) -- testing whether triple-layer enforcement is more
reliable in live runs than the double-layer design (named sub-rules + list-closed clause) in R2.
Base: V-04 R2 structure (COMPLETENESS/EXCLUSIVITY named sub-rules + sealed branches).

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
    Both constraints are required simultaneously.

2d. LOCK: The BLOCKERS list from 2b is now frozen.
    No additions, removals, or revisions to this list are permitted in PHASE 3 or PHASE 4.
    The readiness sentence must be written against this list exactly as emitted in 2b.

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
Before writing the readiness sentence, run the verification scan against the LOCKED list:

  COMPLETENESS CHECK: Take the LOCKED BLOCKERS list from Phase 2.
  List each name. Confirm each appears in the draft readiness sentence.
  Any missing name is a COMPLETENESS violation. Revise sentence before proceeding.

  EXCLUSIVITY CHECK: List each signal name in the draft readiness sentence.
  Confirm each is present in the LOCKED BLOCKERS list.
  Any name outside the LOCKED BLOCKERS list is an EXCLUSIVITY violation.
  Revise sentence before proceeding.

After both checks pass:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
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
  Before writing the READINESS line, run:
  COMPLETENESS CHECK: list each LOCKED BLOCKER name, confirm each appears in the draft line.
  EXCLUSIVITY CHECK: list each name in the draft line, confirm none are outside LOCKED BLOCKERS.
  Any violation: revise until both checks pass.

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  READINESS: {label} -- {blocker names, or "none"}

Section 4 -- Next step:
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-05: Combined ceiling (contract register + LOCK + verification scan)

Axis: Combined ceiling -- G-n contract register (R2 V-05) + COMPLETENESS/EXCLUSIVITY as named
guarantee conditions (R2 V-03/V-05) + sealed branches (R2 V-02/V-04/V-05) + BLOCKERS LOCK (V-01)
+ in-render verification scan (V-02).
Hypothesis: G-n guarantee framing makes invariants testable and prominent before execution (R2
learning); LOCK makes the BLOCKERS list immutable as a first-class directive (R3 V-01); in-render
verification scan makes G-7a/G-7b compliance active rather than declarative (R3 V-02); sealed
branches prevent cross-branch contamination (R2 learning); stacking all five mechanisms covers
every known compliance failure mode across all rounds.

```
/topic:report produces a shareable status artifact for a topic.

This skill makes the following output guarantees:

  G-1. One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
  G-2. Artifact contains a progress table with one row per planned signal and accurate counts.
  G-3. Every open signal is listed with namespace, skill type, and owner populated.
  G-4. Readiness statement present and consistent with progress table counts.
  G-5. One concrete next step naming a specific skill and namespace.
  G-6. When --format teams is set: single ASCII card, max 40 lines, max 80 chars wide, all four sections.
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
    Both G-7a and G-7b are required simultaneously.

2d. LOCK: The BLOCKERS list from 2b is now frozen and final.
    No additions, removals, or revisions are permitted in any subsequent phase.
    The readiness sentence must be written against this list exactly as emitted in 2b.

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
Before writing the readiness sentence, run the G-7 verification scan:

  G-7a COMPLETENESS SCAN: Take the LOCKED BLOCKERS list from Phase 2.
  List each signal name. Confirm each appears in the draft readiness sentence.
  Any missing name is a G-7a violation. Revise the draft before proceeding.

  G-7b EXCLUSIVITY SCAN: List each signal name in the draft readiness sentence.
  Confirm each is present in the LOCKED BLOCKERS list.
  Any extra name is a G-7b violation. Revise the draft before proceeding.

After both scans pass:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
  If BLOCKERS none: "Ready -- all essential signals are present."
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

Card content (four sections required, fulfills G-1 through G-8):

  TOPIC REPORT: {topic}
  DATE: {date}

  +--------------+------------+--------+------------+
  | Namespace    | Skill      | Status | Owner      |
  +--------------+------------+--------+------------+
  | {ns}         | {skill}    | DONE   | {owner}    |
  | {ns}         | {skill}    | OPEN   | {owner}    |
  +--------------+------------+--------+------------+
  Total: {total_done}/{total_planned} ({pct}%)

  Before writing the READINESS line, run:
  G-7a COMPLETENESS SCAN: confirm every LOCKED BLOCKER name appears in the draft line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the draft line is outside LOCKED BLOCKERS.
  Any violation: revise until both scans pass.

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  READINESS: {label} -- {blocker names, or "none"}

  NEXT: {skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```
