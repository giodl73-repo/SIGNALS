# topic-open — Round 6 Variations

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric version**: v6 (C-01 through C-27, aspirational denominator = 19)
**Round context**: R5 all 5 variations scored on v5 rubric (C-01–C-24). Three new excellence patterns identified: C-25 (tool citations at every exit gate condition and every self-check checklist item — not just structural blocks and setup phases), C-26 (comparative framing applied universally to every ordering instruction in the skill — ROW TEMPLATE copy-vs-reconstruct, prose-before-table, and self-check timing all use explicit if/if contrast), C-27 (labeled decision tables at every phase transition — not just primary phases — making every phase entry a structural decision point). Denominator: 16 → 19.

**Variation axes selected**:
- V-01: C-25 axis — exit gate conditions and self-check items carry tool citations at maximum depth
- V-02: C-26 axis — comparative framing applied universally to every ordering instruction
- V-03: C-27 axis — labeled decision tables at all five phase transitions
- V-04: C-25 + C-26 combination — gate/checklist tool citations AND universal comparative framing simultaneously
- V-05: C-25 + C-26 + C-27 full integration — all three new criteria at maximum depth

---

## V-01 — Exit Gate and Checklist Tool Citation

**Axis**: Tool citations appear at every exit gate condition and every self-check checklist item — not just in structural constraint blocks and setup steps. Every gate condition names the specific downstream tool that enforces it and explains the enforcement mechanism precisely. Every Phase 5 checklist item names the tool that will evaluate that criterion when the files are read. C-25 is not a single annotation; it is a discipline applied uniformly at every decision and verification point.

**Hypothesis**: R5 V-01 satisfied C-21 (tool citations in setup) and had some Phase 2 exit gate annotations, but the exit gate items were not all equally specific. C-25 asks: what does the skill look like when every gate condition and every checklist item is fully annotated — no item leaves the model wondering which tool enforces it or how? If enforcement is visible at every gate, the model cannot treat any gate item as advisory.

---

## VOCABULARY LOCK

> Read this block before reading anything else in this skill.
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction — every cell you produce is already constrained.
> **If you skip this block**: you may form row vocabulary before the constraint arrives, making re-scan of all priority cells the most likely repair.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder when the template is rebuilt from memory. `topic-status` date filter reads this field on every status check — a missing date excludes the topic from all coverage queries.

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — `topic-status` parses all five for coverage computation; `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` gates on exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md` — `topic-scanner` uses this pattern for discovery
- **F-05 Owner Role**: role responsible for this signal

---

## CONSTRAINT SURFACE

| Rule | Rationale | What Breaks | Tool |
|------|-----------|-------------|------|
| Priority: `essential` / `recommended` / `optional` only | `topic-status` does exact string comparison on every commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` |
| TOPICS.md row: slug + description + YYYY-MM-DD | `topic-status` date filter reads this field on every status check | Missing date = topic not queryable; status returns no data for the topic | `topic-status` |
| Strategy at `simulations/{topic}/strategy.md` | `topic-status` and `topic-scanner` both glob for this exact path | Flat path = both tools silently return zero coverage results | `topic-status`, `topic-scanner` |
| Commit gate: isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser; coverage computation returns no gate status | `topic-status` |
| Use ROW TEMPLATE — copy, do not reconstruct | Date field dropped at high frequency when rebuilt from memory | C-01 fails; `topic-status` date filter excludes the topic entirely | `topic-status` |

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| Compliant | Write narrative rationale first, then signal table | Owner roles emerge from decision context; each role is the stakeholder accountable to a named question being answered |
| Non-compliant | Write signal table first, then rationale | Owner roles become post-hoc column-fillers with no derivable purpose; C-08 passes mechanically but carries no information |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — **because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path**.

Confirm this topic is not already registered. Stop on collision. Do not create a duplicate.

---

## Phase 2 — Narrative Rationale + Signal Table

Write narrative rationale first (see Phase 2 Decision table above).

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — check before advancing to Phase 3. Every condition names the tool that enforces it:

- [ ] Rationale >= 2 sentences — `topic-status` narrative parser reads the rationale before computing role-coverage; a missing rationale produces no derivable owner context
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` exact string match**: any priority value not in {essential, recommended, optional} is silently excluded from the commit-gate check
- [ ] COV-01: >= 1 `essential` row — **`topic-status` commit-gate check**: without an essential signal, the check returns no gate status; the topic has no defined commit condition
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` namespace grouping**: single-namespace strategies are flagged as monoculture during discovery; coverage breadth is unverifiable
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` role-coverage report**: single-role strategies return degenerate accountability distribution; the report cannot assign signals to differentiated owners
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` discovery pattern**: any item name not matching this pattern is invisible to artifact discovery; the signal is untracked

---

## Phase 3 — Commit Gate

Structurally isolated. Not a subsection of the signal table. `topic-status` reads `## COMMIT GATE` as a named parseable section — a gate embedded inside the signal table fails the section parser; coverage computation returns no gate status.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
- {item-name-2}
[all essential signals by exact item name]
```

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above. Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`. `topic-status` reads this file on every invocation — a malformed or missing row creates silent coverage gaps.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — **because `topic-status` and `topic-scanner` both glob for this specific path**. A flat path causes both tools to silently return zero results.

---

## Phase 5 — Post-Generation Self-Check

Audit what you actually wrote — not what you intended. Run after both files are written. Every check item names the tool that will evaluate it:

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` date filter**: reads this field on every status check; a missing date excludes the topic from all coverage queries permanently.
-> If date missing: return to ROW TEMPLATE above. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` glob**: both tools search this exact path; a flat path causes both to return zero results silently.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` coverage parser**: parses all five fields for coverage computation; a missing field causes that signal to be excluded from the coverage result.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` exact string comparison**: any other value is silently excluded from the commit-gate check; the gate never fires for that signal.

**C-05**: At least one `essential` row? — **`topic-status` commit-gate check**: returns no gate status without an essential signal; the topic has no defined commit condition, and the Design Lead cannot determine when investigation is complete.

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-02 — Universal Comparative Framing

**Axis**: Comparative failure framing is applied to every ordering instruction in the skill — not just the vocabulary block's reading-order meta-instruction (C-22), but every "do X before Y" directive: the ROW TEMPLATE copy-vs-reconstruct instruction, the prose-before-table instruction, and the self-check timing instruction. Each ordering instruction contrasts both paths explicitly using if/if structure. No ordering instruction states a correct sequence without also describing what breaks when the wrong order is followed.

**Hypothesis**: R5 V-02 achieved deep C-22 (vocabulary block's own reading-order uses comparative framing) and had comparative framing in Phase 2 and Phase 5 prose. C-26 asks: what does the skill look like when comparative framing is applied so universally that every "before/after" instruction uses if/if — including the ROW TEMPLATE's copy vs. reconstruct instruction? If the ROW TEMPLATE directive says "If you copy: [what you get] / If you reconstruct: [what breaks]", the model encounters the pattern at every ordering point, not just at phase boundaries.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, any schema definition, or any phase instruction — every cell you write is already constrained. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may already have formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. The most likely outcome: a re-scan pass after all rows are written — fixing errors that would not have occurred had you read this block first.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent downstream breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. `high` does not match `essential`. The commit-gate check silently excludes the signal — no error, no warning, the gate never fires. The Design Lead sees a valid-looking strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values. `topic-status` date filter finds the date field.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries — the topic appears to not exist.

> **COPY — DO NOT RECONSTRUCT.**

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — because `topic-status` parses all five for coverage computation, and `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` gates on exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md`
- **F-05 Owner Role**: role responsible for this signal

---

## CONSTRAINT SURFACE

| Rule | Rationale | What Breaks | Tool |
|------|-----------|-------------|------|
| Priority: `essential` / `recommended` / `optional` only | `topic-status` exact string comparison on commit-gate check | Commit gate silently fails; Design Lead sees passing file that is broken | `topic-status` |
| TOPICS.md row: slug + description + YYYY-MM-DD | `topic-status` date filter reads date field on every check | Topic not queryable by status tools | `topic-status` |
| Strategy at `simulations/{topic}/strategy.md` | `topic-status` and `topic-scanner` glob for this exact path | Both tools silently return zero results for flat paths | `topic-status`, `topic-scanner` |
| Commit gate: isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser | `topic-status` |
| Use ROW TEMPLATE — copy, do not reconstruct | Date field dropped at high frequency when rebuilt from memory | TOPICS.md row missing date; topic excluded from coverage queries | `topic-status` |

---

## Phase 2 Decision: Narrative Order

| Path | Consequence |
|------|-------------|
| **Write rationale first, then signal table** | Owner roles emerge from the decisions you just described — each role is the stakeholder accountable for answering a specific question. Coverage review can verify roles against the rationale. |
| **Write signal table first, then rationale** | Owner roles become retroactive column-fillers. They have no derivable connection to the rationale because the rationale was written to justify the table, not to surface the decisions that determined it. |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

**If the topic does not yet exist**: proceed to Phase 2.

**If the topic already exists**: stop. Report the collision. Do not create a duplicate entry.

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.** (See Phase 2 Decision above.)

**If you write the rationale first**: the decisions you describe surface the question "who should own this signal?" Owner roles emerge as stakeholders named in the rationale. Coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers assigned after the fact. Role differentiation (C-08) passes mechanically but carries no meaning — coverage review cannot verify them against any decision context.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate**:
- [ ] Rationale >= 2 sentences
- [ ] Every priority matches VOCABULARY LOCK exactly — `topic-status` exact string match
- [ ] COV-01: >= 1 `essential` row — `topic-status` commit-gate check returns nothing without an essential signal
- [ ] COV-02: >= 2 distinct namespaces
- [ ] COV-03: >= 2 distinct owner roles
- [ ] All item names: `{topic}-{signal}-{date}.md` — `topic-scanner` discovery pattern

---

## Phase 3 — Commit Gate

Structurally isolated. Not a subsection of Phase 2. `topic-status` reads `## COMMIT GATE` as a named parseable section — a gate embedded inside the signal table fails the parser.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above.

**If you copy the template**: three fields are structurally present. `topic-status` date filter finds the date.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped. `topic-status` excludes the topic from all queries.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md`.

**If written to the correct path**: `topic-status` and `topic-scanner` both find the file; coverage computation proceeds normally.

**If written to a flat path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate.

---

## Phase 5 — Post-Generation Self-Check

**If you run this check after writing both files**: `topic-status` and `topic-scanner` see the same files you are checking — errors are caught and corrected before the topic enters the coverage system.

**If you run this check before writing**: you verify intentions. The tools read files, not intentions; actual output may still fail even if intentions passed.

Run after both files are written.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`?

**C-03**: Every signal row has all five fields F-01 through F-05?

**C-04**: Every priority exactly `essential` / `recommended` / `optional`?

**C-05**: At least one `essential` row?

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-03 — Labeled Decision Tables at All Five Phases

**Axis**: Every one of the five phases is preceded by a named `Phase X Decision: [Name]` table that presents the execution choice as a first-class structural element before the instruction body. Five phases, five decision tables — Phase 1 (Collision Check), Phase 2 (Content Order), Phase 3 (Gate Structure), Phase 4 (Output Write), Phase 5 (Check Timing) — each with consistent Path/Action/Consequence columns. The decision table is always the first thing visible before each phase's instruction, making the choice structural rather than prose.

**Hypothesis**: R5 V-03 showed labeled decision tables at all five phases and achieved the deepest C-23 coverage. C-27 requires exactly this — complete 5-phase coverage, not spot coverage. This variation pushes C-27 to maximum formalization: every table uses the same column structure, every table names both paths explicitly, and every table's consequence column describes the specific tool-level outcome of each choice. The decision tables are not decoration; they are the primary structural frame for the skill.

---

## VOCABULARY LOCK

> Read this block before reading anything else in this skill.
> **If you read this block first**: vocabulary is locked before any row is written — the most common mistake cannot occur.
> **If you skip this block**: row vocabulary may drift before the constraint arrives, requiring a repair re-scan after generation.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a valid-looking strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: `{YYYY-MM-DD}` date field is the most commonly dropped placeholder when the template is rebuilt from memory. `topic-status` date filter reads this field on every status check.

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## FIELD SCHEMA

Five fields per signal row — `topic-status` parses all five for coverage computation; `topic-scanner` reads Item Name for artifact discovery:

- **F-01 Priority**: `essential` / `recommended` / `optional` — `topic-status` exact string match
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md`
- **F-05 Owner Role**: role responsible for this signal

---

## CONSTRAINT SURFACE

| Rule | Rationale | What Breaks | Tool |
|------|-----------|-------------|------|
| Priority: `essential` / `recommended` / `optional` only | `topic-status` exact string comparison | Commit gate silently excludes signal; gate never fires | `topic-status` |
| TOPICS.md row: slug + description + YYYY-MM-DD | `topic-status` date filter reads this field | Topic not queryable by status | `topic-status` |
| Strategy at `simulations/{topic}/strategy.md` | `topic-status` and `topic-scanner` glob this exact path | Both tools return zero results silently | `topic-status`, `topic-scanner` |
| Commit gate: isolated `## COMMIT GATE` section | `topic-status` reads it as a named section | Embedded gate fails the section parser | `topic-status` |
| Use ROW TEMPLATE — copy, do not reconstruct | Date field dropped at high frequency when rebuilt from memory | TOPICS.md missing date; topic excluded from queries | `topic-status` |

---

## Phase 1 Decision: Collision Check

| Path | Action | Consequence |
|------|--------|-------------|
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; no coverage ambiguity; `topic-status` loads TOPICS.md on every check and finds exactly one entry for this topic |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate entry creates ambiguous coverage aggregation; two strategy files with no merge path |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

Confirm topic is not already registered. Stop on collision (see Phase 1 Decision above).

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from the decisions described in the rationale — each role is the stakeholder accountable for answering a specific question; coverage review can verify roles against the stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table, not to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

Write narrative rationale first (see Phase 2 Decision above).

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate**:
- [ ] Rationale >= 2 sentences
- [ ] Every priority matches VOCABULARY LOCK exactly
- [ ] COV-01: >= 1 `essential` row
- [ ] COV-02: >= 2 distinct namespaces
- [ ] COV-03: >= 2 distinct owner roles
- [ ] All item names: `{topic}-{signal}-{date}.md`

---

## Phase 3 Decision: Gate Structure

| Path | Action | Consequence |
|------|--------|-------------|
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading after the signal table, listing all essential signals | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status; commit gate is enforceable |
| **Embedded inside signal table** | Include gate logic as a row, note, or subsection of Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the commit gate silently does not exist |

---

## Phase 3 — Commit Gate

Write as a structurally isolated section (see Phase 3 Decision above).

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
| **Reconstruct row from memory OR write strategy to flat path** | Rebuilt template drops `{YYYY-MM-DD}`; flat path not matched by glob | C-01 fails (missing date) and/or C-02 fails (wrong path); both tools silently return zero results; topic invisible to coverage system |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above. Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md` (see Phase 4 Decision above).

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — `topic-status` and `topic-scanner` glob for this exact path.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run check after writing both files** | Audit the actual files produced | Errors in the output are caught and corrected before the topic enters the coverage system; `topic-status` and `topic-scanner` see the corrected files |
| **Run check before writing** | Audit intentions rather than output | Intentions pass the check; actual files may still fail the criteria — `topic-status` and `topic-scanner` read files, not intentions; errors remain in the output |

---

## Phase 5 — Post-Generation Self-Check

Run after both files are written (see Phase 5 Decision above).

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`?

**C-03**: Every signal row has all five fields F-01 through F-05?

**C-04**: Every priority exactly `essential` / `recommended` / `optional`?

**C-05**: At least one `essential` row?

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-04 — Gate/Checklist Tool Citations + Universal Comparative Framing (C-25 + C-26 Combination)

**Axis**: C-25 (every exit gate condition and every self-check item names its enforcement tool) and C-26 (every ordering instruction uses if/if comparative framing) are applied simultaneously throughout the skill. Every ordering instruction — vocabulary block reading-order, ROW TEMPLATE copy-vs-reconstruct, Phase 2 rationale-before-table, Phase 5 timing — uses explicit if/if contrast. Every gate condition and every Phase 5 checklist item names the specific tool that enforces it and states what that tool checks for.

**Hypothesis**: R5 V-01 was deepest on C-21 (setup tool citation) and had Phase 2 gate annotations; R5 V-02 was deepest on C-22 (recursive meta-comparative framing). Neither combined gate-level tool citations (C-25) with universal ordering instruction framing (C-26). This variation asks: what does a skill look like when the model encounters a tool name at every enforcement point AND encounters if/if contrast at every ordering decision? The density of enforcement visibility and contrast framing should make both correct paths and their tools unambiguous at every step.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction. `topic-status` will find the correct vocabulary in every cell. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may already have formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. `topic-status` will silently exclude those signals from the commit-gate check, and you will need to re-scan all priority cells after generation to repair errors you would have prevented by reading this block first.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake.**

`topic-status` performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values. `topic-status` date filter finds the date field immediately.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries — the topic appears to have no coverage.

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

## CONSTRAINT SURFACE

| Rule | Rationale | What Breaks | Tool |
|------|-----------|-------------|------|
| Priority: `essential` / `recommended` / `optional` only | `topic-status` exact string comparison on commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` |
| TOPICS.md row: slug + description + YYYY-MM-DD | `topic-status` date filter reads this field on every check | Missing date = topic excluded from all status queries | `topic-status` |
| Strategy at `simulations/{topic}/strategy.md` | `topic-status` and `topic-scanner` glob for this exact path | Both tools silently return zero results for flat or wrong paths | `topic-status`, `topic-scanner` |
| Commit gate: isolated `## COMMIT GATE` section | `topic-status` reads it as a named parseable section | Embedded gate fails the section parser; no gate status returned | `topic-status` |
| Use ROW TEMPLATE — copy, do not reconstruct | Date field dropped at high frequency when rebuilt from memory | TOPICS.md row missing date; `topic-status` excludes topic from queries | `topic-status` |

---

## Phase 2 Decision: Content Order

| Path | Consequence |
|------|-------------|
| **Rationale first** — write >= 2 sentence rationale, then build signal table | Owner roles emerge from named decision stakeholders in the rationale; `topic-status` coverage review can verify roles against the rationale |
| **Table first** — build signal table, then add rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table, not to surface decision context |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate entry creates ambiguous coverage aggregation with no merge path.

**If the topic is not in `simulations/TOPICS.md`**: proceed to Phase 2.

**If the topic is already registered**: stop — report the collision. `topic-status` cannot merge two entries; the ambiguity has no resolution path.

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.** (See Phase 2 Decision above.)

**If you write the rationale first**: owner roles in the table emerge as stakeholders accountable to the decisions you named. `topic-status` and coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers. Coverage review cannot verify them against any decision context.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — every condition names its enforcement tool:

- [ ] Rationale >= 2 sentences — `topic-status` narrative context: rationale is read before owner-role coverage is computed; absent rationale = roles cannot be verified against decisions
- [ ] Every priority matches VOCABULARY LOCK exactly — **`topic-status` exact string match**: any out-of-vocabulary priority is silently excluded from the commit-gate check; the gate never fires for that signal
- [ ] COV-01: >= 1 `essential` row — **`topic-status` commit-gate check**: returns no gate status without at least one essential signal; the topic has no defined commit condition
- [ ] COV-02: >= 2 distinct namespaces — **`topic-scanner` namespace grouping**: single-namespace strategies produce degenerate coverage; discovery cannot group signals by domain
- [ ] COV-03: >= 2 distinct owner roles — **`topic-status` role-coverage report**: single-role strategies return degenerate accountability; the report cannot distinguish signal ownership
- [ ] All item names: `{topic}-{signal}-{date}.md` — **`topic-scanner` discovery pattern**: wrong format = artifact invisible to discovery; the signal is untracked in the coverage system

---

## Phase 3 — Commit Gate

Structurally isolated. Not a subsection of Phase 2.

**If isolated as `## COMMIT GATE`**: `topic-status` reads it as a named parseable section; coverage computation returns correct gate status.

**If embedded inside the signal table**: `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the gate silently does not exist.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above.

**If you copy the template**: three fields are structurally present. `topic-status` date filter finds the date.

**If you reconstruct from memory**: `{YYYY-MM-DD}` is most commonly dropped. `topic-status` excludes the topic from all queries.

Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md`.

**If written to the correct path**: `topic-status` and `topic-scanner` both find the file; coverage computation proceeds normally.

**If written to a flat path**: both tools silently return zero results; the topic appears to have no signals, no coverage, and no commit gate.

---

## Phase 5 — Post-Generation Self-Check

**If you run this check after writing both files**: `topic-status` and `topic-scanner` will see the same files you are checking — errors are caught and corrected before they reach the coverage system.

**If you run this check before writing**: you verify intentions. The tools read files, not intentions; actual output may still fail even if your intentions passed.

Run after both files are written.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` date filter**: reads this field on every status check; missing date excludes the topic from all coverage queries.
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` glob**: both tools search this exact path; flat path causes both to return zero results silently.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` coverage parser**: parses all five fields; a missing field excludes that signal from coverage computation.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` exact string comparison**: any other value is silently excluded from the commit-gate check; the gate never fires for that signal.

**C-05**: At least one `essential` row? — **`topic-status` commit-gate check**: returns no gate status without an essential signal; the Design Lead cannot determine when investigation is complete.

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-05 — Full Integration (C-25 + C-26 + C-27)

**Axis**: All three new criteria applied simultaneously at maximum depth: (1) labeled decision tables at all five phases (C-27), (2) every ordering instruction uses if/if comparative framing in the instruction body (C-26), (3) every exit gate condition and every self-check checklist item names its downstream enforcement tool (C-25). This is the most structurally dense variation — every phase entry is a structural decision point, every ordering choice has both paths described, every enforcement point names the responsible tool. C-24 (unified five-column constraint matrix) is also included to achieve constraint-surface compactness simultaneously.

**Hypothesis**: R5 V-03 had labeled decision tables at all five phases; R5 V-04 had deepest C-21 + C-22. Neither combined all three new criteria. This variation asks: what does the skill look like at the intersection of structural formalism (decision tables at every phase), framing discipline (if/if on every ordering instruction), and citation completeness (tool names at every gate and checklist item)? The three properties should reinforce each other — a model that sees both the decision table and the if/if prose for every phase receives the same guidance twice, structured differently. Gate conditions that name tools eliminate the question "who enforces this?" at every verification step.

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
| Any priority vocabulary | `essential` / `recommended` / `optional` exactly | `topic-status` does exact string comparison on every commit-gate check | Commit gate silently excludes signal; gate never fires; file looks valid but is broken | `topic-status` |
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

**If the topic does not exist**: proceed to Phase 2.

**If the topic already exists**: stop. Report the collision. Do not create a duplicate (see Phase 1 Decision above).

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered; `topic-status` coverage review can verify roles against stated decisions |
| **Table first, rationale second** | Build signal table, then write rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context; C-08 passes but carries no information |

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.** (See Phase 2 Decision above.)

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

Write as a structurally isolated section (see Phase 3 Decision above).

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

Run after both files are written (see Phase 5 Decision above).

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? — **`topic-status` date filter**: reads this field on every status check; missing date excludes the topic from all coverage queries permanently.
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? — **`topic-status` and `topic-scanner` glob**: both tools search this exact path; flat path causes both to return zero results silently.

**C-03**: Every signal row has all five fields F-01 through F-05? — **`topic-status` coverage parser**: parses all five fields for coverage computation; missing field excludes that signal from coverage results.

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? — **`topic-status` exact string comparison**: any other value is silently excluded from the commit-gate check; the gate never fires for that signal.

**C-05**: At least one `essential` row? — **`topic-status` commit-gate check**: returns no gate status without an essential signal; the Design Lead cannot determine when investigation is complete.

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.
