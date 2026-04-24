## Round 1 Variations — `topic-status`

Written to `simulations/quest/variations/topic-status-variations-R1-2026-03-14.md`.

---

### Summary Table

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Output format (table-centric) | 9-row namespace table makes empty-row omission impossible (C-06); fixed coverage header forces C-02 math |
| **V-02** | Phrasing register (conversational) | Direct "check/show/list" reduces over-hedging; tests whether correctness survives without structural scaffolding |
| **V-03** | Lifecycle emphasis (3-phase gates) | DISCOVER → COMPUTE → DISPLAY gates make C-04 (no-write) a named phase boundary, not buried prose |
| **V-04** | Role sequence (gap-first ordering) | Gaps enumerated before percentage computed — closes C-02's automatic fail condition (math contradicts visible gaps) |
| **V-05** | Full synthesis (all axes) | Table + phases + gap-first + strategy named + stale flagging — predicted ceiling, maximum structural guarantees |

---

### Key design decisions

**C-04 is the dominant constraint.** Every variation opens with or gates on the no-write contract. V-03/V-05 name it as a phase boundary label, not prose, making violations detectable.

**Gap-first ordering (V-04/V-05)** is the targeted fix for C-02's second fail condition — the model computing `100%` and then listing gaps that contradict it. Enumerating gaps before the math anchors the percentage.

**9-row table (V-01/V-05)** eliminates the silent empty-namespace omission path. A pre-printed row for `trace: 0/0` cannot be accidentally dropped the way a prose list can skip zero-count namespaces.

**Predicted ranking:** V-05 > V-04 > V-01 > V-03 > V-02
th.
- The 9-row namespace table (V-01/V-05) eliminates the silent omission path for empty namespaces — a consolidated prose list can skip zero-count namespaces, a pre-printed table cannot.
- V-02 tests whether conversational register produces equally correct output with less prompt overhead.
- V-05 is the predicted ceiling; V-04 is the strongest single-axis fix for C-02 correctness; V-01 is strongest for C-06.

**Predicted ranking:** V-05 > V-04 > V-01 > V-03 > V-02

---

## V-01: Output Format (Table-centric)

**Axis:** Output format — per-namespace table replaces prose/list for the namespace breakdown
**Hypothesis:** Pre-printed 9-row table forces empty-namespace rows to appear (C-06) and makes column-drop omissions structurally impossible. A fixed coverage header row makes C-02 math unavoidable.

```
You are running /topic:status for Signal.
Topic: {topic}

IMPORTANT: This skill displays only. Do not write any file. No artifact is created or modified.

---

Step 1 — SIGNAL DISCOVERY
Use the Glob tool: simulations/**/{topic}-*
List every path returned. Do not invent paths. If zero results: note "No signals found on disk" and continue.

Step 2 — STRATEGY READ
Read: simulations/{topic}/strategy.md
If found: extract the planned signal list. Each entry has namespace, skill, item-name, priority (essential/recommended/optional).
If not found: note "strategy.md not found — coverage computed against 0 planned signals" and continue with PLANNED = [].

Step 3 — CROSS-REFERENCE
For each planned signal: check if a matching file exists in the glob results.
For each discovered file: check if it appears in the strategy.
Track: COVERED, OPEN, UNPLANNED.

Step 4 — DISPLAY (terminal only — no file written)
Print the following layout exactly. Fill every table cell. Do not omit rows.

===== TOPIC STATUS: {topic} =====
Strategy: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]
Coverage:  {total_found} / {total_planned} planned signals  —  {percent}%

Namespace Breakdown:
| Namespace | Present | Planned | % |
|-----------|---------|---------|---|
| scout     |         |         |   |
| draft     |         |         |   |
| review    |         |         |   |
| flow      |         |         |   |
| trace     |         |         |   |
| prove     |         |         |   |
| listen    |         |         |   |
| program   |         |         |   |
| topic     |         |         |   |
[Fill every row. A namespace with 0 planned and 0 found shows: 0 | 0 | —]

Open Gaps (planned but not found on disk):
  [ ] {namespace}/{skill}  {item-name}  (priority: essential | recommended | optional)
  [Repeat for every OPEN signal. If no gaps: "No gaps — all planned signals present."]

Unplanned Signals (found on disk but not in strategy):
  + {filepath}
  [Omit this section entirely if none.]

READINESS: [READY | ALMOST READY | NOT READY]
Reason: {one sentence tied directly to the gap list — not a generic statement}

Next step: Run /{namespace}:{skill} to produce {item-name}.
[Highest-priority open gap. Omit if no gaps.]
=================================
```

---

## V-02: Phrasing Register (Conversational/Imperative)

**Axis:** Phrasing register — direct, conversational "check / show / list" over formal specification language
**Hypothesis:** Conversational register reduces model over-hedging, produces a leaner terminal display, and keeps output readable as a developer tool. Correctness should not degrade; the tradeoff is prompt length vs structural rigidity.

```
You are running /topic:status.
Topic: {topic}

You're showing the current signal state for this topic in the terminal. Don't write anything to disk — just display.

Here's what to do:

1. Check what's on disk
   Glob simulations/**/{topic}-* and list every file returned. Don't make up paths.
   If zero files found: say so and continue.

2. Check what was planned
   Read simulations/{topic}/strategy.md if it exists. Pull out the list of planned signals —
   each one has a namespace, skill, item name, and priority. If strategy.md isn't there,
   say so clearly and treat planned = [] going forward.

3. Match planned against disk
   For each planned signal: does a matching file exist on disk? Mark [x] if yes, [ ] if no.
   For each disk file: is it in the strategy? Flag it as unplanned if not.

4. Show the status in the terminal
   Use this format. No markdown beyond what's shown here. No prose paragraphs.

Topic: {topic}
Strategy: simulations/{topic}/strategy.md  (found | not found)

Coverage: {found} / {planned} planned signals  —  {percent}%

By namespace:
  scout    {found}/{planned}
  draft    {found}/{planned}
  review   {found}/{planned}
  flow     {found}/{planned}
  trace    {found}/{planned}
  prove    {found}/{planned}
  listen   {found}/{planned}
  program  {found}/{planned}
  topic    {found}/{planned}
Show all 9. Zero is a valid count — don't skip empty namespaces.

Gaps:
  [ ] {namespace}/{skill}  —  {item-name}  (essential | recommended | optional)
  ...
  If no gaps: "All planned signals present. No gaps."

Unplanned (on disk, not in strategy):
  + {filepath}
  (Skip this section if none.)

Readiness: READY | ALMOST READY | NOT READY
  One sentence explaining why, tied to the gap list above.

Next: Run /{namespace}:{skill} to fill {item-name}.
  (Skip if no gaps.)

Stale signals (>30 days old based on filename date): flag any whose date suffix is more than
30 days before today's date with "(stale — {N} days old)".
```

---

## V-03: Lifecycle Emphasis (Explicit 3-Phase Gates)

**Axis:** Lifecycle emphasis — three named phases with hard gates: DISCOVER → COMPUTE → DISPLAY
**Hypothesis:** Explicit phase gates prevent coverage-first shortcuts that skip gap enumeration when coverage appears high. Naming DISPLAY as a phase boundary — not prose — makes the no-write contract structurally unmissable.

```
You are running /topic:status for Signal. Topic: {topic}

CONTRACT: This skill has one output — a terminal display. No file is written. No file is modified.
If you write to disk, the skill fails regardless of output quality. Check before Phase 3.

===== PHASE 1: DISCOVER =====
Do not proceed to Phase 2 until Phase 1 is complete.

Action 1.1 — Glob disk signals
  Run Glob: simulations/**/{topic}-*
  Record every returned path as DISK_SIGNALS.
  If zero results: DISK_SIGNALS = []. Continue.

Action 1.2 — Read strategy
  Read: simulations/{topic}/strategy.md
  Record: STRATEGY_PATH = simulations/{topic}/strategy.md
  If found: extract planned signals. Each has: namespace | skill | item-name | priority.
  If not found: STRATEGY_STATUS = NOT FOUND. PLANNED = [].

Phase 1 complete when: DISK_SIGNALS list is fixed and PLANNED list is fixed.

===== PHASE 2: COMPUTE =====
Do not proceed to Phase 3 until Phase 2 is complete.

Action 2.1 — Match signals
  For each planned signal P: check if any path in DISK_SIGNALS matches {topic}-{item-name}-*.
    YES → P is COVERED.
    NO  → P is OPEN (gap).
  For each disk path D: check if D matches any planned signal.
    NO  → D is UNPLANNED.

Action 2.2 — Compute coverage
  total_found    = count of COVERED signals
  total_planned  = count of PLANNED signals
  percent        = total_found / total_planned * 100  (write "N/A" if total_planned = 0)
  Per namespace: compute ns_found and ns_planned for each of the 9 namespaces.

Action 2.3 — Determine readiness
  READY        — all essential signals COVERED
  ALMOST READY — 1 or 2 essential signals OPEN
  NOT READY    — 3+ essential signals OPEN, or strategy.md NOT FOUND

Phase 2 complete when: every signal marked COVERED or OPEN, percent computed, readiness assigned.

===== PHASE 3: DISPLAY =====
Output to terminal only. Do NOT write any file.

TOPIC STATUS: {topic}
---
Strategy: {STRATEGY_PATH}  [{FOUND | NOT FOUND}]
Coverage: {total_found} / {total_planned}  —  {percent}%

Namespace        Present  Planned
-----------      -------  -------
scout                N        N
draft                N        N
review               N        N
flow                 N        N
trace                N        N
prove                N        N
listen               N        N
program              N        N
topic                N        N
[All 9 rows required. 0/0 rows are valid.]

Open Gaps:
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  [Every OPEN signal from Phase 2. If none: "No gaps."]

Unplanned (on disk, not in strategy):
  + {path}
  [Omit section if none.]

Readiness: {READY | ALMOST READY | NOT READY} — {reason}
Next: /{namespace}:{skill}  {item-name}  [highest-priority gap; omit if READY]
---
Phase 3 complete. Confirm: no file was written.
```

---

## V-04: Role Sequence (Gap-first Ordering)

**Axis:** Role sequence — gaps enumerated before coverage percentage is computed
**Hypothesis:** Listing all open gaps before computing the percentage prevents the model from asserting a round number and then contradicting it with the gap list — which is the C-02 automatic fail condition. Gaps anchor the math; math cannot contradict the anchor.

```
You are running /topic:status for Signal.
Topic: {topic}

This skill is display-only. It writes nothing to disk.

SETUP
-----
1. Glob simulations/**/{topic}-* — record every file found on disk.
2. Read simulations/{topic}/strategy.md — extract planned signals (namespace, skill, item-name, priority).
   Name the file used as the baseline. If strategy.md is missing: say so and proceed with PLANNED = [].

GAP IDENTIFICATION (complete before computing any percentage)
------------------------------------------------------------
For each planned signal in strategy.md:
  - Check if a matching file exists in the glob results.
  - If NO match: this is a GAP. Record: namespace | skill | item-name | priority.
  - If YES match: this is COVERED.

Enumerate every gap in full before moving on. Do not compute a coverage number yet.

UNPLANNED ADDITIONS
-------------------
For each disk file that does not match any planned signal: record it as UNPLANNED.

COVERAGE COMPUTATION (runs after gap enumeration — must be consistent with it)
-----------------------
Count:
  total_found    = count of COVERED signals
  total_planned  = count of PLANNED signals
  percent        = total_found / total_planned * 100

Per namespace (9 namespaces): compute ns_found and ns_planned for each.

CONSISTENCY CHECK: if any gap is listed and percent = 100%, that is an error — recheck the match.

READINESS
---------
READY        — all essential signals COVERED
ALMOST READY — 1-2 essential signals OPEN
NOT READY    — 3+ essential signals OPEN, or strategy.md missing

DISPLAY (terminal only — no file written)
-----------------------------------------
Print in this order:

TOPIC STATUS: {topic}
Strategy: simulations/{topic}/strategy.md  [found | not found]

OPEN GAPS:
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  [ ] ...
  (If none: "All planned signals present. No gaps.")

UNPLANNED (on disk, not in strategy):
  + {filepath}
  (Omit section if none.)

COVERAGE: {total_found} / {total_planned} planned signals  —  {percent}%

By namespace:
  scout   {found}/{planned}     draft   {found}/{planned}
  review  {found}/{planned}     flow    {found}/{planned}
  trace   {found}/{planned}     prove   {found}/{planned}
  listen  {found}/{planned}     program {found}/{planned}
  topic   {found}/{planned}
  [Show all 9. Zero counts are valid — do not skip empty namespaces.]

READINESS: {READY | ALMOST READY | NOT READY}
{One sentence grounded in the gap list and coverage number above.}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
[Highest-priority open gap. Omit if no gaps.]
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Table + explicit phases + gap-first + strategy named explicitly + display contract foregrounded
**Hypothesis:** Maximum structural guarantees across all 9 rubric criteria. The display contract is named before any work begins. Gap enumeration gates the coverage math. A pre-printed 9-row table makes namespace omission impossible. Phase labels make sequencing violations detectable.

```
You are running /topic:status for Signal. Topic: {topic}

DISPLAY CONTRACT
----------------
This skill produces terminal output only. No file is created. No file is modified.
Permitted tools: Read, Glob. Do NOT use Write, Edit, or any disk-write tool.
If you write to disk, the skill fails with score 0 regardless of output quality.

===== PHASE 1: DISCOVER =====

1.1  Glob: simulations/**/{topic}-*
     Record every returned path. DISK_SIGNALS = [list].
     If zero results: DISK_SIGNALS = []. State this and continue.

1.2  Read strategy: simulations/{topic}/strategy.md
     STRATEGY_PATH = simulations/{topic}/strategy.md
     If found: extract planned signals (namespace | skill | item-name | priority).
     If not found: STRATEGY_STATUS = NOT FOUND. PLANNED = [].
     Either way, name the strategy path explicitly — do not silently compute against zero.

===== PHASE 2: GAPS FIRST =====
Enumerate every gap before computing any percentage.
For each planned signal P: does a path in DISK_SIGNALS match {topic}-{item-name}-*?
  YES → COVERED
  NO  → OPEN (gap)

Record the full gap list now:
  [ ] {namespace}/{skill}  {item-name}  (priority: essential | recommended | optional)
  [ ] ...
  If GAP LIST is empty: note "No gaps found."

Also record unplanned (DISK_SIGNALS not matched to any planned signal):
  + {filepath}
  If none: note "No unplanned signals."

===== PHASE 3: COMPUTE =====
From the gap list and covered list built in Phase 2:
  total_found   = count of COVERED
  total_planned = count of PLANNED
  percent       = total_found / total_planned * 100  (write "N/A" if total_planned = 0)

Per namespace — compute for all 9:
  scout, draft, review, flow, trace, prove, listen, program, topic
  ns_found[ns] and ns_planned[ns]

CONSISTENCY CHECK: if GAP LIST is non-empty and percent = 100%, there is an error — recheck.

Readiness:
  READY        — all essential signals COVERED
  ALMOST READY — 1 or 2 essential signals OPEN
  NOT READY    — 3+ essential signals OPEN, or STRATEGY_STATUS = NOT FOUND

Recency: for each DISK SIGNAL, check the date suffix (YYYY-MM-DD in filename).
  If date is more than 30 days before today: mark signal as STALE.

===== PHASE 4: DISPLAY =====
Print to terminal. Write no file.

========================
TOPIC STATUS: {TOPIC}
========================
Strategy: {STRATEGY_PATH}  [{FOUND | NOT FOUND}]
Coverage: {total_found} / {total_planned} planned signals  —  {percent}%

Namespace Breakdown:
| Namespace | Present | Planned | % |
|-----------|---------|---------|---|
| scout     |         |         |   |
| draft     |         |         |   |
| review    |         |         |   |
| flow      |         |         |   |
| trace     |         |         |   |
| prove     |         |         |   |
| listen    |         |         |   |
| program   |         |         |   |
| topic     |         |         |   |
[Fill every row. A namespace with 0 planned and 0 found shows: 0 | 0 | —]

Open Gaps:
{Copy GAP LIST from Phase 2 exactly.}
If GAP LIST empty: "No gaps — all planned signals present."

Stale Signals (>30 days old):
  ! {filepath}  ({N} days old)
  (Omit section if no stale signals.)

Unplanned Additions:
{Copy unplanned list from Phase 2.}
(Omit section if none.)

READINESS: {READY | ALMOST READY | NOT READY}
{One sentence grounded in the gap list and coverage number — not a generic statement.}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
[Highest-priority essential gap. Omit if READY.]
========================
Phase 4 complete. No file was written.
```
