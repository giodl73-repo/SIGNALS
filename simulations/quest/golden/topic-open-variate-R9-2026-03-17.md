# topic-open — Round 9 Variations

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric version**: v7 (C-01 through C-30, aspirational denominator = 22)
**Base**: R8 V-05 — passes all C-01 through C-30 plus prospective C-31 (AMEND completeness), C-32 (gate failure routing), C-33 (recovery column in constraint matrix), C-34 (independent repair surfaces).

**Round context**: R8 scored five variations on the v7 rubric. All five scored 100/100. The R8 scorecard confirmed four prospective criteria from the three R8 axes: C-31 (named AMEND blocks with uniform labels for all five essential criteria), C-32 (explicit GATE FAILURE line with return phase + repair + re-run condition after the Phase 2 exit gate), C-33 (Recovery Path column in DEFAULTS THIS SKILL OVERRIDES for all five constraint rows), C-34 (DEFAULTS and Phase 5 AMEND blocks carry identical repair procedures without cross-referencing each other). R8 V-05 passes all four. R9 probes three structural gaps visible in R8 V-05 but not yet criteriaized: (1) gate coverage completeness — only Phase 2 has a formal exit gate checklist and GATE FAILURE routing; Phases 1, 3, and 4 have decision logic but no gate structure; a model detecting a Phase 1 collision or a Phase 3 embedding error has no formal routing instruction; (2) recommended criteria coverage in Phase 5 — Phase 5 checks only C-01 through C-05 (essential); C-06 (>=2 namespaces), C-07 (prose rationale >=2 sentences), and C-08 (>=2 distinct owner roles) are verified at Phase 2 gate only; a model that passes Phase 2 but later collapses the table has no Phase 5 catch; (3) worked example in FIELD SCHEMA — F-01 through F-05 are defined abstractly; no concrete example row demonstrates the complete five-field pattern including the `{topic}-{signal}-{date}.md` naming convention; a model constructing its first row has no reference artifact.

**Variation axes selected**:
- V-01: Multi-phase exit gates — Phases 1, 3, and 4 each gain a formal exit gate checklist and GATE FAILURE routing line
- V-02: Extended Phase 5 self-check — adds C-06, C-07, and C-08 checks with named AMEND blocks, extending Phase 5 from essential-only coverage to full recommended coverage
- V-03: Worked example in FIELD SCHEMA — adds a concrete filled-in signal row after the field definitions, and an example COMMIT GATE after the template; both use placeholder slugs demonstrating correct format
- V-04: V-01 + V-02 combination — multi-phase gates AND extended self-check
- V-05: V-01 + V-02 + V-03 full integration — all three axes combined

All five variations use R8 V-05 as base.

---

## V-01 — Multi-Phase Exit Gates

**Axis**: Phases 1, 3, and 4 each gain a formal exit gate checklist and GATE FAILURE routing line, matching the pattern established in Phase 2. R8 V-05 has one exit gate (Phase 2). Phases 1, 3, and 4 have decision tables and if/if narrative instructions but no gate checklist and no GATE FAILURE line. A model that detects a Phase 1 collision is told to "stop and report" but receives no formal routing instruction specifying how to exit cleanly. A model that embeds the commit gate in Phase 3 has a decision table describing the wrong path but no gate checklist to confirm the right path was taken. A model that completes Phase 4 has no write-confirmation gate to verify both files landed at the expected paths before the self-check runs.

**Hypothesis**: Asymmetric gate coverage creates asymmetric failure handling. Phase 2's GATE FAILURE line is effective precisely because it names the return phase, repair action, and re-run condition — three things that close the correction loop. Phases 1, 3, and 4 have detection (decision tables + if/if) but no loop closure. Adding gate checklists and GATE FAILURE lines to all four phases creates uniform gate grammar across the skill — any phase can be exited cleanly with a routing instruction. Phase 1's GATE FAILURE is terminal (stop + redirect) rather than return-to-repair, making it the skill's single early-exit point.

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

**Phase 1 Exit Gate** — confirm collision check before proceeding:

- [ ] Topic slug not found in TOPICS.md — **`topic-status` TOPICS.md slug scan** (reads each row's first pipe-delimited field; any row matching the topic slug = duplicate entry exists; `topic-status` coverage aggregation becomes ambiguous with no merge path)

**GATE FAILURE**: If topic found in TOPICS.md — stop this invocation entirely. Do not proceed to Phase 2. Report the collision slug to the user. Determine whether to (a) use the existing topic entry and run `/topic-plan` to update its strategy, or (b) choose a different topic slug and re-invoke `/topic-open` with the new slug. Do not create a duplicate under any interpretation.

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

**Phase 3 Exit Gate** — confirm commit gate structure before proceeding:

- [ ] COMMIT GATE written as standalone `## COMMIT GATE` heading — **`topic-status` section-header scan** (scans strategy.md for a line matching `## COMMIT GATE` exactly; no match = coverage computation returns no gate status; the commit gate silently does not exist)
- [ ] Every essential signal from the signal table is listed in COMMIT GATE by exact F-04 item name — **`topic-status` COMMIT GATE item list** (reads each item in the COMMIT GATE section and matches against F-04 values marked `essential` in the signal table; any missing essential item = gate is structurally incomplete; `topic-status` may report gate-satisfied prematurely)

**GATE FAILURE**: If any item above is unchecked — return to Phase 3. Repair the gate heading or the essential signal list. Re-run this gate before proceeding to Phase 4.

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

**Phase 4 Exit Gate** — confirm both writes landed before proceeding to the self-check:

- [ ] TOPICS.md row appended with slug, description, and YYYY-MM-DD date — **`topic-status` TOPICS.md row presence** (reads the file for a row whose first column matches the topic slug and whose third column contains a valid YYYY-MM-DD value; absent row or malformed date = topic excluded from all status queries)
- [ ] `simulations/{topic}/strategy.md` exists at the correct path — **`topic-scanner` path glob** (executes `simulations/*/strategy.md` glob; no match for this topic = both tools return zero results silently; topic has no coverage history in the system)

**GATE FAILURE**: If any item above is unchecked — return to Phase 4. Re-execute the failing write. Re-run this gate before proceeding to Phase 5.

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

---

---

## V-02 — Extended Phase 5 Self-Check

**Axis**: Phase 5 self-check extended to cover C-06, C-07, and C-08 (recommended criteria) with named AMEND blocks, matching the C-31 repair-protocol pattern established in R8. R8 V-05's Phase 5 checks only C-01 through C-05 (essential criteria). C-06 (>=2 distinct namespaces), C-07 (rationale >= 2 sentences), and C-08 (>=2 distinct owner roles) are verified only at the Phase 2 exit gate. A model that passes Phase 2's gate and then compresses the signal table — removing rows to reduce scope, collapsing namespaces, or unifying owner roles — has no Phase 5 catch. The failure exists in the written file but the self-check never reads for it.

**Hypothesis**: Phase 2's exit gate is a pre-write verification: it confirms the table is structurally sound before the commit gate is written and before the files are flushed. Phase 5 is a post-write audit of the actual files. These are two different verification moments. A table that passes Phase 2 can be modified during Phase 3 and 4 work (e.g., a row deleted, a namespace collapsed, a role unified) without triggering any check. Extending Phase 5 to cover C-06 through C-08 closes this window — any post-Phase-2 modification that degrades recommended coverage is caught before the topic enters the system. The AMEND blocks follow the same `AMEND — {CONDITION NAME}` format established for C-01 through C-05, making Phase 5 a uniform repair protocol across all eight criteria.

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

**C-06**: >= 2 distinct namespaces in the signal table? — **`topic-scanner` F-02 namespace aggregation** (groups F-02 values across all signal rows; fewer than 2 distinct values = monoculture flag; single-namespace investigation cannot verify cross-domain coverage; `topic-status` cannot produce a multi-domain coverage picture).

**AMEND — MONOCULTURE NAMESPACE**: If C-06 fails: return to the rationale. Identify which additional domain provides evidence relevant to the design decisions described. Add at least one signal from a second namespace. Re-scan F-02 values for at least 2 distinct namespaces before marking C-06 passing.

**C-07**: Rationale is >= 2 sentences and states both (1) why this topic requires investigation and (2) what design decisions the signals inform? — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; a single-sentence or absent rationale = owner-role verification skipped in the coverage report; C-08 cannot be verified against decision context).

**AMEND — THIN RATIONALE**: If C-07 fails: return to the rationale block in strategy.md. Add a second sentence naming the specific design decisions the signals will inform. Re-read the rationale to confirm it states both dimensions before marking C-07 passing.

**C-08**: >= 2 distinct owner roles in the signal table? — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by accountable stakeholder).

**AMEND — DEGENERATE OWNERSHIP**: If C-08 fails: return to the rationale. Identify a second stakeholder accountable to a different decision named in the rationale. Assign that role as owner for at least one signal where that accountability is appropriate. Re-scan F-05 values for at least 2 distinct roles before marking C-08 passing.

---

---

## V-03 — Worked Example in FIELD SCHEMA

**Axis**: A concrete filled-in example row is added to FIELD SCHEMA immediately after the field definitions, demonstrating all five fields populated with the correct `{topic}-{signal}-{date}.md` naming convention. A second example is added after the COMMIT GATE template in Phase 3, showing a completed COMMIT GATE section with two essential signals listed by exact item name. Neither example contains abstract placeholders — both use fixed, readable values that pattern-match all tool discovery rules. R8 V-05 has no examples anywhere in the skill body; all schema information is abstract.

**Hypothesis**: F-04 item name errors (`{topic}-{signal}-{date}.md` pattern violations) are the most consequential field errors: `topic-scanner` uses F-04 for discovery; any deviation makes the signal invisible with no error. The FIELD SCHEMA defines the pattern abstractly. A model constructing its first signal row applies the pattern from the abstract definition — with no reference artifact to validate against. A concrete example row provides a second-channel verification: the model can compare its constructed row against the example and detect formatting deviations (wrong date format, missing topic prefix, wrong extension) before writing the file. The COMMIT GATE example serves the same function for gate structure: the model can confirm its written gate matches the example's structural grammar (standalone heading, bullet-per-item, exact item names matching F-04).

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

**Example signal row** — all five fields populated, correct naming pattern, tool-discoverable:

| F-01 Priority | F-02 Namespace | F-03 Skill | F-04 Item Name | F-05 Owner Role |
|--------------|----------------|------------|----------------|-----------------|
| `essential` | `scout` | `scout-competitors` | `my-topic-competitors-2026-01-15.md` | Product Manager |

Replace `my-topic` with your topic slug and `2026-01-15` with today's date throughout. `topic-scanner` matches F-04 against `{topic}-*-YYYY-MM-DD.md` — any deviation (wrong slug prefix, wrong date format, wrong extension) makes the signal invisible to discovery with no error emitted.

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

**Example COMMIT GATE** (two essential signals, correctly formatted):

```
## COMMIT GATE
Design commit requires all essential signals complete:
- my-topic-competitors-2026-01-15.md
- my-topic-requirements-2026-01-15.md
```

Item names in the gate must match F-04 item names exactly — `topic-status` reads each bullet and checks it against the F-04 column in the signal table; any name mismatch = gate item is unresolvable; `topic-status` reports "gate incomplete" even if the signal exists in the table.

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

---

---

## V-04 — Multi-Phase Gates + Extended Self-Check (V-01 + V-02)

**Axes combined**: V-01 (Phases 1, 3, and 4 gain exit gates with GATE FAILURE routing) + V-02 (Phase 5 self-check extended to C-06, C-07, C-08 with AMEND blocks). The skill now has a formal exit gate at every phase: Phase 1 (terminal GATE FAILURE on collision), Phase 2 (return-to-repair GATE FAILURE), Phase 3 (return-to-repair on gate structure failure), Phase 4 (return-to-repair on write failure), Phase 5 (repair protocol covering C-01 through C-08). No phase exits without a routing instruction.

**Hypothesis**: V-01 and V-02 address adjacent gaps — V-01 closes phase-level routing (what does the model do when a phase decision goes wrong), V-02 closes post-write audit coverage (what does Phase 5 catch that Phase 2 may have missed). Together they create a complete repair graph: every phase has a gate, every gate has a GATE FAILURE routing instruction, and Phase 5 audits both essential and recommended criteria. A model executing this skill encounters no phase transition without knowing exactly what to do if the transition condition is not met.

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

**Phase 1 Exit Gate** — confirm collision check before proceeding:

- [ ] Topic slug not found in TOPICS.md — **`topic-status` TOPICS.md slug scan** (reads each row's first pipe-delimited field; any row matching the topic slug = duplicate entry exists; `topic-status` coverage aggregation becomes ambiguous with no merge path)

**GATE FAILURE**: If topic found in TOPICS.md — stop this invocation entirely. Do not proceed to Phase 2. Report the collision slug to the user. Determine whether to (a) use the existing topic entry and run `/topic-plan` to update its strategy, or (b) choose a different topic slug and re-invoke `/topic-open` with the new slug. Do not create a duplicate under any interpretation.

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

**Phase 3 Exit Gate** — confirm commit gate structure before proceeding:

- [ ] COMMIT GATE written as standalone `## COMMIT GATE` heading — **`topic-status` section-header scan** (scans strategy.md for a line matching `## COMMIT GATE` exactly; no match = coverage computation returns no gate status; the commit gate silently does not exist)
- [ ] Every essential signal from the signal table is listed in COMMIT GATE by exact F-04 item name — **`topic-status` COMMIT GATE item list** (reads each item in the COMMIT GATE section and matches against F-04 values marked `essential` in the signal table; any missing essential item = gate is structurally incomplete; `topic-status` may report gate-satisfied prematurely)

**GATE FAILURE**: If any item above is unchecked — return to Phase 3. Repair the gate heading or the essential signal list. Re-run this gate before proceeding to Phase 4.

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

**Phase 4 Exit Gate** — confirm both writes landed before proceeding to the self-check:

- [ ] TOPICS.md row appended with slug, description, and YYYY-MM-DD date — **`topic-status` TOPICS.md row presence** (reads the file for a row whose first column matches the topic slug and whose third column contains a valid YYYY-MM-DD value; absent row or malformed date = topic excluded from all status queries)
- [ ] `simulations/{topic}/strategy.md` exists at the correct path — **`topic-scanner` path glob** (executes `simulations/*/strategy.md` glob; no match for this topic = both tools return zero results silently; topic has no coverage history in the system)

**GATE FAILURE**: If any item above is unchecked — return to Phase 4. Re-execute the failing write. Re-run this gate before proceeding to Phase 5.

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

**C-06**: >= 2 distinct namespaces in the signal table? — **`topic-scanner` F-02 namespace aggregation** (groups F-02 values across all signal rows; fewer than 2 distinct values = monoculture flag; single-namespace investigation cannot verify cross-domain coverage; `topic-status` cannot produce a multi-domain coverage picture).

**AMEND — MONOCULTURE NAMESPACE**: If C-06 fails: return to the rationale. Identify which additional domain provides evidence relevant to the design decisions described. Add at least one signal from a second namespace. Re-scan F-02 values for at least 2 distinct namespaces before marking C-06 passing.

**C-07**: Rationale is >= 2 sentences and states both (1) why this topic requires investigation and (2) what design decisions the signals inform? — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; a single-sentence or absent rationale = owner-role verification skipped in the coverage report; C-08 cannot be verified against decision context).

**AMEND — THIN RATIONALE**: If C-07 fails: return to the rationale block in strategy.md. Add a second sentence naming the specific design decisions the signals will inform. Re-read the rationale to confirm it states both dimensions before marking C-07 passing.

**C-08**: >= 2 distinct owner roles in the signal table? — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by accountable stakeholder).

**AMEND — DEGENERATE OWNERSHIP**: If C-08 fails: return to the rationale. Identify a second stakeholder accountable to a different decision named in the rationale. Assign that role as owner for at least one signal where that accountability is appropriate. Re-scan F-05 values for at least 2 distinct roles before marking C-08 passing.

---

---

## V-05 — Full Integration (V-01 + V-02 + V-03)

**Axes combined**: V-01 (multi-phase exit gates) + V-02 (extended Phase 5 self-check) + V-03 (worked example in FIELD SCHEMA). All three axes compose without structural conflict: the exit gates added by V-01 sit inside Phase 1, 3, and 4 bodies and do not modify schema, examples, or the self-check; the self-check extension added by V-02 appends to Phase 5 after C-05 and does not modify gate content; the examples added by V-03 extend FIELD SCHEMA and Phase 3 template with illustrative rows and do not modify phase logic.

**Hypothesis**: R8 V-05 established three repair layers — DEFAULTS Recovery Path (constraint level), Phase 2 GATE FAILURE (phase level), Phase 5 AMEND blocks (item level). R9 V-05 extends these layers across the full skill: all four phases have gate routing (V-01), Phase 5 covers all eight criteria rather than five (V-02), and the schema carries a concrete reference row the model can validate against before writing (V-03). The reference row adds a fourth verification channel: a model constructing F-04 item names can compare its output against the example to catch deviations before the file is written — earlier than Phase 4 gate, earlier than Phase 5 AMEND, earlier than `topic-scanner` discovery failure. A model encountering the example at schema-read time has the format locked before constructing any row.

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

**Example signal row** — all five fields populated, correct naming pattern, tool-discoverable:

| F-01 Priority | F-02 Namespace | F-03 Skill | F-04 Item Name | F-05 Owner Role |
|--------------|----------------|------------|----------------|-----------------|
| `essential` | `scout` | `scout-competitors` | `my-topic-competitors-2026-01-15.md` | Product Manager |

Replace `my-topic` with your topic slug and `2026-01-15` with today's date throughout. `topic-scanner` matches F-04 against `{topic}-*-YYYY-MM-DD.md` — any deviation (wrong slug prefix, wrong date format, wrong extension) makes the signal invisible to discovery with no error emitted.

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

**Phase 1 Exit Gate** — confirm collision check before proceeding:

- [ ] Topic slug not found in TOPICS.md — **`topic-status` TOPICS.md slug scan** (reads each row's first pipe-delimited field; any row matching the topic slug = duplicate entry exists; `topic-status` coverage aggregation becomes ambiguous with no merge path)

**GATE FAILURE**: If topic found in TOPICS.md — stop this invocation entirely. Do not proceed to Phase 2. Report the collision slug to the user. Determine whether to (a) use the existing topic entry and run `/topic-plan` to update its strategy, or (b) choose a different topic slug and re-invoke `/topic-open` with the new slug. Do not create a duplicate under any interpretation.

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

**Example COMMIT GATE** (two essential signals, correctly formatted):

```
## COMMIT GATE
Design commit requires all essential signals complete:
- my-topic-competitors-2026-01-15.md
- my-topic-requirements-2026-01-15.md
```

Item names in the gate must match F-04 item names exactly — `topic-status` reads each bullet and checks it against the F-04 column in the signal table; any name mismatch = gate item is unresolvable; `topic-status` reports "gate incomplete" even if the signal exists in the table.

**Phase 3 Exit Gate** — confirm commit gate structure before proceeding:

- [ ] COMMIT GATE written as standalone `## COMMIT GATE` heading — **`topic-status` section-header scan** (scans strategy.md for a line matching `## COMMIT GATE` exactly; no match = coverage computation returns no gate status; the commit gate silently does not exist)
- [ ] Every essential signal from the signal table is listed in COMMIT GATE by exact F-04 item name — **`topic-status` COMMIT GATE item list** (reads each item in the COMMIT GATE section and matches against F-04 values marked `essential` in the signal table; any missing essential item = gate is structurally incomplete; `topic-status` may report gate-satisfied prematurely)

**GATE FAILURE**: If any item above is unchecked — return to Phase 3. Repair the gate heading or the essential signal list. Re-run this gate before proceeding to Phase 4.

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

**Phase 4 Exit Gate** — confirm both writes landed before proceeding to the self-check:

- [ ] TOPICS.md row appended with slug, description, and YYYY-MM-DD date — **`topic-status` TOPICS.md row presence** (reads the file for a row whose first column matches the topic slug and whose third column contains a valid YYYY-MM-DD value; absent row or malformed date = topic excluded from all status queries)
- [ ] `simulations/{topic}/strategy.md` exists at the correct path — **`topic-scanner` path glob** (executes `simulations/*/strategy.md` glob; no match for this topic = both tools return zero results silently; topic has no coverage history in the system)

**GATE FAILURE**: If any item above is unchecked — return to Phase 4. Re-execute the failing write. Re-run this gate before proceeding to Phase 5.

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

**C-06**: >= 2 distinct namespaces in the signal table? — **`topic-scanner` F-02 namespace aggregation** (groups F-02 values across all signal rows; fewer than 2 distinct values = monoculture flag; single-namespace investigation cannot verify cross-domain coverage; `topic-status` cannot produce a multi-domain coverage picture).

**AMEND — MONOCULTURE NAMESPACE**: If C-06 fails: return to the rationale. Identify which additional domain provides evidence relevant to the design decisions described. Add at least one signal from a second namespace. Re-scan F-02 values for at least 2 distinct namespaces before marking C-06 passing.

**C-07**: Rationale is >= 2 sentences and states both (1) why this topic requires investigation and (2) what design decisions the signals inform? — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; a single-sentence or absent rationale = owner-role verification skipped in the coverage report; C-08 cannot be verified against decision context).

**AMEND — THIN RATIONALE**: If C-07 fails: return to the rationale block in strategy.md. Add a second sentence naming the specific design decisions the signals will inform. Re-read the rationale to confirm it states both dimensions before marking C-07 passing.

**C-08**: >= 2 distinct owner roles in the signal table? — **`topic-status` F-05 unique-value count** (aggregates F-05 owner role values; single unique value = degenerate accountability distribution; coverage report cannot distinguish signal ownership by accountable stakeholder).

**AMEND — DEGENERATE OWNERSHIP**: If C-08 fails: return to the rationale. Identify a second stakeholder accountable to a different decision named in the rationale. Assign that role as owner for at least one signal where that accountability is appropriate. Re-scan F-05 values for at least 2 distinct roles before marking C-08 passing.
