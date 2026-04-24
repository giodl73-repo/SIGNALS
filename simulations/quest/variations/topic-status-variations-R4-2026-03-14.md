# `/quest:variate` — `topic:status` Round 4 Variations

**Rubric:** v4 (max 150) | **Target criteria:** C-17 (labeled layers), C-18 (pre-seeded assertion table), C-19 (consequence vocabulary saturation)

---

## V-01 — Labeled Redundancy Layers
**Axis:** Lifecycle emphasis
**Hypothesis:** Naming each of the three enforcement mechanisms as `[LAYER 1]`, `[LAYER 2]`, `[LAYER 3]` makes the triple-redundancy verifiable by inspection rather than requiring inference about structural distinctness. Strengthens C-13 → satisfies C-17.

---

```markdown
# topic:status

**Topic:** `{TOPIC}`
**Date:** {TODAY}
**Mode:** DISPLAY ONLY — terminal output, no files written or modified

---

## ENFORCEMENT ARCHITECTURE

This skill enforces correctness through three independently-failing layers.
Each layer targets a distinct failure mode. A skill output is valid only if all three pass.

[LAYER 1 — STRUCTURAL]
The 9-namespace output table is pre-seeded in the display template.
All nine rows are physically present before execution begins.
Empty namespaces render as `0 / 0 — —`. They cannot be omitted by instruction-following failure.
_Failure mode blocked: silent namespace omission._

[LAYER 2 — SEMANTIC]
Every signal named in `strategy.md` is evaluated individually: PRESENT or NOT_PRESENT.
Gaps are identified by name (`{namespace}/{signal-type}`), not by count.
Coverage percentage is computed from named matches, not file counts.
A consistency check blocks the output if `coverage = 100%` and any named gap is NOT_PRESENT.
_Failure mode blocked: aggregate coverage that masks named gaps._

[LAYER 3 — EXECUTION]
Before Phase 3 (DISPLAY), state explicitly: "No file has been written or modified."
If this cannot be stated truthfully, halt. Report the write violation to the user as a skill failure.
Do not proceed to display an output that required a write.
_Failure mode blocked: undetected disk writes silently degrading display-only contract._

---

## PHASE 1 — DISCOVER

**1a. Disk scan**
Glob: `simulations/**/{TOPIC}-*`
Assign all matches to `DISK_SIGNALS`.
If no matches: `DISK_SIGNALS = []`. Do not infer from memory.
Log: `Disk scan complete — {N} files found.`

**1b. Strategy scan**
Read `simulations/{TOPIC}/strategy.md`.
If not found, attempt `simulations/strategy.md`.
If neither found: `PLANNED_SIGNALS = []`. Log: `strategy.md not found — planned baseline is empty.`
Extract each planned signal name to `PLANNED_SIGNALS`. Log the file path used.

**1c. Recency scan**
For each file in `DISK_SIGNALS`, extract date from filename pattern `{TOPIC}-{signal}-{YYYY-MM-DD}.md`.
Flag any signal with date > 30 days ago as `[STALE]`.
Log: `Staleness check complete — {N} signals flagged.`

---

## PHASE 2 — COMPUTE

**2a. Coverage formula**
```
FOUND   = count(DISK_SIGNALS that match a name in PLANNED_SIGNALS)
PLANNED = count(PLANNED_SIGNALS)
COVERAGE_PCT = FOUND / PLANNED * 100   (if PLANNED = 0, output 0% and note empty baseline)
```
Consistency check: if `COVERAGE_PCT = 100%` AND any signal in PLANNED_SIGNALS is NOT_PRESENT
on disk → recompute. If contradiction persists, halt and report.

**2b. Gap list**
For each signal in `PLANNED_SIGNALS` not found in `DISK_SIGNALS`:
- Record: `{namespace}/{signal-type}` — NOT_PRESENT

Sort by namespace priority: scout → draft → review → flow → trace → prove → listen → program → topic

**2c. Readiness verdict**
```
COVERAGE_PCT = 100% AND gaps = 0  →  READY — all planned signals present
COVERAGE_PCT >= 75% AND no scout/draft gaps  →  CONDITIONALLY READY — {N} signals outstanding
Otherwise  →  NOT READY — {N} essential gaps remain
```

**2d. Next action**
Identify the single highest-priority open gap.
Map to its producing skill: `scout-feasibility → /scout:feasibility`, etc.

---

## PHASE 3 — DISPLAY

**[LAYER 3 gate]** — State before rendering:
> "No file has been written or modified. Proceeding to display."

If false: halt. Do not display output.

**Render:**

---

## TOPIC STATUS: {TOPIC}

**Strategy file:** `{STRATEGY_FILE_PATH}` _(not found — no planned baseline)_
**Disk scan pattern:** `simulations/**/{TOPIC}-*`
**As of:** {TODAY}

### COVERAGE
`{FOUND} / {PLANNED} signals present ({COVERAGE_PCT}%)`

### READINESS
`{READINESS_VERDICT}`

### SIGNAL BREAKDOWN BY NAMESPACE

| Namespace | Found | Planned | Pct | Signals Present |
|-----------|------:|--------:|----:|-----------------|
| scout     |       |         |     |                 |
| draft     |       |         |     |                 |
| review    |       |         |     |                 |
| flow      |       |         |     |                 |
| trace     |       |         |     |                 |
| prove     |       |         |     |                 |
| listen    |       |         |     |                 |
| program   |       |         |     |                 |
| topic     |       |         |     |                 |

_(All 9 rows always rendered. Zero counts display as `0 / 0 — —`.)_

### OPEN GAPS _(listed highest-priority namespace first)_
- `{namespace}/{signal-type}` — NOT_PRESENT {[STALE]}
- _(If none: "No gaps — all planned signals present.")_

### NEXT STEP
`{SKILL_INVOCATION}` — closes `{signal-name}` gap

---

_Display only. Enforcement: [LAYER 1] structural pre-seeding · [LAYER 2] named signal evaluation · [LAYER 3] pre-display write gate._
```

---

## V-02 — Assertion Table Pre-Seeded in Template
**Axis:** Output format
**Hypothesis:** Embedding the per-signal assertion table in the output template — with one row per planned signal, `PRESENT`/`NOT_PRESENT` columns pre-allocated — forces per-signal evaluation as output structure rather than as an execution instruction. Omission becomes structurally impossible. Fuses C-14 + C-15 → satisfies C-18.

---

```markdown
# topic:status

**Topic:** `{TOPIC}`
**Date:** {TODAY}
**Mode:** DISPLAY ONLY — no files written or modified

---

## HOW THIS SKILL WORKS

1. Read `strategy.md` to get the list of planned signals for `{TOPIC}`.
2. Glob `simulations/**/{TOPIC}-*` to get signals on disk.
3. **Expand the assertion table below** — one row per planned signal — filling in status.
4. Compute coverage from the completed table.
5. Display. Do not write any file.

---

## PHASE 1 — READ INPUTS

**Disk scan**
Glob: `simulations/**/{TOPIC}-*`
Assign to `DISK_SIGNALS`. If empty: `DISK_SIGNALS = []`.

**Strategy scan**
Read `simulations/{TOPIC}/strategy.md` (fallback: `simulations/strategy.md`).
If not found: note in output. `PLANNED_SIGNALS = []`.
Extract all planned signal names.

---

## PHASE 2 — BUILD ASSERTION TABLE

For each signal in `PLANNED_SIGNALS`, add one row to this template.
**Do not skip signals.** Do not collapse rows. Every planned signal gets its own row.

Fill in each column:
- **Signal:** `{TOPIC}-{namespace}-{signal-type}`
- **Namespace:** one of: scout / draft / review / flow / trace / prove / listen / program / topic
- **On Disk:** YES (if a matching file exists in `DISK_SIGNALS`) or NO
- **Status:** PRESENT or NOT_PRESENT
- **Age:** date from filename, or `—` if not on disk. Append `[STALE]` if > 30 days old.

```
ASSERTION TABLE — {TOPIC} signals
=============================================================
| Signal                              | NS      | On Disk | Status      | Age        |
|-------------------------------------|---------|---------|-------------|------------|
| {TOPIC}-{signal-1}                  | scout   | [FILL]  | [FILL]      | [FILL]     |
| {TOPIC}-{signal-2}                  | scout   | [FILL]  | [FILL]      | [FILL]     |
| {TOPIC}-{signal-3}                  | draft   | [FILL]  | [FILL]      | [FILL]     |
| ...one row per planned signal...    |         |         |             |            |
=============================================================
```

After filling the table:
- `FOUND = count(rows where Status = PRESENT)`
- `PLANNED = total rows`
- `COVERAGE_PCT = FOUND / PLANNED * 100`

Consistency check: if `COVERAGE_PCT = 100%` and any row shows `NOT_PRESENT`, recompute.

---

## PHASE 3 — COMPUTE READINESS AND GAPS

**Gaps:** All rows where `Status = NOT_PRESENT`, sorted by namespace priority:
  scout → draft → review → flow → trace → prove → listen → program → topic

**Readiness verdict:**
- All PRESENT → `READY — all planned signals on disk`
- ≥ 75% PRESENT, no scout/draft gaps → `CONDITIONALLY READY — {N} outstanding`
- Otherwise → `NOT READY — {N} gaps remain`

**Next step:** Highest-priority NOT_PRESENT row → map to producing skill.

---

## PHASE 4 — PRE-DISPLAY GATE

Before displaying output, state:
> "No file was written or modified during this execution."

If false: halt. Report the write as a skill failure. Do not display results.

---

## DISPLAY OUTPUT

---

## TOPIC STATUS: {TOPIC}

**Strategy file:** `{PATH}` _(or: not found)_
**Disk scan:** `simulations/**/{TOPIC}-*` — {N} files found
**As of:** {TODAY}

### PER-SIGNAL ASSERTION TABLE

_(The completed assertion table from Phase 2 goes here, fully populated.)_

### COVERAGE SUMMARY
`{FOUND} / {PLANNED} signals present ({COVERAGE_PCT}%)`

### NAMESPACE BREAKDOWN

| Namespace | Found | Planned | Coverage |
|-----------|------:|--------:|---------:|
| scout     |       |         |          |
| draft     |       |         |          |
| review    |       |         |          |
| flow      |       |         |          |
| trace     |       |         |          |
| prove     |       |         |          |
| listen    |       |         |          |
| program   |       |         |          |
| topic     |       |         |          |

_(All 9 rows rendered. Zero-count rows show `0 / 0 — 0%`.)_

### OPEN GAPS
_(All NOT_PRESENT rows from assertion table, highest-priority namespace first.)_
_(If none: "No gaps — all planned signals present.")_

### READINESS
`{READINESS_VERDICT}`

### NEXT STEP
`{SKILL_INVOCATION}` — closes highest-priority gap

---

_Display only. No files written._
```

---

## V-03 — Consequence Vocabulary Saturation
**Axis:** Phrasing register
**Hypothesis:** Recasting every major section title in commit/risk vocabulary (`COMMIT RISKS`, `COMMIT DECISION`, `HIGHEST PRIORITY RISK`) makes the decision frame architectural rather than annotative. Every evaluation is framed as "what are you committing to?" not "what is the current state?" → satisfies C-19, implies C-16.

---

```markdown
# topic:status

**Topic:** `{TOPIC}`
**Date:** {TODAY}
**Invocation mode:** SIGNAL INTEGRITY AUDIT — terminal display only, no artifacts written

---

## WHAT THIS SKILL ASSESSES

You are not reporting status. You are computing **commit exposure** for `{TOPIC}`.
Every signal gap is a risk you carry into the next decision. Every stale signal is a
commitment based on outdated evidence. This output answers: **Is it safe to commit?**

---

## EXECUTION PHASES

### PHASE 1 — SIGNAL ACQUISITION

**Disk scan**
Glob: `simulations/**/{TOPIC}-*`
Assign all results to `DISK_SIGNALS`.
If empty: `DISK_SIGNALS = []`. Do not infer signals from memory or prior context.

**Planned signal baseline**
Read `simulations/{TOPIC}/strategy.md`.
Fallback: `simulations/strategy.md`.
If neither found: `PLANNED_SIGNALS = []`. Note in output: "No planned baseline — commit exposure is unquantifiable."
Extract all planned signal names to `PLANNED_SIGNALS`. Record the file path for output.

**Evidence age scan**
For each file in `DISK_SIGNALS`, extract date from `{TOPIC}-{signal}-{YYYY-MM-DD}.md`.
Mark signals older than 30 days as `[STALE — evidence may not reflect current system]`.

---

### PHASE 2 — EXPOSURE COMPUTATION

**Coverage formula**
```
PRESENT_COUNT = count(DISK_SIGNALS matching a name in PLANNED_SIGNALS)
PLANNED_COUNT = count(PLANNED_SIGNALS)
COVERAGE_PCT  = PRESENT_COUNT / PLANNED_COUNT * 100
```
If `COVERAGE_PCT = 100%` and any signal is NOT_PRESENT on disk: contradiction. Halt, recompute.

**Commit risks (gap list)**
For each planned signal NOT found on disk:
- Record: `{namespace}/{signal-type}` — UNVERIFIED COMMITMENT

Sort by risk priority: scout → draft → review → flow → trace → prove → listen → program → topic

**Commit decision**
```
COVERAGE = 100%, no gaps → SAFE TO COMMIT — full signal coverage achieved
COVERAGE ≥ 75%, no scout/draft gaps → COMMIT WITH KNOWN EXPOSURE — {N} signals unverified
Otherwise → DO NOT COMMIT — {N} essential signals missing
```

**Highest priority risk**
Single most critical NOT_PRESENT signal. Map to the skill that closes it.

---

### PHASE 3 — DISPLAY GATE

Before rendering: confirm in writing — "No file was written or modified."
If false: halt. Emit: "SKILL FAILURE — write detected during display-only execution."

---

## TERMINAL OUTPUT

---

## COMMIT READINESS AUDIT: {TOPIC}

**Signal baseline:** `{STRATEGY_FILE_PATH}` _(not found — no commit baseline)_
**Scan pattern:** `simulations/**/{TOPIC}-*`
**Audit date:** {TODAY}

---

### COVERAGE EXPOSURE
`{PRESENT_COUNT} of {PLANNED_COUNT} planned signals verified on disk ({COVERAGE_PCT}%)`
_{N} signals are unverified commitments. {N} signals are stale (>30 days)._

---

### COMMIT DECISION
```
{COMMIT_DECISION_VERDICT}
```

---

### SIGNAL EXPOSURE BY NAMESPACE

| Namespace | Verified | Planned | Exposure | Risk |
|-----------|:--------:|:-------:|:--------:|------|
| scout     |          |         |          |      |
| draft     |          |         |          |      |
| review    |          |         |          |      |
| flow      |          |         |          |      |
| trace     |          |         |          |      |
| prove     |          |         |          |      |
| listen    |          |         |          |      |
| program   |          |         |          |      |
| topic     |          |         |          |      |

_(All 9 rows rendered. Zero-coverage rows show as `0 / 0 — UNVERIFIED`.)_

---

### COMMIT RISKS _(highest exposure first)_
- `{namespace}/{signal-type}` — UNVERIFIED COMMITMENT _{[STALE]}_
- _(If none: "No commit risks — all planned signals verified.")_

---

### HIGHEST PRIORITY RISK
**Gap:** `{signal-name}`
**Close with:** `{SKILL_INVOCATION}`
**Commit impact if ignored:** _{what decision is undermined by this gap}_

---

_Audit only. No artifacts written. Commit at your own risk if gaps remain._
```

---

## V-04 — Labeled Layers + Pre-Seeded Assertion Table
**Axes:** Lifecycle emphasis + Output format
**Hypothesis:** Combining explicitly labeled enforcement layers (C-17) with the pre-seeded per-signal assertion table (C-18) achieves structural closure on both the execution mechanism (verifiable by inspection) and the evaluation shape (absorbed into template). The labeled layers make the table's enforcement role explicit.

---

```markdown
# topic:status

**Topic:** `{TOPIC}`
**Date:** {TODAY}
**Mode:** DISPLAY ONLY — no files written, no files modified

---

## ENFORCEMENT ARCHITECTURE

Three enforcement layers prevent the known failure modes of coverage-reporting skills.
Each layer is independent. The skill is valid only if all three are satisfied.

[LAYER 1 — STRUCTURAL]
The 9-namespace summary table is pre-seeded in the display template.
All nine rows are physically present before execution. Zero-count rows render as `0 / 0 — 0%`.
Namespaces cannot be omitted by instruction failure — absence is structurally impossible.

[LAYER 2 — SEMANTIC]
The per-signal assertion table is pre-seeded from `strategy.md` before execution runs.
Each planned signal occupies exactly one row. Execution fills `On Disk` and `Status`.
Gaps are identified by row (NOT_PRESENT), not by subtraction from counts.
Coverage is computed from rows, not from file counts.
A consistency check blocks any output where `COVERAGE = 100%` and any row is NOT_PRESENT.

[LAYER 3 — EXECUTION]
Before Phase 4 (DISPLAY), execute this gate:
> "I have not written or modified any file."
If false: halt. Do not display. Report the write to the user as: "SKILL FAILURE — write detected."

---

## PHASE 1 — READ INPUTS

**1a. Disk scan**
Glob: `simulations/**/{TOPIC}-*`
Assign to `DISK_SIGNALS`. If empty, set `DISK_SIGNALS = []`.
Log: `Disk scan — {N} files found.`

**1b. Strategy scan**
Read `simulations/{TOPIC}/strategy.md` (fallback: `simulations/strategy.md`).
If not found: `PLANNED_SIGNALS = []`. Log file path tried.
Extract all planned signal names. Assign to `PLANNED_SIGNALS`.
Log: `strategy.md found at {PATH} — {N} planned signals.`

**1c. Recency scan**
Parse date from each filename in `DISK_SIGNALS`: `{TOPIC}-{signal}-{YYYY-MM-DD}.md`.
Flag signals > 30 days old: `[STALE]`.

---

## PHASE 2 — BUILD ASSERTION TABLE [LAYER 2]

Construct one row per planned signal. **Do not skip or collapse rows.**

```
ASSERTION TABLE — {TOPIC}
===========================================================================
| Signal Slot                          | NS       | On Disk | Status      | Age    |
|--------------------------------------|----------|---------|-------------|--------|
| {TOPIC}-scout-{signal-1}             | scout    | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-scout-{signal-2}             | scout    | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-draft-{signal-1}             | draft    | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-review-{signal-1}            | review   | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-flow-{signal-1}              | flow     | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-trace-{signal-1}             | trace    | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-prove-{signal-1}             | prove    | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-listen-{signal-1}            | listen   | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-program-{signal-1}           | program  | [FILL]  | [FILL]      | [FILL] |
| {TOPIC}-topic-{signal-1}             | topic    | [FILL]  | [FILL]      | [FILL] |
| ... (one row per PLANNED_SIGNALS)    |          |         |             |        |
===========================================================================
```

**Fill rules:**
- On Disk: YES if file exists in `DISK_SIGNALS`, NO otherwise
- Status: PRESENT (On Disk = YES) or NOT_PRESENT (On Disk = NO)
- Age: date from filename, or `—`. Append `[STALE]` if > 30 days.

---

## PHASE 3 — COMPUTE

**Coverage**
```
FOUND = count(rows where Status = PRESENT)
PLANNED = total rows in assertion table
COVERAGE_PCT = FOUND / PLANNED * 100
```
Consistency check: `COVERAGE_PCT = 100%` AND any NOT_PRESENT row → recompute. Contradiction blocks output.

**Gap list**
All rows where Status = NOT_PRESENT, sorted: scout → draft → review → flow → trace → prove → listen → program → topic

**Readiness**
```
FOUND = PLANNED AND no NOT_PRESENT rows → READY
COVERAGE_PCT ≥ 75% AND no scout/draft NOT_PRESENT → CONDITIONALLY READY — {N} outstanding
Otherwise → NOT READY — {N} gaps remain
```

**Next step**
Highest-priority NOT_PRESENT row → producing skill invocation.

---

## PHASE 4 — DISPLAY

**[LAYER 3 gate]** Confirm: "No file written or modified. Proceeding to display."
If false: halt.

---

## TOPIC STATUS: {TOPIC}

**Strategy file:** `{PATH}` _(not found — no planned baseline)_
**Disk scan:** `simulations/**/{TOPIC}-*`
**As of:** {TODAY}

### PER-SIGNAL ASSERTION TABLE
_(Completed assertion table from Phase 2 — all rows filled.)_

### COVERAGE
`{FOUND} / {PLANNED} signals present ({COVERAGE_PCT}%)`

### NAMESPACE SUMMARY [LAYER 1 — all 9 rows always present]

| Namespace | Found | Planned | Coverage |
|-----------|------:|--------:|---------:|
| scout     |       |         |          |
| draft     |       |         |          |
| review    |       |         |          |
| flow      |       |         |          |
| trace     |       |         |          |
| prove     |       |         |          |
| listen    |       |         |          |
| program   |       |         |          |
| topic     |       |         |          |

### OPEN GAPS _(NOT_PRESENT rows, priority order)_
- `{namespace}/{signal-type}` — NOT_PRESENT {[STALE]}
- _(If none: "No gaps.")_

### READINESS
`{READINESS_VERDICT}`

### NEXT STEP
`{SKILL_INVOCATION}` — closes `{signal-name}`

---

_Enforcement: [LAYER 1] pre-seeded namespace table · [LAYER 2] per-signal assertion rows · [LAYER 3] pre-display write gate. Display only._
```

---

## V-05 — Full Structural Closure (C-17 + C-18 + C-19)
**Axes:** Lifecycle emphasis + Output format + Phrasing register
**Hypothesis:** The combination of labeled enforcement layers, pre-seeded assertion table, and consequence vocabulary saturation achieves complete structural closure: every enforcement mechanism is named and verifiable, every evaluation slot is pre-allocated, and the decision frame is architecturally embedded in the section taxonomy itself. A variation earning all three is the highest-density signal against the v4 rubric.

---

```markdown
# topic:status

**Topic:** `{TOPIC}`
**Date:** {TODAY}
**Invocation mode:** COMMIT RISK AUDIT — terminal display only, no artifacts produced

---

## ENFORCEMENT ARCHITECTURE

Three independently-failing layers enforce the display-only contract and prevent
coverage-inflation failure modes. The skill output is valid only when all three pass.

[LAYER 1 — STRUCTURAL]
The 9-namespace commit-exposure table is pre-seeded in the output template.
All nine rows are physically present before execution. Zero-exposure rows render as
`0 / 0 — UNVERIFIED`. Namespace omission is structurally impossible.

[LAYER 2 — SEMANTIC]
The per-signal commit-risk table is pre-seeded from `strategy.md` before any evaluation runs.
Each planned signal occupies exactly one row with a `VERIFIED`/`UNVERIFIED` commitment slot.
No aggregate subtraction. Each row is evaluated independently.
Consistency gate: if `COVERAGE = 100%` and any row shows `UNVERIFIED` → contradiction, halt.

[LAYER 3 — EXECUTION]
Before Phase 4 (DISPLAY COMMIT AUDIT), state:
> "No file was written or modified. Commit audit output is clean."
If false: halt. Emit: "SKILL FAILURE — write detected in display-only execution."
Do not display output if this gate cannot be passed truthfully.

---

## PHASE 1 — SIGNAL ACQUISITION

**Disk scan**
Glob: `simulations/**/{TOPIC}-*`
Assign to `DISK_SIGNALS`. If empty: `DISK_SIGNALS = []`.
Log: `Signal acquisition complete — {N} artifacts found.`

**Commit baseline scan**
Read `simulations/{TOPIC}/strategy.md` (fallback: `simulations/strategy.md`).
If not found: `PLANNED_SIGNALS = []`.
Log: `Commit baseline: {PATH}` or `Commit baseline: NOT FOUND — commit exposure is unquantifiable.`
Extract all planned signal names to `PLANNED_SIGNALS`.

**Evidence age scan**
Parse date from each filename: `{TOPIC}-{signal}-{YYYY-MM-DD}.md`.
Flag signals older than 30 days as `[STALE — commitment based on outdated evidence]`.

---

## PHASE 2 — BUILD COMMIT RISK TABLE [LAYER 2]

Construct one row per signal in `PLANNED_SIGNALS`. **Do not skip or merge rows.**
This table is the evidence base for the commit decision.

```
COMMIT RISK TABLE — {TOPIC}
==========================================================================
| Commitment Slot                      | NS       | Verified? | Risk     | Evidence Age |
|--------------------------------------|----------|-----------|----------|--------------|
| {TOPIC}-scout-{signal-1}             | scout    | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-scout-{signal-2}             | scout    | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-draft-{signal-1}             | draft    | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-review-{signal-1}            | review   | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-flow-{signal-1}              | flow     | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-trace-{signal-1}             | trace    | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-prove-{signal-1}             | prove    | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-listen-{signal-1}            | listen   | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-program-{signal-1}           | program  | [FILL]    | [FILL]   | [FILL]       |
| {TOPIC}-topic-{signal-1}             | topic    | [FILL]    | [FILL]   | [FILL]       |
| ... (one row per PLANNED_SIGNALS)    |          |           |          |              |
==========================================================================
```

**Fill rules:**
- Verified?: YES (file in `DISK_SIGNALS`) or NO
- Risk: `COMMIT RISK` (Verified = NO) or `CLEARED` (Verified = YES)
- Evidence Age: date from filename, `—` if not on disk. Append `[STALE]` if > 30 days.

---

## PHASE 3 — COMPUTE COMMIT EXPOSURE

**Coverage formula**
```
VERIFIED   = count(rows where Verified = YES)
TOTAL      = total rows
COVERAGE   = VERIFIED / TOTAL * 100
```
Consistency gate: `COVERAGE = 100%` AND any row shows `COMMIT RISK` → recompute. If contradiction persists: halt.

**Open commit risks (gap list)**
All rows where Risk = `COMMIT RISK`, sorted by namespace priority:
  scout → draft → review → flow → trace → prove → listen → program → topic

**Commit decision**
```
VERIFIED = TOTAL, zero COMMIT RISK rows → SAFE TO COMMIT — full verification achieved
COVERAGE ≥ 75%, no scout/draft COMMIT RISK rows → COMMIT WITH KNOWN EXPOSURE — {N} unverified
Otherwise → DO NOT COMMIT — {N} essential commitments unverified
```

**Highest priority risk**
Top-priority COMMIT RISK row → map to producing skill invocation.

---

## PHASE 4 — DISPLAY COMMIT AUDIT

**[LAYER 3 gate]** State before rendering:
> "No file was written or modified. Commit audit output is clean."
If false: halt. Report as skill failure.

---

## COMMIT AUDIT: {TOPIC}

**Commit baseline:** `{PATH}` _(not found — exposure unquantifiable)_
**Signal scan:** `simulations/**/{TOPIC}-*`
**Audit date:** {TODAY}

---

### COVERAGE EXPOSURE
`{VERIFIED} of {TOTAL} planned commitments verified ({COVERAGE}%)`
_Unverified: {N} · Stale evidence: {N} · Commit baseline: {N} planned signals_

---

### COMMIT RISK TABLE [LAYER 2 — per-signal]
_(Completed commit risk table from Phase 2 — all rows populated.)_

---

### COMMIT RISKS BY NAMESPACE [LAYER 1 — all 9 rows always present]

| Namespace | Verified | Planned | Coverage  | Exposure          |
|-----------|:--------:|:-------:|:---------:|-------------------|
| scout     |          |         |           |                   |
| draft     |          |         |           |                   |
| review    |          |         |           |                   |
| flow      |          |         |           |                   |
| trace     |          |         |           |                   |
| prove     |          |         |           |                   |
| listen    |          |         |           |                   |
| program   |          |         |           |                   |
| topic     |          |         |           |                   |

_(All 9 rows always rendered. Zero rows show `0 / 0 — UNVERIFIED`.)_

---

### OPEN COMMIT RISKS _(highest exposure namespace first)_
- `{namespace}/{signal-type}` — COMMIT RISK _{[STALE]}_
- _(If none: "No commit risks — all planned signals verified.")_

---

### COMMIT DECISION
```
{COMMIT_DECISION_VERDICT}
```

---

### HIGHEST PRIORITY RISK
**Unverified commitment:** `{signal-name}`
**Closes with:** `{SKILL_INVOCATION}`
**Commit consequence if ignored:** _{what decision rests on unverified ground}_

---

_Enforcement: [LAYER 1] pre-seeded namespace table · [LAYER 2] per-slot commit risk rows · [LAYER 3] pre-display write gate. Audit only — no artifacts written._
```

---

## Variation Summary

| Var | Axis | Primary Target | Implied Criteria |
|-----|------|---------------|-----------------|
| V-01 | Lifecycle emphasis | C-17 labeled redundancy layers | C-13 triple-redundancy |
| V-02 | Output format | C-18 assertion table pre-seeded in template | C-14 template-first, C-15 per-signal assertion |
| V-03 | Phrasing register | C-19 consequence vocabulary saturation | C-16 consequence-framed verdict |
| V-04 | Lifecycle + Output | C-17 + C-18 | C-13, C-14, C-15 |
| V-05 | Lifecycle + Output + Register | C-17 + C-18 + C-19 | C-13, C-14, C-15, C-16 (full aspirational-3) |

**Scoring hypothesis:** V-05 should approach 150 if all essential + recommended + aspirational tiers are satisfied. V-04 should reach ~135 (v3 ceiling). V-01/V-02/V-03 test whether single-axis additions to a strong v3 baseline each unlock their respective 5-point criteria cleanly.
