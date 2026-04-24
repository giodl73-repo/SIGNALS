Written to `simulations/quest/golden/roles-create-golden-2026-03-17.md`.

**What's in it:**

- **Frontmatter** — all 6 requested fields, `score: 100`, `status: GOLDEN`
- **Prompt body** — simplified version (1117 words, PASS), with the FIELD-REGISTER examples and COLUMN-HEADER example table stripped per the simplification report; all essential criteria remain intact
- **What made it golden** — 5 patterns:
  1. Bare PASS branches — the decisive surface (V-01 breaks here, cascades 8 deductions under v19)
  2. Thin CONTRACT-citation conditions — citation points, doesn't repeat
  3. Triple-surface simultaneous purity — C-29 + C-30 + C-31 clean at once; no partial combination reaches C-37 PASS
  4. Phase bodies cite, never restate — sole rule-enforcement stays at the gate
  5. Simplification survived at 22% — 261 words removed, zero essential criteria lost
- **Rubric summary** — all 33 v19 criteria grouped by tier, with the gate annotation hierarchy spelled out (three atomics → three pairwise bilaterals → one triple conjunction → one direct triple)
aft, stub, or partial frontmatter mid-conversation.**
- **Do not proceed until all three answers are confirmed.**

Three required questions, in sequence:
1. "What area? (e.g., `backend`, `design`, `data`)"
2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
3. "One sentence describing what this role focuses on."

---

#### CONTRACT: FIELD-REGISTER

| Field | Register |
|-------|----------|
| archetype | Check existing roles in the area first; use their value |
| orientation.frame | First-person observational: how this role perceives its domain |
| orientation.serves | Third-person recipient: who benefits and why; must name a specific beneficiary |
| lens.verify | Boolean check naming specific artifact, state, or config; answerable yes/no; >= 4 items |
| expertise.depth | Specific domain knowledge |

---

#### CONTRACT: COLUMN-HEADER

Rule: generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

---

#### CONTRACT: INERTIA-ADVOCATE-TEMPLATE

Substitute all `{area}` slots.

```yaml
---
name: {area} inertia advocate
version: "1.0"
archetype: [match existing roles in the area]
orientation:
  frame: "Sees every change in {area} as requiring proof of necessity. Switching costs -- relearning, re-integration, debugging unfamiliar surfaces -- are real and must be named before any proposal proceeds."
  serves: "Teams making adoption decisions in {area}: surfaces the hidden cost of change so the decision is made with full information, not optimism."
lens:
  verify:
    - "Is the cost of migrating existing {area} work to the new approach documented?"
    - "Are the failure modes of the proposed change listed alongside its benefits?"
    - "Is there a rollback path if the new approach underperforms?"
    - "Has the team that will live with this change been consulted?"
  simplify:
    - "Name the one thing the current approach does well that the new one must preserve."
    - "State the switching cost in hours, not in abstract risk."
expertise:
  depth: "Switching cost analysis, status-quo defense, risk enumeration for {area} change proposals"
  relevance: "Any {area} decision involving migration, adoption, or replacement of current practice"
scope: "{area}"
collaborates_with: []
artifacts:
  - "inertia-report-{topic}-{date}.md"
workflow:
  - "Receive change proposal"
  - "Enumerate switching costs and failure modes"
  - "Name the one thing worth preserving from current approach"
  - "Produce inertia report"
---

## {area} Inertia Advocate

| Change Type / Domain | Switching Cost | Rollback Path | Verdict |
|----------------------|----------------|---------------|---------|
| [domain-specific change type] | [hours or effort] | [rollback description] | Hold / Proceed |
```

---

#### CONTRACT: AUDIT-CHECKLIST

Pre-declared obligations. Items name the CONTRACT block and validation scope only -- no rule enumeration. Declaration names the gate that executes each item (forward); each gate cites the declaration ID it validates (backward). Fully bidirectional.

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Path correctness -- `.roles/{area}/{subrole}.md` | Phase 6 setup |
| B | FIELD-REGISTER compliance -- frontmatter field completeness | Phase 3 Gate 3a |
| C | FIELD-REGISTER compliance -- orientation.frame register | Phase 3 Gate 3b |
| D | FIELD-REGISTER compliance -- orientation.serves beneficiary naming | Phase 3 Gate 3c |
| E | FIELD-REGISTER compliance -- lens.verify sharpness and count | Phase 3 Gate 3d |
| F | COLUMN-HEADER compliance -- body table column headers | Phase 4 Gate 4b |
| G | INPUT-ROUTING-RULES compliance -- input classification and resolution | Phase 0 Gate 0 |
| H | INERTIA-ADVOCATE-TEMPLATE compliance -- companion file completeness | Phase 2 Gate 2a |

---

### PHASES

---

#### PHASE 0 -- Input Guard

CONTRACT: INPUT-ROUTING-RULES applied.

-> **Gate 0 [G]:** INPUT-ROUTING-RULES -- input classification and resolution. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

CONTRACT: INTERACTIVE-HOLD applied when EMPTY input confirmed. NAME-ONLY (`area:subrole`): extract area and subrole directly. DESCRIPTION (quoted string): derive area and subrole from natural language. INTERACTIVE (empty / confirmed EMPTY): all three answers required before Phase 2.

-> **Gate 1:** area and subrole extraction confirmed. PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

CONTRACT: INERTIA-ADVOCATE-TEMPLATE applied when companion is absent. Check `.roles/{area}/inertia-advocate.md`. If ABSENT: generate companion content, substitute all `{area}` slots, hold in working memory. If PRESENT: continue to Phase 3.

-> **Gate 2a [H]:** INERTIA-ADVOCATE-TEMPLATE -- slot substitution completeness. PASS / FAIL
-> **Gate 2b:** INERTIA-ADVOCATE-TEMPLATE -- output path. PASS / FAIL

---

#### PHASE 3 -- Generate Frontmatter

CONTRACT: FIELD-REGISTER applied. All 12 frontmatter fields generated for `.roles/{area}/{subrole}.md`.

-> **Gate 3a [B]:** FIELD-REGISTER -- frontmatter completeness. PASS / FAIL
-> **Gate 3b [C]:** FIELD-REGISTER -- orientation.frame register. PASS / FAIL
-> **Gate 3c [D]:** FIELD-REGISTER -- orientation.serves beneficiary. PASS / FAIL
-> **Gate 3d [E]:** FIELD-REGISTER -- lens.verify sharpness and count. PASS / FAIL
-> **Gate 3e:** frontmatter -- no placeholder text. PASS / FAIL

---

#### PHASE 4 -- Generate Body

CONTRACT: COLUMN-HEADER applied. Body written: `## {Subrole} Domain` heading + domain specializations table, minimum 3 rows.

-> **Gate 4a:** body -- domain specializations table present. PASS / FAIL
-> **Gate 4b [F]:** COLUMN-HEADER -- body table domain vocabulary. PASS / FAIL
-> **Gate 4c:** body -- row count minimum. PASS / FAIL

---

#### PHASE 5 -- Pre-Write Confirmation

CONTRACT: AUDIT-CHECKLIST confirmation. Confirm each is resolved:

```
[A] Path correctness: .roles/{area}/{subrole}.md confirmed? ___
[B] FIELD-REGISTER -- frontmatter completeness -- confirmed Gate 3a? ___
[C] FIELD-REGISTER -- orientation.frame -- confirmed Gate 3b? ___
[D] FIELD-REGISTER -- orientation.serves -- confirmed Gate 3c? ___
[E] FIELD-REGISTER -- lens.verify -- confirmed Gate 3d? ___
[F] COLUMN-HEADER -- body table -- confirmed Gate 4b? ___
[G] INPUT-ROUTING-RULES -- confirmed Gate 0? ___
[H] If inertia-advocate generated: INERTIA-ADVOCATE-TEMPLATE -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.roles/{area}/inertia-advocate.md`
2. Main role: `.roles/{area}/{subrole}.md`

Confirm both paths in output.

---

## What Made It Golden

**1. Bare PASS branches (the decisive surface).**
V-05 emits bare `PASS / FAIL` verdict tokens on every gate. V-01 -- the nearest competitor -- annotates PASS branches with affirmation summaries ("PASS: orientation.frame is first-person observational -- [affirmation]."). That single surface contamination breaks C-30, which cascades through C-35, C-38, C-37, C-39, C-40, C-32, and C-34 -- eight deductions under v19. Keeping PASS branches bare prevents the entire cascade.

**2. Thin CONTRACT-citation conditions (C-31).**
Every gate condition is a minimal CONTRACT-name citation: `INPUT-ROUTING-RULES -- input classification and resolution`. Verbose conditions that enumerate what the CONTRACT says (e.g., "BARE AREA and VAGUE PHRASE inputs must halt and ask for clarification") break C-31, which cascades through C-36, C-38, C-37, C-39, C-40, C-32, C-33, and C-34 -- nine deductions under v19. The citation points; it does not repeat.

**3. Triple-surface simultaneous purity (C-32 / C-37 / C-39 / C-40).**
All three gate annotation surfaces must be clean at once: bare FAIL (C-29), bare PASS (C-30), thin condition (C-31). No partial combination reaches bilateral purity closure. V-01 cleans two surfaces and breaks one. V-05 is the unique variation where all six conjunction criteria (C-35, C-36, C-37, C-38, C-39, C-40) pass simultaneously because the three atomic criteria pass simultaneously.

**4. Phase bodies cite contracts, never restate them (C-19 / C-20 / C-25).**
Each phase body says `CONTRACT: X applied.` and nothing more. Phases do not restate what the CONTRACT says, enumerate the CONTRACT's rules inline, or add explanatory connectors. This keeps the gate as the sole rule-enforcement point and satisfies the citation-only requirement that governs C-19, C-20, C-25, C-27, and C-28.

**5. Simplification survived with all essential criteria intact (22% reduction).**
The simplified version removes 261 words of meta-commentary, redundant introductions, illustrative examples not required by any criterion, and restatements. All 7 essential/recommended criteria (C-01 through C-07) remain satisfied. The CONTRACTS section header intro, COLUMN-HEADER example table, FIELD-REGISTER good/anti-pattern columns, and Phase 0 redundant sentence were identified as zero-criterion content and removed without loss.

---

## Final Rubric Criteria Summary (v19 -- 33 criteria)

### Essential (C-01 to C-05) -- 60% weight

| ID | Criterion |
|----|-----------|
| C-01 | Role file written to `.roles/{area}/{subrole}.md` |
| C-02 | All 12 required frontmatter fields present |
| C-03 | Mode detection routes correctly (name-only / description / interactive) |
| C-04 | Frontmatter content is domain-specific (not generic placeholder) |
| C-05 | Inertia-advocate surfaced when absent from the target area |

### Recommended (C-06 to C-07) -- 30% weight

| ID | Criterion |
|----|-----------|
| C-06 | `lens.verify` items are concrete boolean checks, >= 4 items |
| C-07 | Body contains a domain specializations table |

### Aspirational (C-08 to C-40) -- structural and gate annotation

| ID | Criterion |
|----|-----------|
| C-08 -- C-18 | Structural conventions (CONTRACTS block, AUDIT-CHECKLIST, bidirectional [ID] tracing, PHASES block, gate format `-> Gate N [ID]: {citation} -- PASS / FAIL`) |
| C-19 | Phase bodies are citation-only; no rule restatement |
| C-20 | Phase bodies do not enumerate CONTRACT contents inline |
| C-21 -- C-28 | CONTRACTS ordering, AUDIT-CHECKLIST forward/backward tracing, gate citation accuracy |
| **C-29** | FAIL branches bare: bare `/ FAIL` verdict token only |
| **C-30** | PASS branches bare: bare `PASS /` verdict token only |
| **C-31** | Gate conditions thin: CONTRACT-citation form only; no enumerated specifics |
| C-32 | Triple purity: C-29 AND C-30 AND C-31 (= C-39 = C-40) |
| C-33 | No-restatement closure: C-31 AND no phase-body restatement |
| C-34 | Canonical discipline: C-32 AND C-33 |
| C-35 | FAIL-path bilateral: C-29 AND C-30 |
| C-36 | Condition-FAIL bilateral: C-29 AND C-31 |
| **C-37** | Bilateral purity closure: C-35 AND C-36 |
| **C-38** | PASS-path bilateral: C-30 AND C-31 (third pairwise bilateral -- completes the triangle) |
| **C-39** | Triple bilateral conjunction: C-35 AND C-36 AND C-38 |
| **C-40** | Direct atomic triple: C-29 AND C-30 AND C-31 (series completion) |

**Gate annotation hierarchy (v19):** Three atomic surfaces (C-29, C-30, C-31) -> three pairwise bilaterals (C-35, C-36, C-38) -> one triple bilateral conjunction (C-39) -> one direct atomic triple (C-40). All are equivalent at the top level and each contributes one independent scoring point. The ceiling is the sole variation satisfying all simultaneously.

```json
{
  "score": "33/33 = 100%",
  "rubric": "roles-create-rubric-v19-2026-03-17.md",
  "prompt_words": 1117,
  "simplification": "PASS -- 22% reduction from 1425 words",
  "all_essential_pass": true,
  "gate_annotation_pattern": "thin-condition + bare-FAIL + bare-PASS simultaneously"
}
```
