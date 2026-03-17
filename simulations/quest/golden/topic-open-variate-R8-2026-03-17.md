# topic-open — Round 8 Variations

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric version**: v7 (C-01 through C-30, aspirational denominator = 22)
**Round context**: R7 scored five variations on the v7 rubric. V-05 scored 100/100 (22/22 aspirational) — first perfect composite. R7 scorecard confirmed no new excellence patterns in V-05: the three C-28/C-29/C-30 axes compose cleanly with zero regression. R8 probes three structural gaps visible in V-05 but not yet criteriaized: (1) AMEND incompleteness — V-05 names one AMEND (C-04 priority drift), C-01 has a terse pointer, C-02/C-03/C-05 have no repair instructions; (2) gate failure routing — Phase 2 exit gate detects failures but specifies no recovery path when items are unchecked; (3) constraint matrix recovery — DEFAULTS THIS SKILL OVERRIDES has five columns but no "Recovery Path" for already-violated constraints.

**Variation axes selected**:
- V-01: AMEND completeness — every Phase 5 self-check item has a named AMEND block with exact repair steps; uniform label format across all five
- V-02: Gate failure routing — Phase exit gate concludes with explicit GATE FAILURE line naming return phase and repair condition before re-run
- V-03: Recovery column in constraint matrix — DEFAULTS THIS SKILL OVERRIDES gains sixth column "Recovery Path"
- V-04: V-01 + V-02 combination — AMEND completeness AND gate failure routing
- V-05: V-01 + V-02 + V-03 full integration — complete AMEND coverage, gate routing, recovery-augmented constraint matrix

All five variations use R7 V-05 as base (passes all C-01 through C-30).

---

## V-01 — AMEND Completeness

**Axis**: Every Phase 5 self-check item concludes with a named AMEND block specifying the exact repair procedure. The AMEND vocabulary is uniform: `AMEND — {CONDITION NAME}: If {C-NN} fails: {repair steps}`. V-05 has one AMEND ("AMEND — PRIORITY DRIFT" for C-04) and one terse pointer ("-> If date missing" for C-01). C-02, C-03, and C-05 have no repair instructions. This variation adds named AMEND blocks for all five items, making the self-check a repair protocol rather than an audit checklist.

**Hypothesis**: V-05's Phase 5 self-check is an audit: it detects failures but does not consistently prescribe repair. The AMEND pattern in C-04 is the exception. A model that encounters a failing C-02 check (wrong path) knows the path is wrong but receives no repair directive. Extending AMEND to all five items makes the self-check a closed loop: detect → repair → re-check. The uniformity of the AMEND vocabulary (same label format across all items) also creates a scannable repair surface — a model that failed C-02 can scan for "AMEND — WRONG PATH" without reading surrounding prose.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction. `topic-status` will find the correct vocabulary in every cell. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may have already formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. `topic-status` will silently exclude those signals from the commit-gate check. You will need a re-scan pass after all rows are written — fixing errors that would not have occurred had you read this block first.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent downstream breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values. `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries — the topic appears to have no coverage history.

> **COPY — DO NOT RECONSTRUCT.**

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — `topic-status` parses all five for coverage computation; `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` gates on exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md` — `topic-scanner` uses this for discovery
- **F-05 Owner Role**: role responsible for this signal

---

## DEFAULTS THIS SKILL OVERRIDES

| Default | Rule | Why | What Breaks If You Skip | Tool |
|---------|------|-----|------------------------|------|
| Any priority vocabulary | `essential` / `recommended` / `optional` exactly | `topic-status` exact string comparison on every commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` |
| Free-form TOPICS.md row | Use the ROW TEMPLATE above — 3 fields: slug, description, YYYY-MM-DD | `topic-status` date filter reads the date field on every status check | Missing date = topic excluded from all status queries; coverage unreachable | `topic-status` |
| Table before rationale | Rationale first, signal table second | Owner roles emerge from the decisions described in the rationale — if table comes first, roles are column-fillers; if rationale comes first, roles are stakeholders accountable to named decisions | C-08 passes mechanically but carries no information; coverage review cannot verify roles against decision context | — |
| Inline commit gate | Structurally isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser; coverage computation returns no gate status; the commit gate silently does not exist | `topic-status` |
| Any strategy file location | Write to `simulations/{topic}/strategy.md` specifically | `topic-status` and `topic-scanner` both glob for this exact path | Flat path = both tools silently return zero results; topic appears to have no signals | `topic-status`, `topic-scanner` |

---

## DECISION TABLE SCHEMA

All five phase decision tables in this skill share the same column grammar:

| Path | Action | Consequence |
|------|--------|-------------|

Column definitions:
- **Path**: the execution fork — which branch is being taken (described from the model's perspective)
- **Action**: what you do when this path is chosen (the behavior triggered by that branch)
- **Consequence**: the specific tool-level outcome of that action (what the downstream tools experience as a result)

This schema is fixed across Phase 1 through Phase 5. When you read any phase decision table, column 3 is always the consequence. You do not re-parse each table's column structure — the grammar is established once here and applies uniformly.

---

## Phase 1 Decision: Collision Check

| Path | Action | Consequence |
|------|--------|-------------|
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; `topic-status` loads TOPICS.md on every check and finds exactly one entry; no coverage aggregation ambiguity |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate creates ambiguous coverage aggregation with no merge path; two strategy files cannot be reconciled |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

**If the topic does not exist in TOPICS.md**: proceed to Phase 2. `topic-status` will find exactly one entry; coverage aggregation is unambiguous.

**If the topic already exists in TOPICS.md**: stop. Report the collision. Do not create a duplicate. `topic-status` cannot merge two entries — the ambiguity has no resolution path and coverage aggregation becomes permanently unreliable for this topic.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles in the table emerge as stakeholders accountable to the decisions you just described. Each owner role is the person answerable to a specific question named in the rationale. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers assigned after the fact. Coverage review cannot verify them against any decision context — the roles have no stated accountability because the rationale was written to justify the table, not to surface the decisions that determined it.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool and mechanism:

- [ ] Rationale >= 2 sentences — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; absent block = owner-role verification skipped in coverage report)
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` F-01 exact string match** (tests each F-01 priority cell against `{essential, recommended, optional}` using equality comparison; any non-matching value is silently excluded from the commit-gate computation — no error emitted)
- [ ] COV-01: >= 1 `essential` row — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = no gate status returned; topic has no defined commit condition and investigation completion is undefined)
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` F-02 namespace aggregation** (groups discovered signals by F-02 value; single distinct namespace = monoculture flag; domain coverage cannot be verified across namespaces)
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by role)
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` F-04 pattern glob** (matches F-04 item names against `{topic}-*-YYYY-MM-DD.md`; any item name not matching this pattern is invisible to discovery; the signal is untracked in the coverage system)

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing essential signals by exact item name | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section — not a subsection of Phase 2, not a note inside the signal table.

**If you write the gate as an isolated `## COMMIT GATE` heading**: `topic-status` reads it as a named parseable section and returns correct gate status; the commit gate is enforceable by the toolchain.

**If you embed the gate inside the signal table**: `topic-status` section parser cannot find the `## COMMIT GATE` heading; coverage computation returns no gate status; the commit gate silently does not exist even if the content is present.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 Decision: Output Write

| Path | Action | Consequence |
|------|--------|-------------|
| **Copy ROW TEMPLATE; write strategy to `simulations/{topic}/strategy.md`** | Use the three-field template directly; write strategy to the topic subdirectory | `topic-status` and `topic-scanner` find both files; coverage computation proceeds normally |
| **Reconstruct row from memory OR write strategy to flat path** | Template rebuilt: `{YYYY-MM-DD}` dropped; flat path not matched by glob | C-01 fails (missing date) and/or C-02 fails (wrong path); both tools silently return zero results; topic is invisible to the coverage system |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above.

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries — the topic appears to have no coverage history.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — not to a flat path, not to a root-level file.

**If written to `simulations/{topic}/strategy.md`**: `topic-status` and `topic-scanner` both match the file via their glob; coverage computation proceeds normally.

**If written to any other path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate — with no error to indicate the path is wrong.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

Run this check after writing both files — not before.

**If you run this check after writing both files**: you are auditing the actual output that `topic-status` and `topic-scanner` will read. Errors are caught and corrected before the topic enters the coverage system.

**If you run this check before writing**: you are auditing your intentions, not your output. `topic-status` and `topic-scanner` read files; actual output may still fail even if every intention passes this check.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row; absent or malformed date = topic excluded from all date-range queries; topic appears to not exist in the coverage system).

**AMEND — DATE MISSING**: If C-01 fails: identify the malformed or missing date field in the TOPICS.md row. Return to the ROW TEMPLATE above. Copy the three-field template. Replace the existing row with a correctly populated version. Confirm the date cell matches `YYYY-MM-DD` exactly before re-checking C-01.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently — the topic appears to have no signals).

**AMEND — WRONG PATH**: If C-02 fails: identify the actual path the file was written to. Move the file to `simulations/{topic}/strategy.md`. Verify the directory `simulations/{topic}/` exists; create it if absent. Re-run `topic-status` to confirm the file is found before marking C-02 passing.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**AMEND — MISSING FIELDS**: If C-03 fails: list every row with a missing field. For each row, identify which of F-01 through F-05 is absent. Add the missing value. Re-scan all rows for five-field completeness before marking C-03 passing.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values with the correct VOCABULARY LOCK term. Re-scan all priority cells before marking C-04 passing.

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — NO ESSENTIAL SIGNAL**: If C-05 fails: identify which signal is the minimum viable commit gate item for this topic — the signal whose completion most directly answers whether the feature is ready to design. Promote it from `recommended` to `essential`, or add a new essential signal row. Re-check C-04 (priority vocabulary) after any priority change. Re-run C-05 before marking it passing.

---

---

## V-02 — Gate Failure Routing

**Axis**: Every Phase exit gate concludes with an explicit GATE FAILURE line specifying the return phase, the repair action, and the condition for re-running the gate. The GATE FAILURE line follows the checklist immediately and is unconditional: it applies whenever any item is unchecked. V-05 has no recovery instruction after the Phase 2 exit gate — a model that fails COV-01 receives no instruction for what to do next. V-02 adds: "GATE FAILURE: return to Phase 2 — repair the failing item(s), re-run this gate before proceeding to Phase 3."

**Hypothesis**: The Phase 2 exit gate in V-05 is a detection surface only. A model that reaches the gate with COV-01 unchecked knows the failure but has no routing instruction — does it fix in place and continue? Restart Phase 2 entirely? Skip to Phase 3? GATE FAILURE routing eliminates this ambiguity by naming the exact return point. The routing also closes the gate loop: the gate exists not only to block bad output but to recover it — detection without recovery is incomplete.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction. `topic-status` will find the correct vocabulary in every cell. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may have already formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. `topic-status` will silently exclude those signals from the commit-gate check. You will need a re-scan pass after all rows are written — fixing errors that would not have occurred had you read this block first.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent downstream breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values. `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries — the topic appears to have no coverage history.

> **COPY — DO NOT RECONSTRUCT.**

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — `topic-status` parses all five for coverage computation; `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` gates on exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md` — `topic-scanner` uses this for discovery
- **F-05 Owner Role**: role responsible for this signal

---

## DEFAULTS THIS SKILL OVERRIDES

| Default | Rule | Why | What Breaks If You Skip | Tool |
|---------|------|-----|------------------------|------|
| Any priority vocabulary | `essential` / `recommended` / `optional` exactly | `topic-status` exact string comparison on every commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` |
| Free-form TOPICS.md row | Use the ROW TEMPLATE above — 3 fields: slug, description, YYYY-MM-DD | `topic-status` date filter reads the date field on every status check | Missing date = topic excluded from all status queries; coverage unreachable | `topic-status` |
| Table before rationale | Rationale first, signal table second | Owner roles emerge from the decisions described in the rationale — if table comes first, roles are column-fillers; if rationale comes first, roles are stakeholders accountable to named decisions | C-08 passes mechanically but carries no information; coverage review cannot verify roles against decision context | — |
| Inline commit gate | Structurally isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser; coverage computation returns no gate status; the commit gate silently does not exist | `topic-status` |
| Any strategy file location | Write to `simulations/{topic}/strategy.md` specifically | `topic-status` and `topic-scanner` both glob for this exact path | Flat path = both tools silently return zero results; topic appears to have no signals | `topic-status`, `topic-scanner` |

---

## DECISION TABLE SCHEMA

All five phase decision tables in this skill share the same column grammar:

| Path | Action | Consequence |
|------|--------|-------------|

Column definitions:
- **Path**: the execution fork — which branch is being taken (described from the model's perspective)
- **Action**: what you do when this path is chosen (the behavior triggered by that branch)
- **Consequence**: the specific tool-level outcome of that action (what the downstream tools experience as a result)

This schema is fixed across Phase 1 through Phase 5. When you read any phase decision table, column 3 is always the consequence. You do not re-parse each table's column structure — the grammar is established once here and applies uniformly.

---

## Phase 1 Decision: Collision Check

| Path | Action | Consequence |
|------|--------|-------------|
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; `topic-status` loads TOPICS.md on every check and finds exactly one entry; no coverage aggregation ambiguity |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate creates ambiguous coverage aggregation with no merge path; two strategy files cannot be reconciled |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

**If the topic does not exist in TOPICS.md**: proceed to Phase 2. `topic-status` will find exactly one entry; coverage aggregation is unambiguous.

**If the topic already exists in TOPICS.md**: stop. Report the collision. Do not create a duplicate. `topic-status` cannot merge two entries — the ambiguity has no resolution path and coverage aggregation becomes permanently unreliable for this topic.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles in the table emerge as stakeholders accountable to the decisions you just described. Each owner role is the person answerable to a specific question named in the rationale. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers assigned after the fact. Coverage review cannot verify them against any decision context — the roles have no stated accountability because the rationale was written to justify the table, not to surface the decisions that determined it.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool and mechanism:

- [ ] Rationale >= 2 sentences — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; absent block = owner-role verification skipped in coverage report)
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` F-01 exact string match** (tests each F-01 priority cell against `{essential, recommended, optional}` using equality comparison; any non-matching value is silently excluded from the commit-gate computation — no error emitted)
- [ ] COV-01: >= 1 `essential` row — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = no gate status returned; topic has no defined commit condition and investigation completion is undefined)
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` F-02 namespace aggregation** (groups discovered signals by F-02 value; single distinct namespace = monoculture flag; domain coverage cannot be verified across namespaces)
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by role)
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` F-04 pattern glob** (matches F-04 item names against `{topic}-*-YYYY-MM-DD.md`; any item name not matching this pattern is invisible to discovery; the signal is untracked in the coverage system)

**GATE FAILURE**: If any item above is unchecked — return to Phase 2. Repair the failing item(s) in the strategy file. Re-run this gate in full before proceeding to Phase 3. Do not proceed with any unchecked item outstanding.

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing essential signals by exact item name | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section — not a subsection of Phase 2, not a note inside the signal table.

**If you write the gate as an isolated `## COMMIT GATE` heading**: `topic-status` reads it as a named parseable section and returns correct gate status; the commit gate is enforceable by the toolchain.

**If you embed the gate inside the signal table**: `topic-status` section parser cannot find the `## COMMIT GATE` heading; coverage computation returns no gate status; the commit gate silently does not exist even if the content is present.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 Decision: Output Write

| Path | Action | Consequence |
|------|--------|-------------|
| **Copy ROW TEMPLATE; write strategy to `simulations/{topic}/strategy.md`** | Use the three-field template directly; write strategy to the topic subdirectory | `topic-status` and `topic-scanner` find both files; coverage computation proceeds normally |
| **Reconstruct row from memory OR write strategy to flat path** | Template rebuilt: `{YYYY-MM-DD}` dropped; flat path not matched by glob | C-01 fails (missing date) and/or C-02 fails (wrong path); both tools silently return zero results; topic is invisible to the coverage system |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above.

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries — the topic appears to have no coverage history.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — not to a flat path, not to a root-level file.

**If written to `simulations/{topic}/strategy.md`**: `topic-status` and `topic-scanner` both match the file via their glob; coverage computation proceeds normally.

**If written to any other path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate — with no error to indicate the path is wrong.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

Run this check after writing both files — not before.

**If you run this check after writing both files**: you are auditing the actual output that `topic-status` and `topic-scanner` will read. Errors are caught and corrected before the topic enters the coverage system.

**If you run this check before writing**: you are auditing your intentions, not your output. `topic-status` and `topic-scanner` read files; actual output may still fail even if every intention passes this check.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row; absent or malformed date = topic excluded from all date-range queries; topic appears to not exist in the coverage system).
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently — the topic appears to have no signals).

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-03 — Recovery Column in Constraint Matrix

**Axis**: DEFAULTS THIS SKILL OVERRIDES gains a sixth column: "Recovery Path". The existing five columns describe the constraint forward — what to do and why. The Recovery Path column describes the constraint backward — if you have already violated it, how do you repair the output. V-05 has no consolidated repair surface in the constraint matrix; recovery instructions exist only in Phase 5's self-check (C-04 / partial C-01). V-03 adds recovery as a first-class column in the matrix, making constraint violation repairable at the point of reading the default, not only at the point of discovering the failure in Phase 5.

**Hypothesis**: The DEFAULTS matrix in V-05 is a prevention surface: read it before you execute and you will not make the error. But a model that missed the block — or read it and made the error anyway — has no repair map at the constraint level. A Recovery Path column adds a repair contract at the same structural level as the prevention contract. A model that already wrote a flat-path strategy file can scan DEFAULTS, find the relevant row, read the Recovery Path, and repair without searching Phase 5. The constraint matrix becomes a bidirectional contract: prevention and repair in the same row.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction. `topic-status` will find the correct vocabulary in every cell. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may have already formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. `topic-status` will silently exclude those signals from the commit-gate check. You will need a re-scan pass after all rows are written — fixing errors that would not have occurred had you read this block first.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent downstream breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values. `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries — the topic appears to have no coverage history.

> **COPY — DO NOT RECONSTRUCT.**

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — `topic-status` parses all five for coverage computation; `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` gates on exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md` — `topic-scanner` uses this for discovery
- **F-05 Owner Role**: role responsible for this signal

---

## DEFAULTS THIS SKILL OVERRIDES

| Default | Rule | Why | What Breaks If You Skip | Tool | Recovery Path |
|---------|------|-----|------------------------|------|---------------|
| Any priority vocabulary | `essential` / `recommended` / `optional` exactly | `topic-status` exact string comparison on every commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` | List every priority cell with invalid vocabulary. Replace each with the correct VOCABULARY LOCK term. Re-scan all rows before re-running `topic-status`. |
| Free-form TOPICS.md row | Use the ROW TEMPLATE above — 3 fields: slug, description, YYYY-MM-DD | `topic-status` date filter reads the date field on every status check | Missing date = topic excluded from all status queries; coverage unreachable | `topic-status` | Locate the topic's row in TOPICS.md. Copy the ROW TEMPLATE above. Replace the malformed row with a correctly populated three-field version. Confirm the date cell matches `YYYY-MM-DD`. |
| Table before rationale | Rationale first, signal table second | Owner roles emerge from the decisions described in the rationale — if table comes first, roles are column-fillers; if rationale comes first, roles are stakeholders accountable to named decisions | C-08 passes mechanically but carries no information; coverage review cannot verify roles against decision context | — | Write the rationale now, before any further work. Review each owner role cell: revise any role that does not name a stakeholder accountable to a specific decision in the rationale. |
| Inline commit gate | Structurally isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser; coverage computation returns no gate status; the commit gate silently does not exist | `topic-status` | Extract the gate content from wherever it is embedded. Write a new standalone `## COMMIT GATE` section after the signal table, listing essential signals by exact item name. Delete the embedded version. |
| Any strategy file location | Write to `simulations/{topic}/strategy.md` specifically | `topic-status` and `topic-scanner` both glob for this exact path | Flat path = both tools silently return zero results; topic appears to have no signals | `topic-status`, `topic-scanner` | Identify the actual path the file was written to. Move the file to `simulations/{topic}/strategy.md`. Verify `simulations/{topic}/` exists; create it if absent. |

---

## DECISION TABLE SCHEMA

All five phase decision tables in this skill share the same column grammar:

| Path | Action | Consequence |
|------|--------|-------------|

Column definitions:
- **Path**: the execution fork — which branch is being taken (described from the model's perspective)
- **Action**: what you do when this path is chosen (the behavior triggered by that branch)
- **Consequence**: the specific tool-level outcome of that action (what the downstream tools experience as a result)

This schema is fixed across Phase 1 through Phase 5. When you read any phase decision table, column 3 is always the consequence. You do not re-parse each table's column structure — the grammar is established once here and applies uniformly.

---

## Phase 1 Decision: Collision Check

| Path | Action | Consequence |
|------|--------|-------------|
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; `topic-status` loads TOPICS.md on every check and finds exactly one entry; no coverage aggregation ambiguity |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate creates ambiguous coverage aggregation with no merge path; two strategy files cannot be reconciled |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

**If the topic does not exist in TOPICS.md**: proceed to Phase 2. `topic-status` will find exactly one entry; coverage aggregation is unambiguous.

**If the topic already exists in TOPICS.md**: stop. Report the collision. Do not create a duplicate. `topic-status` cannot merge two entries — the ambiguity has no resolution path and coverage aggregation becomes permanently unreliable for this topic.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles in the table emerge as stakeholders accountable to the decisions you just described. Each owner role is the person answerable to a specific question named in the rationale. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers assigned after the fact. Coverage review cannot verify them against any decision context — the roles have no stated accountability because the rationale was written to justify the table, not to surface the decisions that determined it.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool and mechanism:

- [ ] Rationale >= 2 sentences — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; absent block = owner-role verification skipped in coverage report)
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` F-01 exact string match** (tests each F-01 priority cell against `{essential, recommended, optional}` using equality comparison; any non-matching value is silently excluded from the commit-gate computation — no error emitted)
- [ ] COV-01: >= 1 `essential` row — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = no gate status returned; topic has no defined commit condition and investigation completion is undefined)
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` F-02 namespace aggregation** (groups discovered signals by F-02 value; single distinct namespace = monoculture flag; domain coverage cannot be verified across namespaces)
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by role)
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` F-04 pattern glob** (matches F-04 item names against `{topic}-*-YYYY-MM-DD.md`; any item name not matching this pattern is invisible to discovery; the signal is untracked in the coverage system)

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing essential signals by exact item name | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section — not a subsection of Phase 2, not a note inside the signal table.

**If you write the gate as an isolated `## COMMIT GATE` heading**: `topic-status` reads it as a named parseable section and returns correct gate status; the commit gate is enforceable by the toolchain.

**If you embed the gate inside the signal table**: `topic-status` section parser cannot find the `## COMMIT GATE` heading; coverage computation returns no gate status; the commit gate silently does not exist even if the content is present.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 Decision: Output Write

| Path | Action | Consequence |
|------|--------|-------------|
| **Copy ROW TEMPLATE; write strategy to `simulations/{topic}/strategy.md`** | Use the three-field template directly; write strategy to the topic subdirectory | `topic-status` and `topic-scanner` find both files; coverage computation proceeds normally |
| **Reconstruct row from memory OR write strategy to flat path** | Template rebuilt: `{YYYY-MM-DD}` dropped; flat path not matched by glob | C-01 fails (missing date) and/or C-02 fails (wrong path); both tools silently return zero results; topic is invisible to the coverage system |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above.

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries — the topic appears to have no coverage history.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — not to a flat path, not to a root-level file.

**If written to `simulations/{topic}/strategy.md`**: `topic-status` and `topic-scanner` both match the file via their glob; coverage computation proceeds normally.

**If written to any other path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate — with no error to indicate the path is wrong.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

Run this check after writing both files — not before.

**If you run this check after writing both files**: you are auditing the actual output that `topic-status` and `topic-scanner` will read. Errors are caught and corrected before the topic enters the coverage system.

**If you run this check before writing**: you are auditing your intentions, not your output. `topic-status` and `topic-scanner` read files; actual output may still fail even if every intention passes this check.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row; absent or malformed date = topic excluded from all date-range queries; topic appears to not exist in the coverage system).
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row. (See DEFAULTS Recovery Path for the repair procedure.)

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently — the topic appears to have no signals).

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-04 — AMEND Completeness + Gate Failure Routing (V-01 + V-02)

**Axes combined**: V-01 (named AMEND procedures for all five Phase 5 self-check items) + V-02 (GATE FAILURE routing line after Phase 2 exit gate). The two axes operate at different scopes and compose without interference: V-02's GATE FAILURE routes to Phase 2 for any gate item; V-01's AMEND blocks specify what to repair once the self-check is reached. A model following both will: hit the gate, read the GATE FAILURE routing, return to Phase 2, repair the strategy file, re-run the gate, proceed to Phase 5, and find a named AMEND for any specific failing item there.

**Hypothesis**: V-01 and V-02 address adjacent gaps in V-05's self-correction surface. V-05 detects failures but provides repair instructions inconsistently (V-01's gap) and provides no phase-level routing when failures occur (V-02's gap). Combining them makes the entire correction workflow explicit: gate failure → phase routing → item-level repair → re-check. Each step has a named instruction. A model cannot be left without a next action at any point in the failure path.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction. `topic-status` will find the correct vocabulary in every cell. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may have already formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. `topic-status` will silently exclude those signals from the commit-gate check. You will need a re-scan pass after all rows are written — fixing errors that would not have occurred had you read this block first.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent downstream breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values. `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries — the topic appears to have no coverage history.

> **COPY — DO NOT RECONSTRUCT.**

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — `topic-status` parses all five for coverage computation; `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` gates on exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md` — `topic-scanner` uses this for discovery
- **F-05 Owner Role**: role responsible for this signal

---

## DEFAULTS THIS SKILL OVERRIDES

| Default | Rule | Why | What Breaks If You Skip | Tool |
|---------|------|-----|------------------------|------|
| Any priority vocabulary | `essential` / `recommended` / `optional` exactly | `topic-status` exact string comparison on every commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` |
| Free-form TOPICS.md row | Use the ROW TEMPLATE above — 3 fields: slug, description, YYYY-MM-DD | `topic-status` date filter reads the date field on every status check | Missing date = topic excluded from all status queries; coverage unreachable | `topic-status` |
| Table before rationale | Rationale first, signal table second | Owner roles emerge from the decisions described in the rationale — if table comes first, roles are column-fillers; if rationale comes first, roles are stakeholders accountable to named decisions | C-08 passes mechanically but carries no information; coverage review cannot verify roles against decision context | — |
| Inline commit gate | Structurally isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser; coverage computation returns no gate status; the commit gate silently does not exist | `topic-status` |
| Any strategy file location | Write to `simulations/{topic}/strategy.md` specifically | `topic-status` and `topic-scanner` both glob for this exact path | Flat path = both tools silently return zero results; topic appears to have no signals | `topic-status`, `topic-scanner` |

---

## DECISION TABLE SCHEMA

All five phase decision tables in this skill share the same column grammar:

| Path | Action | Consequence |
|------|--------|-------------|

Column definitions:
- **Path**: the execution fork — which branch is being taken (described from the model's perspective)
- **Action**: what you do when this path is chosen (the behavior triggered by that branch)
- **Consequence**: the specific tool-level outcome of that action (what the downstream tools experience as a result)

This schema is fixed across Phase 1 through Phase 5. When you read any phase decision table, column 3 is always the consequence. You do not re-parse each table's column structure — the grammar is established once here and applies uniformly.

---

## Phase 1 Decision: Collision Check

| Path | Action | Consequence |
|------|--------|-------------|
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; `topic-status` loads TOPICS.md on every check and finds exactly one entry; no coverage aggregation ambiguity |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate creates ambiguous coverage aggregation with no merge path; two strategy files cannot be reconciled |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

**If the topic does not exist in TOPICS.md**: proceed to Phase 2. `topic-status` will find exactly one entry; coverage aggregation is unambiguous.

**If the topic already exists in TOPICS.md**: stop. Report the collision. Do not create a duplicate. `topic-status` cannot merge two entries — the ambiguity has no resolution path and coverage aggregation becomes permanently unreliable for this topic.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles in the table emerge as stakeholders accountable to the decisions you just described. Each owner role is the person answerable to a specific question named in the rationale. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers assigned after the fact. Coverage review cannot verify them against any decision context — the roles have no stated accountability because the rationale was written to justify the table, not to surface the decisions that determined it.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool and mechanism:

- [ ] Rationale >= 2 sentences — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; absent block = owner-role verification skipped in coverage report)
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` F-01 exact string match** (tests each F-01 priority cell against `{essential, recommended, optional}` using equality comparison; any non-matching value is silently excluded from the commit-gate computation — no error emitted)
- [ ] COV-01: >= 1 `essential` row — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = no gate status returned; topic has no defined commit condition and investigation completion is undefined)
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` F-02 namespace aggregation** (groups discovered signals by F-02 value; single distinct namespace = monoculture flag; domain coverage cannot be verified across namespaces)
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by role)
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` F-04 pattern glob** (matches F-04 item names against `{topic}-*-YYYY-MM-DD.md`; any item name not matching this pattern is invisible to discovery; the signal is untracked in the coverage system)

**GATE FAILURE**: If any item above is unchecked — return to Phase 2. Repair the failing item(s) in the strategy file. Re-run this gate in full before proceeding to Phase 3. Do not proceed with any unchecked item outstanding.

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing essential signals by exact item name | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section — not a subsection of Phase 2, not a note inside the signal table.

**If you write the gate as an isolated `## COMMIT GATE` heading**: `topic-status` reads it as a named parseable section and returns correct gate status; the commit gate is enforceable by the toolchain.

**If you embed the gate inside the signal table**: `topic-status` section parser cannot find the `## COMMIT GATE` heading; coverage computation returns no gate status; the commit gate silently does not exist even if the content is present.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 Decision: Output Write

| Path | Action | Consequence |
|------|--------|-------------|
| **Copy ROW TEMPLATE; write strategy to `simulations/{topic}/strategy.md`** | Use the three-field template directly; write strategy to the topic subdirectory | `topic-status` and `topic-scanner` find both files; coverage computation proceeds normally |
| **Reconstruct row from memory OR write strategy to flat path** | Template rebuilt: `{YYYY-MM-DD}` dropped; flat path not matched by glob | C-01 fails (missing date) and/or C-02 fails (wrong path); both tools silently return zero results; topic is invisible to the coverage system |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above.

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries — the topic appears to have no coverage history.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — not to a flat path, not to a root-level file.

**If written to `simulations/{topic}/strategy.md`**: `topic-status` and `topic-scanner` both match the file via their glob; coverage computation proceeds normally.

**If written to any other path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate — with no error to indicate the path is wrong.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

Run this check after writing both files — not before.

**If you run this check after writing both files**: you are auditing the actual output that `topic-status` and `topic-scanner` will read. Errors are caught and corrected before the topic enters the coverage system.

**If you run this check before writing**: you are auditing your intentions, not your output. `topic-status` and `topic-scanner` read files; actual output may still fail even if every intention passes this check.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row; absent or malformed date = topic excluded from all date-range queries; topic appears to not exist in the coverage system).

**AMEND — DATE MISSING**: If C-01 fails: locate the topic's row in TOPICS.md. Copy the ROW TEMPLATE. Replace the malformed row with a correctly populated three-field version. Confirm the date cell matches `YYYY-MM-DD` exactly before re-checking C-01.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently — the topic appears to have no signals).

**AMEND — WRONG PATH**: If C-02 fails: identify the actual path the file was written to. Move the file to `simulations/{topic}/strategy.md`. Verify `simulations/{topic}/` exists; create it if absent. Re-run `topic-status` to confirm the file is now found before marking C-02 passing.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**AMEND — MISSING FIELDS**: If C-03 fails: list every row with a missing field. For each row, identify which of F-01 through F-05 is absent. Add the missing value. Re-scan all rows for five-field completeness before marking C-03 passing.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values with the correct VOCABULARY LOCK term. Re-scan all priority cells before marking C-04 passing.

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — NO ESSENTIAL SIGNAL**: If C-05 fails: identify the signal that is the minimum viable commit gate item for this topic. Promote it from `recommended` to `essential`, or add a new essential signal row. Re-check C-04 after any priority change before marking C-05 passing.

---

---

## V-05 — Full Integration (V-01 + V-02 + V-03)

**Axes combined**: V-01 (AMEND completeness) + V-02 (gate failure routing) + V-03 (recovery column in constraint matrix). All three repair surfaces are present simultaneously: the DEFAULTS matrix provides a repair contract at the constraint level (V-03); the Phase 2 exit gate provides a phase-level recovery routing instruction (V-02); the Phase 5 self-check provides item-level repair procedures for all five essential criteria (V-01). A model encountering any failure mode has a repair path available at every structural layer it may be reading: matrix, gate, or self-check.

**Hypothesis**: R7 V-05 closed the detection surface — every failure mode is detected. R8 V-05 closes the repair surface. A model failing any constraint in V-03's DEFAULTS row can follow the Recovery Path column to repair without reaching Phase 5. A model failing the Phase 2 gate follows the GATE FAILURE line to return to Phase 2 with explicit routing. A model that passes the gate but fails Phase 5 follows the named AMEND block for the specific criterion. The three surfaces form a repair cascade: earliest possible correction at the constraint level; phase-level routing at the gate; item-level procedure at the self-check. No failure mode is left without a prescribed next action.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction. `topic-status` will find the correct vocabulary in every cell. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may have already formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. `topic-status` will silently exclude those signals from the commit-gate check. You will need a re-scan pass after all rows are written — fixing errors that would not have occurred had you read this block first.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent downstream breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values. `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries — the topic appears to have no coverage history.

> **COPY — DO NOT RECONSTRUCT.**

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — `topic-status` parses all five for coverage computation; `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` gates on exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md` — `topic-scanner` uses this for discovery
- **F-05 Owner Role**: role responsible for this signal

---

## DEFAULTS THIS SKILL OVERRIDES

| Default | Rule | Why | What Breaks If You Skip | Tool | Recovery Path |
|---------|------|-----|------------------------|------|---------------|
| Any priority vocabulary | `essential` / `recommended` / `optional` exactly | `topic-status` exact string comparison on every commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` | List every priority cell with invalid vocabulary. Replace each with the correct VOCABULARY LOCK term. Re-scan all rows before re-running `topic-status`. |
| Free-form TOPICS.md row | Use the ROW TEMPLATE above — 3 fields: slug, description, YYYY-MM-DD | `topic-status` date filter reads the date field on every status check | Missing date = topic excluded from all status queries; coverage unreachable | `topic-status` | Locate the topic's row in TOPICS.md. Copy the ROW TEMPLATE above. Replace the malformed row with a correctly populated three-field version. Confirm date matches `YYYY-MM-DD`. |
| Table before rationale | Rationale first, signal table second | Owner roles emerge from the decisions described in the rationale — if table comes first, roles are column-fillers; if rationale comes first, roles are stakeholders accountable to named decisions | C-08 passes mechanically but carries no information; coverage review cannot verify roles against decision context | — | Write the rationale now, before any further work. Review each owner role cell and revise to name a stakeholder accountable to a specific decision in the rationale. |
| Inline commit gate | Structurally isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser; coverage computation returns no gate status; the commit gate silently does not exist | `topic-status` | Extract the gate content from wherever it is embedded. Write a new standalone `## COMMIT GATE` section after the signal table. List essential signals by exact item name. Delete the embedded version. |
| Any strategy file location | Write to `simulations/{topic}/strategy.md` specifically | `topic-status` and `topic-scanner` both glob for this exact path | Flat path = both tools silently return zero results; topic appears to have no signals | `topic-status`, `topic-scanner` | Identify the actual path written. Move the file to `simulations/{topic}/strategy.md`. Verify `simulations/{topic}/` exists; create it if absent. |

---

## DECISION TABLE SCHEMA

All five phase decision tables in this skill share the same column grammar:

| Path | Action | Consequence |
|------|--------|-------------|

Column definitions:
- **Path**: the execution fork — which branch is being taken (described from the model's perspective)
- **Action**: what you do when this path is chosen (the behavior triggered by that branch)
- **Consequence**: the specific tool-level outcome of that action (what the downstream tools experience as a result)

This schema is fixed across Phase 1 through Phase 5. When you read any phase decision table, column 3 is always the consequence. You do not re-parse each table's column structure — the grammar is established once here and applies uniformly.

---

## Phase 1 Decision: Collision Check

| Path | Action | Consequence |
|------|--------|-------------|
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; `topic-status` loads TOPICS.md on every check and finds exactly one entry; no coverage aggregation ambiguity |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate creates ambiguous coverage aggregation with no merge path; two strategy files cannot be reconciled |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

**If the topic does not exist in TOPICS.md**: proceed to Phase 2. `topic-status` will find exactly one entry; coverage aggregation is unambiguous.

**If the topic already exists in TOPICS.md**: stop. Report the collision. Do not create a duplicate. `topic-status` cannot merge two entries — the ambiguity has no resolution path and coverage aggregation becomes permanently unreliable for this topic.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles in the table emerge as stakeholders accountable to the decisions you just described. Each owner role is the person answerable to a specific question named in the rationale. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers assigned after the fact. Coverage review cannot verify them against any decision context — the roles have no stated accountability because the rationale was written to justify the table, not to surface the decisions that determined it.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool and mechanism:

- [ ] Rationale >= 2 sentences — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; absent block = owner-role verification skipped in coverage report)
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` F-01 exact string match** (tests each F-01 priority cell against `{essential, recommended, optional}` using equality comparison; any non-matching value is silently excluded from the commit-gate computation — no error emitted)
- [ ] COV-01: >= 1 `essential` row — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = no gate status returned; topic has no defined commit condition and investigation completion is undefined)
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` F-02 namespace aggregation** (groups discovered signals by F-02 value; single distinct namespace = monoculture flag; domain coverage cannot be verified across namespaces)
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by role)
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` F-04 pattern glob** (matches F-04 item names against `{topic}-*-YYYY-MM-DD.md`; any item name not matching this pattern is invisible to discovery; the signal is untracked in the coverage system)

**GATE FAILURE**: If any item above is unchecked — return to Phase 2. Repair the failing item(s) in the strategy file. Re-run this gate in full before proceeding to Phase 3. Do not proceed with any unchecked item outstanding.

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing essential signals by exact item name | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section — not a subsection of Phase 2, not a note inside the signal table.

**If you write the gate as an isolated `## COMMIT GATE` heading**: `topic-status` reads it as a named parseable section and returns correct gate status; the commit gate is enforceable by the toolchain.

**If you embed the gate inside the signal table**: `topic-status` section parser cannot find the `## COMMIT GATE` heading; coverage computation returns no gate status; the commit gate silently does not exist even if the content is present.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 Decision: Output Write

| Path | Action | Consequence |
|------|--------|-------------|
| **Copy ROW TEMPLATE; write strategy to `simulations/{topic}/strategy.md`** | Use the three-field template directly; write strategy to the topic subdirectory | `topic-status` and `topic-scanner` find both files; coverage computation proceeds normally |
| **Reconstruct row from memory OR write strategy to flat path** | Template rebuilt: `{YYYY-MM-DD}` dropped; flat path not matched by glob | C-01 fails (missing date) and/or C-02 fails (wrong path); both tools silently return zero results; topic is invisible to the coverage system |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above.

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries — the topic appears to have no coverage history.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — not to a flat path, not to a root-level file.

**If written to `simulations/{topic}/strategy.md`**: `topic-status` and `topic-scanner` both match the file via their glob; coverage computation proceeds normally.

**If written to any other path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate — with no error to indicate the path is wrong.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

Run this check after writing both files — not before.

**If you run this check after writing both files**: you are auditing the actual output that `topic-status` and `topic-scanner` will read. Errors are caught and corrected before the topic enters the coverage system.

**If you run this check before writing**: you are auditing your intentions, not your output. `topic-status` and `topic-scanner` read files; actual output may still fail even if every intention passes this check.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row; absent or malformed date = topic excluded from all date-range queries; topic appears to not exist in the coverage system).

**AMEND — DATE MISSING**: If C-01 fails: locate the topic's row in TOPICS.md. Copy the ROW TEMPLATE above. Replace the malformed row with a correctly populated three-field version. Confirm the date cell matches `YYYY-MM-DD` exactly before re-checking C-01.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently — the topic appears to have no signals).

**AMEND — WRONG PATH**: If C-02 fails: identify the actual path the file was written to. Move the file to `simulations/{topic}/strategy.md`. Verify `simulations/{topic}/` exists; create it if absent. Re-run `topic-status` to confirm the file is now found before marking C-02 passing.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**AMEND — MISSING FIELDS**: If C-03 fails: list every row with a missing field. For each row, identify which of F-01 through F-05 is absent. Add the missing value. Re-scan all rows for five-field completeness before marking C-03 passing.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values with the correct VOCABULARY LOCK term. Re-scan all priority cells before marking C-04 passing.

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — NO ESSENTIAL SIGNAL**: If C-05 fails: identify the signal that is the minimum viable commit gate item for this topic. Promote it from `recommended` to `essential`, or add a new essential signal row. Re-check C-04 after any priority change before marking C-05 passing.
