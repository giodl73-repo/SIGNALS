# topic-open — Round 7 Variations

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric version**: v7 (C-01 through C-30, aspirational denominator = 22)
**Round context**: R6 scored three single-axis variations on the v6 rubric (C-01–C-27, denominator 19). V-01 passed C-25 (gate/checklist tool citations with two-slot format) but failed C-26, C-23, C-27. V-02 passed C-26 (universal if/if in every ordering instruction) but failed C-25, C-23, C-27. V-03 passed C-27 (five labeled decision tables, consistent Path/Action/Consequence columns) but failed C-25 and C-26. Three new excellence patterns extracted: C-28 (uniform column schema across all decision tables — not just consistent labels but declared structural grammar), C-29 (tool citations include the enforcement mechanism — how the tool checks, not just which tool and what), C-30 (ordering instructions carry inline if/if independent of decision tables — no delegation to "see Phase X Decision above"). Denominator: 19 → 22.

**Variation axes selected**:
- V-01: C-28 axis — explicit DECISION TABLE SCHEMA block declared before all phase tables, anchoring Path/Action/Consequence grammar as a document-wide standard
- V-02: C-29 axis — every exit gate condition and self-check item names the tool, what it checks, AND the check mechanism (field reference + operation)
- V-03: C-30 axis — every ordering instruction is self-contained; all "see Phase X Decision above" delegation removed; if/if framing present inline without back-reference
- V-04: C-28 + C-29 combination — schema declaration AND enforcement-mechanism citations simultaneously
- V-05: C-28 + C-29 + C-30 full integration — declared schema, mechanism-level citations, and fully self-contained ordering instructions at maximum depth

All five variations use R6 V-05 as base (passes C-25, C-26, C-27 + all C-01 through C-24).

---

## V-01 — Declared Decision Table Schema (C-28)

**Axis**: A DECISION TABLE SCHEMA block is declared immediately before the first phase decision table. The block names the three-column grammar (Path / Action / Consequence), defines each column's role, and explicitly states that all five phase decision tables share this schema. The declaration converts column consistency from an observed property into an asserted one — a model reading the first decision table has already been told what each column means in every table, without re-parsing.

**Hypothesis**: R6 V-03 achieved C-27 (five labeled tables, Path/Action/Consequence) and R6 V-05 compounded all three axes. The tables already use consistent columns — but consistency without declaration is an implicit contract. C-28 asks: what changes when the schema is explicit? A model that reads "all five phase decision tables share this grammar" before encountering the first table loads the column contract once and applies it universally. The declaration also makes C-28 auditable: a scorer can verify the assertion against any table without inferring whether the author intended consistency or happened to achieve it. Schema-as-assertion vs schema-as-pattern is the operative distinction.

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

**If the topic does not exist**: proceed to Phase 2.

**If the topic already exists**: stop. Report the collision. Do not create a duplicate.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles emerge as stakeholders accountable to the decisions you named. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers. Coverage review cannot verify them against any decision context.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool:

- [ ] Rationale >= 2 sentences — `topic-status` narrative context: rationale is the basis for owner-role coverage verification; absent rationale = role accountability is unverifiable
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` exact string match**: out-of-vocabulary priority is silently excluded from the commit-gate check; the gate never fires for that signal
- [ ] COV-01: >= 1 `essential` row — **`topic-status` commit-gate check**: returns no gate status without an essential signal; the topic has no defined commit condition
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` namespace grouping**: single-namespace strategies produce degenerate discovery; signals cannot be grouped by domain
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` role-coverage report**: single-role strategies return degenerate accountability distribution; the report cannot assign signals to differentiated owners
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` discovery pattern**: wrong format = artifact invisible to discovery; signal is untracked in the coverage system

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing essential signals by exact item name | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section.

**If isolated as `## COMMIT GATE`**: `topic-status` reads it as a named parseable section; coverage computation returns correct gate status.

**If embedded inside the signal table**: `topic-status` section parser cannot find it; the commit gate silently does not exist.

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

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md`.

**If written to the correct path**: `topic-status` and `topic-scanner` both find the file; coverage computation proceeds normally.

**If written to a flat path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

**If you run this check after writing both files**: `topic-status` and `topic-scanner` see the same files you are checking — errors are caught and corrected before they reach the coverage system.

**If you run this check before writing**: you verify intentions. The tools read files, not intentions; actual output may still fail even if intentions passed.

Run after both files are written.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` date filter**: reads this field on every status check; missing date excludes the topic from all coverage queries permanently.
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` glob**: both tools search this exact path; flat path causes both to return zero results silently.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` coverage parser**: parses all five fields for coverage computation; missing field excludes that signal from coverage results.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` exact string comparison**: any other value is silently excluded from the commit-gate check; the gate never fires for that signal.

**C-05**: At least one `essential` row? — **`topic-status` commit-gate check**: returns no gate status without an essential signal; the Design Lead cannot determine when investigation is complete.

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-02 — Enforcement Mechanism in Tool Citations (C-29)

**Axis**: Every tool citation at an exit gate condition or self-check checklist item specifies not just the tool name and what it checks, but the enforcement mechanism — the specific field read and operation performed. Citations follow the format: `tool` + `what` + `via` + `how` (field reference + operation type). For example: "**`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`)". The mechanism makes the contract self-explanatory: a model can understand why the rule matters without consulting the tool's documentation.

**Hypothesis**: R6 V-01 achieved C-25 (tool name + what it checks) by annotating every gate and checklist item with the tool and its check target. C-29 asks: what is added when the mechanism — the field and operation — is also named? A model that sees "topic-status F-01 exact string match" understands both what will break and the exact structural reason: the failure is a comparison failure against a specific field, not a general tool rejection. Mechanism-level citations eliminate the inferential gap between "this rule exists" and "this is how the rule is enforced at the field level."

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

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

**If the topic does not exist**: proceed to Phase 2.

**If the topic already exists**: stop. Report the collision. Do not create a duplicate.

---

## Phase 1 Decision: Collision Check

| Path | Action | Consequence |
|------|--------|-------------|
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; `topic-status` loads TOPICS.md on every check and finds exactly one entry; no coverage aggregation ambiguity |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate creates ambiguous coverage aggregation with no merge path; two strategy files cannot be reconciled |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles emerge as stakeholders accountable to the decisions you named. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers. Coverage review cannot verify them against any decision context.

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

Write as a structurally isolated section.

**If isolated as `## COMMIT GATE`**: `topic-status` reads it as a named parseable section; coverage computation returns correct gate status.

**If embedded inside the signal table**: `topic-status` section parser cannot find it; the commit gate silently does not exist.

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

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md`.

**If written to the correct path**: `topic-status` and `topic-scanner` both find the file; coverage computation proceeds normally.

**If written to a flat path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

**If you run this check after writing both files**: `topic-status` and `topic-scanner` see the same files you are checking — errors are caught and corrected before they reach the coverage system.

**If you run this check before writing**: you verify intentions. The tools read files, not intentions; actual output may still fail even if intentions passed.

Run after both files are written.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row; absent or malformed date = topic excluded from all date-range queries; topic appears to not exist in the coverage system).
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently — the topic appears to have no signals).

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-03 — Self-Contained Ordering Instructions (C-30)

**Axis**: Every ordering instruction in the skill carries its own inline if/if comparison in the instruction body. No instruction delegates its comparative framing to a nearby decision table. The phrases "see Phase X Decision above," "as noted above," or equivalent table references are removed from all instruction bodies. Decision tables remain as structural pre-phase elements (C-27) — they are not removed. But the instruction body for each phase independently contains the if/if contrast, so a model executing a phase without having internalized the preceding decision table still encounters the critical branch condition directly in the instruction text.

**Hypothesis**: R6 V-05 achieved deep C-26 (universal comparative framing on every ordering instruction) but V-03 was specifically penalized for delegating its framing to decision tables ("see Phase X Decision above"). C-30 asks: what changes when the decision table and the instruction body both carry the if/if independently? The decision table is a pre-phase structural element; the instruction body is the execution frame. A model executing the instruction at runtime may not have the decision table loaded in its active context window — if the if/if exists only in the table, the instruction is incomplete at the point of execution. Self-contained instructions are correct at any context depth.

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

**Phase 2 Exit Gate** — every condition names its enforcement tool:

- [ ] Rationale >= 2 sentences — `topic-status` narrative context: rationale is the basis for owner-role coverage verification; absent rationale = role accountability is unverifiable
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` exact string match**: out-of-vocabulary priority is silently excluded from the commit-gate check; the gate never fires for that signal
- [ ] COV-01: >= 1 `essential` row — **`topic-status` commit-gate check**: returns no gate status without an essential signal; the topic has no defined commit condition
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` namespace grouping**: single-namespace strategies produce degenerate discovery; signals cannot be grouped by domain
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` role-coverage report**: single-role strategies return degenerate accountability distribution; the report cannot assign signals to differentiated owners
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` discovery pattern**: wrong format = artifact invisible to discovery; signal is untracked in the coverage system

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing essential signals by exact item name | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section — not a subsection of Phase 2, not a note inside the signal table.

**If you write the gate as an isolated `## COMMIT GATE` heading**: `topic-status` reads it as a named parseable section; coverage computation returns correct gate status; the commit gate is enforceable by the toolchain.

**If you embed the gate inside the signal table**: `topic-status` section parser cannot find the `## COMMIT GATE` heading; coverage computation returns no gate status; the commit gate silently does not exist even if the content is accurate.

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

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` date filter**: reads this field on every status check; missing date excludes the topic from all coverage queries permanently.
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` glob**: both tools search this exact path; flat path causes both to return zero results silently.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` coverage parser**: parses all five fields for coverage computation; missing field excludes that signal from coverage results.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` exact string comparison**: any other value is silently excluded from the commit-gate check; the gate never fires for that signal.

**C-05**: At least one `essential` row? — **`topic-status` commit-gate check**: returns no gate status without an essential signal; the Design Lead cannot determine when investigation is complete.

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-04 — Schema Declaration + Enforcement Mechanism (C-28 + C-29)

**Axis**: Two axes applied simultaneously. (1) A DECISION TABLE SCHEMA block declares the Path/Action/Consequence column grammar as a document-wide standard before Phase 1's decision table — column definitions are established once and apply to all five phase tables. (2) Every exit gate condition and every self-check checklist item names the tool, what it checks, and the check mechanism (field reference + operation type), following the format: `tool` + `what` + `via` + `how`. The two additions are complementary: schema declaration makes the decision surface scannable as a coherent system; mechanism-level citations make the enforcement surface legible at the field level.

**Hypothesis**: V-01 adds schema declaration alone; V-02 adds mechanism-level citations alone. Neither combination is present in the R6 variations. C-28 and C-29 operate on different layers — C-28 on the structural frame (decision table columns), C-29 on the enforcement annotations (gate and checklist citations). A model that reads a declared schema and mechanism-level citations receives two independent precision upgrades: it knows what each decision table column means before the first table, and it knows exactly how each enforcement tool operates at the field level. The combination should not produce interference — the two signals reinforce understanding at different structural depths.

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

**If the topic does not exist**: proceed to Phase 2.

**If the topic already exists**: stop. Report the collision. Do not create a duplicate.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

**If you write the rationale first**: owner roles emerge as stakeholders accountable to the decisions you named. `topic-status` coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers. Coverage review cannot verify them against any decision context.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool and mechanism:

- [ ] Rationale >= 2 sentences — **`topic-status` rationale presence check** (reads the strategy file for a prose block before the signal table; absent block = owner-role verification skipped in coverage report)
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` F-01 exact string match** (tests each F-01 priority cell against `{essential, recommended, optional}` using equality comparison; any non-matching value is silently excluded from the commit-gate computation — no error emitted)
- [ ] COV-01: >= 1 `essential` row — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = no gate status returned; topic has no defined commit condition)
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

Write as a structurally isolated section.

**If isolated as `## COMMIT GATE`**: `topic-status` reads it as a named parseable section; coverage computation returns correct gate status.

**If embedded inside the signal table**: `topic-status` section parser cannot find it; the commit gate silently does not exist.

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

**If you copy the template**: three fields are structurally present; `topic-status` date filter finds the date field.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped; `topic-status` excludes the topic from all queries.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md`.

**If written to the correct path**: `topic-status` and `topic-scanner` both find the file; coverage computation proceeds normally.

**If written to a flat path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Audit the actual files produced | Errors in actual output are caught; `topic-status` and `topic-scanner` see the corrected files when they next run |
| **Run before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

**If you run this check after writing both files**: `topic-status` and `topic-scanner` see the same files you are checking — errors are caught and corrected before they reach the coverage system.

**If you run this check before writing**: you verify intentions. The tools read files, not intentions; actual output may still fail even if intentions passed.

Run after both files are written.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` TOPICS.md column-3 read** (reads the third pipe-separated column on the topic's row; absent or malformed date = topic excluded from all date-range queries; topic appears to not exist in the coverage system).
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently).

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-05 — Full Integration (C-28 + C-29 + C-30)

**Axis**: All three new criteria applied simultaneously at maximum depth. (1) DECISION TABLE SCHEMA block explicitly declares Path/Action/Consequence as the document-wide column grammar before Phase 1. (2) Every exit gate condition and every self-check item names the tool, what it checks, and the enforcement mechanism — field reference + operation type. (3) Every ordering instruction carries its own inline if/if contrast in the instruction body; all "see Phase X Decision above" delegation is removed; each instruction is self-contained at the point of reading. Decision tables (C-27) remain as structural pre-phase elements and are not removed — the instruction body carries the contrast independently, so both layers reinforce the same branch condition.

**Hypothesis**: V-01, V-02, and V-03 each achieve one new criterion against the R6 V-05 base. V-04 combines C-28 and C-29. V-05 combines all three. C-28 (schema declaration), C-29 (mechanism citations), and C-30 (self-contained instructions) are structurally independent — each operates at a different layer of the skill (decision table frame, enforcement annotations, ordering instruction body). The combination should produce no regression: a model encounters a declared schema, annotated enforcement contracts, and self-contained if/if at every ordering point. The three properties stack without interference, and together they close the three gaps that prevented R6 V-01, V-02, V-03 from simultaneously passing all three criteria.

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
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` path glob** (both tools execute `simulations/*/strategy.md` glob; a flat path or wrong directory produces no match; both tools return zero results silently — the topic appears to have no signals).

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` five-field row parser** (reads each row for exactly five populated fields; any row with a missing field is excluded from the coverage computation; that signal does not appear in the coverage report).

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` F-01 exact string match** (tests each priority cell against `{essential, recommended, optional}`; non-matching value = silently excluded from commit-gate check; the gate never fires for that signal — no warning emitted).

**C-05**: At least one `essential` row? — **`topic-status` F-01 essential-row count** (counts rows where F-01 = 'essential'; zero count = gate status not returned; the Design Lead cannot determine when investigation is complete).

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.
