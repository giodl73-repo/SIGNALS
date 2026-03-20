Written to `simulations/quest/variations/rhythm-track-variations-R1-2026-03-20.md`.

---

## Summary

**5 variations, 3 single-axis then 2 combined:**

| # | Axis | Hypothesis |
|---|------|-----------|
| **V-01** | Output format — table-based verification | Column structure prevents row skipping; blank cells are visually obvious failures |
| **V-02** | Lifecycle emphasis — pre-flight gates + reconciliation step | Forces MODULE.md gate to block empty tables; reconciliation step eliminates P1 count mismatches mechanically |
| **V-03** | Phrasing register — conversational auditor voice | Question-answer framing may produce richer reasoning traces; risk is verbosity without accuracy gain |
| **V-04** | Output format + Lifecycle emphasis | Combines table columns (structural defense) with reconciliation step (procedural defense) — widest coverage of the known failure modes |
| **V-05** | Role sequence + Formal register — two-pass Mapper/Skeptic | Adversarial second pass challenges SATISFIED verdicts via three specific probes (silent divergence, citation-without-use, terminology drift) — targets P1 violations that single-pass normalizes away |

The most promising candidates for scoring are **V-04** (targets the two most common mechanical failures directly) and **V-05** (targets the harder failure of missed P1s). V-01 and V-02 are the cleanest single-axis tests to isolate which intervention carries the most weight.


Extract and state explicitly:
1. The paper list in dependency order (P01, P01b, P02, ...)
2. The paper-to-paper dependency edges (P02 depends on P01b, etc.)
3. The structural results each dependency carries (formulas, definitions, quantities, mechanisms)

**Gate**: If MODULE.md yields zero dependency edges, stop and output: "TRACK INCOMPLETE — no dependency annotations found in MODULE.md. Cannot proceed."

---

### PHASE 2 — DEPENDENCY MAP

Build the dependency table. Every edge from Phase 1 becomes one row.

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|
| D-01 | ...  | ...| ...            | Definition / Structural / Empirical / Causal |

Transfer type definitions:
- **Definition**: a term, formula, or notation that all later papers must use verbatim
- **Structural**: a mathematical framework that constrains how later papers set up their formalism
- **Empirical**: a measured or computed number that later papers treat as a known quantity
- **Causal**: a mechanism or explanation that later papers extend or apply

Do not proceed to Phase 3 until every dependency edge has a row.

---

### PHASE 3 — VERIFICATION TABLE

For every D-ID row in Phase 2, fill one row of the verification table. No row may be skipped. If a paper cannot be read, mark every cell "UNREADABLE" and set Verdict to VIOLATED.

| D-ID | Cited in target? | Correct form? | Modification justified? | Verdict | Gap description |
|------|-----------------|---------------|------------------------|---------|-----------------|
| D-01 | YES / NO / IMPLICITLY | YES / NO / MODIFIED: [describe] | YES / NO / N/A | SATISFIED / PARTIAL / VIOLATED | — or exact description |
| D-02 | ... | ... | ... | ... | ... |

Column rules:
- **Cited in target?** — YES if the source paper is named; IMPLICITLY if the result is used but the source is not named; NO if neither.
- **Correct form?** — YES if the transferred item appears as-is; MODIFIED if it appears in an altered form (describe the alteration); NO if it is absent.
- **Modification justified?** — YES if the paper explains why the form changed; NO if it does not; N/A if Correct form? = YES.
- **Verdict** — SATISFIED: cited and used correctly. PARTIAL: used but not cited, or modified without justification. VIOLATED: absent or contradicted.
- **Gap description** — required for PARTIAL and VIOLATED; must name the specific section where the gap appears.

IMPLICIT citation note: If Cited = IMPLICITLY, add a one-sentence note on whether implicit use is sufficient for a reviewer or whether an explicit citation is needed.

---

### PHASE 4 — DEPENDENCY REGISTER

Summarize with severity labels. Derive directly from Phase 3 — no new judgments here.

| D-ID | Verdict | Severity | What needs to change |
|------|---------|----------|---------------------|
| D-01 | SATISFIED | — | — |
| D-02 | PARTIAL | P2 | [exact fix, naming section] |
| D-03 | VIOLATED | P1 | [exact fix, naming section] |

Severity rules:
- P1: A later paper contradicts or ignores a structural result — breaks the track's causal chain
- P2: A dependency is used but not cited, or used in an undeclared modified form
- P3: Dependency is cited but integration could be more explicit

Count your P1 rows now. This count must appear verbatim in Phase 5 and in the artifact frontmatter.

---

### PHASE 5 — TRACK HEALTH

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]
P1 violations: [n]   <- must equal the count of P1 rows in Phase 4
P2 gaps: [n]
P3 notes: [n]
Track integrity: SOUND / PARTIAL / BROKEN

Integrity rules (apply strictly):
  BROKEN  = at least one P1 violation
  PARTIAL = zero P1, at least one P2
  SOUND   = zero P1, zero P2

Critical path to next submission:
  [List D-IDs that must be resolved before the next paper in the track can be submitted]
  [State "none" only when P1 violations = 0 and P2 gaps = 0]
```

---

### PHASE 6 — AMEND

Three targeted fixes, in severity order:

**Fix 1 (P1):** [Name the paper, name the section, state the exact change]
**Fix 2 (P2):** [Name the paper, name the section, state the exact change]
**Fix 3 (P3):** [Name the paper, name the section, state the exact change]

Each fix must be actionable by a co-author without reading this report — if they can't make the change from Fix 1 alone, the fix is too generic.

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter required: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-02 — Lifecycle Emphasis: Hard Gates and Pre-Flight Checks

**Axis**: Lifecycle emphasis — add explicit pre-flight gates at Phase 1 and Phase 3 that halt forward progress if inputs are insufficient, and add a reconciliation step between Phase 4 and Phase 5 to force the P1 count to match.

**Hypothesis**: The P1 count mismatch failure mode happens because Phase 5 is written after Phase 4 without recounting. A mandatory reconciliation step — "recount P1 rows before writing Phase 5" — eliminates this mechanically.

---

You are running /rhythm-track for: {{topic}}

Verify the dependency chain across papers in a research track. Read MODULE.md and the individual papers. Check whether each paper correctly references and uses the structural results it depends on.

---

### PHASE 1 — MODULE SCAN (pre-flight)

**Step 1.1 — Read MODULE.md** for {{topic}}.

**Step 1.2 — Extract**:
- Paper list in order
- Dependency edges (which paper depends on which, and what it depends on)
- Structural results in each edge (formulas, definitions, quantities, mechanisms that must transfer)

**Step 1.3 — Pre-flight check**:
- [ ] MODULE.md was found and read
- [ ] At least one dependency edge was found
- [ ] Each edge has a named structural result (not just "uses P01")

If any box cannot be checked, output the reason and stop. Do not fabricate a dependency table from assumptions.

---

### PHASE 2 — DEPENDENCY MAP

For each edge from Phase 1, produce one row:

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|

Transfer types: Definition / Structural / Empirical / Causal (see original definitions).

After completing the table, count the rows and record: **Total dependencies: [n]**

---

### PHASE 3 — DEPENDENCY VERIFICATION

For every D-ID, read the target paper and produce a verification block. No block may be omitted.

**Pre-phase check**: Confirm you have the count from Phase 2. You must produce exactly that many blocks.

```
D-[NN]: [From] -> [To]: [what transfers]
Target paper: [title or filename]
  Cited?             YES / NO / IMPLICITLY
  Correct form?      YES / NO / MODIFIED: [describe]
  Mod. justified?    YES / NO / N/A
  Verdict:           SATISFIED / PARTIAL / VIOLATED
  Gap (if any):      [exact section and what is wrong]
  Implicit note:     [if IMPLICITLY: is implicit use sufficient for a reviewer?]
```

After all blocks are written, count: **Blocks written: [n]** — must equal Total dependencies from Phase 2.

---

### PHASE 4 — DEPENDENCY REGISTER

Transfer verdicts and severity from Phase 3 into a summary table:

| D-ID | Verdict | Severity | Required change |
|------|---------|----------|----------------|

Severity: P1 (structural break), P2 (citation/form gap), P3 (integration note)

**Reconciliation step — do this before Phase 5**:
- Recount every P1 row in this table: **P1 count = [n]**
- Recount every P2 row: **P2 count = [n]**
- These exact numbers go into Phase 5 and the artifact frontmatter.

---

### PHASE 5 — TRACK HEALTH

Using the reconciled counts from Phase 4:

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]  <- must equal Phase 2 row count
P1 violations: [n]        <- must equal Phase 4 P1 recount
P2 gaps: [n]              <- must equal Phase 4 P2 recount
Track integrity: SOUND / PARTIAL / BROKEN

Integrity derivation (show your work):
  P1 violations = [n] -> [BROKEN if >0, else continue]
  P2 gaps = [n]       -> [PARTIAL if >0 and P1=0, else SOUND]
  Result: [SOUND / PARTIAL / BROKEN]

Critical path to next submission:
  D-IDs blocking submission: [list or "none"]
```

---

### PHASE 6 — AMEND

Three targeted fixes in priority order. Each fix must name: (a) the paper, (b) the section, (c) the exact change.

1. [P1 fix — the violation that breaks the track]
2. [P2 fix — the gap a reviewer will notice]
3. [P3 fix — the integration improvement]

If P1 violations = 0, Fix 1 addresses the highest-severity P2 gap. State this explicitly.

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-03 — Phrasing Register: Conversational Auditor Voice

**Axis**: Phrasing register — rewrite in a conversational auditor voice, as if the skill is walking through a checklist with a co-author, asking questions and reporting findings. Imperative commands become direct questions with expected answers.

**Hypothesis**: A question-answer framing may produce more thorough reasoning traces because the model is prompted to answer each question explicitly rather than fill in a template. The risk is that output becomes verbose without improving accuracy.

---

You are running /rhythm-track for: {{topic}}

You are auditing the dependency chain of a research track. Your job is to answer one central question: *Does each paper actually use the structural results it claims to depend on?* Walk through it systematically.

---

### Step 1 — What does the track look like?

Read MODULE.md for {{topic}}.

Answer these questions from what you read:
- What papers are in this track, and in what order?
- Which paper depends on which? What does each dependency carry?
- What are the specific structural results — formulas, definitions, quantities, mechanisms — that must transfer from one paper to another?

If MODULE.md doesn't give you enough to answer these questions, say so and stop. Don't guess at dependencies that aren't documented.

---

### Step 2 — Map the dependencies

For each dependency edge you found, write a row in this table:

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|

Transfer type options: Definition (term/formula must be used verbatim), Structural (mathematical framework constrains later formalism), Empirical (number treated as known), Causal (mechanism extended or applied).

---

### Step 3 — Check each dependency

For every row in Step 2, go read the target paper and answer:

*For D-[NN]: [From] → [To], carrying [what transfers]:*

- Does the target paper cite the source? (YES — named explicitly / IMPLICITLY — uses the result but doesn't name it / NO — neither)
  - If IMPLICITLY: would a reviewer expect an explicit citation here, or is implicit use acceptable?
- Does it use the result in the correct form? (YES / MODIFIED — describe how / NO — absent)
  - If MODIFIED: does the paper explain why it changed the form? (YES / NO / NOT ADDRESSED)
- Given all of the above: SATISFIED, PARTIAL, or VIOLATED?
  - If PARTIAL or VIOLATED: what exactly is wrong, and in which section?

Work through every D-ID. Do not skip any.

---

### Step 4 — What did you find?

Summarize the findings in a register:

| D-ID | Verdict | Severity | What needs to change |
|------|---------|----------|---------------------|

Severity: P1 (a later paper contradicts or ignores a structural result — the track's causal chain breaks), P2 (used but not cited, or modified without disclosure — reviewers will notice), P3 (cited but could be better integrated)

Before moving on: count your P1 rows. Write the number here. You'll need it again.

---

### Step 5 — How is the track doing?

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]
P1 violations: [n]    <- use the count from Step 4
P2 gaps: [n]
Track integrity: SOUND / PARTIAL / BROKEN
  (BROKEN if any P1; PARTIAL if P2 but no P1; SOUND if neither)

What must be fixed before the next paper in the track can be submitted?
  [List the D-IDs, or "nothing — track is ready"]
```

---

### Step 6 — What should the team do?

Give three targeted fixes, most urgent first:

1. **[Highest severity]** In [paper], section [§X.Y]: [exactly what to change]
2. **[Next]** In [paper], section [§X.Y]: [exactly what to change]
3. **[Next]** In [paper], section [§X.Y]: [exactly what to change]

Each fix should be specific enough that a co-author can act on it without reading this report first.

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-04 — Combined: Table-First + Hard Gates

**Axes**: Output format (table-based verification) + Lifecycle emphasis (pre-flight gates, reconciliation step).

**Hypothesis**: The two most mechanical failure modes — empty tables and P1 count mismatches — require both structural (table columns force decisions) and procedural (reconciliation step forces recounting) defenses. Combining them addresses the widest set of failure modes simultaneously.

---

You are running /rhythm-track for: {{topic}}

Audit the dependency chain across papers in a research track. Read MODULE.md and the individual papers. For each paper-to-paper dependency, verify whether the structural result actually transfers correctly.

---

### PHASE 1 — MODULE SCAN

Read MODULE.md for {{topic}}.

Extract:
- Paper list in dependency order
- Dependency edges (source paper, target paper, what the target depends on)
- Structural results per edge: specific formulas, definitions, quantities, or mechanisms that must appear in the target paper

**Pre-flight gate**:

| Check | Status |
|-------|--------|
| MODULE.md found and read | PASS / FAIL |
| At least one dependency edge found | PASS / FAIL |
| Each edge has a named structural result | PASS / FAIL |

If any check is FAIL: state the reason and stop. The table will be empty if MODULE.md has no dependency annotations — say so rather than fabricating rows.

---

### PHASE 2 — DEPENDENCY MAP

One row per dependency edge. Complete all cells before proceeding.

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|
| D-01 | | | | Definition / Structural / Empirical / Causal |

**Row count checkpoint**: Total dependency rows = [n]. This number is used to verify Phase 3 completeness.

Transfer types:
- Definition: a term or formula used verbatim in all downstream papers
- Structural: a mathematical framework that constrains later papers' formalism
- Empirical: a number treated as a known quantity in later papers
- Causal: a mechanism that later papers extend, apply, or challenge

---

### PHASE 3 — VERIFICATION TABLE

Fill one row per D-ID. The row count must equal the Phase 2 checkpoint.

| D-ID | Cited in target? | Correct form? | Mod. justified? | Verdict | Gap (section + description) | Implicit note |
|------|-----------------|---------------|-----------------|---------|----------------------------|---------------|
| D-01 | YES/NO/IMPLICITLY | YES/NO/MODIFIED:[desc] | YES/NO/N/A | SATISFIED/PARTIAL/VIOLATED | — | [if IMPLICITLY: sufficient for reviewers?] |

Column rules:
- **Cited in target?**: YES = source paper named; IMPLICITLY = result used, source not named; NO = absent
- **Correct form?**: YES = as-is; MODIFIED = describe the alteration; NO = absent
- **Mod. justified?**: YES = paper explains the change; NO = undeclared; N/A = not modified
- **Verdict**: SATISFIED (cited + correct), PARTIAL (used but uncited OR modified without disclosure), VIOLATED (absent or contradicted)
- **Gap**: required text for PARTIAL and VIOLATED — must name the section

**Completeness check**: Count rows filled = [n]. Must equal Phase 2 row count.

---

### PHASE 4 — DEPENDENCY REGISTER

Derived directly from Phase 3. No new judgments.

| D-ID | Verdict | Severity | Required change |
|------|---------|----------|----------------|

Severity: P1 (structural break), P2 (citation/form gap), P3 (integration note)

**Reconciliation (required before Phase 5)**:

| Metric | Count |
|--------|-------|
| P1 rows in this table | [n] |
| P2 rows in this table | [n] |
| P3 rows in this table | [n] |

Copy these exact numbers into Phase 5 and the frontmatter. Do not recount.

---

### PHASE 5 — TRACK HEALTH

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]    <- Phase 2 row count
P1 violations: [n]          <- Phase 4 reconciliation P1 count
P2 gaps: [n]                <- Phase 4 reconciliation P2 count
Track integrity: [derive below]

Integrity derivation:
  IF P1 violations > 0 THEN BROKEN
  ELSE IF P2 gaps > 0 THEN PARTIAL
  ELSE SOUND
  -> Track integrity: SOUND / PARTIAL / BROKEN

Critical path to next submission:
  D-IDs that must be resolved: [list or "none — track is ready"]
```

---

### PHASE 6 — AMEND

Three fixes, highest severity first. Each must include: paper name, section reference, exact change.

**Fix 1 (P1 or highest-severity P2 if P1 = 0)**:
In [paper], §[section]: [exact change — specific enough to act on without reading this report]

**Fix 2**:
In [paper], §[section]: [exact change]

**Fix 3**:
In [paper], §[section]: [exact change]

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN

---

## V-05 — Combined: Two-Pass (Mapper + Skeptic) + Formal Register

**Axes**: Role sequence (two-pass adversarial structure) + Phrasing register (formal/technical, third-person).

**Hypothesis**: A single-pass audit may miss P1 violations because the model becomes anchored to the author's framing. A second "skeptic" pass — specifically tasked with challenging every SATISFIED verdict and looking for contradictions — surfaces violations that the first pass normalized away. The formal register enforces rigor and prevents hedging.

---

You are running /rhythm-track for: {{topic}}

Execute a two-pass dependency audit. The first pass (Mapper) establishes the dependency structure and produces initial verdicts. The second pass (Skeptic) challenges every SATISFIED and PARTIAL verdict, looking for structural contradictions and silent divergences.

---

### PASS 1 — MAPPER

#### M-1: Module Scan

Read MODULE.md for {{topic}}. Extract:
- Ordered paper list
- Dependency edges (source, target, what transfers)
- Per-edge structural result: the specific formula, definition, quantity, or mechanism that must appear in the target paper

Prerequisite check: If MODULE.md contains no dependency annotations, output "AUDIT BLOCKED — no dependency structure documented" and halt.

#### M-2: Dependency Map

| D-ID | From | To | What transfers | Transfer type |
|------|------|----|----------------|---------------|

Transfer types: Definition / Structural / Empirical / Causal

#### M-3: Initial Verification

For each D-ID, read the target paper and produce a verification block:

```
D-[NN]: [From] -> [To]: [what transfers]
  Cited?          YES / NO / IMPLICITLY
  Correct form?   YES / NO / MODIFIED: [describe]
  Mod justified?  YES / NO / N/A
  Initial verdict: SATISFIED / PARTIAL / VIOLATED
  Evidence:       [quote or section reference from target paper]
```

#### M-4: Mapper Register

| D-ID | Initial verdict | Severity | Notes |
|------|----------------|----------|-------|

---

### PASS 2 — SKEPTIC

The Skeptic reads the Mapper's output and applies three challenges to every row.

**Challenge protocol** — apply to every D-ID, in order:

**Challenge A — Silent divergence**: Does the target paper's formalism produce results that are numerically or structurally inconsistent with the source paper's result, even if it appears to cite it correctly? Check whether the target paper's equations, when evaluated, would produce different outputs than the source paper's.

**Challenge B — Citation without use**: Is the source paper cited in the target paper's related work or introduction but absent from the sections where the structural result should actually appear?

**Challenge C — Terminology drift**: Does the target paper use different variable names, notation, or terminology for the same concept? If so, is the equivalence stated explicitly?

For each D-ID:

```
D-[NN] — Skeptic review:
  Challenge A (silent divergence): [finding or "none found"]
  Challenge B (citation without use): [finding or "none found"]
  Challenge C (terminology drift): [finding or "none found"]
  Revised verdict: SATISFIED / PARTIAL / VIOLATED
  Revision rationale: [why verdict changed, or "unchanged"]
```

---

### FINAL REGISTER

Produce the definitive register using Skeptic-revised verdicts. Where Mapper and Skeptic disagree, the Skeptic verdict stands.

| D-ID | Mapper verdict | Skeptic verdict | Final verdict | Severity | Required change |
|------|---------------|-----------------|---------------|----------|----------------|

Severity: P1 (structural break in causal chain), P2 (citation or form gap), P3 (integration note)

**P1 count**: [n] — record this number exactly.

---

### TRACK HEALTH

```
Track: {{topic}}
Papers checked: [n]
Dependencies mapped: [n]
P1 violations: [n]    <- Final Register P1 count
P2 gaps: [n]
Track integrity: SOUND / PARTIAL / BROKEN
  BROKEN  = P1 > 0
  PARTIAL = P1 = 0 and P2 > 0
  SOUND   = P1 = 0 and P2 = 0

Skeptic escalations (Mapper SATISFIED -> Skeptic VIOLATED/PARTIAL): [list D-IDs or "none"]

Critical path to next submission:
  [D-IDs blocking submission, or "none"]
```

---

### AMEND

Three targeted amendments, highest severity first. Each amendment must state: (1) paper, (2) section, (3) exact change required.

**Amendment 1**: [paper] §[section] — [exact change]
**Amendment 2**: [paper] §[section] — [exact change]
**Amendment 3**: [paper] §[section] — [exact change]

If an amendment requires coordinated changes across multiple papers (e.g., a P1 violation where both source and target must change), list all affected locations.

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path>: write flat into <path>/
Frontmatter: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN
