## Quest Score — topic-achievements (Round 6)

---

### Rubric Context

v6 adds **C-20** (each gate declares a specific inspectable output schema) and **C-21** (uniform gate architecture — all phases gated, no step-labeled phases). Scoring formula: `(essential/5×60) + (recommended/3×30) + (aspirational/13×10)`. Max = 100.

Aspirational criteria C-09 through C-19 are carried from R5 V-05 (golden baseline). All R6 variations declare they preserve that baseline.

---

## V-01 — Schema Preface

### Essential (C-01 – C-05)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 — One state per achievement | PASS | Template enforces exactly one of EARNED / IN-PROGRESS / LOCKED per row; no combined states |
| C-02 — Falsified named as honesty signal | PASS | Falsified row carries "followed evidence over assumptions: [REVISION_EVENT]" framing |
| C-03 — Artifact-grounded classification | PASS | Invariant C requires EARNED rows to cite filename+date; CLASSIFY phase assigns artifacts from scan |
| C-04 — IN-PROGRESS shows numeric progress | PASS | Template has `[N] of 5 artifacts`, `[N] of [M] prove artifacts`, `[N] of 3 chain links` throughout |
| C-05 — Next action is specific | PASS | Next Action block names `/[SKILL]`, artifact path, achievement, current→target state, and a why-sentence linked to CLASSIFY output |

**Essential: 5/5 → 60 pts**

### Recommended (C-06 – C-08)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-06 — All 7 categories represented | PASS | All 7 rows in template: Exploration, Depth, Coverage, Quality, Chain, Discovery, Corps/Crew |
| C-07 — EARNED carries dates | PASS | Invariant C + template slot `[EARNED_ARTIFACT]` = "filename — date" |
| C-08 — Frontmatter includes state counts | PASS | YAML frontmatter declares `earned:`, `in_progress:`, `locked:` populated from STATE GATE output |

**Recommended: 3/3 → 30 pts**

### Aspirational (C-09 – C-21)

C-09 through C-19 are preserved baseline from R5 V-05 per frontmatter declaration. Treating as PASS (11).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 – C-19 (baseline) | PASS ×11 | Invariants A–D declared, pre-printed Falsified row, pre-printed LOCKED text, CLASSIFY before STATE, entry conditions enforced per phase |
| C-20 — Gate schema declared | PASS | Each phase opens with a named `GATE SCHEMA:` preface block before instructions. SCAN GATE: 3 specific labeled fields. CLASSIFY GATE: full 8-line schema (7 category lines + summary). STATE GATE: 5 fields including sum-to-7. WRITE GATE: 2 fields. All verifiable by inspection. |
| C-21 — Uniform gate architecture | **PARTIAL** | All 4 phases contain gate schemas, but section headers read "PHASE 1 — SCAN", "PHASE 2 — CLASSIFY", "PHASE 3 — FILL TEMPLATE", "PHASE 4 — WRITE ARTIFACT" — step labels, not gate labels. No registry establishes upfront that all 4 are gates; the model discovers this phase by phase. The architecture is uniform in practice but architecturally ambiguous from the headers. |

**Aspirational: 12.5/13 → 9.62 pts**

**V-01 Composite: 60 + 30 + 9.62 = 99.6 — Gold**

---

## V-02 — Gate Registry Table

### Essential: 5/5 → 60 pts *(same template and invariants)*

### Recommended: 3/3 → 30 pts *(same template and frontmatter)*

### Aspirational (C-09 – C-21)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 – C-19 (baseline) | PASS ×11 | Baseline preserved |
| C-20 — Gate schema declared | PASS | Registry table at preamble declares all 4 gate schemas before Phase 1. CLASSIFY GATE row explicitly lists all 7 category lines in the table cell (compressed inline but fully specified). Per-phase instructions reference registry; CLASSIFY phase adds: "A count line without category lines does not match the registry schema." Schema discoverable without scanning phases. |
| C-21 — Uniform gate architecture | PASS | Registry table names all 4 phases as gates before Phase 1 begins. Section headers: "PHASE 1 — SCAN GATE", "PHASE 2 — CLASSIFY GATE", "PHASE 3 — FILL TEMPLATE (STATE GATE)", "PHASE 4 — WRITE GATE." Uniform gate labels in both registry and section headers. No ungated phases. |

**Aspirational: 13/13 → 10 pts**

**V-02 Composite: 60 + 30 + 10 = 100 — Platinum**

---

## V-03 — Fail-Surface Closure

### Essential: 5/5 → 60 pts

### Recommended: 3/3 → 30 pts

### Aspirational (C-09 – C-21)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 – C-19 (baseline) | PASS ×11 | Baseline preserved |
| C-20 — Gate schema declared | PASS | Every gate has a `PASS:` block (exact output structure) and a `FAIL:` block (specific forms that do NOT clear). CLASSIFY GATE PASS shows full 8-line schema; FAIL lists 5 specific failure modes including "Only a count line without the 7 labeled category lines." Schema is verifiable in both directions. |
| C-21 — Uniform gate architecture | PASS | Section headers: "PHASE 1 — SCAN GATE", "PHASE 2 — CLASSIFY GATE", "PHASE 3 — FILL TEMPLATE (STATE GATE)", "PHASE 4 — WRITE GATE." All 4 use gate labels. No phase is a named step. Every phase has a gate contract with PASS and FAIL. |

**Aspirational: 13/13 → 10 pts**

**V-03 Composite: 60 + 30 + 10 = 100 — Platinum**

---

## V-04 — Registry + Fail-Surface Closure

### Essential: 5/5 → 60 pts

### Recommended: 3/3 → 30 pts

### Aspirational (C-09 – C-21)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 – C-19 (baseline) | PASS ×11 | Baseline preserved |
| C-20 — Gate schema declared | PASS | Registry table at preamble pre-declares all 4 PASS schemas. Per-phase FAIL blocks add defensive closure ("Summary count only, without the 7 labeled category lines"). C-20 met by two simultaneous mechanisms: registry declares structure, FAIL block declares what breaks inspection. |
| C-21 — Uniform gate architecture | PASS | Registry table names all 4 phases as gates. Section headers: "PHASE 1 — SCAN GATE", "PHASE 2 — CLASSIFY GATE", "PHASE 3 — FILL TEMPLATE (STATE GATE)", "PHASE 4 — WRITE GATE." Registry states: "A phase is not complete until its gate schema output is produced as declared above." |

**Aspirational: 13/13 → 10 pts**

**V-04 Composite: 60 + 30 + 10 = 100 — Platinum**

---

## V-05 — Golden Synthesis (Registry + Schema Preface + Fail-Surface Closure)

### Essential: 5/5 → 60 pts

### Recommended: 3/3 → 30 pts

### Aspirational (C-09 – C-21)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 – C-19 (baseline) | PASS ×11 | Baseline preserved per frontmatter; all four session invariants, pre-printed Falsified contract, LOCKED cell text, CLASSIFY-before-STATE ordering, all phases gated |
| C-20 — Gate schema declared | PASS | Three-layer coverage: (1) registry table at preamble declares all 4 schemas (architectural overview); (2) each phase opens with a `GATE SCHEMA (preface — read before executing)` block before instructions (goal-state immediacy); (3) FAIL conditions per gate close the failure surface ("summary count only without 7 labeled lines does not clear CLASSIFY GATE"). Schema is declared before execution begins, reinforced immediately before phase work, and bounded by explicit failure modes. |
| C-21 — Uniform gate architecture | PASS | Registry states "all 4 phases are gated" and names them before Phase 1. Section headers: "PHASE 1 — SCAN GATE", "PHASE 2 — CLASSIFY GATE", "PHASE 3 — FILL TEMPLATE (STATE GATE)", "PHASE 4 — WRITE GATE." Every phase carries gate label in header AND gate schema as preface. No ungated phases anywhere. |

**Aspirational: 13/13 → 10 pts**

**V-05 Composite: 60 + 30 + 10 = 100 — Platinum**

---

## Rankings

| Rank | Variation | Score | Grade |
|------|-----------|-------|-------|
| 1 (tied) | V-02 — Gate Registry | 100 | Platinum |
| 1 (tied) | V-03 — Fail-Surface Closure | 100 | Platinum |
| 1 (tied) | V-04 — Registry + FAIL | 100 | Platinum |
| 1 (tied) | V-05 — Golden Synthesis | 100 | Platinum |
| 5 | V-01 — Schema Preface | 99.6 | Gold |

---

## Excellence Signals from V-05 (Golden Synthesis)

**What made V-05 the designated golden synthesis** despite tying numerically with V-02–V-04:

**1. Three-layer schema reinforcement serves distinct cognitive functions at different execution moments**
Registry = architectural overview before any work begins. Preface = goal-state immediacy just before each phase executes. FAIL conditions = defensive closure that forces the model to navigate around named failure modes. These three mechanisms aren't redundant; they act at different points in the execution chain — setup, phase entry, and schema inspection.

**2. Schema preface inverts the discovery order**
R5 placed gate schemas at the END of each phase (after instructions). This means the model executed the phase before encountering the output format, treating the schema as a format reminder. V-05's preface placement means the model reads "here is exactly what you must produce" BEFORE reading what work to do — the schema becomes a goal state, not a retrospective check.

**3. The single source of truth problem is solved three ways simultaneously**
V-02 solves it with the registry (one place to look). V-03 solves it with FAIL conditions (two-sided contracts). V-05 makes the registry, preface, and FAIL conditions mutually consistent — any one of the three independently verifies the gate output. A model that misses the registry will encounter the preface; a model that misses the preface will encounter the FAIL block.

**V-01's sole gap** was architectural: section headers used step labels (SCAN, CLASSIFY, FILL TEMPLATE, WRITE ARTIFACT) without GATE terminology, and no registry established upfront that the architecture was uniformly gated. All four gate schemas were present and specific — but the architecture had to be discovered sequentially rather than declared.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Three-layer schema declaration (registry + preface + FAIL) serves distinct cognitive functions at different execution moments — registry gives architectural overview before work begins, preface gives goal-state immediacy at phase entry, FAIL conditions give defensive closure during inspection — making the mechanisms mutually reinforcing rather than redundant", "Schema preface placement inverts the discovery order: declaring gate output before phase instructions converts the schema from a retrospective format reminder into a prospective goal state the model works toward"]}
```
