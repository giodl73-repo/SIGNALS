Written to `simulations/quest/variations/topic-status-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — `topic-status`

### Summary

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Phrasing register (command-mode) | Every instruction is a verb-object directive, zero prose. Structural guarantees survive in template shape, not explanatory sentences. |
| **V-02** | Output format (template-first declaration) | Complete output skeleton shown *before* any instructions — model absorbs C-12 (gap-first) and C-10 (9-row table) by seeing the template, not by being told. |
| **V-03** | Role sequence (per-signal assertion chain) | Replace "find gaps" with "evaluate each planned signal as PRESENT/NOT_PRESENT." NOT_PRESENT set IS the gap list — consistency guaranteed by construction. |
| **V-04** | Inertia framing (ship-risk / unknowns) | Rename "gaps" to "unknowns," anchor readiness verdict to a "ship risk" sentence. C-05 becomes a decision instrument, not a coverage label. |
| **V-05** | Full synthesis (all structural bonuses) | Template-first + phase gates + gap-first + pre-printed table + inertia framing. Predicted to close all 12 criteria and score 115/115. |

---

### Key design decisions

**Why R1 variations don't score 115 against the v2 rubric:**
- R1 V-05: output template shows `Namespace Breakdown` *then* `Open Gaps` — C-12 fails because coverage precedes the gap list
- R1 V-02: uses instruction `"Show all 9. Zero is a valid count — don't skip"` — C-10 fails because omission is instruction-dependent, not structurally impossible
- R1 V-03: truncated, but its CONTRACT block (`"If you write to disk, the skill fails regardless of output quality. Check before Phase 3."`) is the best C-11 formulation written in this skill — inherited verbatim in all R2 variations

**C-10/C-11/C-12 are the floor in R2, not the differentiator.** Every variation bakes them in. The primary axis sits on top of that structural floor.

**Predicted ranking:** V-05 > V-02 > V-03 > V-04 > V-01

**Predicted divergence watches:**
- C-11 in V-01/V-04: phase labels present but pre-display check is a single line, not a named gate — may score as C-04 rather than C-11
- C-10 in V-03: table in display section is instruction-positioned, not template-pre-seeded — scorecard may award C-06 credit only
- C-05 in V-04: "ship risk" sentence is the richest readiness framing across all 5 variations; may outperform V-03 on that criterion specifically
- V-05 ceiling risk: the explicit `NOTE: OPEN GAPS section appears before COVERAGE line above. Do not reorder.` is the structural hedge against a C-12 failure that would drop 115 → 110
lanatory sentences
**Hypothesis:** Command-mode syntax (imperative, dense, one directive per line) reduces the instruction surface area where a model can misinterpret or partially-apply a rule. Structural guarantees survive because they live in the template shape, not in explanatory prose that can be hedged or abbreviated.

```
/topic:status -- Signal
Topic: {topic}

CONTRACT: Display only. No file written. No file modified.
Allowed: Read, Glob. Forbidden: Write, Edit, any disk-write tool.
Violation = score 0 regardless of output quality.

----- PHASE 1: DISCOVER -----

1.1  Glob: simulations/**/{topic}-*
     Record every returned path -> DISK_SIGNALS
     Zero results: DISK_SIGNALS = []

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace|skill|item-name|priority) ...]
     Missing: STRATEGY_STATUS = NOT FOUND
              PLANNED = []
              Record: "strategy.md not found"

Phase 1 complete when DISK_SIGNALS and PLANNED are both fixed.

----- PHASE 2: GAPS (complete before any percentage) -----

For each P in PLANNED:
  Match in DISK_SIGNALS for *{topic}*{P.item-name}*?
  YES -> COVERED
  NO  -> OPEN -- record: P.namespace | P.skill | P.item-name | P.priority

For each D in DISK_SIGNALS unmatched by any P:
  -> UNPLANNED -- record D

GAP LIST is now closed. Do not revise it in later phases.

Phase 2 complete when every P is COVERED or OPEN.

----- PHASE 3: COMPUTE (from Phase 2 only) -----

  total_found   = |COVERED|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)
  Consistency:  if GAP LIST non-empty and percent = 100% -> ERROR, recheck Phase 2

  Per namespace -- compute all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns]

  Readiness:
    READY        -- 0 essential OPEN
    ALMOST READY -- 1-2 essential OPEN
    NOT READY    -- 3+ essential OPEN, or STRATEGY_STATUS = NOT FOUND

  Stale: parse YYYY-MM-DD date suffix for each D in DISK_SIGNALS
    > 30 days before today -> mark STALE, record age in days

Phase 3 complete when percent, ns counts, readiness, and stale set are all fixed.

----- PHASE 4: DISPLAY -----
Pre-display gate: has any file been written? YES -> stop, report failure. NO -> continue.

TOPIC STATUS: {topic}
Strategy: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

OPEN GAPS:
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  (none: "No gaps -- all planned signals present.")

UNPLANNED:
  + {path}
  (omit section if none)

STALE (>30 days):
  ! {path}  ({N} days)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned  --  {percent}%

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
(All 9 rows required. Zero row: 0 | 0 | --)

READINESS: {READY | ALMOST READY | NOT READY} -- {one sentence from gap list}
NEXT: Run /{namespace}:{skill} to produce {item-name}.
      (omit if READY)

Phase 4 complete. No file was written.
```

---

## V-02: Output Format (Template-First Declaration)

**Axis:** Output format -- the complete output template is declared at the top of the skill prompt, before any execution instructions. The model sees what it must produce before it reads what to do.
**Hypothesis:** A model that has absorbed the output shape -- including the 9-row pre-printed table and gaps-before-coverage ordering -- before reading the steps is less likely to reorder or omit sections than one that constructs the format from instructions alone. C-12 and C-10 are satisfied by seeing the template, not by being told about them. The instructions become "how to fill the template" rather than "what to produce."

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT: This skill produces terminal output only.
No file is created. No file is modified. If you write to disk, the skill fails with score 0.
Verify no disk writes occurred before rendering the output template below.

======================================================
OUTPUT TEMPLATE -- fill every field, render to terminal
======================================================

TOPIC STATUS: {topic}
Strategy: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

OPEN GAPS:
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (if none: "No gaps -- all planned signals present.")

UNPLANNED (on disk, not in signal plan):
  + {filepath}
  ...
  (omit this section entirely if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days old)
  (omit this section entirely if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%

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
Fill all 9 rows. A namespace with no planned and no present signals renders: 0 | 0 | --

READINESS: {READY | ALMOST READY | NOT READY}
{One sentence grounded in the gap list -- not a generic statement.}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
           (Omit if READY -- no open gaps.)

======================================================

EXECUTION STEPS -- gather the values to fill the template above
--------------------------------------------------------------

Phase 1 -- DISCOVER

  1.1  Glob: simulations/**/{topic}-*
       DISK_SIGNALS = every returned path, verbatim.
       If zero: DISK_SIGNALS = []. State "No signals found on disk" and continue.

  1.2  Read: simulations/{topic}/strategy.md
       If found:   PLANNED = list of (namespace | skill | item-name | priority) entries.
                   Note the path explicitly -- this is the signal plan baseline.
       If missing: PLANNED = []. State "strategy.md not found -- no planned baseline."

Phase 2 -- GAPS (enumerate before computing any percentage)

  For each P in PLANNED: is there a path in DISK_SIGNALS matching *{topic}*{P.item-name}*?
    YES -> COVERED
    NO  -> OPEN -- this becomes a GAP line in the template (OPEN GAPS section)

  For each D in DISK_SIGNALS not matching any P.item-name -> UNPLANNED line in template.

  The complete gap list is now fixed. Do not compute coverage yet.

Phase 3 -- COMPUTE (anchored to Phase 2 results)

  total_found   = count(COVERED)
  total_planned = count(PLANNED)
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)
  Consistency check: if gap list is non-empty and percent = 100%, recheck Phase 2.

  Per namespace -- fill table rows for all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic

  Readiness:
    READY        -- all essential signals COVERED
    ALMOST READY -- 1-2 essential signals OPEN
    NOT READY    -- 3+ essential OPEN, or strategy.md not found

  Stale: for each path in DISK_SIGNALS, parse YYYY-MM-DD date suffix.
         > 30 days before today -> STALE, compute age = today - date.

Phase 4 -- RENDER

  Verify: no file has been written. If uncertain: fail rather than proceed.
  Fill in the output template at the top of this prompt. Render to terminal.
  Do not change the section order from the template. OPEN GAPS must appear before COVERAGE.
```

---

## V-03: Role Sequence (Per-Signal Assertion Chain)

**Axis:** Role sequence -- the skill evaluates each planned signal as an individual boolean assertion (PRESENT / NOT_PRESENT) before any aggregation. The gap list is defined as "the set of FALSE assertions."
**Hypothesis:** Framing gap identification as a verification operation rather than a search-and-collect operation changes the cognitive model. The model must evaluate every planned signal individually before it can declare the gap list complete. This reduces batch-omission errors where a low-count namespace is skipped entirely. It also makes the consistency check trivial: if the assertion table has any NOT_PRESENT row, coverage < 100% by definition.

```
/topic:status for Signal -- Assertion Mode
Topic: {topic}

DISPLAY CONTRACT
This skill produces terminal output only. No file is written. No file is modified.
Permitted tools: Read, Glob only. Write and Edit are forbidden.
If you write to disk, the skill fails regardless of output quality.
>> Verify before Phase 4: has any file been written? If yes: stop and report failure.

===== PHASE 1: LOAD =====

1.1  Glob: simulations/**/{topic}-*
     DISK = set of every returned path. This set is now fixed.
     Zero results: DISK = {}. State "No signals found on disk."

1.2  Read: simulations/{topic}/strategy.md
     Found:   BASELINE = "simulations/{topic}/strategy.md"
              PLANNED = list of (namespace | skill | item-name | priority)
     Missing: BASELINE = NOT FOUND
              PLANNED = {}
              State: "No signal plan found -- assertion baseline is empty."

Phase 1 gate: DISK and PLANNED are both fixed and will not change.

===== PHASE 2: ASSERT =====

For each entry P in PLANNED, evaluate exactly one assertion:

  ASSERT: a path in DISK matches *{topic}*{P.item-name}*
  TRUE  -> P.assertion = PRESENT
  FALSE -> P.assertion = NOT_PRESENT

Evaluate every P individually before proceeding. Do not skip any entry.
The result is a complete ASSERTION TABLE:

  namespace | skill | item-name | priority | PRESENT | NOT_PRESENT

After evaluating all entries:
  GAP LIST     = all rows where NOT_PRESENT = TRUE
  COVERED LIST = all rows where PRESENT = TRUE
  UNPLANNED    = paths in DISK not matching any P.item-name

Phase 2 gate: every P in PLANNED has exactly one of PRESENT or NOT_PRESENT marked.

===== PHASE 3: AGGREGATE =====

From the ASSERTION TABLE only (no re-globbing):

  total_found   = |COVERED LIST|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Structural consistency: if GAP LIST is non-empty and percent = 100%, the assertion
  table has an error -- re-evaluate Phase 2.

  Per namespace (all 9 -- compute even if zero): ns_found and ns_planned.

  Readiness:
    READY        -- GAP LIST contains no essential entries
    ALMOST READY -- GAP LIST contains 1-2 essential entries
    NOT READY    -- GAP LIST contains 3+ essential entries, or BASELINE = NOT FOUND

  Stale: parse YYYY-MM-DD date suffix for each path in DISK.
         Age = today minus that date. If age > 30 days: mark STALE.

Phase 3 gate: percent, namespace counts, readiness verdict, and stale set all fixed.

===== PHASE 4: DISPLAY =====
Pre-display contract check: no file written or modified?
  CONFIRMED: proceed. NOT CONFIRMED: stop and report "SKILL FAILED: disk write detected."

TOPIC STATUS: {topic}
Strategy: {BASELINE}  [FOUND | NOT FOUND]

OPEN GAPS (NOT_PRESENT assertions from Phase 2):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "All assertions return PRESENT. No gaps.")

UNPLANNED (in DISK, not asserted against any planned entry):
  + {path}
  (omit section if none)

STALE (>30 days old):
  ! {path}  ({N} days)
  (omit section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%
(derived from assertion table above -- consistent by construction)

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
(All 9 rows required. Zero-assertion rows render as: 0 | 0 | --)

READINESS: {READY | ALMOST READY | NOT READY} -- {sentence grounded in GAP LIST}
NEXT: Run /{namespace}:{skill} to produce {item-name}.
      (Highest-priority NOT_PRESENT essential entry. Omit if READY.)

Phase 4 complete. No file was written.
```

---

## V-04: Inertia Framing (Ship-Risk / Unknowns)

**Axis:** Inertia framing -- gaps are framed as "unknowns before shipping" rather than missing files; the readiness verdict includes a "ship risk" line naming what the team is betting if they commit now
**Hypothesis:** Renaming "gaps" to "unknowns" and anchoring the readiness verdict to a concrete ship-risk statement changes the output from a status report into a decision instrument. C-05 (readiness verdict) becomes semantically richer because it is directly tied to a consequence, not just a count. C-09 (next step) becomes more urgent because the skill has already framed why the gap matters. The inertia framing also tests whether vocabulary shift affects model behavior or is purely cosmetic.

```
/topic:status for Signal
Topic: {topic}

This skill answers: "What does the team not know yet, and is it safe to commit to this feature?"

DISPLAY CONTRACT
Output is terminal only. No file is created. No file is modified.
Permitted tools: Read, Glob. If you write to disk, the skill fails.
>> Verify before Step 4: have any files been written? Stop if yes.

===== STEP 1: INVENTORY =====

1.1  Glob: simulations/**/{topic}-*
     EVIDENCE = every returned path. These files are what is known.
     Zero results: EVIDENCE = []. State "No evidence gathered yet."

1.2  Read: simulations/{topic}/strategy.md
     This file defines the signal plan -- what evidence was judged necessary.
     Found:   PLAN_PATH = "simulations/{topic}/strategy.md"
              PLANNED = [(namespace | skill | item-name | priority) ...]
     Missing: PLAN_PATH = NOT FOUND
              PLANNED = []
              State: "Signal plan not found -- cannot assess completeness."

Step 1 complete when EVIDENCE and PLANNED are fixed.

===== STEP 2: UNKNOWNS (enumerate before computing coverage) =====

For each P in PLANNED: is there a path in EVIDENCE matching *{topic}*{P.item-name}*?
  YES: KNOWN (covered)
  NO:  UNKNOWN (gap) -- record: P.namespace | P.skill | P.item-name | P.priority

For each path in EVIDENCE not matching any P.item-name: UNPLANNED EVIDENCE.

The complete UNKNOWNS LIST is now fixed. Do not compute coverage yet.

Step 2 complete when every planned signal is classified.

===== STEP 3: ASSESS =====

From UNKNOWNS LIST and KNOWN set (not from re-globbing):

  total_known    = count of KNOWN signals
  total_planned  = count of PLANNED signals
  percent        = total_known / total_planned * 100  (N/A if total_planned = 0)
  Consistency:   if UNKNOWNS LIST is non-empty and percent = 100%, recheck Step 2.

  Per namespace (all 9 -- include zero-signal namespaces): ns_known, ns_planned.

  Readiness:
    READY        -- UNKNOWNS LIST has no essential entries
    ALMOST READY -- UNKNOWNS LIST has 1-2 essential entries
    NOT READY    -- UNKNOWNS LIST has 3+ essential entries, or signal plan not found

  Ship risk (for the readiness line):
    READY:        "No essential unknowns -- safe to proceed."
    ALMOST READY: "Committing now means shipping without: {list essential unknowns by item-name}"
    NOT READY:    "Committing now means shipping without: {list essential unknowns by item-name}"

  Stale: parse YYYY-MM-DD date suffix for each path in EVIDENCE.
         > 30 days before today -> STALE, age = today minus that date in days.

Step 3 complete when coverage, namespace counts, readiness, ship risk, stale set all fixed.

===== STEP 4: DISPLAY =====
Pre-display check: no file written or modified?
CONFIRMED -> proceed. UNCERTAIN -> stop, report failure.

========================
TOPIC STATUS: {topic}
========================
Signal plan: {PLAN_PATH}  [FOUND | NOT FOUND]

UNKNOWNS (signals not yet gathered):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "All planned signals gathered. No unknowns.")

UNPLANNED EVIDENCE (on disk, not in signal plan):
  + {path}
  (omit section if none)

STALE EVIDENCE (>30 days old):
  ! {path}  ({N} days -- may not reflect current state)
  (omit section if none)

COVERAGE: {total_known} / {total_planned} planned signals  --  {percent}%

| Namespace | Known | Planned | % |
|-----------|-------|---------|---|
| scout     |       |         |   |
| draft     |       |         |   |
| review    |       |         |   |
| flow      |       |         |   |
| trace     |       |         |   |
| prove     |       |         |   |
| listen    |       |         |   |
| program   |       |         |   |
| topic     |       |         |   |
(All 9 rows required. Zero row: 0 | 0 | --)

READINESS: {READY | ALMOST READY | NOT READY}
Ship risk: {sentence from Step 3 -- "safe to proceed" if READY, or names essential unknowns}

NEXT: Run /{namespace}:{skill} to fill unknown: {item-name}.
      (Highest-priority essential UNKNOWN. Omit if READY.)
========================
Step 4 complete. No file was written.
```

---

## V-05: Full Synthesis (All Axes -- Targeting 115/115)

**Axes:** Template-first + phase gates + gap-first + pre-printed table + inertia framing + compact commands
**Hypothesis:** All structural guarantees aligned in a single skill body: the output template (C-10, C-12) is shown before any execution instructions; the display contract is named before any work begins (C-11); OPEN GAPS appears in the template before COVERAGE (C-12 via template ordering, not instruction); the 9-row table is pre-seeded (C-10 via template, not instruction); ship risk grounds the readiness verdict (C-05); named skill invocation targets the highest-priority gap (C-09). Phase gates prevent coverage-first shortcuts. Predicted to close all 12 criteria and score 115/115.

```
/topic:status -- Signal
Topic: {topic}

DISPLAY CONTRACT
The only output this skill produces is a terminal display.
No file is written. No file is modified. Permitted tools: Read, Glob.
If you write to disk, the skill fails with score 0 regardless of output quality.

This skill answers: "What's known, what's missing, and is it safe to commit?"

======================================================
TARGET OUTPUT -- fill every field, then render to terminal
======================================================

TOPIC STATUS: {topic}
Signal plan: simulations/{topic}/strategy.md  [FOUND | NOT FOUND]

OPEN GAPS (signals not yet gathered):
  [ ] {namespace}/{skill}  {item-name}  ({priority})
  ...
  (none: "No gaps -- all planned signals present.")

UNPLANNED EVIDENCE (on disk, not in signal plan):
  + {filepath}
  (omit this section if none)

STALE EVIDENCE (>30 days old):
  ! {filepath}  ({N} days -- may not reflect current state)
  (omit this section if none)

COVERAGE: {total_found} / {total_planned} planned signals  --  {percent}%

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
All 9 rows required. Zero row format: 0 | 0 | --

READINESS: {READY | ALMOST READY | NOT READY}
Ship risk: {consequence sentence -- "safe to proceed" if READY, or names essential gaps}

NEXT STEP: Run /{namespace}:{skill} to produce {item-name}.
           (Highest-priority essential gap. Omit if READY.)

======================================================
NOTE: OPEN GAPS section appears before COVERAGE line above.
Do not reorder. The coverage number summarizes the gap list -- not the other way around.
======================================================

EXECUTION PHASES -- compute the values to fill the target output
---------------------------------------------------------------

===== PHASE 1: DISCOVER =====
Gate: do not proceed to Phase 2 until both actions complete and results are fixed.

1.1  Glob: simulations/**/{topic}-*
     DISK_SIGNALS = [every returned path, verbatim]
     Zero results: DISK_SIGNALS = []. State "No signals found on disk" and continue.

1.2  Read: simulations/{topic}/strategy.md
     Found:   STRATEGY_STATUS = FOUND
              PLANNED = [(namespace | skill | item-name | priority) ...]
     Missing: STRATEGY_STATUS = NOT FOUND. PLANNED = [].
              Note: "Signal plan not found -- no planned baseline."
     Either way: name the path explicitly in the output. Do not silently compute against zero.

===== PHASE 2: GAPS FIRST =====
Gate: enumerate the complete gap list before computing any percentage.

For each P in PLANNED: does DISK_SIGNALS contain a path matching *{topic}*{P.item-name}*?
  YES -> COVERED
  NO  -> OPEN (gap) -- record: P.namespace | P.skill | P.item-name | P.priority

For each D in DISK_SIGNALS not matching any P.item-name:
  -> UNPLANNED -- record D.

GAP LIST is now complete and fixed.
Do not compute coverage until Phase 3.

===== PHASE 3: COMPUTE =====
Gate: all calculations derived from Phase 2 results only. No re-globbing.

  total_found   = |COVERED|
  total_planned = |PLANNED|
  percent       = total_found / total_planned * 100  (N/A if total_planned = 0)

  Consistency: if GAP LIST is non-empty and percent = 100% -- ERROR. Recheck Phase 2.

  Per namespace -- compute for all 9:
    scout, draft, review, flow, trace, prove, listen, program, topic
    ns_found[ns], ns_planned[ns]

  Readiness:
    READY        -- 0 essential entries in GAP LIST
    ALMOST READY -- 1-2 essential entries in GAP LIST
    NOT READY    -- 3+ essential entries in GAP LIST, or STRATEGY_STATUS = NOT FOUND

  Ship risk sentence:
    READY:     "No essential gaps -- safe to proceed."
    otherwise: "Committing now means shipping without: {list essential gap item-names}"

  Stale: parse YYYY-MM-DD date suffix for each path in DISK_SIGNALS.
         Age = today minus date. If > 30 days: record as STALE with age.

===== PHASE 4: DISPLAY =====
Pre-display gate: has any file been written or modified?
  YES  -> stop. Output: "SKILL FAILED: disk write detected."
  NO   -> proceed.

Fill in the target output at the top of this prompt. Render to terminal.
Render order: OPEN GAPS -> UNPLANNED -> STALE -> COVERAGE -> TABLE -> READINESS -> NEXT.
Do not change the section order defined in the target output.

Phase 4 complete. No file was written.
```

---

### Criteria coverage matrix (v2 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Signal discovery | YES | YES | YES | YES | YES |
| C-02 Coverage percentage | YES | YES | YES | YES | YES |
| C-03 Gap identification | YES | YES | YES | YES | YES |
| C-04 Display-only (stated) | YES | YES | YES | YES | YES |
| C-05 Readiness verdict | YES | YES | YES | YES+ | YES+ |
| C-06 Namespace breakdown | YES | YES | YES | YES | YES |
| C-07 Strategy cross-ref | YES | YES | YES | YES | YES |
| C-08 Recency awareness | YES | YES | YES | YES | YES |
| C-09 Actionable next step | YES | YES | YES | YES | YES |
| C-10 Structural table (template) | YES | YES+ | YES | YES | YES+ |
| C-11 Phase-gated disk-check | YES | YES | YES+ | YES | YES+ |
| C-12 Gap-first output ordering | YES | YES+ | YES | YES | YES+ |
| **Predicted score** | **110** | **113** | **112** | **112** | **115** |

`+` = strongest treatment of that criterion in this variation
`YES` = criterion met but not the leading approach
Predicted scores are estimates; actual scores depend on whether structural enforcement
is judged as meeting the pass condition versus instruction-only.

---

### Predicted vs. actual divergence watch

**Most likely scoring surprises:**
- **C-11 in V-01 and V-04:** Phase labels exist but the pre-display check is a single line, not a named gate. Scorecard may award partial credit only.
- **C-10 in V-03:** Table is in the display section but follows instruction-based positioning, not template-first declaration. May be judged C-06-equivalent rather than C-10-equivalent.
- **C-05 in V-04:** "Ship risk" sentence is the richest readiness framing across all variations. If scorecard rewards semantic quality, V-04 may outperform V-03 on C-05 despite lower structural guarantees elsewhere.
- **V-05 ceiling:** If all four `+` criteria hold, score = 115. Single failure on C-12 ordering drops to 110. The explicit ordering note at the bottom of the target output is the structural hedge against this.
