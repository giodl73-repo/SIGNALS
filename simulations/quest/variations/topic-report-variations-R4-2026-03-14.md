Written to `simulations/quest/variations/topic-report-variations-R4-2026-03-14.md`.

---

## Variations: topic-report R4

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (inline annotations with co-located examples, C-17 isolated) | Dense inline [RULE] annotations with worked examples at each governed position; no standalone LOCK step, no verification scan — tests whether example co-location improves compliance beyond rule co-location alone |
| V-02 | Lifecycle + phrasing register (standalone LOCK + inline annotations, C-15 + C-17) | Phase-level LOCK as pre-commitment declaration + inline [RULE COMPLETENESS]/[RULE EXCLUSIVITY] at template application site — two enforcement layers at different structural depths without an active scan |
| V-03 | Output format + phrasing register (verification scan + inline annotations, C-16 + C-17) | Inline [RULE] annotation declares constraint at governed position, scan executes it at same position — declaration + verification co-located; tests whether proximity compensates for absent LOCK |
| V-04 | Combined triple (C-15 + C-16 + C-17) | Adds inline [RULE] annotations to V-04 R3 (LOCK + scan); minimum design expected to score 100/100 under v4 |
| V-05 | Combined ceiling (contract + LOCK + scan + inline) | Adds inline [RULE G-7a]/[RULE G-7b] to V-05 R3; contract label chains through to template annotation — closes the last gap in V-05 R3's live-run coverage |

---

**Predicted scores under v4 rubric** (aspirational max = 9):

| Variation | C-15 | C-16 | C-17 | Aspirational | Composite |
|-----------|------|------|------|-------------|-----------|
| V-01 | FAIL | FAIL | PASS | 7/9 | ~97.8 |
| V-02 | PASS | FAIL | PASS | 8/9 | ~98.9 |
| V-03 | FAIL | PASS | PASS | 8/9 | ~98.9 |
| V-04 | PASS | PASS | PASS | 9/9 | **100** |
| V-05 | PASS | PASS | PASS | 9/9 | **100** |

Key discriminator: C-15 requires a standalone phase-level LOCK step (2d), not just an inline [RULE BLOCKERS-FREEZE] annotation — so V-01 (inline-only) and V-03 (scan + inline, no LOCK step) fail C-15. V-04 and V-05 are the golden candidates under v4.

**Minimal golden: V-04.** Adds inline annotations to V-04 R3 with minimal overhead — the one mechanism that was missing from R3's highest-scoring non-ceiling design.
; formula denominator updates accordingly.

R3 variations under v4:
- V-01 R3: passes C-15, fails C-16, fails C-17 -- aspirational 7/9 (~97.8)
- V-02 R3: fails C-15, passes C-16, fails C-17 -- aspirational 7/9 (~97.8)
- V-03 R3: fails C-15 (inline BLOCKERS-FREEZE does not satisfy the standalone phase-level LOCK
  criterion), fails C-16, passes C-17 -- aspirational 7/9 (~97.8)
- V-04 R3: passes C-15, passes C-16, fails C-17 -- aspirational 8/9 (~98.9)
- V-05 R3: passes C-15, passes C-16, fails C-17 -- aspirational 8/9 (~98.9)

No R3 variation scores 100/100 under v4. The discriminator is C-17 (inline annotation style),
which none of the R3 triple-mechanism designs include. R4 adds C-17 to existing mechanisms to
find the minimal golden design and the ceiling.

**Predicted scores under v4:**

| Variation | C-15 | C-16 | C-17 | Aspirational | Predicted composite |
|-----------|------|------|------|-------------|---------------------|
| V-01 | FAIL | FAIL | PASS | 7/9 | ~97.8 |
| V-02 | PASS | FAIL | PASS | 8/9 | ~98.9 |
| V-03 | FAIL | PASS | PASS | 8/9 | ~98.9 |
| V-04 | PASS | PASS | PASS | 9/9 | **100** |
| V-05 | PASS | PASS | PASS | 9/9 | **100** |

**Scoring note for C-15:** The inline annotation form [RULE BLOCKERS-FREEZE] (V-03 R3 style)
does NOT satisfy C-15. The criterion requires a standalone named LOCK directive that is
independently prominent -- a separate phase-level step (e.g., 2d. LOCK: ...) distinct in
structural position from the bidirectionality rules. An inline annotation embedded alongside
[RULE BLOCKERS-COMPLETENESS] and [RULE BLOCKERS-EXCLUSIVITY] satisfies C-17 (inline annotation
style) but fails C-15 (standalone LOCK directive). V-01 R4 deliberately uses the inline-only
form to test C-17 without contaminating the C-15 mechanism.

**Single-axis discriminators for V-01 through V-03:**
- V-01 vs V-03 R3: V-01 adds co-located worked examples to each [RULE] annotation; tests density
- V-02 vs V-01 R3: V-02 adds inline [RULE] annotations to the phase-level LOCK design
- V-03 vs V-02 R3: V-03 adds inline [RULE] annotations to the scan design; no standalone LOCK

**Recommended scoring order:** V-01 to establish C-17 baseline -- V-02 and V-03 to test which
pairs with C-17 better -- V-04 as minimal golden candidate -- V-05 as full ceiling.

**Minimal R4 increment: V-04.** Takes V-04 R3 (the minimal triple enforcement design) and adds
the one missing mechanism (inline annotations). Expected 100/100 at lowest complexity cost.

---

## V-01: Phrasing register (inline annotations with co-located examples)

Axis: Phrasing register -- comprehensive inline [RULE] annotations with worked examples embedded
at each governed template position; no standalone LOCK step (only R2-era embedded list-closure
clause); no verification scan.
Hypothesis: V-03 R3 placed [RULE] markers at key template positions but each annotation stated
the rule without a worked example; the model still needed to translate the rule into a specific
output action. Adding a compact worked example directly inside each [RULE] annotation at its
governed position reduces the translation distance from rule to action, testing whether
example co-location improves compliance beyond rule co-location alone.

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

[RULE BLOCKERS-COMPLETENESS: Every name in the BLOCKERS list above must appear in the readiness
 sentence. Example: BLOCKERS = prove-analysis, review-design => sentence must contain both
 "prove-analysis" and "review-design". Missing either name is a violation.]

[RULE BLOCKERS-EXCLUSIVITY: No name outside the BLOCKERS list above may appear in the readiness
 sentence. Example: BLOCKERS = prove-analysis => sentence must NOT include "review-design" even
 if review-design is OPEN. Including any extra name is a violation.]

This list is closed. Do not revise it in any phase that follows.

=== RENDER ===

[RULE BRANCH-SEAL: Check --format flag. Execute ONE branch only. Do not reference the other
 branch's format descriptions while executing the active branch.]

--- BRANCH A: DEFAULT (active when --format teams NOT set) ---

Write simulations/{topic}/status-{date}.md.

Frontmatter:
  skill: topic-report
  topic: {topic}
  date: {date}
  signals_found: {total_done}
  signals_planned: {total_planned}

PROGRESS TABLE
[RULE TABLE-SOURCE: Use DISCOVER values only. Do not re-derive from artifacts in this slot.
 Example: if DISCOVER counted 4 DONE, the table shows 4 DONE rows -- not a recount.]
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. Total row: {total_done}/{total_planned} ({pct}%)
Owner = "unassigned" if not specified in strategy.md.

OPEN SIGNALS
[RULE OPEN-FORMAT: One line per OPEN signal, plain text. Format exactly:
   - namespace: {ns} / skill: {skill-type} / owner: {owner}
 If total_open == 0: "None -- all planned signals gathered."]

READINESS
[RULE COMPLETENESS: The sentence written immediately below this annotation must name every
 signal in the BLOCKERS list. Example (BLOCKERS = prove-analysis, review-design):
   correct: "Not ready -- missing prove-analysis (prove) and review-design (review)."
   violation: "Not ready -- missing prove-analysis (prove)." (review-design is absent)]

[RULE EXCLUSIVITY: The sentence written immediately below this annotation must not name any
 signal outside the BLOCKERS list. Example (BLOCKERS = prove-analysis):
   correct: "Not ready -- missing prove-analysis (prove)."
   violation: "Not ready -- missing prove-analysis and review-design." (review-design not in list)]

Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence -- satisfies COMPLETENESS and EXCLUSIVITY}"
  If BLOCKERS none: "Ready -- all essential signals are present."

NEXT STEP
[RULE NEXT-CONCRETE: Must name a specific skill and namespace. Generic steps ("gather more
 signals") violate this rule. Source: highest-priority entry from OPEN SIGNALS.
 If open list is empty: "Run /topic:story to synthesize all gathered signals."]

--- BRANCH B: TEAMS FORMAT (active when --format teams IS set) ---

[RULE BRANCH-B-SEAL: This branch is self-contained. Do not reference Branch A's format
 descriptions while executing this branch.]

Write simulations/{topic}/status-{date}.md.

[RULE CHAR-PROHIBIT: Before writing any output for this branch, confirm all of the following.
 None of these characters may appear anywhere in the card output:
   Backtick (`): count must be zero. Example violation: `scout/market` -- remove backticks.
   Angle brackets (< and >): count must be zero. Example violation: <owner> -- remove brackets.
 Additional constraints: no pound-sign header lines; max 80 characters per line;
 max 40 lines total; table borders use only + - | characters.]

Four sections required:

SECTION 1:
  TOPIC REPORT: {topic}
  DATE: {date}

SECTION 2:
  [RULE TABLE-BORDERS: Table borders use only + - | characters. No markdown table syntax here.
   Example compliant row: | scout  | market  | DONE | alice |]
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

  [RULE COMPLETENESS: READINESS line must name every signal in the BLOCKERS list. Example:
   BLOCKERS = scout/market, prove/analysis => line must contain "scout/market" and
   "prove/analysis". Omitting either is a violation.]
  [RULE EXCLUSIVITY: READINESS line must not name any signal outside the BLOCKERS list. Example:
   BLOCKERS = scout/market => line must NOT include prove/analysis. Any extra name is a violation.]
  READINESS: {label} -- {every blocker name from list, or "none"}

SECTION 4:
  [RULE NEXT-CONCRETE: Must name a specific skill and namespace. No generic steps.]
  NEXT: {concrete skill} ({namespace})

=== CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-02: Lifecycle + phrasing register (standalone LOCK + inline annotations)

Axis: Lifecycle emphasis + phrasing register -- standalone phase-level LOCK step (2d) combined
with inline [RULE COMPLETENESS] / [RULE EXCLUSIVITY] annotations at the exact template positions
they govern in both Branch A and Branch B; no verification scan.
Hypothesis: V-01 R3 showed that a phase-level LOCK step makes list immutability independently
prominent before the RENDER phase; V-03 R3 showed that inline [RULE] annotations at template
positions eliminate cross-phase recall distance; combining a pre-commitment LOCK (declared before
execution) with local inline constraints (present at the write point) creates two enforcement
layers at different depths -- phase-level pre-commitment and template-level locality -- without
requiring an active scan procedure.

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

[RULE BRANCH-SEAL: Read --format flag. Execute ONE branch only. Do not reference the other
 branch's format descriptions when executing the active branch.]

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
[RULE SLOT1-SOURCE: PHASE 1 values only -- do not re-derive in this slot.]
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. Total row: **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if not in strategy.md.

### SLOT 2 -- OPEN SIGNALS
One line per OPEN signal, plain text:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None -- all planned signals gathered." if total_open == 0.

### SLOT 3 -- READINESS
[RULE COMPLETENESS: The sentence written immediately below must name every signal in the LOCKED
 BLOCKERS list (step 2b, frozen by step 2d). Any signal in that list not appearing in this
 sentence is a COMPLETENESS violation. Use the list exactly as emitted -- no substitutions.]

[RULE EXCLUSIVITY: The sentence written immediately below must not name any signal outside the
 LOCKED BLOCKERS list. Any name here that is absent from the LOCKED list is an EXCLUSIVITY
 violation, even if that signal is OPEN.]

Format:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence -- complies with COMPLETENESS and EXCLUSIVITY rules above}"
  If BLOCKERS none: "Ready -- all essential signals are present."
  Example (BLOCKERS = prove-analysis, review-design):
    "Not ready -- missing prove-analysis (prove) and review-design (review)."

### SLOT 4 -- NEXT STEP
[RULE NEXT-CONCRETE: Must name a specific skill and namespace. Generic steps fail this slot.
 Source: highest-priority entry in SLOT 2.
 If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."]

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

[RULE CHAR-PROHIBIT: Apply before writing. These are the only character rules for Branch B:
  1. Zero backtick characters (`). None anywhere in the card output.
  2. Zero angle-bracket characters (< and >). None anywhere in the card output.
  3. No pound-sign header lines.
  4. Max 80 characters per line.
  5. Max 40 lines total.
  6. Table borders: + - | only.]

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

  [RULE COMPLETENESS: READINESS line must name every signal in the LOCKED BLOCKERS list (step 2b,
   frozen by step 2d). Any signal absent from this line is a COMPLETENESS violation.]
  [RULE EXCLUSIVITY: READINESS line must not name any signal outside the LOCKED BLOCKERS list.
   Any extra name is an EXCLUSIVITY violation.]
  READINESS: {label} -- {every blocker name from LOCKED list, or "none"}

Section 4 -- Next step:
  [RULE NEXT-CONCRETE: Must name specific skill and namespace. No generic steps.]
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-03: Output format + phrasing register (verification scan + inline annotations)

Axis: Output format + phrasing register -- inline [RULE] annotations declaring constraints at the
governed template position, immediately followed by an active COMPLETENESS CHECK / EXCLUSIVITY
CHECK scan at the same position; no standalone phase-level LOCK step (only embedded list-closure
clause from R2).
Hypothesis: V-02 R3 showed the scan substitutes action for recall; V-03 R3 showed inline [RULE]
annotations substitute local declaration for cross-phase recall; placing declaration then
verification at the same template site creates two co-located enforcement layers -- the annotation
commits the model to the rule, the scan forces it to execute the rule -- without requiring a
phase-level LOCK. Tests whether proximity (declaration + verification at the write point) can
compensate for the absence of a pre-commitment LOCK.

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
[RULE SLOT1-SOURCE: PHASE 1 values only -- do not re-derive in this slot.]
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. Total row: **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if not in strategy.md.

### SLOT 2 -- OPEN SIGNALS
One line per OPEN signal, plain text:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None -- all planned signals gathered." if total_open == 0.

### SLOT 3 -- READINESS
[RULE COMPLETENESS: The sentence below must name every signal in the PHASE 2 BLOCKERS list.
 Any BLOCKER name absent from the sentence is a COMPLETENESS violation.]
[RULE EXCLUSIVITY: The sentence below must not name any signal outside the PHASE 2 BLOCKERS list.
 Any name in the sentence not present in the BLOCKERS list is an EXCLUSIVITY violation.]

Before writing the readiness sentence, run the verification scan:

  COMPLETENESS CHECK: List each name from the PHASE 2 BLOCKERS list.
  For each: confirm the name appears in the draft readiness sentence.
  Any missing name is a COMPLETENESS violation. Revise the draft before proceeding.

  EXCLUSIVITY CHECK: List each signal name in the draft readiness sentence.
  For each: confirm it is present in the PHASE 2 BLOCKERS list.
  Any extra name is an EXCLUSIVITY violation. Revise the draft before proceeding.

After both checks pass, write:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence -- verified against COMPLETENESS and EXCLUSIVITY}"
  If BLOCKERS none: "Ready -- all essential signals are present."
  Example (BLOCKERS = prove-analysis, review-design):
    "Not ready -- missing prove-analysis (prove) and review-design (review)."

### SLOT 4 -- NEXT STEP
[RULE NEXT-CONCRETE: Must name a specific skill and namespace. Generic steps fail this slot.
 Source: highest-priority entry in SLOT 2.
 If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."]

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

[RULE CHAR-PROHIBIT: Apply before writing. These are the only format rules for Branch B:
  1. Zero backtick characters (`). None anywhere in the card output.
  2. Zero angle-bracket characters (< and >). None anywhere in the card output.
  3. No pound-sign header lines.
  4. Max 80 characters per line.
  5. Max 40 lines total.
  6. Table borders: + - | only.]

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

  [RULE COMPLETENESS: READINESS line must name every signal in the PHASE 2 BLOCKERS list.
   Any absent BLOCKER name is a COMPLETENESS violation.]
  [RULE EXCLUSIVITY: READINESS line must not name any signal outside the PHASE 2 BLOCKERS list.
   Any extra name is an EXCLUSIVITY violation.]

  Before writing the READINESS line, run:
  COMPLETENESS CHECK: list each BLOCKER name, confirm each appears in the draft line.
  EXCLUSIVITY CHECK: list each name in the draft line, confirm none are outside BLOCKERS.
  Any violation: revise until both checks pass.

  READINESS: {label} -- {blocker names, or "none"}

Section 4 -- Next step:
  [RULE NEXT-CONCRETE: Must name specific skill and namespace. No generic steps.]
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-04: Combined triple (standalone LOCK + verification scan + inline annotations)

Axis: Combined -- standalone LOCK step (C-15) + in-render verification scan (C-16) + inline [RULE]
annotations at all governed template positions (C-17).
Hypothesis: V-04 R3 combined LOCK + scan and scored 100/100 under v3 but lacks inline annotations
(fails C-17 under v4); V-03 R3 combined inline annotations with an inline freeze (satisfies C-17
but not C-15); V-04 R4 tests whether adding inline [RULE COMPLETENESS] / [RULE EXCLUSIVITY]
annotations immediately before the scan instructions -- so the model encounters declaration then
verification at the same template site, after a phase-level LOCK pre-committed the list -- is the
minimal design that scores 100/100 under v4.

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

[RULE BRANCH-SEAL: Read --format flag. Execute ONE branch only. Do not reference the other
 branch's format descriptions when executing the active branch.]

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
[RULE SLOT1-SOURCE: PHASE 1 values only -- do not re-derive in this slot.]
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. Total row: **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if not in strategy.md.

### SLOT 2 -- OPEN SIGNALS
One line per OPEN signal, plain text:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None -- all planned signals gathered." if total_open == 0.

### SLOT 3 -- READINESS
[RULE COMPLETENESS: The sentence written below must name every signal in the LOCKED BLOCKERS
 list (step 2b, frozen by step 2d). Any signal in that list not appearing in the sentence is
 a COMPLETENESS violation.]
[RULE EXCLUSIVITY: The sentence written below must not name any signal outside the LOCKED
 BLOCKERS list. Any extra name in the sentence is an EXCLUSIVITY violation.]

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
[RULE NEXT-CONCRETE: Must name a specific skill and namespace. Generic steps fail this slot.
 Source: highest-priority entry in SLOT 2.
 If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."]

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

[RULE CHAR-PROHIBIT: Apply before writing. These are the only format rules for Branch B:
  1. Zero backtick characters (`). None anywhere in the card output.
  2. Zero angle-bracket characters (< and >). None anywhere in the card output.
  3. No pound-sign header lines.
  4. Max 80 characters per line.
  5. Max 40 lines total.
  6. Table borders: + - | only.]

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

  [RULE COMPLETENESS: READINESS line must name every signal in the LOCKED BLOCKERS list (step 2b,
   frozen by step 2d). Any absent BLOCKER name is a COMPLETENESS violation.]
  [RULE EXCLUSIVITY: READINESS line must not name any signal outside the LOCKED BLOCKERS list.
   Any extra name is an EXCLUSIVITY violation.]

  Before writing the READINESS line, run:
  COMPLETENESS CHECK: list each LOCKED BLOCKER name, confirm each appears in the draft line.
  EXCLUSIVITY CHECK: list each name in the draft line, confirm none are outside LOCKED BLOCKERS.
  Any violation: revise until both checks pass.

  READINESS: {label} -- {blocker names from LOCKED list, or "none"}

Section 4 -- Next step:
  [RULE NEXT-CONCRETE: Must name specific skill and namespace. No generic steps.]
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-05: Combined ceiling (contract register + LOCK + scan + inline annotations)

Axis: Combined ceiling -- G-n contract register (R2 V-05) + standalone LOCK (R3 V-01) + in-render
G-7a/G-7b verification scan (R3 V-02/V-05) + inline [RULE G-7a] / [RULE G-7b] annotations at
all governed template positions (C-17).
Hypothesis: V-05 R3 was the ceiling design (contract + LOCK + scan) but lacked inline annotations,
failing C-17 under v4; adding inline [RULE] markers at template positions -- where the rule name
matches the contract guarantee label (e.g., [RULE G-7a COMPLETENESS]) -- creates a direct chain:
contract register declares G-7a at the top, phase-level LOCK freezes the list, inline annotation
re-asserts G-7a at the governed position, scan verifies G-7a before write; every known failure
mode covered at every structural level.

```
/topic:report produces a shareable status artifact for a topic.

This skill makes the following output guarantees:

  G-1. One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
  G-2. Artifact contains a progress table with one row per planned signal and accurate counts.
  G-3. Every open signal is listed with namespace, skill type, and owner populated.
  G-4. Readiness statement present and consistent with progress table counts.
  G-5. One concrete next step naming a specific skill and namespace.
  G-6. When --format teams is set: single ASCII card, max 40 lines, max 80 chars wide, all four
       sections present.
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

[RULE BRANCH-SEAL: Read --format flag. Execute ONE branch only. Do not reference the other
 branch's format descriptions when executing the active branch.]

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
[RULE SLOT1-SOURCE: PHASE 1 values only -- do not re-derive in this slot.]
Markdown table: Namespace | Skill | Priority | Status | Owner
One row per planned signal. Total row: **Total** | | | {total_done}/{total_planned} ({pct}%) |
Owner = "unassigned" if not in strategy.md.

SLOT 2 -- OPEN SIGNALS (fulfills G-3)
One line per OPEN signal, plain text, no code fencing:
  - namespace: {ns} / skill: {skill-type} / owner: {owner}
"None -- all planned signals gathered." if total_open == 0.

SLOT 3 -- READINESS (fulfills G-4, G-7)
[RULE G-7a COMPLETENESS: The sentence written below must name every signal in the LOCKED BLOCKERS
 list (step 2b, frozen by step 2d). Any signal in that list absent from the sentence is a G-7a
 violation. Use the LOCKED list exactly as emitted -- no substitutions or additions.]
[RULE G-7b EXCLUSIVITY: The sentence written below must not name any signal outside the LOCKED
 BLOCKERS list. Any name in the sentence not present in the LOCKED list is a G-7b violation.]

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
[RULE NEXT-CONCRETE: Must name a specific skill and namespace. Generic steps fail G-5.
 Source: highest-priority entry in SLOT 2.
 If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."]

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

[RULE G-8 VERIFICATION: Before writing, confirm the card satisfies G-8 (fulfills G-8):
  Backtick count = 0.      Scan every character. Any backtick (`) is a G-8 violation.
  Angle-bracket count = 0. Scan every character. Any < or > is a G-8 violation.
  No pound-sign header lines.
  Max 40 lines total.
  Max 80 characters per line.
  Table borders use only: + - |]

Card content (four sections required, fulfills G-1 through G-8):

  TOPIC REPORT: {topic}
  DATE: {date}

  [RULE TABLE-FORMAT: Table borders use only + - | characters. No markdown table syntax.]
  +--------------+------------+--------+------------+
  | Namespace    | Skill      | Status | Owner      |
  +--------------+------------+--------+------------+
  | {ns}         | {skill}    | DONE   | {owner}    |
  | {ns}         | {skill}    | OPEN   | {owner}    |
  +--------------+------------+--------+------------+
  Total: {total_done}/{total_planned} ({pct}%)

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  [RULE G-7a COMPLETENESS: READINESS line must name every signal in the LOCKED BLOCKERS list
   (step 2b, frozen by step 2d). Any absent BLOCKER name is a G-7a violation.]
  [RULE G-7b EXCLUSIVITY: READINESS line must not name any signal outside the LOCKED BLOCKERS
   list. Any extra name is a G-7b violation.]

  Before writing the READINESS line, run:
  G-7a COMPLETENESS SCAN: confirm every LOCKED BLOCKER name appears in the draft line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the draft line is outside LOCKED BLOCKERS.
  Any violation: revise until both scans pass.

  READINESS: {label} -- {blocker names from LOCKED list, or "none"}

  [RULE NEXT-CONCRETE: Must name specific skill and namespace. No generic steps. Fulfills G-5.]
  NEXT: {skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```
