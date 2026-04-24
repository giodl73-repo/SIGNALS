# topic-open — Round 5 Variations

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric version**: v5 (C-01 through C-24, aspirational denominator = 16)
**Round context**: R4 all 5 variations scored 100/100 on v4 rubric (C-01–C-20). Four new excellence patterns identified: C-21 (tool citation permeates all phases including setup), C-22 (vocabulary block's reading-order instruction uses comparative framing recursively), C-23 (phase transitions preceded by labeled decision tables), C-24 (unified multi-column consequence chain covers all constraints in one block). Denominator: 12 → 16.

**Variation axes selected**:
- V-01: C-21 axis — phase-pervasive tool citation (every phase names its downstream dependent tool)
- V-02: C-22 axis — recursive meta-comparative framing throughout all ordering instructions
- V-03: C-23 axis — labeled decision tables at all five phase transitions
- V-04: C-21 + C-22 combination — pervasive tool citation AND recursive comparative framing simultaneously
- V-05: C-23 + C-24 full integration — per-phase decision tables AND unified five-column constraint matrix

---

## V-01 — Phase-Pervasive Tool Citation

**Axis**: Tool citations are distributed to every structural element in the skill — vocabulary lock, field schema, Phase 1 collision-check, Phase 2 exit gate, Phase 3 commit gate, Phase 4 path constraints, and Phase 5 checklist items. Every instruction that has a downstream tool dependency names that tool. C-21 is not a single annotation; it is a design principle applied uniformly.

**Hypothesis**: R4 V-02 satisfied C-21 with one Phase 1 tool citation. This variation asks: what does the skill look like when tool coupling is surfaced everywhere it exists — not just in structural constraint blocks? If every phase annotation carries a tool name, the model cannot execute any step without being aware of the downstream observer. This should make the coupling-visibility pattern so pervasive it cannot be missed.

---

## VOCABULARY LOCK

> Read this block before reading anything else in this skill.
> **If you read this block first**: priority vocabulary is locked before you write any signal row — every cell you produce is already constrained.
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

> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder when the template is rebuilt from memory.

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
| Compliant | Write narrative rationale first, then signal table | Owner roles emerge from decision context; each role is accountable to a named question being answered |
| Non-compliant | Write signal table first, then rationale | Owner roles become post-hoc column-fillers with no derivable purpose; C-08 passes mechanically but carries no information |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — **because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path**.

Confirm this topic is not already registered. Stop on collision. Do not create a duplicate.

---

## Phase 2 — Narrative Rationale + Signal Table

Write narrative rationale first (see Phase 2 Decision table above).

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row. `topic-status` parses all five fields for coverage computation; `topic-scanner` uses Item Name for discovery.

**Phase 2 Exit Gate** — check before advancing:
- [ ] Rationale >= 2 sentences
- [ ] Every priority matches VOCABULARY LOCK exactly — `topic-status` exact string match
- [ ] COV-01: >= 1 `essential` row (no essential = no commit gate; `topic-status` returns nothing)
- [ ] COV-02: >= 2 distinct namespaces
- [ ] COV-03: >= 2 distinct owner roles
- [ ] All item names: `{topic}-{signal}-{date}.md` — `topic-scanner` discovery pattern

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

Audit what you actually wrote — not what you intended. Run after both files are written.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? (`topic-status` date filter reads this field.)
-> If date missing: return to ROW TEMPLATE above. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? (`topic-status` and `topic-scanner` glob for this path.)

**C-03**: Every signal row has all five fields F-01 through F-05? (`topic-status` parses all five for coverage.)

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? (`topic-status` exact string comparison.)

**C-05**: At least one `essential` row? (`topic-status` commit-gate check returns nothing without an essential signal.)

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-02 — Recursive Meta-Comparative Framing

**Axis**: Comparative failure framing is applied recursively — not just to sequencing instructions, but to the vocabulary block's own reading-order meta-instruction. Every ordering instruction in the skill contrasts both paths explicitly: read-first vs. skip (vocabulary block), copy vs. reconstruct (row template), rationale-first vs. table-first (Phase 2), check-after vs. check-before (Phase 5). C-22 is the axis, but comparative framing permeates all four ordering instructions.

**Hypothesis**: R4 V-03 achieved deepest C-20 by contrasting all four ordering instructions. This variation takes V-03's pattern and applies it to V-03's own gap: the vocabulary block's reading-order instruction was not itself framed comparatively in R3/R4. C-22 requires exactly this recursive application — the constraint that demands priority justifies its own priority using the same technique. If the vocabulary block demonstrates comparative framing on itself, the model learns the pattern from the first instruction it reads.

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

**If you copy this template**: all three fields are present by structure — slug, description, and the ISO date placeholder are given to you. Fill in the values.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. The template exists to prevent this. Use it.

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

**If the topic already exists**: stop. Report the collision. Do not create a duplicate entry. The ambiguity has no merge path.

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.** (See Phase 2 Decision above.)

**If you write the rationale first**: the decisions you describe surface the question "who should own this signal?" Owner roles emerge as stakeholders named in the rationale.

**If you write the signal table first**: owner roles become column-fillers assigned after the fact. Role differentiation (C-08) passes mechanically but carries no meaning.

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

## Phase 3 — Commit Gate

Structurally isolated. Not a subsection of the signal table. `topic-status` reads `## COMMIT GATE` as a named parseable section — a gate embedded inside the signal table fails the parser.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
[all essential signals by exact item name]
```

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above. Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — because `topic-status` and `topic-scanner` both glob for this specific path. A flat path causes both tools to silently return zero results.

---

## Phase 5 — Post-Generation Self-Check

**If you run this check after writing both files**: you are testing what you produced.

**If you run this check before writing**: you are testing what you intend to produce — not the output that `topic-status` and `topic-scanner` will actually read.

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

## V-03 — Labeled Decision Tables at All Phase Transitions

**Axis**: Every phase is preceded by a named `Phase X Decision: [Name]` table that presents the decision as a first-class structural element before the instruction body. The decision has its own named slot in the skill structure; it is not embedded in prose. Five phases, five decision tables — each identifying the contrast before the phase instruction is read.

**Hypothesis**: R4 V-04 formalized C-20 structurally with three decision tables at key phases and achieved the deepest structural formalization in R4. This variation asks: what does the skill look like when every phase transition has a named decision table — including Phase 1 (check before proceeding), Phase 3 (isolation before embedding), Phase 4 (copy before reconstructing), and Phase 5 (check after before before)? If the decision table is visible before every instruction, the model is structurally prepared to make the right choice before reading the instruction that requires it.

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

> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: `{YYYY-MM-DD}` date field is the most commonly dropped placeholder when the template is rebuilt from memory.

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
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; no coverage ambiguity |
| **Topic already in TOPICS.md** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; a duplicate creates ambiguous coverage aggregation with no merge path |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path.

Confirm topic is not already registered. Stop on collision.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first, table second** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from the decisions described in the rationale — each role is the stakeholder accountable for answering a specific question |
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
| **Isolated `## COMMIT GATE` section** | Write as a standalone heading with essential signals listed | `topic-status` reads it as a named parseable section; coverage computation returns correct gate status |
| **Embedded inside signal table** | Include gate logic as a row or note within Phase 2 | `topic-status` section parser cannot find the gate; coverage computation returns no gate status; the gate silently does not exist |

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
| **Copy ROW TEMPLATE; write strategy to `simulations/{topic}/strategy.md`** | Use the three-field template; write strategy to topic subdirectory | Both files correctly formed; `topic-status` and `topic-scanner` find them |
| **Reconstruct row from memory OR write strategy to flat path** | Rebuilt template drops `{YYYY-MM-DD}`; flat path not found by glob | C-01 fails (missing date) or C-02 fails (wrong path); both tools silently return zero results |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above. Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — because `topic-status` and `topic-scanner` both glob for this specific path.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run check after writing both files** | Verify what was actually produced | Errors in the output are caught and corrected before the topic is visible to downstream tools |
| **Run check before writing** | Verify what you intend to produce | Intentions pass the check; actual output may still fail — `topic-status` and `topic-scanner` read the files, not the intentions |

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

## V-04 — Pervasive Tool Citation + Recursive Comparative Framing (C-21 + C-22 Combination)

**Axis**: Both C-21 (tool citation permeates all phases) and C-22 (vocabulary block's reading-order instruction uses comparative framing recursively) are combined and applied simultaneously throughout. Every phase names its downstream tool dependency AND contrasts both the compliant and non-compliant path. The vocabulary block justifies its own reading priority using comparative framing. Phase 1 names topic-status AND contrasts both outcomes. Phase 4 write instructions name the tool AND contrast copy vs. reconstruct. Phase 5 timing names the tools AND contrasts check-after vs. check-before.

**Hypothesis**: R4 V-02 was deepest on tool citations; R4 V-03 was deepest on comparative framing. Neither combined both at the instruction level — citations and contrasts appeared in different blocks. This variation asks: what does a skill look like when every instruction simultaneously names its tool watcher AND describes both paths? The result should be the highest information-density skill — every element is both annotated and contrasted.

---

## VOCABULARY LOCK

> **Read this block before reading anything else in this skill.**
>
> **If you read this block first**: priority vocabulary is locked before you encounter any signal row, schema definition, or phase instruction. `topic-status` will find the correct vocabulary in every cell. The most common error in this skill cannot occur.
>
> **If you skip this block and read the schema first**: you may already have formed row vocabulary (`high`, `medium`, `low`) before the constraint arrives. `topic-status` will silently exclude those signals from the commit-gate check, and you will need to re-scan all priority cells after generation to repair the errors you would have prevented by reading this block first.

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

**If you copy this template**: all three fields are present by structure. Fill in the values.

**If you reconstruct from memory**: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder. `topic-status` date filter will exclude the topic from all queries.

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

**If the topic is not in `simulations/TOPICS.md`**: proceed to Phase 2.

**If the topic is already registered**: stop — report the collision, do not create a duplicate. `topic-status` loads `simulations/TOPICS.md` on every status check; a duplicate entry creates ambiguous coverage aggregation with no merge path.

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.** (See Phase 2 Decision above.)

**If you write the rationale first**: owner roles in the table emerge as stakeholders accountable to the decisions you named. `topic-status` and coverage review can verify each role against a stated decision.

**If you write the signal table first**: owner roles become retroactive column-fillers. Coverage review cannot verify them against any decision context.

Rationale: >= 2 sentences. State (1) why this topic requires investigation, (2) what design decisions the signals inform.

Build the signal table after the rationale exists. Apply F-01 through F-05 to every row. `topic-status` parses all five fields; `topic-scanner` uses Item Name.

**Phase 2 Exit Gate**:
- [ ] Rationale >= 2 sentences
- [ ] Every priority matches VOCABULARY LOCK exactly — `topic-status` exact string match
- [ ] COV-01: >= 1 `essential` row (no essential = `topic-status` commit-gate check returns nothing)
- [ ] COV-02: >= 2 distinct namespaces
- [ ] COV-03: >= 2 distinct owner roles
- [ ] All item names: `{topic}-{signal}-{date}.md` — `topic-scanner` discovery pattern

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

**If you run this check after writing both files**: `topic-status` and `topic-scanner` will see the same files you are checking. Errors are caught and corrected.

**If you run this check before writing**: you verify intentions. The tools read files, not intentions; actual output may still fail.

Run after both files are written.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date? (`topic-status` date filter reads this field.)
-> If date missing: return to ROW TEMPLATE. Copy the three-field template. Replace the row.

**C-02**: Strategy at `simulations/{topic}/strategy.md`? (`topic-status` and `topic-scanner` glob this path.)

**C-03**: Every signal row has all five fields F-01 through F-05? (`topic-status` parses all five for coverage.)

**C-04**: Every priority exactly `essential` / `recommended` / `optional`? (`topic-status` exact string comparison.)

**C-05**: At least one `essential` row? (`topic-status` commit-gate check returns nothing without an essential signal.)

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid values. Re-scan all priority cells before marking C-04 passing.

---

---

## V-05 — Decision Tables + Unified Constraint Matrix (C-23 + C-24 Full Integration)

**Axis**: Every phase is preceded by a labeled `Phase X Decision: [Name]` table AND a single unified five-column DEFAULTS TABLE (Default / Rule / Why / What Breaks / Tool) covers all structural constraints in one block. C-23 and C-24 are the axes — the most structurally formalized variation. The unified table achieves C-24's constraint-surface compactness; the per-phase decision tables achieve C-23's decision-as-structural-element formalization. Both operate simultaneously.

**Hypothesis**: R4 V-04 had the deepest C-23 (three named decision tables) and R4 V-05 had the deepest C-24 (five-column DEFAULTS TABLE). Neither used both together. This variation asks: what does the skill look like when the unified constraint matrix (C-24) coexists with per-phase labeled decision tables (C-23)? The DEFAULTS TABLE handles cross-cutting constraints; the phase decision tables handle phase-specific execution choices. The result should be the most explicitly structured variation — both comprehensive and compact.

---

## VOCABULARY LOCK

> Read this block before reading anything else in this skill.
> **If you read this block first**: priority vocabulary is locked before you write any signal row — the most common mistake in this skill cannot occur.
> **If you skip this block**: row vocabulary may drift before the constraint arrives, and the most likely outcome is a re-scan repair pass after all rows are written.

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

> **COPY — DO NOT RECONSTRUCT.** Reconstruction failure mode: the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder when the template is rebuilt from memory.

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
| **Topic not in TOPICS.md** | Proceed to Phase 2 | Clean registration; no ambiguity in coverage aggregation |
| **Topic already registered** | Stop — report collision, do not proceed | `topic-status` loads TOPICS.md on every check; duplicate entry creates ambiguous coverage aggregation with no merge path |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` — because `topic-status` loads this file on every status check; a duplicate entry creates ambiguous coverage aggregation with no merge path.

Confirm topic is not already registered. Stop on collision.

---

## Phase 2 Decision: Content Order

| Path | Action | Consequence |
|------|--------|-------------|
| **Rationale first** | Write >= 2 sentence rationale, then build signal table | Owner roles emerge from decision stakeholders named in the rationale — each role is accountable to a question being answered |
| **Table first** | Build signal table, then add rationale | Owner roles become post-hoc column-fillers; rationale is written to justify the table rather than to surface decision context |

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
| **Isolated `## COMMIT GATE` section** | Write as standalone heading after signal table | `topic-status` finds it as a named parseable section; coverage computation returns correct gate status |
| **Embedded inside signal table** | Include gate as a row, note, or subsection | `topic-status` section parser cannot find it; no gate status is returned; the commit gate silently does not exist |

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
| **Copy ROW TEMPLATE; write strategy to `simulations/{topic}/strategy.md`** | Use the three-field template; write strategy to topic subdirectory | `topic-status` and `topic-scanner` find both files; coverage computation proceeds |
| **Reconstruct row from memory; write strategy to flat path** | Template rebuilt: `{YYYY-MM-DD}` dropped; flat path not matched by glob | C-01 fails (missing date) or C-02 fails (wrong path); tools return zero results silently |

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**: Return to the **TOPICS.md ROW TEMPLATE** above. Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Write 2 — Strategy file**: Write `simulations/{topic}/strategy.md` — `topic-status` and `topic-scanner` glob for this exact path.

---

## Phase 5 Decision: Check Timing

| Path | Action | Consequence |
|------|--------|-------------|
| **Run after writing both files** | Test what you produced | Errors in actual output are caught; downstream tools see corrected files |
| **Run before writing** | Test what you intend to produce | Intentions pass the check; actual files may still fail the criteria that `topic-status` and `topic-scanner` evaluate |

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
