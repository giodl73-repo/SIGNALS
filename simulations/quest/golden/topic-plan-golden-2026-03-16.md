---
skill: quest-golden
skill_target: topic-plan
date: 2026-03-15
rounds: 20
rubric_final: topic-plan-rubric-v21-2026-03-15.md
score: 73
status: GOLDEN
---

# topic:plan — Golden Prompt

## Prompt Body

```
You are running `topic:plan` — strategy revision for a Signal topic.

**Do not read strategy.md until Phase 2.**

---

### Phase 1: Signal Inventory

Scan `simulations/` across all 9 namespaces:
`scout` / `draft` / `review` / `flow` / `trace` / `prove` / `listen` / `program` / `topic`

For each, produce a table:

| Filename | Date | Content summary |
|----------|------|-----------------|

---

### Phase 2: Read strategy.md

Open `simulations/topic/[topic-name]/strategy.md`. Record:
- Strategy creation date (name it explicitly)
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

Cite at least one concrete reference to the strategy's structure.

---

### Phase 3: Delta Detection

Label each artifact:
- **PRIOR** — referenced or planned in strategy
- **NEW** — not referenced in strategy

For each NEW artifact, classify: **CONFIRMS** / **EXPANDS** / **CHALLENGES**

Only NEW artifacts drive proposals.

---

### Phase 4: Typed Change Proposals

Every namespace must have a row — silence is not a null declaration.

| Namespace | Proposal type | Evidence | Before | After | Defense |
|-----------|--------------|----------|--------|-------|---------|

- **Proposal type**: `ADD` / `REMOVE` / `REPRIORITIZE` / `NO CHANGE`
- **Evidence**: artifact filename (required for every non-null row)
- **Before**: current strategy language, or `(none)` for ADD
- **After**: proposed new language, or `(unchanged)` for NO CHANGE
- **Defense**: for `NO CHANGE`, explain why existing strategy is sufficient; `"no new signals"` only valid if namespace produced zero NEW artifacts

---

### Phase 5: Confirmation Gate

**STOP. Do not modify strategy.md.**

Present the complete proposal table.

> Confirm proposals? **YES / NO / REVISED**

Do not open strategy.md for writing until the user confirms YES.
If REVISED: incorporate user edits and re-present the full table for final confirmation.
If YES: apply changes and report the resulting diff.
```

---

## What Made It Golden

**1. Inventory-first epistemic ordering.**
The hard gate `"Do not read strategy.md until Phase 2"` forces all 9 namespace signal tables to be built before the strategy frame is visible. This prevents strategy vocabulary from anchoring the initial artifact classification — the evidence base becomes vocabulary-independent before the prior frame is opened. No rubric criterion in C-01–C-58 enforced this; it was identified as a candidate for C-59.

**2. Phase-locked read sequencing.**
Each phase has exactly one action and a hard dependency: Phase 1 completes the inventory, Phase 2 reads strategy, Phase 3 classifies, Phase 4 proposes, Phase 5 gates. The ordering is structural, not advisory — later phases are definitionally unavailable until earlier ones complete.

**3. Every namespace must have a row — silence is not a null declaration.**
The proposal table requires a row for all 9 namespaces. A namespace producing `NO CHANGE` still requires a per-row defense. This closes the "silent omission" failure mode where an agent skips weak-signal namespaces rather than explicitly accounting for them.

**4. Evidence required for every non-null proposal row.**
The `Evidence` column is mandatory for every `ADD`, `REMOVE`, and `REPRIORITIZE` row — not just for rows where evidence is convenient. This forces grounding: a proposal without an artifact filename cannot be submitted.

**5. Typed confirmation gate with three-branch resolution.**
Phase 5 stops before writing and requires explicit `YES / NO / REVISED` confirmation. `REVISED` has a defined loop: incorporate edits and re-present the full table. This prevents partial acceptance and ensures the confirmed table is always the authoritative record before strategy.md is modified.

---

## Final Rubric Summary — v21 (59 criteria)

### Essential (5) — all must pass

| ID | Criterion |
|----|-----------|
| C-01 | Read strategy.md — output cites concrete reference to existing strategy structure |
| C-02 | Signal inventory — all 9 namespaces assessed with artifact filenames + dates |
| C-03 | Delta detection — NEW vs PRIOR split; only NEW drives proposals; strategy date named |
| C-04 | Typed change proposals — ADD / REMOVE / REPRIORITIZE; silence not a null declaration |
| C-05 | Confirmation gate — stops before modifying strategy.md; presents YES/NO/REVISED |

### Recommended (3) — need 2/3 for golden

| ID | Criterion |
|----|-----------|
| C-06 | Evidence citation — artifact filename in every non-null proposal row |
| C-07 | Before/after diff — Before/After structure present for each proposal |
| C-08 | Inertia justification — per-row reason why NO CHANGE is sufficient |

### Aspirational (51) — C-09 through C-59

Key clusters:
- **C-09–C-42**: Core depth criteria (unchanged from v12) — covering classification completeness, strategy date freshness, gate ordering, schema block declarations
- **C-43–C-47** (v13–v14): Cell-exhaustive gate enumeration; numbered Gate-0 label; schema-gate checklist atomicity; pass-threshold annotation; condition-line self-containment
- **C-48–C-49** (v15): Single-STOP halt declaration; condition-line self-containment attestation
- **C-50–C-51** (v16): Semantic category grouping in condition line; pass/halt specification co-location in labeled field
- **C-52–C-53** (v17): Pass-threshold count derivation arithmetic exposed; procedural pre-proposal step as named schema block
- **C-58** (v20): Defense basis temporal audit — PRE-READ / POST-READ / POST-SIGNAL column distinguishes genuine prior justification from post-hoc rationalization
- **C-59** (candidate): Inventory-first epistemic ordering — all 9 namespace tables completed before strategy.md is opened

### Round 20 Variation Scores

| Variation | Score | % | C-58 |
|-----------|-------|---|------|
| V-01 (role sequence) | 10.5/58 | 18% | FAIL |
| V-02 (temporal audit) | 12/58 | 21% | PASS |
| V-03 (Gate-0 arch) | 40.5/58 | 70% | FAIL |
| V-04 (V-01+V-02 combo) | 36/58 | 62% | PASS |
| V-05 (full combo) | **42.5/58** | **73%** | PASS |

Simplification applied to V-01 axis: PASS (36% reduction). Golden prompt uses simplified body.
