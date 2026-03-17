Reading the three scorecards now before writing anything.

**Scorecard analysis — what each variation achieves:**

- **V-01 (98.4, 16/19)**: Passes C-25 cleanly. Evidence reads: "every item names tool + what-it-checks" — the citation format carries two slots, not one. Fails C-26 because ROW TEMPLATE's "COPY — DO NOT RECONSTRUCT" has no if/if inline. Fails C-23 and C-27 (only Phase 2 table).

- **V-02 (98.4, 16/19)**: Passes C-26 cleanly. Evidence reads: "If you copy…/If you reconstruct…" inline in ROW TEMPLATE body; Phase 4 has if/if for both writes; Phase 5 has if/if for timing. Every ordering instruction carries if/if in its own instruction body. Fails C-25 (gate items 1, 4, 5 lack tool citations; Phase 5 checklist has zero). Fails C-23 and C-27.

- **V-03 (~98.9, 17/19)**: Passes C-27 cleanly. Evidence reads: "Five labeled decision tables… consistent Path/Action/Consequence columns." The tables share a column schema — not just labels, but structural grammar. Fails C-25 (exit gate items are a bare checklist; Phase 5 checklist has no tool citations). Fails C-26 because "ordering instructions delegate to tables rather than using if/if directly" — V-03 writes "see Phase X Decision above," outsourcing the contrast rather than carrying it inline.

**Three new excellence patterns:**

1. **From V-01's C-25 deep pass** — tool citations at exit gates use two slots: tool name *and* what the tool checks. C-25 requires the name; V-01 adds the mechanism. New pattern: every tool citation at a gate or checklist item specifies the enforcement contract, not just the enforcer.

2. **From V-02's C-26 deep pass, V-03's C-26 fail** — V-03 fails C-26 specifically because it delegates to decision tables ("see Phase X Decision above") rather than carrying if/if inline. V-02 passes because every ordering instruction contains its own comparative framing in the instruction body itself. New pattern: ordering instructions are self-contained — they do not outsource their if/if to a nearby table.

3. **From V-03's C-27 deep pass** — C-27 requires labeled decision tables at every phase; V-03 adds consistent column schema (Path/Action/Consequence) across all five. The tables form a scannable system rather than phase-by-phase ad hoc entries. New pattern: decision table columns are uniform across all phases.

These become C-28, C-29, C-30. Denominator 19 → 22.

---

```markdown
# Rubric: topic-open (v7)

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Outputs**: entry in `TOPICS.md` + `simulations/{topic}/strategy.md`

**v7 change**: Added C-28, C-29, C-30 from Round 6 excellence signals. C-28 extends C-27's
labeled-decision-table requirement to include column schema consistency — all decision tables
in the skill share the same column grammar (e.g., Path / Action / Consequence), making the
decision surface scannable as a coherent system rather than phase-by-phase ad hoc tables.
C-29 extends C-25's tool-citation requirement at gates and checklist items to include the
enforcement mechanism — each citation names not just which tool but what the tool checks
(e.g., "topic-status checks for ≥1 essential row via F-05 field scan"), so the model
understands the contract each tool enforces, not just which tool is involved. C-30 extends
C-26's universal-comparative-framing requirement to prohibit delegation — every ordering
instruction carries its own inline if/if in the instruction body and does not outsource the
contrast to "see Phase X Decision above" or any equivalent table reference, making each
instruction self-contained at the point of reading. Aspirational denominator updated from
19 to 22.

---

## Essential Criteria (60% of composite)

Must all pass. Without these the output is not useful.

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | TOPICS.md entry exists | correctness | `simulations/TOPICS.md` contains a row for the new topic with at least: topic slug, short description, and start date |
| C-02 | Strategy file at correct path | correctness | Strategy written to `simulations/{topic}/strategy.md` — not to a flat path, not inline in TOPICS.md |
| C-03 | All five signal fields present | correctness | Every signal row contains all five required fields: namespace, skill, item name, owner role, priority — no field omitted or collapsed |
| C-04 | Priority vocabulary is valid | correctness | Every signal priority value is exactly one of: `essential` / `recommended` / `optional` — no substitutions (high/medium/low or other) |
| C-05 | At least one essential signal declared | coverage | Strategy contains at least one signal marked `essential` — a topic with no essential signals has no defined commit gate |

---

## Recommended Criteria (30% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Signal set spans multiple namespaces | coverage | At least 2 distinct namespaces |
| C-07 | Strategy includes a prose rationale | depth | >= 2 sentences explaining why + what decision it informs |
| C-08 | Owner roles are differentiated | depth | At least 2 distinct owner roles |

---

## Aspirational Criteria (10% of composite)

C-09/C-10 carry over from v1. C-11 through C-15 added in v2. C-16 and C-17 added in v3.
C-18, C-19, and C-20 added in v4. C-21, C-22, C-23, and C-24 added in v5. C-25, C-26,
and C-27 added in v6. **C-28, C-29, and C-30 are new in v7.**

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines an explicit commit gate | depth | Named COMMIT GATE section with exact item names |
| C-10 | Item names follow artifact naming convention | format | `{topic}-{signal}-{date}.md` pattern throughout |
| C-11 | Vocabulary constraint declared before instruction body | skill-design | Vocab rule in a standalone block preceding the instruction sequence — not buried inside column definitions |
| C-12 | Post-generation self-check phase present | skill-design | Checkbox list after output generation with at least one item per essential criterion |
| C-13 | Self-correction loop targets C-04 by name | skill-design | AMEND step asks a named question about priority drift (e.g., "Did any row use high/medium/low?") — not a generic review pass |
| C-14 | C-04 constraint framed with downstream consequence | skill-design | Vocab rule accompanied by failure consequence explanation ("Wrong vocabulary = silent breakage / most common mistake") — giving the model a reason to care, not just a rule to follow |
| C-15 | Prose rationale sequenced before signal table | skill-design | Skill instructs model to write prose rationale first, before constructing the signal table — so role differentiation (C-08) emerges from decision context rather than post-hoc count enforcement |
| C-16 | TOPICS.md row template is field-complete | skill-design | Skill includes a literal row template containing all three canonical fields: topic slug, short description, and `{YYYY-MM-DD}` date placeholder — not just instructions to "add a row"; the template itself encodes every required field |
| C-17 | Sequencing instruction is causal, not positional | skill-design | Skill explains *why* the prose rationale precedes the signal table (e.g., "so owner roles emerge from decision context rather than post-hoc count enforcement") — the instruction provides a reason, not just an order |
| C-18 | Template accompanied by anti-reconstruction directive | skill-design | Skill explicitly prohibits reconstruction of the row template — e.g., "copy this — do not reconstruct" or equivalent. C-16 requires the template to exist and be field-complete; C-18 requires the skill to name the bypass failure mode and close it by direct prohibition |
| C-19 | Structural constraints cite downstream tool dependency | skill-design | Path and/or field schema rules are accompanied by a named downstream tool that depends on them — e.g., "topic-status and topic-scanner glob for this specific path", "topic-status parses all five fields for coverage computation". A generic consequence ("it won't work") does not pass; the specific tool must be named |
| C-20 | Sequencing instruction uses comparative failure framing | skill-design | Sequencing instruction contrasts both paths explicitly — what happens if the model follows the correct order *and* what happens if it doesn't — side by side. C-17 requires a causal reason for the correct path; C-20 requires the non-compliant path to also be described, making the consequence concrete through contrast rather than assertion |
| C-21 | Tool citation permeates all phases, including setup | skill-design | Tool citations are not limited to structural constraint blocks — at least one setup or collision-check step also names a downstream tool and explains the coupling (e.g., "because topic-status loads this file on every status check; a duplicate entry creates ambiguous coverage aggregation"). C-19 covers path/schema constraints; C-21 requires tool coupling to be surfaced wherever it exists in the skill, including phase 1 |
| C-22 | Vocabulary block applies meta-comparative framing to its own reading-order instruction | skill-design | The vocabulary block's instruction to read it first is itself framed using comparative failure framing — contrasting what happens when the block is read first vs. skipped (e.g., "If you read this block first… / If you skip this block…"). C-20 applies to sequencing instructions; C-22 requires that the vocabulary block justify its own priority using the same technique it describes — recursive application of comparative framing |
| C-23 | Phase transitions preceded by labeled decision tables | skill-design | Each phase (or the primary phases) is preceded by a named decision table — e.g., "Phase X Decision: [Name]" — that presents the contrast as a first-class structural element before the instruction body. C-20 requires contrast to be present; C-23 requires it to be formalized as a labeled pre-phase table, making the decision a structural slot in the skill rather than embedded prose |
| C-24 | Unified multi-column consequence chain covers all constraints in one block | skill-design | The skill contains a single compact table encoding all major constraints with columns for: rule, rationale, failure consequence, and named downstream tool (or equivalent five-column structure). This table simultaneously satisfies C-19 (tool column) and C-20 (consequence column) for every constraint in one block, achieving constraint surface compactness rather than distributing annotations across the skill |
| C-25 | Exit gate conditions and self-check items carry tool citations | skill-design | Every exit gate condition and every self-check checklist item names the downstream tool that enforces it — not just structural constraint blocks and setup phases. C-21 requires tool citation in setup and collision-check steps; C-25 requires that same citation discipline to extend to the gates themselves and to the post-generation checklist, so the enforcement mechanism is visible at every decision and verification point in the skill |
| C-26 | Comparative framing applied to every ordering instruction in the skill | skill-design | Every "do X before Y" instruction in the skill — including the row template copy-vs-reconstruct instruction, the prose-before-table instruction, and the self-check timing instruction — uses explicit if/if comparative framing. C-22 requires comparative framing on the vocabulary block's own priority meta-instruction; C-26 requires that technique to be applied universally: no ordering instruction in the skill states a correct order without also describing what breaks when the incorrect order is followed |
| C-27 | Labeled decision tables present at every phase transition | skill-design | Every phase — not just primary phases — is preceded by its own named decision table (e.g., "Phase X Decision: [Name]") that contrasts both paths before the instruction body. C-23 requires labeled pre-phase tables at primary phases; C-27 requires complete coverage: each of the five phases has its own labeled decision table, making every phase entry a structural decision point rather than prose continuation of the previous phase |
| **C-28** | **Decision tables across all phases share a consistent column schema** | **skill-design** | All labeled decision tables in the skill use the same column grammar — e.g., Path / Action / Consequence, or Correct / Incorrect / What-Breaks — not just consistent labels but a unified structural schema. C-27 requires labeled decision tables at every phase; C-28 requires those tables to be structurally parallel so the decision surface is scannable as a coherent system: a reader encountering any phase decision immediately knows which column to look at for the consequence, rather than re-parsing each table's idiosyncratic structure |
| **C-29** | **Exit gate and self-check tool citations include the enforcement mechanism** | **skill-design** | Each tool citation at an exit gate condition or self-check checklist item specifies not just which tool but what the tool checks — e.g., "topic-status checks for ≥1 essential row via F-05 field scan" rather than just "topic-status". C-25 requires the tool name to appear at every gate and checklist item; C-29 requires those citations to also name the check mechanism, so the model understands the contract each tool enforces and not merely which tool is involved — making the gate conditions self-explanatory without requiring the model to consult the tool's own documentation |
| **C-30** | **Ordering instructions carry inline comparative framing independent of decision tables** | **skill-design** | Every ordering instruction contains its own if/if contrast in the instruction body — it does not delegate the comparative framing to "see Phase X Decision above" or any equivalent table reference. C-26 requires universal comparative framing on every ordering instruction; C-30 requires that framing to be present inline in the instruction text itself, so each instruction is self-contained at the point of reading: a model executing Phase 4 without having internalized Phase 4's decision table still encounters the critical branch condition in the instruction body, not by reference |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)
```

**Composite bands:**
- 90–100: Excellent — skip revision
- 75–89: Good — minor gaps, low-priority revision
- 60–74: Acceptable — recommended revision
- Below 60: Essential failure — mandatory revision before use
```
