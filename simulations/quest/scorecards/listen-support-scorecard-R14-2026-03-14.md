## Round 14 Scorecard — listen-support (v13 rubric, 255 pts)

### Methodology

All five R14 variations are built on the R13 V-04 base, which held C-01 through C-39 at ceiling (250/255, failing only C-40). R14's objective is: fix C-40 across all variations; test whether C-41 and format/register changes cause regressions or surface additional gains. C-01 through C-35 are treated as inherited PASS for all variations (preserved without modification). Detailed evaluation focuses on C-36 through C-41.

---

### C-36 through C-41 — Evidence by Variation

#### C-36 — Exception Block Paraphrase-Clause Field

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | `Paraphrase clause:` named field present in every EXCEPTION SIGN-OFF BLOCK |
| V-02 | PASS | Numbered field 5 `Paraphrase clause:` in every EXCEPTION SIGN-OFF BLOCK |
| V-03 | PASS | `Paraphrase clause:` named field present in Phase 1 and Phase 3 blocks |
| V-04 | PASS | Numbered field 5 `Paraphrase clause:` (V-01+V-02 merge preserves both) |
| V-05 | PASS | Named `Paraphrase clause:` field in EXCEPTION SIGN-OFF BLOCKs |

---

#### C-37 — Verbatim Anchor at Step 4

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | `Verbatim from 2C: [quote your exact first sentence... copy it word for word, do not paraphrase]` |
| V-02 | PASS | `Required item 2 -- Verbatim from 2C: [copy your exact first sentence... word for word, do not paraphrase]` |
| V-03 | PASS | `Verbatim from 2C: [quote your exact first sentence... copy it word for word, do not paraphrase]` |
| V-04 | PASS | `Required item 2 -- Verbatim from 2C:` (inherited from V-02 format axis) |
| V-05 | PASS | `Verbatim from 2C: [copy your exact first sentence... word for word, do not paraphrase]` |

---

#### C-38 — Dual-Field "Both Lines" Gate

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Two labeled fields in fenced block; `Do not fill the table until both lines are written` |
| V-02 | PASS | Two labeled items (`Required item 1`, `Required item 2`); `both required items`; `Do not fill any cell...` |
| V-03 | PASS | Two labeled fields; `Both of the following lines must be written before any row...` — two distinct labeled fields present, satisfying structural requirement |
| V-04 | PASS | Two labeled items + competitor gate header; imperative `Do not fill any cell...` |
| V-05 | PASS | Two labeled fields in fenced block; `Do not fill the table until both lines are written` |

---

#### C-39 — Every-Assignment Scope Confirmation

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | `Confirmation: this rule applies to every severity assignment in the table below.` present after the dual-field block |
| V-02 | PASS | `Confirmation: this rule applies to every severity assignment in the table below.` present after Required items |
| V-03 | **FAIL** | Scope confirmation sentence absent. Coverage matrix intentionally drops C-39 to isolate lifecycle-emphasis axis |
| V-04 | PASS | `Confirmation: this rule applies to every severity assignment in the table below.` present |
| V-05 | PASS | `Confirmation: this rule applies to every severity assignment in the table below.` present |

---

#### C-40 — Verbatim Instruction in Exception Block Paraphrase Clause

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | `-- do not paraphrase, do not summarize, copy it verbatim word-for-word from your Step 2C block` |
| V-02 | PASS | `-- copy it verbatim from your Step 2C block, do not paraphrase` (item 5) |
| V-03 | PASS | `-- do not paraphrase, do not summarize, copy it word-for-word` in Phase 1 and Phase 3 EXCEPTION blocks |
| V-04 | PASS | `-- do not paraphrase, do not summarize, copy it verbatim word-for-word from your Step 2C block` (item 5) |
| V-05 | PASS | `-- do not paraphrase, do not summarize, copy it verbatim word-for-word from your Step 2C block` |

C-40 is fixed across all five R14 variations. This is the universal gain from R13 V-04 (250/255) to R14.

---

#### C-41 — Imperative Dual-Field Gate Language

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | `Do not fill the table until both lines are written:` — unconditional imperative, no modal softening |
| V-02 | PASS | `Do not fill any cell in the table until both items are written:` — imperative, applies to cells not rows |
| V-03 | **FAIL** | `Both of the following lines must be written before any row in the table is populated` — declarative "must be written" carries modal interpretive slack; intentional drop per axis design |
| V-04 | PASS | `Do not fill any cell in the table until both items are written:` — imperative (V-02 form) |
| V-05 | PASS | `Do not fill the table until both lines are written:` — imperative (V-01 form) |

---

### C-01 through C-35 — Inherited From R13 V-04

All five variations preserve C-01 through C-35 mechanisms without modification. R13 V-04 held all of these at ceiling. Spot-check of structural elements:

- **C-11 STATUS QUO**: 1a/1b/1c blocks present in all variations — PASS
- **C-12 inertia competitor naming**: `INERTIA COMPETITOR:` block with prohibition on generic phrases — PASS all
- **C-14 phase body templates**: Steps 2B templates with `[INERTIA COMPETITOR]` placeholder intact — PASS all
- **C-19 mode declaration**: `You ARE the persona` + explicit third-person prohibition present in all Step 3 — PASS all
- **C-25 switching-friction 4-field format**: `Migrating from:` / `Expected behavior:` / `Actual behavior:` / `Migration impact:` fields intact in Step 7 — PASS all
- **C-34 Step 2C cross-reference in Step 4**: All variations point back to Step 2C for both the confirmed and verbatim lines — PASS all

No regressions detected in C-01 through C-35 for any variation.

---

### Composite Scores

| Variation | C-36 | C-37 | C-38 | C-39 | C-40 | C-41 | C-01–35 | **Score** |
|-----------|------|------|------|------|------|------|---------|-----------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (all) | **255/255** |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (all) | **255/255** |
| V-03 | PASS | PASS | PASS | FAIL | PASS | FAIL | PASS (all) | **245/255** |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (all) | **255/255** |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (all) | **255/255** |

C-39 = 5 pts, C-41 = 5 pts (from R13 differential: 245 = 255 - 5 - 5 on same failure combination).

---

### Ranking

1. **V-01, V-02, V-04, V-05** — tied at **255/255** (ceiling)
2. **V-03** — **245/255** (C-39, C-41 intentionally dropped for axis isolation)

---

### Excellence Signals — Patterns from the Top-Scoring Variations

**1. C-40 verbatim mandate in the Paraphrase clause field is the universal unlock.**
The single addition — "do not paraphrase, do not summarize, copy it verbatim word-for-word from your Step 2C block" — converts the exception block from a faithful-restatement field to a string-retrieval field. This is the mechanism that moves from 250 to 255 for all four ceiling variations. The specific three-part formulation ("do not paraphrase, do not summarize, copy it verbatim word-for-word") is stronger than any single-clause form because it forecloses three distinct compression paths simultaneously.

**2. Competitor name re-anchoring before generation checkpoints (V-04, V-05).**
V-04 adds `Competitor in scope:` at the top of Step 4 before the table; V-05 adds this gate at both Steps 4 and 5. Neither gate is required by any criterion, but both create a structural redundancy: the model writes the product name twice before generating severity assignments (Step 4) and again before generating card bodies (Step 5). This pattern compresses tool-name fidelity drift across eight card bodies without touching any existing criterion mechanism.

**3. Numbered checklist explicitness at the Step-4 pre-commitment gate (V-02, V-04).**
Replacing the fenced code block with `Required item 1 --` / `Required item 2 --` labeled items changes the cognitive register from "fill this template" to "complete these checklist actions sequentially." The C-38 dual-field requirement and C-41 imperative prohibition both survive the format change cleanly. The numbered format may improve compliance quality for the verbatim field specifically, since "Required item 2" places the verbatim retrieval task in the same cognitive register as a checklist completion rather than a template slot.

**4. V-03's lifecycle framing fields demonstrate that exception block self-documentation is additive without requiring C-39/C-41 sacrifice.**
The `Fallback status:` field in V-03's phase-separated exception blocks is the cleanest structural addition of the round: it makes the severity rationale self-contained within each block (scorer can verify Grounds without cross-referencing the inference rule). This pattern can be backported to ceiling variations (V-01, V-04, V-05) without dropping C-39 or C-41, combining lifecycle self-documentation with scope confirmation and imperative gate language. V-03's deliberate axis isolation confirms the pattern is composable.

---

```json
{"top_score": 255, "all_essential_pass": true, "new_patterns": ["Competitor name re-anchor gate at Step 4 header reduces tool-name fidelity drift before severity table generation", "Dual-placement competitor gates at Steps 4 and 5 apply product-name re-anchoring at each major card-body generation checkpoint", "Numbered checklist format for Step-4 pre-commitment gate increases cognitive explicitness of two-field sequence vs fenced template", "Lifecycle framing field (Fallback status) in phase-separated exception blocks makes severity rationale self-documenting per block without requiring cross-reference to inference rule"]}
```
