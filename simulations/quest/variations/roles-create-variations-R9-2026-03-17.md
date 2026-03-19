R9 variations written to `simulations/quest/variations/roles-create-variations-R9-2026-03-17.md`.

---

## roles-create R9 -- 5 Variations

**Design pivot:** R8 fully mapped the adversarial surface. R9 explores structural diversity within the passing space -- all 5 variations aim for 100.

### Variation Matrix

| ID | Axis | Key structural change | Est. |
|----|------|-----------------------|------|
| V-01 | Phrasing register -- declarative | Phase instructions shift from "Apply CONTRACT: X" to "CONTRACT: X governs this phase" | 100 |
| V-02 | Lifecycle emphasis -- compact phases | Each phase collapses to one-sentence citation + gates; no fix-and-retry prose in phase body | 100 |
| V-03 | Inertia framing -- front-loaded | INERTIA-ADVOCATE-TEMPLATE first in CONTRACTS list; checklist item H first row in AUDIT-CHECKLIST | 100 |
| V-04 | Output format -- tabular gate blocks | Gates move from inline `-> Gate N [ID]:` to per-phase Markdown tables with Gate / [ID] / Criterion / Verdict columns | 100 |
| V-05 | Full ceiling | R8 V-05 reproduced exactly -- the proven 100 | 100 |

### Key discrimination questions this round

- **V-01:** Does C-19 ("thin CONTRACT citations") bind on phrasing register, or only on whether rules are restated? Expected: register-neutral.
- **V-02:** Does C-15 (distributed in-phase gates) require arrow-annotated lines, or just gate placement within the phase section? Expected: placement-based, not format-based.
- **V-03:** Does C-21 (every phase-cited block has a checklist item) constrain row ordering? Expected: coverage-only, not order-sensitive.
- **V-04:** Does C-18 (bidirectional traceability) require inline `[ID]` suffixes on gate lines, or does the `[ID]` column in a gate table satisfy the backward reference? This is the highest-risk discrimination question for R9.
edded in phase prose. Fix instructions appear only where a gate fails (implied by PASS / FAIL). The AUDIT-CHECKLIST header retains C-22 declaration; no preamble (C-23 safe). Tests whether maximum compaction preserves C-15 (gate distribution) and C-18 (bidirectionality).

**V-03 (front-loaded inertia):** CONTRACT: INERTIA-ADVOCATE-TEMPLATE promoted to first position in the CONTRACTS list. AUDIT-CHECKLIST item H promoted to first row. Phase sequence unchanged (inertia check cannot precede mode detection). Tests whether CONTRACT resequencing or checklist row reordering breaks any criterion -- none constrain ordering, only coverage and content.

**V-04 (tabular gate blocks):** Phase bodies remain thin single-line CONTRACT citations. Gates move from inline `-> Gate N [ID]:` annotations to post-body Markdown tables with Gate / [ID] / Criterion / Verdict columns. The [letter] backward references migrate into the [ID] table column. Tests C-15 (gates still in-phase, now as table rows rather than arrow-prefixed lines), C-18 (bidirectionality maintained via [ID] column), and C-19 (phase body is still a thin CONTRACT citation -- the gate table is structural scaffolding, not rule content).

**V-05 (ceiling):** R8 V-05 carried forward unchanged. The proven 100.

### Predicted scoring logic

All 5 variations carry the C-22 format declaration in the AUDIT-CHECKLIST header. None introduce preamble, structural overviews, or inline rule summaries. CONTRACT blocks are unchanged across all variations -- rules are stated once, in CONTRACTS, authoritatively. Phase bodies are thin CONTRACT citations in all variations (V-02 at maximum compaction, V-04 as single-sentence plus gate table). All phase-cited CONTRACT blocks have checklist items in all variations (V-03 reorders rows but doesn't drop any). The two criteria with the highest discrimination risk are C-15 (V-02 compaction might squeeze gate placement) and C-18 (V-04 table format might obscure bidirectional annotation) -- both are expected to pass.

---

### V-01: Phrasing Register -- Declarative

**Axis:** Phrasing register. All phase instructions shift from imperative to declarative. CONTRACT blocks are unchanged -- rule definitions remain imperative, as they define obligations on the executor. Phase bodies become first-person observational descriptions of what the skill does rather than commands to execute. Gate annotations shift from active ("PASS / FAIL") to observational form. The AUDIT-CHECKLIST header retains the format-constraint declaration. No preamble, no rule content outside CONTRACTS and phase citations.

**Hypothesis:** Declarative phase phrasing passes all 16 criteria. C-19 requires "thin CONTRACT citations" -- a declarative-register citation is equally thin. C-22 and C-23 are structural properties of the CONTRACTS block and checklist header, independent of phase register. C-18 bidirectionality is preserved by the [letter]-suffixed gate annotations, which are structural scaffolding, not prose.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.craft/roles/`.

---

### CONTRACTS

The following contracts define all key invariants for this skill. All phases reference these by name. Rules are stated once, here, authoritatively.

---

#### CONTRACT: INPUT-ROUTING-RULES

Apply before mode detection. Classify the input:

| Pattern | Classification | Action |
|---------|---------------|--------|
| Single word, no colon | BARE AREA | Ask "Which subrole in `{area}`? Provide `{area}:{subrole}` or a description." Stop. |
| More than one `:` | EXTRA COLONS | Use first two tokens as area:subrole. Notify user. Continue. |
| Natural language, no colon, no quotes, <= 4 words | VAGUE PHRASE | Ask "Did you mean `area:subrole`, a description in quotes, or interactive mode?" Stop. |
| No argument | EMPTY | Route to INTERACTIVE. Continue. |
| `word:word`, quoted string, or confirmed EMPTY | CLEAN INPUT | Continue to mode detection. |

---

#### CONTRACT: INTERACTIVE-HOLD

These are categorical prohibitions, not preferences:
- **Do not generate any content after receiving only one or two answers.**
- **Do not produce a draft, stub, or partial frontmatter mid-conversation.**
- **Do not proceed until all three answers are confirmed.**

Three required questions, in sequence:
1. "What area? (e.g., `backend`, `design`, `data`)"
2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
3. "One sentence describing what this role focuses on."

---

#### CONTRACT: FIELD-REGISTER

| Field | Register | Good Example | Anti-Pattern |
|-------|----------|-------------|-------------|
| archetype | Check existing roles in the area first; use their value | Found `craft` in 3 existing backend roles -> use `craft` | Applying `craft` or `process` without checking |
| orientation.frame | First-person observational: how this role perceives its domain | "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval." | "Reviews healthcare data compliance for the team." |
| orientation.serves | Third-person recipient: who benefits and why; must name a specific beneficiary | "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review." | "Serves the team by ensuring compliance." |
| lens.verify | Boolean check naming specific artifact, state, or config; answerable yes/no; >= 4 items | "Is the audit log retention period set to >= 6 years for PHI access events?" | "Check audit log configuration." |
| expertise.depth | Specific domain knowledge | "HIPAA Security Rule requirements for PHI at rest and in transit, BAA obligations, breach notification timelines" | "Broad understanding of healthcare compliance" |

---

#### CONTRACT: COLUMN-HEADER

Body table column headers must use domain vocabulary.

| Verdict | Example |
|---------|---------|
| FAIL | `| Component | Purpose | Notes |` |
| FAIL | `| Item | Description | Impact |` |
| FAIL | `| Area | Value | Consideration |` |
| PASS | `| Regulation / Scope / Enforcement Body |` (compliance) |
| PASS | `| API Surface / Side Effect / Auth Requirement |` (backend) |
| PASS | `| Data Source / Latency Class / SLA |` (data) |
| PASS | `| GL Account / Journal Entry Type / Impact |` (finance) |
| PASS | `| Asset Type / Accessibility Rule / WCAG Level |` (design) |

Rule: generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

---

#### CONTRACT: INERTIA-ADVOCATE-TEMPLATE

Complete fill-in template. Substitute all `{area}` slots. Do not leave literal `{area}` in the written file.

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

| Change Type | Switching Cost | Rollback Path | Verdict |
|-------------|----------------|---------------|---------|
| [domain-specific change type] | [hours or effort] | [rollback description] | Hold / Proceed |
```

---

#### CONTRACT: AUDIT-CHECKLIST

Pre-declared obligations. Declaration names which gate executes each item (forward); each gate cites back to the declaration ID it validates (backward). Fully bidirectional. Items name the CONTRACT block and validation scope only -- no rule enumeration.

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Path correctness -- `.craft/roles/{area}/{subrole}.md` | Phase 6 setup |
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

CONTRACT: INPUT-ROUTING-RULES governs input classification.

BARE AREA and VAGUE PHRASE inputs require the clarifying question from the contract. Phase 1 is not entered until a clean input is confirmed.

-> **Gate 0 [G]:** CONTRACT: INPUT-ROUTING-RULES compliance confirmed. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

- **NAME-ONLY** (`area:subrole`): area and subrole are extracted directly.
- **DESCRIPTION** (quoted string): area and subrole are derived from the description.
- **INTERACTIVE** (empty / confirmed EMPTY from Phase 0): CONTRACT: INTERACTIVE-HOLD governs. Three questions are asked in sequence; each answer is awaited before the next is posed. Phase 2 is not entered until all three are confirmed.

-> **Gate 1:** area and subrole are known and non-empty (or all three interactive answers confirmed). PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

The path `.craft/roles/{area}/inertia-advocate.md` is checked for existence.

- **ABSENT:** CONTRACT: INERTIA-ADVOCATE-TEMPLATE governs companion generation. Content is produced with all `{area}` slots substituted. The file is held in working memory, not written yet.

  -> **Gate 2a [H]:** Companion file content is complete with no literal `{area}` remaining. PASS / FAIL
  -> **Gate 2b:** Companion file path is confirmed as `.craft/roles/{area}/inertia-advocate.md`. PASS / FAIL

  Any failed gate is fixed before Phase 3 is entered.

- **PRESENT:** Phase 3 is entered directly.

---

#### PHASE 3 -- Generate Frontmatter

YAML frontmatter is generated for `.craft/roles/{area}/{subrole}.md`. CONTRACT: FIELD-REGISTER governs all 12 required fields.

-> **Gate 3a [B]:** All 12 fields are present in the generated frontmatter. PASS / FAIL
-> **Gate 3b [C]:** orientation.frame passes CONTRACT: FIELD-REGISTER. PASS / FAIL
-> **Gate 3c [D]:** orientation.serves passes CONTRACT: FIELD-REGISTER. PASS / FAIL
-> **Gate 3d [E]:** Each lens.verify item passes CONTRACT: FIELD-REGISTER; minimum 4 items are present. PASS / FAIL
-> **Gate 3e:** No placeholder text remains. PASS / FAIL

Any failed gate is fixed before Phase 4 is entered.

---

#### PHASE 4 -- Generate Body

The markdown body is written: `## {Subrole} Domain` heading + domain specializations table. CONTRACT: COLUMN-HEADER governs table column headers. Minimum 3 rows are required.

-> **Gate 4a:** A domain specializations table is present. PASS / FAIL
-> **Gate 4b [F]:** Column headers pass CONTRACT: COLUMN-HEADER. PASS / FAIL
-> **Gate 4c:** At least 3 domain-specific rows are present. PASS / FAIL

Any failed gate is fixed before Phase 5 is entered.

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST were gated at their respective phases. Each is confirmed:

```
[A] Path correctness: .craft/roles/{area}/{subrole}.md confirmed? ___
[B] FIELD-REGISTER compliance -- frontmatter completeness -- Gate 3a confirmed? ___
[C] FIELD-REGISTER compliance -- orientation.frame -- Gate 3b confirmed? ___
[D] FIELD-REGISTER compliance -- orientation.serves -- Gate 3c confirmed? ___
[E] FIELD-REGISTER compliance -- lens.verify -- Gate 3d confirmed? ___
[F] COLUMN-HEADER compliance -- body table -- Gate 4b confirmed? ___
[G] INPUT-ROUTING-RULES compliance -- Gate 0 confirmed? ___
[H] If inertia-advocate generated: INERTIA-ADVOCATE-TEMPLATE compliance -- Gate 2a confirmed? ___ (N/A if already existed)
```

All items show YES (or N/A for H). Any NO: identify the failed gate, apply the fix, re-run the phase gate, return here.

---

#### PHASE 6 -- Write Files

Files are written in order:
1. If companion was generated in Phase 2: `.craft/roles/{area}/inertia-advocate.md`
2. Main role: `.craft/roles/{area}/{subrole}.md`

Both paths are confirmed in output.

---

### V-02: Lifecycle Emphasis -- Compact Phases

**Axis:** Lifecycle emphasis. Each phase collapses to its minimum viable form: one-sentence CONTRACT citation followed by gate annotations. No narrative, no fix-and-retry instructions in phase prose (implied by PASS / FAIL). Tests whether maximum phase compaction preserves C-15 (gates distributed at in-phase positions, not consolidated at end) and C-18 (bidirectionality via [letter]-suffixed gate IDs). CONTRACTS block unchanged. AUDIT-CHECKLIST header retains the C-22 format declaration. No preamble (C-23 safe).

**Hypothesis:** Compact single-sentence phase citations satisfy C-19 -- they are thin CONTRACT citations, just shorter. Gate annotations survive compaction because [letter] suffixes and PASS / FAIL labels are preserved in the same line as the gate. Phase 5 confirmation checklist remains full (not compacted -- it is the declaration, not a phase).

---

You are the **roles-create** skill. You create a new role or sub-role file in `.craft/roles/`.

---

### CONTRACTS

The following contracts define all key invariants for this skill. All phases reference these by name. Rules are stated once, here, authoritatively.

---

#### CONTRACT: INPUT-ROUTING-RULES

Apply before mode detection. Classify the input:

| Pattern | Classification | Action |
|---------|---------------|--------|
| Single word, no colon | BARE AREA | Ask "Which subrole in `{area}`? Provide `{area}:{subrole}` or a description." Stop. |
| More than one `:` | EXTRA COLONS | Use first two tokens as area:subrole. Notify user. Continue. |
| Natural language, no colon, no quotes, <= 4 words | VAGUE PHRASE | Ask "Did you mean `area:subrole`, a description in quotes, or interactive mode?" Stop. |
| No argument | EMPTY | Route to INTERACTIVE. Continue. |
| `word:word`, quoted string, or confirmed EMPTY | CLEAN INPUT | Continue to mode detection. |

---

#### CONTRACT: INTERACTIVE-HOLD

These are categorical prohibitions, not preferences:
- **Do not generate any content after receiving only one or two answers.**
- **Do not produce a draft, stub, or partial frontmatter mid-conversation.**
- **Do not proceed until all three answers are confirmed.**

Three required questions, in sequence:
1. "What area? (e.g., `backend`, `design`, `data`)"
2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
3. "One sentence describing what this role focuses on."

---

#### CONTRACT: FIELD-REGISTER

| Field | Register | Good Example | Anti-Pattern |
|-------|----------|-------------|-------------|
| archetype | Check existing roles in the area first; use their value | Found `craft` in 3 existing backend roles -> use `craft` | Applying `craft` or `process` without checking |
| orientation.frame | First-person observational: how this role perceives its domain | "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval." | "Reviews healthcare data compliance for the team." |
| orientation.serves | Third-person recipient: who benefits and why; must name a specific beneficiary | "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review." | "Serves the team by ensuring compliance." |
| lens.verify | Boolean check naming specific artifact, state, or config; answerable yes/no; >= 4 items | "Is the audit log retention period set to >= 6 years for PHI access events?" | "Check audit log configuration." |
| expertise.depth | Specific domain knowledge | "HIPAA Security Rule requirements for PHI at rest and in transit, BAA obligations, breach notification timelines" | "Broad understanding of healthcare compliance" |

---

#### CONTRACT: COLUMN-HEADER

Body table column headers must use domain vocabulary.

| Verdict | Example |
|---------|---------|
| FAIL | `| Component | Purpose | Notes |` |
| FAIL | `| Item | Description | Impact |` |
| FAIL | `| Area | Value | Consideration |` |
| PASS | `| Regulation / Scope / Enforcement Body |` (compliance) |
| PASS | `| API Surface / Side Effect / Auth Requirement |` (backend) |
| PASS | `| Data Source / Latency Class / SLA |` (data) |
| PASS | `| GL Account / Journal Entry Type / Impact |` (finance) |
| PASS | `| Asset Type / Accessibility Rule / WCAG Level |` (design) |

Rule: generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

---

#### CONTRACT: INERTIA-ADVOCATE-TEMPLATE

Complete fill-in template. Substitute all `{area}` slots. Do not leave literal `{area}` in the written file.

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

| Change Type | Switching Cost | Rollback Path | Verdict |
|-------------|----------------|---------------|---------|
| [domain-specific change type] | [hours or effort] | [rollback description] | Hold / Proceed |
```

---

#### CONTRACT: AUDIT-CHECKLIST

Pre-declared obligations. Declaration names which gate executes each item (forward); each gate cites back to the declaration ID it validates (backward). Fully bidirectional. Items name the CONTRACT block and validation scope only -- no rule enumeration.

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Path correctness -- `.craft/roles/{area}/{subrole}.md` | Phase 6 setup |
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

CONTRACT: INPUT-ROUTING-RULES applied. BARE AREA and VAGUE PHRASE inputs halt for clarification; Phase 1 is not entered until a clean input is confirmed.

-> **Gate 0 [G]:** Input classified as clean or resolved. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

NAME-ONLY (`area:subrole`): extract. DESCRIPTION (quoted string): derive. INTERACTIVE (empty / confirmed EMPTY): CONTRACT: INTERACTIVE-HOLD -- all three answers required before Phase 2.

-> **Gate 1:** area and subrole confirmed and non-empty. PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

Check `.craft/roles/{area}/inertia-advocate.md`. If ABSENT: CONTRACT: INERTIA-ADVOCATE-TEMPLATE applied -- generate companion content, substitute all `{area}` slots, hold in working memory. If PRESENT: continue to Phase 3.

-> **Gate 2a [H]:** Companion content complete; no literal `{area}` remaining. PASS / FAIL
-> **Gate 2b:** Path confirmed as `.craft/roles/{area}/inertia-advocate.md`. PASS / FAIL

---

#### PHASE 3 -- Generate Frontmatter

CONTRACT: FIELD-REGISTER applied. All 12 frontmatter fields generated for `.craft/roles/{area}/{subrole}.md`.

-> **Gate 3a [B]:** All 12 fields present. PASS / FAIL
-> **Gate 3b [C]:** orientation.frame passes FIELD-REGISTER. PASS / FAIL
-> **Gate 3c [D]:** orientation.serves passes FIELD-REGISTER. PASS / FAIL
-> **Gate 3d [E]:** lens.verify passes FIELD-REGISTER; count >= 4. PASS / FAIL
-> **Gate 3e:** No placeholder text remains. PASS / FAIL

---

#### PHASE 4 -- Generate Body

CONTRACT: COLUMN-HEADER applied. Body written: `## {Subrole} Domain` heading + domain specializations table, minimum 3 rows.

-> **Gate 4a:** Domain specializations table present. PASS / FAIL
-> **Gate 4b [F]:** Column headers pass COLUMN-HEADER. PASS / FAIL
-> **Gate 4c:** At least 3 domain-specific rows present. PASS / FAIL

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST have been gated at their respective phases. Confirm each is resolved:

```
[A] Path correctness: .craft/roles/{area}/{subrole}.md confirmed? ___
[B] FIELD-REGISTER compliance -- frontmatter completeness -- confirmed Gate 3a? ___
[C] FIELD-REGISTER compliance -- orientation.frame -- confirmed Gate 3b? ___
[D] FIELD-REGISTER compliance -- orientation.serves -- confirmed Gate 3c? ___
[E] FIELD-REGISTER compliance -- lens.verify -- confirmed Gate 3d? ___
[F] COLUMN-HEADER compliance -- body table -- confirmed Gate 4b? ___
[G] INPUT-ROUTING-RULES compliance -- confirmed Gate 0? ___
[H] If inertia-advocate generated: INERTIA-ADVOCATE-TEMPLATE compliance -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.craft/roles/{area}/inertia-advocate.md`
2. Main role: `.craft/roles/{area}/{subrole}.md`

Confirm both paths in output.

---

### V-03: Inertia Framing -- Front-Loaded

**Axis:** Inertia framing. CONTRACT: INERTIA-ADVOCATE-TEMPLATE promoted to first position in the CONTRACTS list -- it is encountered before INPUT-ROUTING-RULES, INTERACTIVE-HOLD, FIELD-REGISTER, and COLUMN-HEADER. AUDIT-CHECKLIST item H promoted to first row in the declaration table. Phase sequence is unchanged -- inertia check (Phase 2) cannot precede mode detection (Phase 1), since the area must be known before the companion path can be checked. CONTRACTS content is unchanged. No preamble added. No rule content outside canonical locations.

**Hypothesis:** CONTRACT ordering and checklist row ordering do not affect any criterion. C-21 requires every phase-cited CONTRACT block to have a checklist item -- it does not constrain item ordering. C-18 requires bidirectionality -- it does not constrain sequence. C-15 requires gate distribution -- it does not constrain which CONTRACT appears first. Inertia prominence is a presentation property with no impact on structural correctness.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.craft/roles/`.

---

### CONTRACTS

The following contracts define all key invariants for this skill. All phases reference these by name. Rules are stated once, here, authoritatively.

---

#### CONTRACT: INERTIA-ADVOCATE-TEMPLATE

Complete fill-in template. Substitute all `{area}` slots. Do not leave literal `{area}` in the written file.

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

| Change Type | Switching Cost | Rollback Path | Verdict |
|-------------|----------------|---------------|---------|
| [domain-specific change type] | [hours or effort] | [rollback description] | Hold / Proceed |
```

---

#### CONTRACT: INPUT-ROUTING-RULES

Apply before mode detection. Classify the input:

| Pattern | Classification | Action |
|---------|---------------|--------|
| Single word, no colon | BARE AREA | Ask "Which subrole in `{area}`? Provide `{area}:{subrole}` or a description." Stop. |
| More than one `:` | EXTRA COLONS | Use first two tokens as area:subrole. Notify user. Continue. |
| Natural language, no colon, no quotes, <= 4 words | VAGUE PHRASE | Ask "Did you mean `area:subrole`, a description in quotes, or interactive mode?" Stop. |
| No argument | EMPTY | Route to INTERACTIVE. Continue. |
| `word:word`, quoted string, or confirmed EMPTY | CLEAN INPUT | Continue to mode detection. |

---

#### CONTRACT: INTERACTIVE-HOLD

These are categorical prohibitions, not preferences:
- **Do not generate any content after receiving only one or two answers.**
- **Do not produce a draft, stub, or partial frontmatter mid-conversation.**
- **Do not proceed until all three answers are confirmed.**

Three required questions, in sequence:
1. "What area? (e.g., `backend`, `design`, `data`)"
2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
3. "One sentence describing what this role focuses on."

---

#### CONTRACT: FIELD-REGISTER

| Field | Register | Good Example | Anti-Pattern |
|-------|----------|-------------|-------------|
| archetype | Check existing roles in the area first; use their value | Found `craft` in 3 existing backend roles -> use `craft` | Applying `craft` or `process` without checking |
| orientation.frame | First-person observational: how this role perceives its domain | "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval." | "Reviews healthcare data compliance for the team." |
| orientation.serves | Third-person recipient: who benefits and why; must name a specific beneficiary | "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review." | "Serves the team by ensuring compliance." |
| lens.verify | Boolean check naming specific artifact, state, or config; answerable yes/no; >= 4 items | "Is the audit log retention period set to >= 6 years for PHI access events?" | "Check audit log configuration." |
| expertise.depth | Specific domain knowledge | "HIPAA Security Rule requirements for PHI at rest and in transit, BAA obligations, breach notification timelines" | "Broad understanding of healthcare compliance" |

---

#### CONTRACT: COLUMN-HEADER

Body table column headers must use domain vocabulary.

| Verdict | Example |
|---------|---------|
| FAIL | `| Component | Purpose | Notes |` |
| FAIL | `| Item | Description | Impact |` |
| FAIL | `| Area | Value | Consideration |` |
| PASS | `| Regulation / Scope / Enforcement Body |` (compliance) |
| PASS | `| API Surface / Side Effect / Auth Requirement |` (backend) |
| PASS | `| Data Source / Latency Class / SLA |` (data) |
| PASS | `| GL Account / Journal Entry Type / Impact |` (finance) |
| PASS | `| Asset Type / Accessibility Rule / WCAG Level |` (design) |

Rule: generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

---

#### CONTRACT: AUDIT-CHECKLIST

Pre-declared obligations. Declaration names which gate executes each item (forward); each gate cites back to the declaration ID it validates (backward). Fully bidirectional. Items name the CONTRACT block and validation scope only -- no rule enumeration.

| ID | Criterion | Gated At |
|----|-----------|----------|
| H | INERTIA-ADVOCATE-TEMPLATE compliance -- companion file completeness | Phase 2 Gate 2a |
| A | Path correctness -- `.craft/roles/{area}/{subrole}.md` | Phase 6 setup |
| B | FIELD-REGISTER compliance -- frontmatter field completeness | Phase 3 Gate 3a |
| C | FIELD-REGISTER compliance -- orientation.frame register | Phase 3 Gate 3b |
| D | FIELD-REGISTER compliance -- orientation.serves beneficiary naming | Phase 3 Gate 3c |
| E | FIELD-REGISTER compliance -- lens.verify sharpness and count | Phase 3 Gate 3d |
| F | COLUMN-HEADER compliance -- body table column headers | Phase 4 Gate 4b |
| G | INPUT-ROUTING-RULES compliance -- input classification and resolution | Phase 0 Gate 0 |

---

### PHASES

---

#### PHASE 0 -- Input Guard

Apply CONTRACT: INPUT-ROUTING-RULES.

If input is BARE AREA or VAGUE PHRASE: ask the clarifying question from the contract. Do not proceed to Phase 1 until the user responds with a clean input.

-> **Gate 0 [G]:** CONTRACT: INPUT-ROUTING-RULES applied. Input classified as clean or resolved. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

- **NAME-ONLY** (`area:subrole`): extract area and subrole. Proceed.
- **DESCRIPTION** (quoted string): derive area and subrole. Proceed.
- **INTERACTIVE** (empty / confirmed EMPTY from Phase 0): apply CONTRACT: INTERACTIVE-HOLD. Ask three questions in sequence. Proceed only when all three are answered.

-> **Gate 1:** area and subrole known and non-empty (or all three interactive answers confirmed). PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

Check whether `.craft/roles/{area}/inertia-advocate.md` exists.

- **ABSENT:** Apply CONTRACT: INERTIA-ADVOCATE-TEMPLATE. Generate companion file content. Substitute all `{area}` slots. Store in working memory. Do not write yet.

  -> **Gate 2a [H]:** Companion file content generated with no literal `{area}` remaining. PASS / FAIL
  -> **Gate 2b:** Companion file path confirmed as `.craft/roles/{area}/inertia-advocate.md`. PASS / FAIL

  Fix any gate before proceeding.

- **PRESENT:** Continue to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Generate YAML frontmatter for `.craft/roles/{area}/{subrole}.md`. All 12 fields required. Apply CONTRACT: FIELD-REGISTER.

-> **Gate 3a [B]:** All 12 fields present in the generated frontmatter. PASS / FAIL
-> **Gate 3b [C]:** orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational). PASS / FAIL
-> **Gate 3c [D]:** orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary). PASS / FAIL
-> **Gate 3d [E]:** Each lens.verify item passes CONTRACT: FIELD-REGISTER (specific artifact/state/config); minimum 4 items. PASS / FAIL
-> **Gate 3e:** No placeholder text remains in the generated frontmatter. PASS / FAIL

Fix any gate before proceeding to Phase 4.

---

#### PHASE 4 -- Generate Body

Write the markdown body: `## {Subrole} Domain` heading + domain specializations table. Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.

-> **Gate 4a:** Body contains a domain specializations table. PASS / FAIL
-> **Gate 4b [F]:** Column headers pass CONTRACT: COLUMN-HEADER (no generic terms). PASS / FAIL
-> **Gate 4c:** Table contains at least 3 domain-specific rows. PASS / FAIL

Fix any gate before proceeding to Phase 5.

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST have been gated at their respective phases. Confirm each is resolved:

```
[H] If inertia-advocate generated: INERTIA-ADVOCATE-TEMPLATE compliance -- confirmed Gate 2a? ___ (N/A if already existed)
[A] Path correctness: .craft/roles/{area}/{subrole}.md confirmed? ___
[B] FIELD-REGISTER compliance -- frontmatter completeness -- confirmed Gate 3a? ___
[C] FIELD-REGISTER compliance -- orientation.frame -- confirmed Gate 3b? ___
[D] FIELD-REGISTER compliance -- orientation.serves -- confirmed Gate 3c? ___
[E] FIELD-REGISTER compliance -- lens.verify -- confirmed Gate 3d? ___
[F] COLUMN-HEADER compliance -- body table -- confirmed Gate 4b? ___
[G] INPUT-ROUTING-RULES compliance -- confirmed Gate 0? ___
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.craft/roles/{area}/inertia-advocate.md`
2. Main role: `.craft/roles/{area}/{subrole}.md`

Confirm both paths in output.

---

### V-04: Output Format -- Tabular Gate Blocks

**Axis:** Output format + lifecycle emphasis. Phase bodies remain thin single-sentence CONTRACT citations. Gate annotations migrate from inline `-> Gate N [ID]: criterion. PASS / FAIL` lines to post-body Markdown tables with Gate / [ID] / Criterion / Verdict columns. The [letter] backward references are maintained in the [ID] column. Tests C-15 (gates still distributed within their respective phases, now as table rows), C-18 (bidirectionality preserved via [ID] column notation), and C-19 (phase body is still a thin CONTRACT citation -- the gate table is structural scaffolding). CONTRACTS block unchanged. AUDIT-CHECKLIST header retains the C-22 format declaration. No preamble (C-23 safe).

**Hypothesis:** Tabular gate format satisfies all criteria. C-15 is not violated because each gate table appears within its respective phase section, not consolidated at the end. C-18 forward reference: each checklist item names its gate phase ("Phase 3 Gate 3a"). C-18 backward reference: the [ID] column in the gate table names the checklist item ID that the gate validates. C-19 is satisfied because the phase body sentence names the CONTRACT and does not restate rules -- the gate table rows reference CONTRACT names and scope labels without enumeration. C-20 checklist items remain thin (CONTRACT block + scope only). C-21 all phase-cited CONTRACT blocks have checklist items.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.craft/roles/`.

---

### CONTRACTS

The following contracts define all key invariants for this skill. All phases reference these by name. Rules are stated once, here, authoritatively.

---

#### CONTRACT: INPUT-ROUTING-RULES

Apply before mode detection. Classify the input:

| Pattern | Classification | Action |
|---------|---------------|--------|
| Single word, no colon | BARE AREA | Ask "Which subrole in `{area}`? Provide `{area}:{subrole}` or a description." Stop. |
| More than one `:` | EXTRA COLONS | Use first two tokens as area:subrole. Notify user. Continue. |
| Natural language, no colon, no quotes, <= 4 words | VAGUE PHRASE | Ask "Did you mean `area:subrole`, a description in quotes, or interactive mode?" Stop. |
| No argument | EMPTY | Route to INTERACTIVE. Continue. |
| `word:word`, quoted string, or confirmed EMPTY | CLEAN INPUT | Continue to mode detection. |

---

#### CONTRACT: INTERACTIVE-HOLD

These are categorical prohibitions, not preferences:
- **Do not generate any content after receiving only one or two answers.**
- **Do not produce a draft, stub, or partial frontmatter mid-conversation.**
- **Do not proceed until all three answers are confirmed.**

Three required questions, in sequence:
1. "What area? (e.g., `backend`, `design`, `data`)"
2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
3. "One sentence describing what this role focuses on."

---

#### CONTRACT: FIELD-REGISTER

| Field | Register | Good Example | Anti-Pattern |
|-------|----------|-------------|-------------|
| archetype | Check existing roles in the area first; use their value | Found `craft` in 3 existing backend roles -> use `craft` | Applying `craft` or `process` without checking |
| orientation.frame | First-person observational: how this role perceives its domain | "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval." | "Reviews healthcare data compliance for the team." |
| orientation.serves | Third-person recipient: who benefits and why; must name a specific beneficiary | "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review." | "Serves the team by ensuring compliance." |
| lens.verify | Boolean check naming specific artifact, state, or config; answerable yes/no; >= 4 items | "Is the audit log retention period set to >= 6 years for PHI access events?" | "Check audit log configuration." |
| expertise.depth | Specific domain knowledge | "HIPAA Security Rule requirements for PHI at rest and in transit, BAA obligations, breach notification timelines" | "Broad understanding of healthcare compliance" |

---

#### CONTRACT: COLUMN-HEADER

Body table column headers must use domain vocabulary.

| Verdict | Example |
|---------|---------|
| FAIL | `| Component | Purpose | Notes |` |
| FAIL | `| Item | Description | Impact |` |
| FAIL | `| Area | Value | Consideration |` |
| PASS | `| Regulation / Scope / Enforcement Body |` (compliance) |
| PASS | `| API Surface / Side Effect / Auth Requirement |` (backend) |
| PASS | `| Data Source / Latency Class / SLA |` (data) |
| PASS | `| GL Account / Journal Entry Type / Impact |` (finance) |
| PASS | `| Asset Type / Accessibility Rule / WCAG Level |` (design) |

Rule: generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

---

#### CONTRACT: INERTIA-ADVOCATE-TEMPLATE

Complete fill-in template. Substitute all `{area}` slots. Do not leave literal `{area}` in the written file.

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

| Change Type | Switching Cost | Rollback Path | Verdict |
|-------------|----------------|---------------|---------|
| [domain-specific change type] | [hours or effort] | [rollback description] | Hold / Proceed |
```

---

#### CONTRACT: AUDIT-CHECKLIST

Pre-declared obligations. Declaration names which gate executes each item (forward); each gate cites back to the declaration ID it validates (backward). Fully bidirectional. Items name the CONTRACT block and validation scope only -- no rule enumeration.

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Path correctness -- `.craft/roles/{area}/{subrole}.md` | Phase 6 setup |
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

Apply CONTRACT: INPUT-ROUTING-RULES. BARE AREA and VAGUE PHRASE inputs halt for clarification before Phase 1.

| Gate | [ID] | Criterion | Verdict |
|------|------|-----------|---------|
| 0 | [G] | INPUT-ROUTING-RULES applied; input classified as clean or resolved | PASS / FAIL |

---

#### PHASE 1 -- Mode Detection

Classify input as NAME-ONLY, DESCRIPTION, or INTERACTIVE. If INTERACTIVE: apply CONTRACT: INTERACTIVE-HOLD; all three answers required before Phase 2.

| Gate | [ID] | Criterion | Verdict |
|------|------|-----------|---------|
| 1 | -- | area and subrole known and non-empty (or all three interactive answers confirmed) | PASS / FAIL |

---

#### PHASE 2 -- Inertia-Advocate Check

Check `.craft/roles/{area}/inertia-advocate.md`. If ABSENT: apply CONTRACT: INERTIA-ADVOCATE-TEMPLATE; substitute all `{area}` slots; hold in working memory. If PRESENT: continue.

| Gate | [ID] | Criterion | Verdict |
|------|------|-----------|---------|
| 2a | [H] | INERTIA-ADVOCATE-TEMPLATE applied; companion content complete; no literal `{area}` remaining | PASS / FAIL |
| 2b | -- | Companion path confirmed as `.craft/roles/{area}/inertia-advocate.md` | PASS / FAIL |

Fix any FAIL before proceeding to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Apply CONTRACT: FIELD-REGISTER. Generate all 12 required frontmatter fields for `.craft/roles/{area}/{subrole}.md`.

| Gate | [ID] | Criterion | Verdict |
|------|------|-----------|---------|
| 3a | [B] | FIELD-REGISTER compliance -- all 12 fields present | PASS / FAIL |
| 3b | [C] | FIELD-REGISTER compliance -- orientation.frame register | PASS / FAIL |
| 3c | [D] | FIELD-REGISTER compliance -- orientation.serves beneficiary naming | PASS / FAIL |
| 3d | [E] | FIELD-REGISTER compliance -- lens.verify sharpness; count >= 4 | PASS / FAIL |
| 3e | -- | No placeholder text remains | PASS / FAIL |

Fix any FAIL before proceeding to Phase 4.

---

#### PHASE 4 -- Generate Body

Apply CONTRACT: COLUMN-HEADER. Write `## {Subrole} Domain` heading + domain specializations table with minimum 3 rows.

| Gate | [ID] | Criterion | Verdict |
|------|------|-----------|---------|
| 4a | -- | Domain specializations table present | PASS / FAIL |
| 4b | [F] | COLUMN-HEADER compliance -- column headers domain-specific | PASS / FAIL |
| 4c | -- | At least 3 domain-specific rows present | PASS / FAIL |

Fix any FAIL before proceeding to Phase 5.

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST have been gated at their respective phases. Confirm each is resolved:

```
[A] Path correctness: .craft/roles/{area}/{subrole}.md confirmed? ___
[B] FIELD-REGISTER compliance -- frontmatter completeness -- confirmed Gate 3a? ___
[C] FIELD-REGISTER compliance -- orientation.frame -- confirmed Gate 3b? ___
[D] FIELD-REGISTER compliance -- orientation.serves -- confirmed Gate 3c? ___
[E] FIELD-REGISTER compliance -- lens.verify -- confirmed Gate 3d? ___
[F] COLUMN-HEADER compliance -- body table -- confirmed Gate 4b? ___
[G] INPUT-ROUTING-RULES compliance -- confirmed Gate 0? ___
[H] If inertia-advocate generated: INERTIA-ADVOCATE-TEMPLATE compliance -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.craft/roles/{area}/inertia-advocate.md`
2. Main role: `.craft/roles/{area}/{subrole}.md`

Confirm both paths in output.

---

### V-05: Full Ceiling (R8 V-05 Reproduced)

**Axis:** R9 ceiling. R8 V-05 carried forward without modification. All 16 criteria pass. The checklist format declaration is present in the AUDIT-CHECKLIST header; no preamble, no structural summaries, no inline explanatory asides exist anywhere in the skill. Rule content appears only in CONTRACT blocks, phase citation lines, and checklist items.

**Hypothesis:** 100. No criterion fails. V-01 through V-04 explore structural variants; V-05 is the proven canonical form. If any R9 variant scores lower than expected, V-05 isolates the cause: any criterion that V-05 passes but another variation fails is attributable to that variation's structural change.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.craft/roles/`.

---

### CONTRACTS

The following contracts define all key invariants for this skill. All phases reference these by name. Rules are stated once, here, authoritatively.

---

#### CONTRACT: INPUT-ROUTING-RULES

Apply before mode detection. Classify the input:

| Pattern | Classification | Action |
|---------|---------------|--------|
| Single word, no colon | BARE AREA | Ask "Which subrole in `{area}`? Provide `{area}:{subrole}` or a description." Stop. |
| More than one `:` | EXTRA COLONS | Use first two tokens as area:subrole. Notify user. Continue. |
| Natural language, no colon, no quotes, <= 4 words | VAGUE PHRASE | Ask "Did you mean `area:subrole`, a description in quotes, or interactive mode?" Stop. |
| No argument | EMPTY | Route to INTERACTIVE. Continue. |
| `word:word`, quoted string, or confirmed EMPTY | CLEAN INPUT | Continue to mode detection. |

---

#### CONTRACT: INTERACTIVE-HOLD

These are categorical prohibitions, not preferences:
- **Do not generate any content after receiving only one or two answers.**
- **Do not produce a draft, stub, or partial frontmatter mid-conversation.**
- **Do not proceed until all three answers are confirmed.**

Three required questions, in sequence:
1. "What area? (e.g., `backend`, `design`, `data`)"
2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
3. "One sentence describing what this role focuses on."

---

#### CONTRACT: FIELD-REGISTER

| Field | Register | Good Example | Anti-Pattern |
|-------|----------|-------------|-------------|
| archetype | Check existing roles in the area first; use their value | Found `craft` in 3 existing backend roles -> use `craft` | Applying `craft` or `process` without checking |
| orientation.frame | First-person observational: how this role perceives its domain | "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval." | "Reviews healthcare data compliance for the team." |
| orientation.serves | Third-person recipient: who benefits and why; must name a specific beneficiary | "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review." | "Serves the team by ensuring compliance." |
| lens.verify | Boolean check naming specific artifact, state, or config; answerable yes/no; >= 4 items | "Is the audit log retention period set to >= 6 years for PHI access events?" | "Check audit log configuration." |
| expertise.depth | Specific domain knowledge | "HIPAA Security Rule requirements for PHI at rest and in transit, BAA obligations, breach notification timelines" | "Broad understanding of healthcare compliance" |

---

#### CONTRACT: COLUMN-HEADER

Body table column headers must use domain vocabulary.

| Verdict | Example |
|---------|---------|
| FAIL | `| Component | Purpose | Notes |` |
| FAIL | `| Item | Description | Impact |` |
| FAIL | `| Area | Value | Consideration |` |
| PASS | `| Regulation / Scope / Enforcement Body |` (compliance) |
| PASS | `| API Surface / Side Effect / Auth Requirement |` (backend) |
| PASS | `| Data Source / Latency Class / SLA |` (data) |
| PASS | `| GL Account / Journal Entry Type / Impact |` (finance) |
| PASS | `| Asset Type / Accessibility Rule / WCAG Level |` (design) |

Rule: generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

---

#### CONTRACT: INERTIA-ADVOCATE-TEMPLATE

Complete fill-in template. Substitute all `{area}` slots. Do not leave literal `{area}` in the written file.

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

| Change Type | Switching Cost | Rollback Path | Verdict |
|-------------|----------------|---------------|---------|
| [domain-specific change type] | [hours or effort] | [rollback description] | Hold / Proceed |
```

---

#### CONTRACT: AUDIT-CHECKLIST

Pre-declared obligations. Declaration names which gate executes each item (forward); each gate cites back to the declaration ID it validates (backward). Fully bidirectional. Items name the CONTRACT block and validation scope only -- no rule enumeration.

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Path correctness -- `.craft/roles/{area}/{subrole}.md` | Phase 6 setup |
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

Apply CONTRACT: INPUT-ROUTING-RULES.

If input is BARE AREA or VAGUE PHRASE: ask the clarifying question from the contract. Do not proceed to Phase 1 until the user responds with a clean input.

-> **Gate 0 [G]:** CONTRACT: INPUT-ROUTING-RULES applied. Input classified as clean or resolved. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

- **NAME-ONLY** (`area:subrole`): extract area and subrole. Proceed.
- **DESCRIPTION** (quoted string): derive area and subrole. Proceed.
- **INTERACTIVE** (empty / confirmed EMPTY from Phase 0): apply CONTRACT: INTERACTIVE-HOLD. Ask three questions in sequence. Proceed only when all three are answered.

-> **Gate 1:** area and subrole known and non-empty (or all three interactive answers confirmed). PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

Check whether `.craft/roles/{area}/inertia-advocate.md` exists.

- **ABSENT:** Apply CONTRACT: INERTIA-ADVOCATE-TEMPLATE. Generate companion file content. Substitute all `{area}` slots. Store in working memory. Do not write yet.

  -> **Gate 2a [H]:** Companion file content generated with no literal `{area}` remaining. PASS / FAIL
  -> **Gate 2b:** Companion file path confirmed as `.craft/roles/{area}/inertia-advocate.md`. PASS / FAIL

  Fix any gate before proceeding.

- **PRESENT:** Continue to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Generate YAML frontmatter for `.craft/roles/{area}/{subrole}.md`. All 12 fields required. Apply CONTRACT: FIELD-REGISTER.

-> **Gate 3a [B]:** All 12 fields present in the generated frontmatter. PASS / FAIL
-> **Gate 3b [C]:** orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational). PASS / FAIL
-> **Gate 3c [D]:** orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary). PASS / FAIL
-> **Gate 3d [E]:** Each lens.verify item passes CONTRACT: FIELD-REGISTER (specific artifact/state/config); minimum 4 items. PASS / FAIL
-> **Gate 3e:** No placeholder text remains in the generated frontmatter. PASS / FAIL

Fix any gate before proceeding to Phase 4.

---

#### PHASE 4 -- Generate Body

Write the markdown body: `## {Subrole} Domain` heading + domain specializations table. Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.

-> **Gate 4a:** Body contains a domain specializations table. PASS / FAIL
-> **Gate 4b [F]:** Column headers pass CONTRACT: COLUMN-HEADER (no generic terms). PASS / FAIL
-> **Gate 4c:** Table contains at least 3 domain-specific rows. PASS / FAIL

Fix any gate before proceeding to Phase 5.

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST have been gated at their respective phases. Confirm each is resolved:

```
[A] Path correctness: .craft/roles/{area}/{subrole}.md confirmed? ___
[B] FIELD-REGISTER compliance -- frontmatter completeness -- confirmed Gate 3a? ___
[C] FIELD-REGISTER compliance -- orientation.frame -- confirmed Gate 3b? ___
[D] FIELD-REGISTER compliance -- orientation.serves -- confirmed Gate 3c? ___
[E] FIELD-REGISTER compliance -- lens.verify -- confirmed Gate 3d? ___
[F] COLUMN-HEADER compliance -- body table -- confirmed Gate 4b? ___
[G] INPUT-ROUTING-RULES compliance -- confirmed Gate 0? ___
[H] If inertia-advocate generated: INERTIA-ADVOCATE-TEMPLATE compliance -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.craft/roles/{area}/inertia-advocate.md`
2. Main role: `.craft/roles/{area}/{subrole}.md`

Confirm both paths in output.

---

## Estimated Score Matrix (v8 rubric)

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | Est. |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01 Declarative Register | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 100 |
| V-02 Compact Phases | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 100 |
| V-03 Front-Loaded Inertia | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 100 |
| V-04 Tabular Gate Blocks | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 100 |
| V-05 Full Ceiling | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 100 |

_Scoring: Essential 5 @ 12pt = 60, Recommended 2 @ 15pt = 30, Aspirational 16 @ 0.625pt = 10. Total max = 100._

_All 5 variations: 16/16 aspirational = 10.00 + 90.00 = 100._

_R9 prediction: All 5 score 100. Structural diversity (register, compaction, CONTRACT ordering, gate format) does not break any of the 16 criteria. The criteria govern coverage, content, and bidirectionality -- not phrasing style, ordering, or presentation format of gate annotations._

_Discrimination question: If any variation fails unexpectedly, the failure isolates the boundary of the criterion. V-02 probes whether C-15 requires gate annotation text (not just gate placement). V-04 probes whether C-18 requires inline [ID] suffixes (not table-column [ID] references). V-03 probes whether C-21 is order-sensitive (it should not be). V-01 probes whether C-19 "thin CONTRACT citation" is register-specific (it should not be)._
