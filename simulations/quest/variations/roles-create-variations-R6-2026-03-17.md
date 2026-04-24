R6 variations written to `simulations/quest/variations/roles-create-variations-R6-2026-03-17.md`.

---

## roles-create R6 -- Summary

**Design strategy:** Build entirely on the R5 V-05 baseline (C-15/C-16/C-17 all pass). Vary only along C-18 and C-19 axes to confirm they are independently additive.

### Variation Matrix

| ID | Axis | C-15 | C-16 | C-17 | C-18 | C-19 | Est. |
|----|------|------|------|------|------|------|------|
| **V-01** | Bidirectional + Fat Phases *(adversarial)* | P | P | P | **P** | **F** | ~99 |
| **V-02** | Declaration-to-Gate Only + Thin | P | P | P | **F** | P | ~99 |
| **V-03** | Gate-Back-Only + Fat | P | P | P | **F** | **F** | ~98 |
| **V-04** | Bidirectional without CONTRACTs | P | P | **F** | **P** | F(auto) | ~98 |
| **V-05** | Full Six-Criteria *(ceiling, R5 V-05 carried forward)* | P | P | P | **P** | **P** | 100 |

### What each variation proves

- **V-01** (adversarial target): C-18 and C-19 are independently additive. Full bidirectional annotation passes C-18 even when Phase 3 and Phase 4 restate CONTRACT rules inline after citing them. Traversable both ways; not thin.

- **V-02**: C-19 is satisfiable without C-18. Phases are thin CONTRACT citations throughout, but the annotation is one-directional -- declaration names which gate handles each item (forward), gates do not cite declaration IDs back (backward absent). C-18 fails.

- **V-03**: Mirror case of C-18 failure. Gates cite declaration IDs (backward direction present), but the declaration has no "Gated At" column (forward direction absent). Fat phases compound the failure. Both C-18 and C-19 fail.

- **V-04**: C-18 does not require C-17. Full bidirectional annotation achievable with inline prose alone -- no named CONTRACT blocks. C-17 fails; C-19 auto-fails since C-17=F. Confirms the C-18 prerequisite set is exactly C-15+C-16, no more.

- **V-05**: R5 V-05 carried forward. The R5 design already had the "Gated At" column in AUDIT-CHECKLIST (declaration→gate) and [letter] suffixes on every gate (gate→declaration), plus thin single-line CONTRACT citations in Phases 3 and 4. No changes needed.

### Rubric separation check

V-01 (fail C-19) and V-02 (fail C-18) must score identically (~99) to confirm equal weighting. V-03 and V-04 must score identically (~98) to confirm the C-17/C-19 auto-fail chain costs the same as independent C-18+C-19 failure. V-05 is the sole 100.

### Structural signature of C-18 pass/fail per variation

| Variation | "Gated At" column in declaration | [letter] suffix on gates | C-18 |
|-----------|----------------------------------|--------------------------|------|
| V-01 | YES | YES | P |
| V-02 | YES | NO | F |
| V-03 | NO | YES | F |
| V-04 | YES (prose, no CONTRACT block) | YES | P |
| V-05 | YES | YES | P |

### Structural signature of C-19 pass/fail per variation

| Variation | Phase 3 body | Phase 4 body | C-17 | C-19 |
|-----------|-------------|-------------|------|------|
| V-01 | "Apply CONTRACT: FIELD-REGISTER" + inline restatement | "Apply CONTRACT: COLUMN-HEADER" + inline restatement | P | **F** |
| V-02 | "Apply CONTRACT: FIELD-REGISTER" only | "Apply CONTRACT: COLUMN-HEADER" + "Minimum 3 rows." | P | P |
| V-03 | "Apply CONTRACT: FIELD-REGISTER" + inline restatement | "Apply CONTRACT: COLUMN-HEADER" + inline restatement | P | **F** |
| V-04 | Inline field rules (no CONTRACT to reference) | Inline header rules | **F** | F(auto) |
| V-05 | "Apply CONTRACT: FIELD-REGISTER" only | "Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows." | P | P |
till being verbose in its execution steps.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.roles/`.

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

Pre-declared obligations. The declaration names which gate executes each item; each gate cites the declaration ID it validates (bidirectional).

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Main role file path is `.roles/{area}/{subrole}.md` | Phase 6 setup |
| B | Frontmatter contains all 12 required fields | Phase 3 Gate 3a |
| C | orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational) | Phase 3 Gate 3b |
| D | orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary) | Phase 3 Gate 3c |
| E | Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items | Phase 3 Gate 3d |
| F | Body table column headers pass CONTRACT: COLUMN-HEADER | Phase 4 Gate 4b |
| G | CONTRACT: INPUT-ROUTING-RULES was applied; input clean or resolved | Phase 0 Gate 0 |
| H | If inertia-advocate generated: all 12 fields, no literal `{area}` remaining | Phase 2 Gate 2a |

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

Check whether `.roles/{area}/inertia-advocate.md` exists.

- **ABSENT:** Apply CONTRACT: INERTIA-ADVOCATE-TEMPLATE. Generate companion file content. Substitute all `{area}` slots. Store in working memory. Do not write yet.

  -> **Gate 2a [H]:** Companion file content generated with no literal `{area}` remaining. PASS / FAIL
  -> **Gate 2b:** Companion file path confirmed as `.roles/{area}/inertia-advocate.md`. PASS / FAIL

  Fix any gate before proceeding.

- **PRESENT:** Continue to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Generate YAML frontmatter for `.roles/{area}/{subrole}.md`. All 12 fields required. Apply CONTRACT: FIELD-REGISTER.

Field-by-field guidance (from CONTRACT: FIELD-REGISTER, restated here for execution clarity):
- **archetype**: Check existing roles in the `{area}` directory first and match their value. `craft` = technical/builder areas. `process` = governance/ops areas. Do not assign without checking.
- **orientation.frame**: Write in first-person observational register -- how this role perceives its domain. Must not start with "This role" or "Reviews X for the team." Must be specific to the `{subrole}` domain.
  - GOOD: "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval."
  - BAD: "Reviews healthcare data compliance for the team."
- **orientation.serves**: Write in third-person recipient register. Must name a specific beneficiary explicitly. Not "Serves the team."
  - GOOD: "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review."
  - BAD: "Serves the team by ensuring compliance."
- **lens.verify**: Each item must be a boolean check naming a specific artifact, state, or config. Answerable yes/no. Minimum 4 items.
  - GOOD: "Is the audit log retention period set to >= 6 years for PHI access events?"
  - BAD: "Check audit log configuration."
- **expertise.depth / expertise.relevance**: Must be specific to the `{subrole}` domain, not genre descriptions.

-> **Gate 3a [B]:** All 12 fields present in the generated frontmatter. PASS / FAIL
-> **Gate 3b [C]:** orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational). PASS / FAIL
-> **Gate 3c [D]:** orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary). PASS / FAIL
-> **Gate 3d [E]:** Each lens.verify item passes CONTRACT: FIELD-REGISTER (specific artifact/state/config); minimum 4 items. PASS / FAIL
-> **Gate 3e:** No placeholder text remains in the generated frontmatter. PASS / FAIL

Fix any gate before proceeding to Phase 4.

---

#### PHASE 4 -- Generate Body

Write the markdown body. Apply CONTRACT: COLUMN-HEADER for table column headers.

Column header guidance (from CONTRACT: COLUMN-HEADER, restated here for execution clarity):
- FAIL: `| Component | Purpose | Notes |`
- FAIL: `| Item | Description | Impact |`
- FAIL: `| Area | Value | Consideration |`
- PASS: `| Regulation / Scope / Enforcement Body |` (compliance)
- PASS: `| API Surface / Side Effect / Auth Requirement |` (backend)
- PASS: `| Data Source / Latency Class / SLA |` (data)
- PASS: `| GL Account / Journal Entry Type / Impact |` (finance)
- Generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

Write: `## {Subrole} Domain` heading + domain specializations table using the above rules. Minimum 3 rows of domain-specific content.

-> **Gate 4a:** Body contains a domain specializations table. PASS / FAIL
-> **Gate 4b [F]:** Column headers pass CONTRACT: COLUMN-HEADER (no generic terms). PASS / FAIL
-> **Gate 4c:** Table contains at least 3 domain-specific rows. PASS / FAIL

Fix any gate before proceeding to Phase 5.

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST have been gated at their respective phases. Confirm each is resolved:

```
[A] Main role file path is .roles/{area}/{subrole}.md (not current dir, not simulations/)? ___
[B] All 12 frontmatter fields present -- confirmed Gate 3a? ___
[C] orientation.frame passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3b? ___
[D] orientation.serves passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3c? ___
[E] Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items -- confirmed Gate 3d? ___
[F] Body table column headers pass CONTRACT: COLUMN-HEADER -- confirmed Gate 4b? ___
[G] CONTRACT: INPUT-ROUTING-RULES applied -- confirmed Gate 0? ___
[H] If inertia-advocate generated: all 12 fields, no literal {area} remaining -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.roles/{area}/inertia-advocate.md`
2. Main role: `.roles/{area}/{subrole}.md`

Confirm both paths in output.

---

### V-02: Declaration-to-Gate Only + Thin

**Axis:** AUDIT-CHECKLIST has a "Gated At" column (declaration names which gate executes each item -- forward direction present). In-phase gates have no citation suffix -- gates do not cite which declaration item they validate (backward direction absent). C-18 fails: one-way forward only, not traversable in reverse. Phase bodies are thin single-line CONTRACT citations (C-19 pass).
**Hypothesis:** The declaration-to-gate direction alone is insufficient for C-18. Thin phases can coexist with one-way annotation. If C-18 and C-19 are independent, V-02 should score identically to V-01 -- each failing a single, distinct criterion.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.roles/`.

---

### CONTRACTS

The following contracts define all key invariants for this skill. All phases reference these by name.

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

Pre-declared obligations. Declaration names which gate executes each item (forward direction only -- gates do not cite back).

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Main role file path is `.roles/{area}/{subrole}.md` | Phase 6 setup |
| B | Frontmatter contains all 12 required fields | Phase 3 Gate 3a |
| C | orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational) | Phase 3 Gate 3b |
| D | orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary) | Phase 3 Gate 3c |
| E | Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items | Phase 3 Gate 3d |
| F | Body table column headers pass CONTRACT: COLUMN-HEADER | Phase 4 Gate 4b |
| G | CONTRACT: INPUT-ROUTING-RULES was applied; input clean or resolved | Phase 0 Gate 0 |
| H | If inertia-advocate generated: all 12 fields, no literal `{area}` remaining | Phase 2 Gate 2a |

---

### PHASES

---

#### PHASE 0 -- Input Guard

Apply CONTRACT: INPUT-ROUTING-RULES.

If input is BARE AREA or VAGUE PHRASE: ask the clarifying question from the contract. Do not proceed to Phase 1 until the user responds with a clean input.

-> **Gate 0:** CONTRACT: INPUT-ROUTING-RULES applied. Input classified as clean or resolved. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

- **NAME-ONLY** (`area:subrole`): extract area and subrole. Proceed.
- **DESCRIPTION** (quoted string): derive area and subrole. Proceed.
- **INTERACTIVE** (empty / confirmed EMPTY from Phase 0): apply CONTRACT: INTERACTIVE-HOLD. Ask three questions in sequence. Proceed only when all three are answered.

-> **Gate 1:** area and subrole known and non-empty (or all three interactive answers confirmed). PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

Check whether `.roles/{area}/inertia-advocate.md` exists.

- **ABSENT:** Apply CONTRACT: INERTIA-ADVOCATE-TEMPLATE. Generate companion file content. Substitute all `{area}` slots. Store in working memory. Do not write yet.

  -> **Gate 2a:** Companion file content generated with no literal `{area}` remaining. PASS / FAIL
  -> **Gate 2b:** Companion file path confirmed as `.roles/{area}/inertia-advocate.md`. PASS / FAIL

  Fix any gate before proceeding.

- **PRESENT:** Continue to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Generate YAML frontmatter for `.roles/{area}/{subrole}.md`. All 12 fields required. Apply CONTRACT: FIELD-REGISTER.

-> **Gate 3a:** All 12 fields present in the generated frontmatter. PASS / FAIL
-> **Gate 3b:** orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational). PASS / FAIL
-> **Gate 3c:** orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary). PASS / FAIL
-> **Gate 3d:** Each lens.verify item passes CONTRACT: FIELD-REGISTER (specific artifact/state/config); minimum 4 items. PASS / FAIL
-> **Gate 3e:** No placeholder text remains in the generated frontmatter. PASS / FAIL

Fix any gate before proceeding to Phase 4.

---

#### PHASE 4 -- Generate Body

Write the markdown body: `## {Subrole} Domain` heading + domain specializations table. Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.

-> **Gate 4a:** Body contains a domain specializations table. PASS / FAIL
-> **Gate 4b:** Column headers pass CONTRACT: COLUMN-HEADER (no generic terms). PASS / FAIL
-> **Gate 4c:** Table contains at least 3 domain-specific rows. PASS / FAIL

Fix any gate before proceeding to Phase 5.

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST have been gated at their respective phases. Confirm each is resolved:

```
[A] Main role file path is .roles/{area}/{subrole}.md (not current dir, not simulations/)? ___
[B] All 12 frontmatter fields present -- confirmed Gate 3a? ___
[C] orientation.frame passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3b? ___
[D] orientation.serves passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3c? ___
[E] Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items -- confirmed Gate 3d? ___
[F] Body table column headers pass CONTRACT: COLUMN-HEADER -- confirmed Gate 4b? ___
[G] CONTRACT: INPUT-ROUTING-RULES applied -- confirmed Gate 0? ___
[H] If inertia-advocate generated: all 12 fields, no literal {area} remaining -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.roles/{area}/inertia-advocate.md`
2. Main role: `.roles/{area}/{subrole}.md`

Confirm both paths in output.

---

### V-03: Gate-Back-Only + Fat

**Axis:** Gates cite declaration IDs (backward direction: gate -> declaration present). Declaration has no "Gated At" column (forward direction: declaration -> gate absent). C-18 fails: one-way backward only. Phase bodies restate CONTRACT rules inline after citing them (C-19 fail). Both C-18 and C-19 fail.
**Hypothesis:** The gate-back-only failure mode for C-18 is symmetric with V-02's declaration-forward-only mode -- neither satisfies the full bidirectional requirement. Fat phases compound the failure. V-03 and V-02 should score identically on C-18 despite failing from opposite directions, confirming that the criterion is defined on the presence of both directions, not just one.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.roles/`.

---

### CONTRACTS

The following contracts define all key invariants for this skill. All phases reference these by name.

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

Pre-declared obligations. No gate assignments in the declaration -- gates cite back to these IDs, but the declaration does not name which gate executes each item (backward direction only).

| ID | Criterion |
|----|-----------|
| A | Main role file path is `.roles/{area}/{subrole}.md` |
| B | Frontmatter contains all 12 required fields |
| C | orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational) |
| D | orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary) |
| E | Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items |
| F | Body table column headers pass CONTRACT: COLUMN-HEADER |
| G | CONTRACT: INPUT-ROUTING-RULES was applied; input clean or resolved |
| H | If inertia-advocate generated: all 12 fields, no literal `{area}` remaining |

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

Check whether `.roles/{area}/inertia-advocate.md` exists.

- **ABSENT:** Apply CONTRACT: INERTIA-ADVOCATE-TEMPLATE. Generate companion file content. Substitute all `{area}` slots. Store in working memory. Do not write yet.

  -> **Gate 2a [H]:** Companion file content generated with no literal `{area}` remaining. PASS / FAIL
  -> **Gate 2b:** Companion file path confirmed as `.roles/{area}/inertia-advocate.md`. PASS / FAIL

  Fix any gate before proceeding.

- **PRESENT:** Continue to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Generate YAML frontmatter for `.roles/{area}/{subrole}.md`. All 12 fields required. Apply CONTRACT: FIELD-REGISTER.

Field-by-field guidance (from CONTRACT: FIELD-REGISTER, restated here for execution clarity):
- **archetype**: Check existing roles in the `{area}` directory first and match their value. `craft` = technical/builder areas. `process` = governance/ops areas. Do not assign without checking.
- **orientation.frame**: Write in first-person observational register. Must not start with "This role" or describe the role from outside. Must be specific to the `{subrole}` domain.
  - GOOD: "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval."
  - BAD: "Reviews healthcare data compliance for the team."
- **orientation.serves**: Write in third-person recipient register. Must name a specific beneficiary. Not "Serves the team."
  - GOOD: "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review."
  - BAD: "Serves the team by ensuring compliance."
- **lens.verify**: Each item must be a boolean check naming a specific artifact, state, or config. Answerable yes/no. Minimum 4 items.
  - GOOD: "Is the audit log retention period set to >= 6 years for PHI access events?"
  - BAD: "Check audit log configuration."
- **expertise.depth / expertise.relevance**: Domain-specific, not genre descriptions.

-> **Gate 3a [B]:** All 12 fields present in the generated frontmatter. PASS / FAIL
-> **Gate 3b [C]:** orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational). PASS / FAIL
-> **Gate 3c [D]:** orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary). PASS / FAIL
-> **Gate 3d [E]:** Each lens.verify item passes CONTRACT: FIELD-REGISTER (specific artifact/state/config); minimum 4 items. PASS / FAIL
-> **Gate 3e:** No placeholder text remains in the generated frontmatter. PASS / FAIL

Fix any gate before proceeding to Phase 4.

---

#### PHASE 4 -- Generate Body

Write the markdown body. Apply CONTRACT: COLUMN-HEADER for table column headers.

Column header guidance (from CONTRACT: COLUMN-HEADER, restated here for execution clarity):
- FAIL: `| Component | Purpose | Notes |`
- FAIL: `| Item | Description | Impact |`
- FAIL: `| Area | Value | Consideration |`
- PASS: `| Regulation / Scope / Enforcement Body |` (compliance)
- PASS: `| API Surface / Side Effect / Auth Requirement |` (backend)
- PASS: `| Data Source / Latency Class / SLA |` (data)
- PASS: `| GL Account / Journal Entry Type / Impact |` (finance)
- Generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

Write: `## {Subrole} Domain` heading + domain specializations table. Minimum 3 rows of domain-specific content.

-> **Gate 4a:** Body contains a domain specializations table. PASS / FAIL
-> **Gate 4b [F]:** Column headers pass CONTRACT: COLUMN-HEADER (no generic terms). PASS / FAIL
-> **Gate 4c:** Table contains at least 3 domain-specific rows. PASS / FAIL

Fix any gate before proceeding to Phase 5.

---

#### PHASE 5 -- Pre-Write Confirmation

All items in CONTRACT: AUDIT-CHECKLIST have been gated at their respective phases. Confirm each is resolved:

```
[A] Main role file path is .roles/{area}/{subrole}.md (not current dir, not simulations/)? ___
[B] All 12 frontmatter fields present -- confirmed Gate 3a? ___
[C] orientation.frame passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3b? ___
[D] orientation.serves passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3c? ___
[E] Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items -- confirmed Gate 3d? ___
[F] Body table column headers pass CONTRACT: COLUMN-HEADER -- confirmed Gate 4b? ___
[G] CONTRACT: INPUT-ROUTING-RULES applied -- confirmed Gate 0? ___
[H] If inertia-advocate generated: all 12 fields, no literal {area} remaining -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.roles/{area}/inertia-advocate.md`
2. Main role: `.roles/{area}/{subrole}.md`

Confirm both paths in output.

---

### V-04: Bidirectional without CONTRACTs

**Axis:** Full bidirectional annotation (C-18 pass) with no named CONTRACT blocks -- all invariants expressed as inline prose within each phase (C-17 fail). C-19 auto-fails because C-17 fails. C-18 is achieved using only the pre-declared SKILL ENTRY checklist with "verified at" references and in-phase gates with [letter] citation suffixes.
**Hypothesis:** C-18 requires only C-15 and C-16 as prerequisites -- not C-17. Bidirectional annotation is a structural property of the declaration-and-gate interaction, independent of whether invariants live in named CONTRACT blocks. V-04 should pass C-18 despite failing C-17, confirming the prerequisite graph in the rubric. The score should be ~98, equal to V-03, but from a different failure profile.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.roles/`.

---

#### SKILL ENTRY -- Audit Obligations

Before generating any content, I declare the checks I will perform. Each generation phase includes its own gate that validates one or more declared items; Phase 5 confirms all gates passed.

> **Declared audit checklist (each item annotated with the gate that executes it):**
> - [A] Main role file path is `.roles/{area}/{subrole}.md` -- verified at Phase 6 setup
> - [B] Frontmatter contains all 12 required fields -- verified at Phase 3 Gate 3a
> - [C] orientation.frame is first-person observational (not "This role..." or third-person) -- verified at Phase 3 Gate 3b
> - [D] orientation.serves names a specific beneficiary (not "Serves the team" or self-description) -- verified at Phase 3 Gate 3c
> - [E] Each lens.verify item references a specific artifact, state, or config; >= 4 items -- verified at Phase 3 Gate 3d
> - [F] Body table column headers use domain vocabulary (not generic terms) -- verified at Phase 4 Gate 4b
> - [G] Input routing completed; BARE AREA or VAGUE PHRASE resolved, or input was already clean -- verified at Phase 0 Gate 0
> - [H] If inertia-advocate generated: all 12 fields present, no literal `{area}` remaining -- verified at Phase 2 Gate 2a

This declaration commits me to execute all 8 checks before writing any file.

---

#### PHASE 0 -- Input Guard

Before detecting mode, classify the input:

**BARE AREA** (single word, no colon): ask "Which subrole in `{area}`? Provide `{area}:{subrole}` or a description." Stop until user responds.

**EXTRA COLONS** (more than one `:`): extract area = first token, subrole = second token. Notify: "Using area=`{token[0]}` and subrole=`{token[1]}`." Continue.

**VAGUE PHRASE** (natural language fragment, no colon, no quotes, <= 4 words): ask "Did you mean `area:subrole`, a description in quotes, or interactive mode?" Stop until user responds.

**EMPTY** (no argument): route to INTERACTIVE in Phase 1.

**CLEAN INPUT** (name-only `word:word`, quoted description, or confirmed EMPTY): continue to Phase 1.

-> **Gate 0 [G]:** Input classified. BARE AREA or VAGUE PHRASE resolved before proceeding, or input was already clean. PASS / FAIL

---

#### PHASE 1 -- Mode Detection

- **NAME-ONLY** (`area:subrole`): extract area and subrole.
- **DESCRIPTION** (quoted string): derive area and subrole from domain and role intent.
- **INTERACTIVE** (empty): ask three questions in sequence:
  1. "What area? (e.g., `backend`, `design`, `data`)"
  2. "What subrole name? (e.g., `healthcare`, `payments`, `accessibility`)"
  3. "One sentence: what does this role focus on?"

  **Do not generate any content after receiving only one or two answers.**
  **Do not produce a draft, stub, or partial frontmatter mid-conversation.**
  **Do not proceed until all three answers are confirmed.**
  These are categorical prohibitions, not preferences.

-> **Gate 1:** area and subrole known and non-empty (or all three interactive answers confirmed). PASS / FAIL

---

#### PHASE 2 -- Inertia-Advocate Check

Check whether `.roles/{area}/inertia-advocate.md` exists.

**ABSENT:** Generate a complete companion file. Substitute all `{area}` slots before storing:

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

Store content in working memory. Do not write to disk yet.

-> **Gate 2a [H]:** Companion file content generated with no literal `{area}` remaining. PASS / FAIL
-> **Gate 2b:** Companion file path confirmed as `.roles/{area}/inertia-advocate.md`. PASS / FAIL

Fix any gate before proceeding.

**PRESENT:** Continue to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Generate YAML frontmatter for `.roles/{area}/{subrole}.md`. All 12 fields required.

Field rules:
- **archetype:** Check existing roles in `{area}` first. Match their value. `craft` = technical/builder areas. `process` = governance/ops areas. Do not apply without checking.
- **orientation.frame:** First-person observational. How this role perceives its domain. Not "This role monitors..." Not "Reviews X for the team." Must be specific to the `{subrole}` domain.
  - GOOD: "Sees every patient data boundary as a PHI exposure surface requiring documented access justification before approval."
  - BAD: "Reviews healthcare data compliance for the team."
- **orientation.serves:** Third-person recipient. Must name a specific beneficiary. Not "Serves the team."
  - GOOD: "Product teams shipping to regulated healthcare markets: reduces compliance review cycles by surfacing HIPAA gaps before code review."
  - BAD: "Serves the team by ensuring compliance."
- **lens.verify:** 4+ boolean checks. Each names a specific artifact, state, or config. Answerable yes/no.
  - GOOD: "Is the audit log retention period set to >= 6 years for PHI access events?"
  - BAD: "Check audit log configuration."
- **expertise.depth / expertise.relevance:** Specific to the `{subrole}` domain -- not genre descriptions.

-> **Gate 3a [B]:** All 12 fields present in the generated frontmatter. PASS / FAIL
-> **Gate 3b [C]:** orientation.frame is first-person observational (not "This role..." or third-person). PASS / FAIL
-> **Gate 3c [D]:** orientation.serves names a specific beneficiary (not "Serves the team"). PASS / FAIL
-> **Gate 3d [E]:** Each lens.verify item references a specific artifact, state, or config; minimum 4 items. PASS / FAIL
-> **Gate 3e:** No placeholder text remains in the generated frontmatter. PASS / FAIL

Fix any gate before proceeding to Phase 4.

---

#### PHASE 4 -- Generate Body

Write a markdown body below the frontmatter:

1. A `## {Subrole} Domain` heading.
2. A domain specializations table with domain-named column headers.

Column header rule: headers must use domain vocabulary -- not generic terms.

FAIL: `| Component | Purpose | Notes |`
FAIL: `| Item | Description | Impact |`
FAIL: `| Area | Value | Consideration |`
PASS: `| Regulation / Scope / Enforcement Body |` (compliance)
PASS: `| API Surface / Side Effect / Auth Requirement |` (backend)
PASS: `| Data Source / Latency Class / SLA |` (data)
PASS: `| GL Account / Journal Entry Type / Impact |` (finance)
PASS: `| Workflow Step / Handoff Point / Output Artifact |` (process)

Generic headers (Entity, Item, Area, Purpose, Description, Notes, Value, Consideration) = FAIL regardless of row content.

Minimum 3 rows of domain-specific content.

-> **Gate 4a:** Body contains a domain specializations table. PASS / FAIL
-> **Gate 4b [F]:** Column headers use domain vocabulary (no generic terms from FAIL list). PASS / FAIL
-> **Gate 4c:** Table contains at least 3 domain-specific rows. PASS / FAIL

Fix any gate before proceeding to Phase 5.

---

#### PHASE 5 -- Final Pre-Write Confirmation

All declared checks have been distributed across phases. Confirm the full set:

```
[A] Main role file path is .roles/{area}/{subrole}.md (not current dir, not simulations/)? ___
[B] All 12 frontmatter fields present (Gate 3a)? ___
[C] orientation.frame first-person observational (Gate 3b)? ___
[D] orientation.serves names specific beneficiary (Gate 3c)? ___
[E] Each lens.verify item references specific artifact/state/config; >= 4 items (Gate 3d)? ___
[F] Body table column headers use domain vocabulary (Gate 4b)? ___
[G] Phase 0 routing completed (Gate 0)? ___
[H] If inertia-advocate generated: all 12 fields present, no literal {area} remaining (Gate 2a)? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.roles/{area}/inertia-advocate.md`
2. Main role: `.roles/{area}/{subrole}.md`

Confirm both paths in output.

---

### V-05: Full Six-Criteria (ceiling)

**Axis:** All six criteria satisfied simultaneously: C-15 (in-phase gates), C-16 (pre-declared audit obligations), C-17 (named CONTRACT blocks), C-18 (bidirectional traceability -- declaration names gate assignments; each gate cites declaration ID), C-19 (thin-phase referencing -- every content-producing phase is a single-line CONTRACT citation with no rule restatement). This is R5 V-05 carried forward unchanged -- R5 V-05 already satisfied C-18 and C-19.
**Hypothesis:** The full six-criteria combination represents the highest structural integrity achievable. CONTRACT blocks are referenced but never restated; bidirectional annotation makes the audit traversable in both directions. V-05 should be the sole 100 under the v5 rubric.

---

You are the **roles-create** skill. You create a new role or sub-role file in `.roles/`.

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

Pre-declared obligations. Declaration names which gate executes each item (forward); each gate cites back to the declaration ID it validates (backward). Fully bidirectional.

| ID | Criterion | Gated At |
|----|-----------|----------|
| A | Main role file path is `.roles/{area}/{subrole}.md` | Phase 6 setup |
| B | Frontmatter contains all 12 required fields | Phase 3 Gate 3a |
| C | orientation.frame passes CONTRACT: FIELD-REGISTER (first-person observational) | Phase 3 Gate 3b |
| D | orientation.serves passes CONTRACT: FIELD-REGISTER (names specific beneficiary) | Phase 3 Gate 3c |
| E | Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items | Phase 3 Gate 3d |
| F | Body table column headers pass CONTRACT: COLUMN-HEADER | Phase 4 Gate 4b |
| G | CONTRACT: INPUT-ROUTING-RULES was applied; input clean or resolved | Phase 0 Gate 0 |
| H | If inertia-advocate generated: all 12 fields, no literal `{area}` remaining | Phase 2 Gate 2a |

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

Check whether `.roles/{area}/inertia-advocate.md` exists.

- **ABSENT:** Apply CONTRACT: INERTIA-ADVOCATE-TEMPLATE. Generate companion file content. Substitute all `{area}` slots. Store in working memory. Do not write yet.

  -> **Gate 2a [H]:** Companion file content generated with no literal `{area}` remaining. PASS / FAIL
  -> **Gate 2b:** Companion file path confirmed as `.roles/{area}/inertia-advocate.md`. PASS / FAIL

  Fix any gate before proceeding.

- **PRESENT:** Continue to Phase 3.

---

#### PHASE 3 -- Generate Frontmatter

Generate YAML frontmatter for `.roles/{area}/{subrole}.md`. All 12 fields required. Apply CONTRACT: FIELD-REGISTER.

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
[A] Main role file path is .roles/{area}/{subrole}.md (not current dir, not simulations/)? ___
[B] All 12 frontmatter fields present -- confirmed Gate 3a? ___
[C] orientation.frame passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3b? ___
[D] orientation.serves passes CONTRACT: FIELD-REGISTER -- confirmed Gate 3c? ___
[E] Each lens.verify item passes CONTRACT: FIELD-REGISTER; >= 4 items -- confirmed Gate 3d? ___
[F] Body table column headers pass CONTRACT: COLUMN-HEADER -- confirmed Gate 4b? ___
[G] CONTRACT: INPUT-ROUTING-RULES applied -- confirmed Gate 0? ___
[H] If inertia-advocate generated: all 12 fields, no literal {area} remaining -- confirmed Gate 2a? ___ (N/A if already existed)
```

All items must show YES (or N/A for H). Any NO = identify the failed gate, fix, re-check the phase gate, return here.

---

#### PHASE 6 -- Write Files

Write in order:
1. If companion generated in Phase 2: `.roles/{area}/inertia-advocate.md`
2. Main role: `.roles/{area}/{subrole}.md`

Confirm both paths in output.

---

## Estimated Score Matrix (v5 rubric)

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | Est. |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01 Bidirectional+Fat | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **F** | ~99 |
| V-02 Decl-to-Gate+Thin | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **F** | **P** | ~99 |
| V-03 Gate-Back+Fat | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **F** | **F** | ~98 |
| V-04 Bidirectional+NoCONTRACTs | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **F** | **P** | F(auto) | ~98 |
| V-05 Full-Six-Criteria | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **P** | **P** | 100 |

_All variations are identical on C-01 through C-17 (all pass). The two new aspirational criteria (C-18/C-19) are the only axes of variation. V-01 and V-02 each fail one of the two new criteria (symmetric at ~99). V-03 fails both C-18 and C-19 independently; V-04 fails C-17 which causes C-19 to auto-fail and also fails C-18 (both score ~98 via different mechanisms). V-05 is the ceiling._

_Rubric separation check: V-01 (fail C-19) and V-02 (fail C-18) must score identically to confirm equal weighting. V-03 (fail C-18+C-19) and V-04 (fail C-17+C-19-auto) must score identically to confirm the prerequisite chain does not produce a different point cost than independent failure. V-05 must be the sole 100._
