Written to `simulations/quest/variations/topic-report-variations-R5-2026-03-14.md`.

---

## Variations: topic-report R5

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Phrasing register (C-20 isolation) | Two-part correct/violation examples inside each [RULE] at SLOT 3; no contract register; LOCK + scan unchanged from R4 V-04 baseline |
| **V-02** | Lifecycle emphasis (C-18 explicit) | Named `=== THREE-LAYER WRITE POINT ===` block at SLOT 3 labels all three enforcement layers as a structural mandate; no worked examples |
| **V-03** | Output format (C-20 compact form) | Same axis as V-01 but compact single-line examples — "... not '...' (names omitted)" — tests whether example density is a live-run variable |
| **V-04** | Combined: C-19 + C-20 | R4 V-05 baseline (C-18+C-19 contract chaining) + multi-line worked examples on [RULE G-7a]/[RULE G-7b] — R5 minimal golden candidate |
| **V-05** | Combined ceiling: C-18 explicit + C-19 + C-20 + inertia framing | All of V-04 + explicit three-layer header + NEXT STEP anchored to stall cost ("Leaving this open holds the topic at Not Ready") |

---

**Predicted scores under v5** (aspirational max = 12):

| Variation | C-18 | C-19 | C-20 | Aspirational | Composite |
|-----------|------|------|------|-------------|-----------|
| V-01 | PASS | FAIL | PASS | 11/12 | ~99.2 |
| V-02 | PASS | FAIL | FAIL | 10/12 | ~98.3 |
| V-03 | PASS | FAIL | PASS* | 11/12 | ~99.2 |
| V-04 | PASS | PASS | PASS | 12/12 | **100** |
| V-05 | PASS | PASS | PASS | 12/12 | **100** |

*V-03 C-20 is conditional — compact one-liner must still name both the correct output pattern and the violation pattern to satisfy the rubric criterion.

**Key discriminators:**
- V-01 vs V-04 R4: adds worked examples only (C-20 isolated)
- V-02 vs V-04 R4: adds explicit three-layer header only (C-18 explicit vs. structural)
- V-03 vs V-01: compact example form vs. verbose — density axis for C-20
- V-04 vs V-05 R4: adds C-20 examples to the contract foundation — minimal golden candidate
- V-05 vs V-04 R5: adds explicit three-layer header + inertia framing — ceiling reliability test

**Recommended scoring order:** V-02 first (establishes explicit C-18 baseline without C-20) → V-01 + V-03 (calibrate C-20 verbose vs. compact) → V-04 as R5 minimal golden → V-05 as full ceiling.
--|
| V-01 | PASS | FAIL | PASS | 11/12 | ~99.2 |
| V-02 | PASS | FAIL | FAIL | 10/12 | ~98.3 |
| V-03 | PASS | FAIL | PASS* | 11/12 | ~99.2 |
| V-04 | PASS | PASS | PASS | 12/12 | **100** |
| V-05 | PASS | PASS | PASS | 12/12 | **100** |

*V-03 C-20 PASS is conditional: compact examples must include both a correct output form and
 a violation label at the governed slot. Rubric requires a "correct/violation example" -- single
 line may satisfy the letter if it names both cases, but is the riskier design.

R4 baseline under v5:
- V-04 R4: C-18 PASS, C-19 FAIL, C-20 FAIL -- aspirational ~9-10/12 (discrepancy in rubric
  notes; scorecard to resolve)
- V-05 R4: C-18 PASS, C-19 PASS, C-20 FAIL -- aspirational 10/12

No R4 variation passes C-20. The R5 discriminator is C-20 (worked examples). V-04 R5 + V-05 R5
combine C-20 with the R4 contract foundation to reach the 12/12 ceiling.

**Minimal R5 increment: V-04.** Takes V-05 R4 (the minimal C-19 design) and adds C-20 examples
at the lowest complexity cost. Expected 100/100 under v5.

**Single-axis discriminators:**
- V-01 vs V-04 R4: V-01 adds worked examples (C-20) in verbose two-part form; all else identical
- V-02 vs V-04 R4: V-02 adds explicit three-layer write-point header; no examples
- V-03 vs V-01:    V-03 uses compact inline example form; V-01 uses verbose two-part form
- V-04 vs V-05 R4: V-04 adds worked examples (C-20) to the V-05 R4 contract foundation
- V-05 vs V-04 R5: V-05 adds explicit three-layer header + inertia framing at NEXT STEP

**Recommended scoring order:** V-02 to establish C-18 explicit vs. structural (expected 10/12) --
V-01 and V-03 to calibrate C-20 verbose vs. compact form -- V-04 as R5 minimal golden candidate --
V-05 as full ceiling.

---

## V-01: Phrasing register (worked examples in [RULE] annotations, C-20 isolation)

Axis: Phrasing register -- adds structured two-part correct/violation examples inside [RULE
COMPLETENESS] and [RULE EXCLUSIVITY] at SLOT 3 and Branch B Section 3; no contract register
(no C-19); standalone LOCK and scan unchanged from R4 V-04 baseline (C-15, C-16, C-17 all
retained).
Hypothesis: R4 V-01 isolated C-20 but lacked C-15 and C-16 -- the absence of LOCK and scan
limited its score to 97.8. R5 V-01 tests C-20 on top of the R4 minimal golden (which already
has C-15+C-16+C-17+C-18), so any lift from worked examples is attributable purely to C-20
without entanglement with the LOCK or scan failure modes.

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
 list (step 2b, frozen by step 2d). Any signal in that list absent from the sentence is a
 COMPLETENESS violation. Use the LOCKED list exactly as emitted -- no substitutions.
   correct:   "Not ready -- missing prove/analysis (prove) and review/design (review)."
              (both BLOCKER names present)
   violation: "Not ready -- missing prove/analysis (prove)."
              (review/design is in BLOCKERS but absent from sentence -- COMPLETENESS violation)]

[RULE EXCLUSIVITY: The sentence written below must not name any signal outside the LOCKED
 BLOCKERS list. Any name in the sentence not present in the LOCKED list is an EXCLUSIVITY
 violation, even if that signal is OPEN.
   correct:   "Not ready -- missing prove/analysis (prove)."
              (only BLOCKER names present)
   violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)."
              (scout/market is OPEN but not in BLOCKERS list -- EXCLUSIVITY violation)]

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
  Example (BLOCKERS = prove/analysis, review/design):
    "Not ready -- missing prove/analysis (prove) and review/design (review)."

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

  [RULE COMPLETENESS: READINESS line must name every signal in the LOCKED BLOCKERS list
   (step 2b, frozen by step 2d). Any absent BLOCKER name is a COMPLETENESS violation.
     correct:   "NOT READY -- scout/market, prove/analysis" (all BLOCKER names present)
     violation: "NOT READY -- scout/market" (prove/analysis in BLOCKERS but absent from line)]

  [RULE EXCLUSIVITY: READINESS line must not name any signal outside the LOCKED BLOCKERS list.
   Any extra name is an EXCLUSIVITY violation.
     correct:   "NOT READY -- scout/market" (only names from BLOCKERS list)
     violation: "NOT READY -- scout/market, review/design" (review/design not in BLOCKERS)]

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

## V-02: Lifecycle emphasis (explicit three-layer write-point header, no worked examples)

Axis: Lifecycle emphasis -- a named THREE-LAYER WRITE POINT block at SLOT 3 and Branch B
Section 3 explicitly labels all three enforcement layers (LAYER 1 DECLARE / LAYER 2 ANCHOR /
LAYER 3 VERIFY) as a structural mandate that must be executed in order; no worked examples added;
all other mechanics identical to R4 V-04.
Hypothesis: R4 V-04 achieves three-layer co-location (C-18) through structural presence alone --
the [RULE] annotations, the LOCKED list reference in the scan, and the scan itself all appear at
SLOT 3 without a named header. R5 V-02 tests whether naming C-18 as an explicit mandate (giving
the model a recovery point that enumerates all three required layers before it encounters any of
them) improves live-run consistency without the added overhead of worked examples. Isolates the
lifecycle-emphasis axis from C-20 to measure each contribution separately.

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

=== THREE-LAYER WRITE POINT ===
All three enforcement layers are active at this write point. No cross-phase recall required.
  LAYER 1 -- DECLARE:  [RULE COMPLETENESS] and [RULE EXCLUSIVITY] annotations immediately below.
  LAYER 2 -- ANCHOR:   LOCKED BLOCKERS list from step 2d -- referenced by name in the scan.
  LAYER 3 -- VERIFY:   COMPLETENESS CHECK and EXCLUSIVITY CHECK scan executes below.
Execute all three layers in order before writing the readiness sentence.
=== END THREE-LAYER WRITE POINT ===

[RULE COMPLETENESS: The sentence written below must name every signal in the LOCKED BLOCKERS
 list (step 2b, frozen by step 2d). Any signal in that list absent from the sentence is a
 COMPLETENESS violation. Use the LOCKED list exactly as emitted -- no substitutions.]

[RULE EXCLUSIVITY: The sentence written below must not name any signal outside the LOCKED
 BLOCKERS list. Any name in the sentence not present in the LOCKED list is an EXCLUSIVITY
 violation, even if that signal is OPEN.]

Execute LAYER 3 scan against the LOCKED list (Layer 2 anchor):

  COMPLETENESS CHECK: Take the LOCKED BLOCKERS list from Phase 2 (Layer 2 anchor).
  List each name. Confirm each appears in the draft readiness sentence.
  Any missing name is a COMPLETENESS violation. Revise sentence before proceeding.

  EXCLUSIVITY CHECK: List each signal name in the draft readiness sentence.
  Confirm each is present in the LOCKED BLOCKERS list (Layer 2 anchor).
  Any name outside the LOCKED BLOCKERS list is an EXCLUSIVITY violation.
  Revise sentence before proceeding.

After all three layers satisfied:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
  If BLOCKERS none: "Ready -- all essential signals are present."
  Example (BLOCKERS = prove/analysis, review/design):
    "Not ready -- missing prove/analysis (prove) and review/design (review)."

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

  === THREE-LAYER WRITE POINT ===
  LAYER 1 -- DECLARE: [RULE COMPLETENESS] and [RULE EXCLUSIVITY] below.
  LAYER 2 -- ANCHOR:  LOCKED BLOCKERS list (step 2d) -- no revision permitted.
  LAYER 3 -- VERIFY:  COMPLETENESS CHECK and EXCLUSIVITY CHECK below.
  Execute all three before writing READINESS line.
  === END THREE-LAYER WRITE POINT ===

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  [RULE COMPLETENESS: READINESS line must name every signal in the LOCKED BLOCKERS list (step 2b,
   frozen by step 2d). Any absent BLOCKER name is a COMPLETENESS violation.]

  [RULE EXCLUSIVITY: READINESS line must not name any signal outside the LOCKED BLOCKERS list.
   Any extra name is an EXCLUSIVITY violation.]

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

## V-03: Output format (compact inline example form for C-20)

Axis: Output format -- worked examples (C-20) in compact single-line inline form embedded within
each [RULE] annotation rather than the structured two-line correct:/violation: block used in
V-01; format: "[RULE COMPLETENESS: every BLOCKER named -- 'Not ready -- missing scout/market'
not 'Not ready -- missing signals' (names omitted)]"; standalone LOCK and scan unchanged from
R4 V-04 baseline; no contract register.
Hypothesis: Compact single-line examples satisfy C-20 at lower prompt overhead than V-01's
verbose form. The rubric requires "a compact correct/violation example immediately after the
rule statement" -- the compact form meets the letter of C-20 if it names both the correct
output pattern and the violation pattern at the governed slot. Testing against V-01 determines
whether example density is a live-run variable or whether only presence/absence matters.

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
[RULE COMPLETENESS: every BLOCKER name must appear in the readiness sentence --
 "Not ready -- missing prove/analysis and review/design" not "Not ready -- missing signals"
 (omitting signal names is a COMPLETENESS violation)]

[RULE EXCLUSIVITY: no name outside the BLOCKERS list may appear in the readiness sentence --
 "Not ready -- missing prove/analysis" not "Not ready -- missing prove/analysis and scout/market"
 (scout/market outside BLOCKERS list is an EXCLUSIVITY violation)]

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
  Example (BLOCKERS = prove/analysis, review/design):
    "Not ready -- missing prove/analysis (prove) and review/design (review)."

### SLOT 4 -- NEXT STEP
[RULE NEXT-CONCRETE: name a specific skill and namespace -- "Run /scout:feasibility (scout)"
 not "gather more signals" (generic steps violate this rule)]

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

  [RULE COMPLETENESS: READINESS line must name every BLOCKER --
   "NOT READY -- scout/market, prove/analysis" not "NOT READY -- signals missing"
   (names omitted is a COMPLETENESS violation)]

  [RULE EXCLUSIVITY: READINESS line must not name signals outside BLOCKERS --
   "NOT READY -- scout/market" not "NOT READY -- scout/market, review/design"
   (review/design not in BLOCKERS is an EXCLUSIVITY violation)]

  Before writing the READINESS line, run:
  COMPLETENESS CHECK: list each LOCKED BLOCKER name, confirm each appears in the draft line.
  EXCLUSIVITY CHECK: list each name in the draft line, confirm none are outside LOCKED BLOCKERS.
  Any violation: revise until both checks pass.

  READINESS: {label} -- {blocker names from LOCKED list, or "none"}

Section 4 -- Next step:
  [RULE NEXT-CONCRETE: name a specific skill and namespace, not a generic step.]
  NEXT: {concrete skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-04: Combined C-19 + C-20 (contract register + worked examples -- R5 minimal golden candidate)

Axis: Combined -- G-n contract register with G-7a/G-7b label chaining (C-19, from R4 V-05
baseline) + multi-line correct/violation worked examples added to [RULE G-7a] and [RULE G-7b]
annotations at SLOT 3 and Branch B Section 3 (C-20); three-layer co-location (C-18) present
structurally as in R4 V-05; no explicit THREE-LAYER block header (reserved for V-05 ceiling).
Hypothesis: R4 V-05 achieves C-18 + C-19 but not C-20 (scores 10/12 under v5). Adding worked
examples to the [RULE G-7a]/[RULE G-7b] annotations within the established contract chain
(register label -> annotation label -> scan header label) passes all three new v5 criteria
without introducing any mechanism not already present in the R4 design. This is the R5 minimal
golden candidate: three new criteria achieved at minimum structural overhead.

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
 violation. Use the LOCKED list exactly as emitted -- no substitutions or additions.
   correct:   "Not ready -- missing prove/analysis (prove) and review/design (review)."
              (both BLOCKER names present -- satisfies G-7a)
   violation: "Not ready -- missing prove/analysis (prove)."
              (review/design in LOCKED BLOCKERS but absent from sentence -- G-7a violation)]

[RULE G-7b EXCLUSIVITY: The sentence written below must not name any signal outside the LOCKED
 BLOCKERS list. Any name in the sentence not present in the LOCKED list is a G-7b violation.
   correct:   "Not ready -- missing prove/analysis (prove)."
              (only names from LOCKED BLOCKERS -- satisfies G-7b)
   violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)."
              (scout/market not in LOCKED BLOCKERS list -- G-7b violation)]

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
  Example (BLOCKERS = prove/analysis, review/design):
    "Not ready -- missing prove/analysis (prove) and review/design (review)."

SLOT 4 -- NEXT STEP (fulfills G-5)
[RULE NEXT-CONCRETE: Must name a specific skill and namespace. Generic steps fail G-5.
 Source: highest-priority entry in SLOT 2.
 If SLOT 2 empty: "Run /topic:story to synthesize all gathered signals."]

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

[RULE G-8 VERIFICATION: Before writing, confirm the card satisfies G-8:
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
   (step 2b, frozen by step 2d). Any absent BLOCKER name is a G-7a violation.
     correct:   "NOT READY -- scout/market, prove/analysis" (all BLOCKER names present)
     violation: "NOT READY -- scout/market" (prove/analysis in BLOCKERS but absent from line)]

  [RULE G-7b EXCLUSIVITY: READINESS line must not name any signal outside the LOCKED BLOCKERS
   list. Any extra name is a G-7b violation.
     correct:   "NOT READY -- scout/market" (only names from LOCKED BLOCKERS list)
     violation: "NOT READY -- scout/market, review/design" (review/design not in BLOCKERS)]

  G-7a COMPLETENESS SCAN: confirm every LOCKED BLOCKER name appears in the draft line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the draft line is outside LOCKED BLOCKERS.
  Any violation: revise until both scans pass.

  READINESS: {label} -- {blocker names from LOCKED list, or "none"}

  [RULE NEXT-CONCRETE: Must name specific skill and namespace. No generic steps. Fulfills G-5.]
  NEXT: {skill} ({namespace})

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```

---

## V-05: Combined ceiling (explicit three-layer header + C-19 + C-20 + inertia framing)

Axis: Combined ceiling -- all of V-04 R5 (G-n contract register C-19 + worked examples C-20)
plus an explicit THREE-LAYER WRITE POINT header at SLOT 3 and Branch B Section 3 (names all
three enforcement layers as a structural mandate, strengthening C-18 from structural consequence
to explicit directive) and inertia framing at SLOT 4 (anchors next step to stall cost: "Leaving
{skill} open holds the topic at {current readiness state}").
Hypothesis: V-04 R5 achieves 12/12 aspirational through structural mechanisms; V-05 R5 adds
explicit three-layer naming and inertia framing as reliability mechanisms that do not add new
criteria but reduce live-run variance. The explicit write-point header gives the model a named
recovery point if attention degrades mid-generation at SLOT 3; inertia framing forces a concrete
cost statement at SLOT 4 that improves C-05 specificity. Same predicted score as V-04 (12/12)
but expected higher practical consistency across runs -- the R5 ceiling design.

```
/topic:report produces a shareable status artifact for a topic.

This skill makes the following output guarantees:

  G-1. One artifact written to simulations/{topic}/status-{date}.md; path echoed on completion.
  G-2. Artifact contains a progress table with one row per planned signal and accurate counts.
  G-3. Every open signal is listed with namespace, skill type, and owner populated.
  G-4. Readiness statement present and consistent with progress table counts.
  G-5. One concrete next step naming a specific skill and namespace, anchored to stall cost.
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

=== THREE-LAYER WRITE POINT ===
All three enforcement layers are active at this write point. No cross-phase recall required.
  LAYER 1 -- DECLARE:  [RULE G-7a] and [RULE G-7b] annotations immediately below.
  LAYER 2 -- ANCHOR:   LOCKED BLOCKERS list from step 2d -- referenced by name in G-7 scans.
  LAYER 3 -- VERIFY:   G-7a COMPLETENESS SCAN and G-7b EXCLUSIVITY SCAN execute below.
Execute all three layers in order before writing the readiness sentence.
=== END THREE-LAYER WRITE POINT ===

[RULE G-7a COMPLETENESS: The sentence written below must name every signal in the LOCKED BLOCKERS
 list (step 2b, frozen by step 2d). Any signal in that list absent from the sentence is a G-7a
 violation. Use the LOCKED list exactly as emitted -- no substitutions or additions.
   correct:   "Not ready -- missing prove/analysis (prove) and review/design (review)."
              (both BLOCKER names present -- satisfies G-7a)
   violation: "Not ready -- missing prove/analysis (prove)."
              (review/design in LOCKED BLOCKERS but absent from sentence -- G-7a violation)]

[RULE G-7b EXCLUSIVITY: The sentence written below must not name any signal outside the LOCKED
 BLOCKERS list. Any name in the sentence not present in the LOCKED list is a G-7b violation.
   correct:   "Not ready -- missing prove/analysis (prove)."
              (only names from LOCKED BLOCKERS -- satisfies G-7b)
   violation: "Not ready -- missing prove/analysis (prove) and scout/market (scout)."
              (scout/market not in LOCKED BLOCKERS list -- G-7b violation)]

Execute LAYER 3 -- G-7 verification scan (LAYER 2 LOCKED list as reference):

  G-7a COMPLETENESS SCAN: Take the LOCKED BLOCKERS list from Phase 2 (Layer 2 anchor).
  List each signal name. Confirm each appears in the draft readiness sentence.
  Any missing name is a G-7a violation. Revise the draft before proceeding.

  G-7b EXCLUSIVITY SCAN: List each signal name in the draft readiness sentence.
  Confirm each is present in the LOCKED BLOCKERS list (Layer 2 anchor).
  Any extra name is a G-7b violation. Revise the draft before proceeding.

After all three layers satisfied:
  "Readiness: [Ready | Not Ready | Conditionally Ready]"
  "{one sentence}"
  If BLOCKERS none: "Ready -- all essential signals are present."
  Example (BLOCKERS = prove/analysis, review/design):
    "Not ready -- missing prove/analysis (prove) and review/design (review)."

SLOT 4 -- NEXT STEP (fulfills G-5)
[RULE NEXT-CONCRETE: Must name a specific skill and namespace. Anchor to stall cost:
 state the concrete action, then the cost of not acting -- "Run /scout:feasibility (scout).
 Leaving this open holds the topic at Not Ready." Generic steps (e.g., "gather more signals")
 fail G-5. Source: highest-priority entry in SLOT 2.
 If SLOT 2 empty: "Run /topic:story (topic). All essential signals present -- ready to move
 from gather phase to synthesis phase."]

====================================================================
BRANCH B -- TEAMS FORMAT (execute only when --format teams IS set)
[This branch is self-contained. Do not reference Branch A instructions.]
====================================================================

Write simulations/{topic}/status-{date}.md.

[RULE G-8 VERIFICATION: Before writing, confirm the card satisfies G-8:
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

  === THREE-LAYER WRITE POINT ===
  LAYER 1 -- DECLARE: [RULE G-7a] and [RULE G-7b] below.
  LAYER 2 -- ANCHOR:  LOCKED BLOCKERS list (step 2d) -- referenced in scans.
  LAYER 3 -- VERIFY:  G-7a and G-7b scans below.
  Execute all three before writing READINESS line.
  === END THREE-LAYER WRITE POINT ===

  OPEN ({total_open}):
    {namespace}/{skill} ({owner})

  [RULE G-7a COMPLETENESS: READINESS line must name every signal in the LOCKED BLOCKERS list
   (step 2b, frozen by step 2d). Any absent BLOCKER name is a G-7a violation.
     correct:   "NOT READY -- scout/market, prove/analysis" (all BLOCKER names present)
     violation: "NOT READY -- scout/market" (prove/analysis in BLOCKERS but absent from line)]

  [RULE G-7b EXCLUSIVITY: READINESS line must not name any signal outside the LOCKED BLOCKERS
   list. Any extra name is a G-7b violation.
     correct:   "NOT READY -- scout/market" (only names from LOCKED BLOCKERS list)
     violation: "NOT READY -- scout/market, review/design" (review/design not in BLOCKERS)]

  G-7a COMPLETENESS SCAN: confirm every LOCKED BLOCKER name appears in the draft line.
  G-7b EXCLUSIVITY SCAN: confirm no name in the draft line is outside LOCKED BLOCKERS.
  Any violation: revise until both scans pass.

  READINESS: {label} -- {blocker names from LOCKED list, or "none"}

  [RULE NEXT-CONCRETE: Name specific skill and namespace. Anchor to stall cost. Fulfills G-5.]
  NEXT: {skill} ({namespace}) -- leaving open holds topic at {readiness label}

=== PHASE 4: CONFIRM ===

"Report written to simulations/{topic}/status-{date}.md"
```
