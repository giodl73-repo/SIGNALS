---
skill: quest-variate
skill_target: org-build
round: 12
date: 2026-03-16
rubric_version: 8
---

# Variate R12 — org-build

5 complete prompt body variations for the `org-build` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (IA written first across all areas before any standard/specialized roles) | V-01, V-04 |
| Output format (scan-record-driven: flat record blocks as primary structure) | V-02, V-05 |
| Lifecycle emphasis (double-guard phase gates + strict entry conditions) | V-03, V-05 |
| Inertia framing (inertia assessment surface-up, templates pre-declared before any file written) | V-04 |
| Phrasing register (full technical imperative: MUST/FORBIDDEN throughout, no advisory language) | V-05 |

---

## V-01 — Role Sequence: Inertia-Advocate First

**Axis**: Role sequence
**Hypothesis**: Writing every inertia-advocate file across all areas before any standard or
specialized role eliminates C-03 failures by construction. Because the IA phase runs before any
other role file exists on disk, coverage cannot be silently lost to output pressure during
per-area role writing. Writing IA files while the inertia assessment (Phase 2) is still in
working memory also produces stronger C-11 / C-17 compliance: the scope template is freshly
resolved and applied verbatim. Risk: splitting IA writing from the rest of per-area role writing
adds a phase boundary and may complicate the VERIFY count at Phase 6.

---

You are running `org-build`. Scan the repo at the provided path, or auto-detect if no path is
given. If `--scan` is provided, read the named scan-results file instead of scanning directly.
The `--depth` flag is `standard` (default) or `deep`.

Work through phases in order. FORBIDDEN: beginning any phase before emitting that phase's
record block. FORBIDDEN: emitting a record block before completing all work in that phase.

---

### PHASE 1 — SCAN

**Entry condition**: repo path accessible, or scan-results file readable.

Scan the repo (or scan-results) to discover the organizational structure. Identify:
- Named areas, teams, or service domains visible in directory structure, CODEBASE.md,
  OWNERS files, or equivalent
- Existing `.craft/roles/` subdirectories (if any)
- Technology domains and discipline clusters
- Approximate team scale indicators (number of service owners, CODEBASE sections, etc.)

Bind the depth flag now:

```
T1-DEPTH-FLAG: [standard | deep]   <- from --depth flag; default is standard
```

MUST bind the role count floor to T1-DEPTH-FLAG in this phase instruction:
- T1-DEPTH-FLAG = standard → MUST enumerate 20–30 roles total across all areas
- T1-DEPTH-FLAG = deep     → MUST enumerate 50+ roles total across all areas

FORBIDDEN: stating a flat count range without binding it to T1-DEPTH-FLAG value.
FORBIDDEN: proceeding to Phase 2 before emitting the Phase 1 record block below.

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:   [standard | deep]
T1-ROLE-TARGET:  [20-30 | 50+]
T1-AREA-LIST:    [comma-separated area names discovered]
T1-AREA-COUNT:   [n]
T1-SOURCE:       [repo | scan-results]
T1-SCAN-NOTES:   [any gaps, ambiguities, or inferred areas]
===
```

---

### PHASE 2 — INERTIA ASSESSMENT

**Entry condition**: Phase 1 record block emitted. T1-AREA-COUNT and T1-AREA-LIST are the
binding inputs for this phase. FORBIDDEN: executing Phase 2 before Phase 1 record block
is emitted.

Assess the flat-case pressure for this org. Evaluate:

1. **Coordination surface**: How many cross-area dependencies exist? High dependency density
   raises pressure.
2. **Decision latency risk**: Can the areas in T1-AREA-LIST operate without a coordination
   layer? If two or more areas must synchronize weekly to ship, pressure is at least MODERATE.
3. **Span-of-control signal**: Does the scan reveal a single implicit owner spanning 4+ areas?
   Raises pressure toward ELEVATED.
4. **Scale signal**: Does headcount evidence suggest >15 people? Raises pressure.

FLAT-CASE-PRESSURE is a closed set: LOW | MODERATE | ELEVATED | HIGH.

T2-VERDICT is a closed set: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED.

Verdict derivation:
- LOW or MODERATE pressure → T2-VERDICT = CAN-OPERATE-FLAT
- ELEVATED or HIGH pressure → T2-VERDICT = STRUCTURE-WARRANTED

VERDICT GUARD: Only one verdict. FORBIDDEN: writing both CAN-OPERATE-FLAT and
STRUCTURE-WARRANTED. FORBIDDEN: omitting both and leaving verdict blank.

IA scope templates — apply verbatim based on T2-PRESSURE and T2-VERDICT:

> **LOW / CAN-OPERATE-FLAT**: "The inertia-advocate operates as a velocity-preservation
> check — the org is structurally sound; this role monitors for premature complexity. Scope:
> challenge every proposed coordination layer before it ossifies into permanent structure."

> **MODERATE / CAN-OPERATE-FLAT**: "The inertia-advocate operates as a coordination-cost
> sentinel — flat structure is viable but strained at current scale; this role tracks the point
> at which coordination cost exceeds hierarchy cost. Scope: own the threshold number and surface
> it before each headcount decision."

> **ELEVATED / STRUCTURE-WARRANTED**: "The inertia-advocate operates as a structural-change
> auditor — hierarchy is indicated but the inertia cost of introducing it must be paid
> explicitly; this role documents what the flat org did well and ensures the new structure
> preserves it. Scope: produce a cost-of-transition ledger before any structural change is
> ratified."

> **HIGH / STRUCTURE-WARRANTED**: "The inertia-advocate operates as a continuity guardian
> during structural transition — the org must add hierarchy and the risk is losing the
> coordination velocity of the flat phase; this role owns the handoff protocol between flat and
> structured operation. Scope: write the runbook that flat-era contributors will follow during
> the transition."

FORBIDDEN: paraphrasing or adapting the template text. The scope field in every IA file MUST
contain the exact template text for the applicable T2-PRESSURE / T2-VERDICT combination.

FORBIDDEN: beginning Phase 3 before emitting the Phase 2 record block below.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE:  [LOW | MODERATE | ELEVATED | HIGH]
T2-VERDICT:   [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-TEMPLATE-KEY: [LOW/CAN | MOD/CAN | ELE/STR | HIGH/STR]
T2-ANTI-PATTERN-REQUIRED:  [cat-3, cat-2 (if CAN-OPERATE-FLAT) | cat-1, cat-4 (if STRUCTURE-WARRANTED)]
T2-ANTI-PATTERN-FORBIDDEN: [cat-1, cat-4 (if CAN-OPERATE-FLAT) | cat-2, cat-3 (if STRUCTURE-WARRANTED)]
===
```

---

### PHASE 3 — WRITE INERTIA-ADVOCATE FILES (all areas, before any other role)

**Entry condition**: Phase 2 record block emitted. T2-VERDICT, T2-PRESSURE, T2-IA-TEMPLATE-KEY
are the binding inputs. FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.

For each area in T1-AREA-LIST, write the IA file before any other role file for that area.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five required fields — no placeholder text:

- **orientation**: Why a senior member of this area would defend the existing arrangement.
  Name the specific concern drawn from the area's technical context discovered in Phase 1.
- **lens**: Domain-specific status quo this advocate protects. MUST reference at least one
  term from the area's name or discovered context. No generic "stability" language.
- **expertise**: What makes this person's skepticism credible. Name the specific systems,
  processes, or decisions they have built or run in this area.
- **scope**: Apply the T2-IA-TEMPLATE-KEY template VERBATIM. Copy the exact template text.
  No paraphrase. No adaptation. The exact template text.
- **collaborates_with**: Which roles this advocate engages — name counterparts by role slug.
  Specify forum (design review, sprint planning, architecture board) and cadence.

MUST: lens and expertise MUST differ between areas. Two IA files with identical lens text is
a build error. Two IA files with identical expertise text is a build error.

After each IA file: `IA-WRITTEN: [area-slug] — lens: "[first 6 words of lens field]"`

FORBIDDEN: beginning Phase 4 before emitting the Phase 3 record block.

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-IA-FILES-WRITTEN:  [n]
T3-AREAS-COVERED:     [list area slugs]
T3-AREAS-MISSING:     [list any area from T1-AREA-LIST without an IA file, or "none"]
T3-SCOPE-TEMPLATE:    [confirmed: verbatim from T2-IA-TEMPLATE-KEY]
===
```

---

### PHASE 4 — WRITE REMAINING ROLE FILES

**Entry condition**: Phase 3 record block emitted. T1-DEPTH-FLAG, T1-ROLE-TARGET, T1-AREA-LIST,
T3-IA-FILES-WRITTEN are the binding inputs. FORBIDDEN: executing Phase 4 before Phase 3 record
block is emitted.

For each area in T1-AREA-LIST, write standard roles then specialized roles. IA files already
exist from Phase 3 — do not overwrite them.

Role count constraint (from T1-DEPTH-FLAG):
- T1-DEPTH-FLAG = standard → total files across all areas MUST be 20–30 (including IA files)
- T1-DEPTH-FLAG = deep     → total files across all areas MUST be 50+ (including IA files)

FORBIDDEN: writing fewer than the lower bound for the active T1-DEPTH-FLAG value.

**Standard role files** (roles that recur across multiple areas):

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Required fields:
- **orientation**: Perspective this role brings
- **lens**: Domain focus — specific aspect of system or product
- **expertise**: What this role knows that others do not
- **scope**: `standard`
- **collaborates_with**: Key counterpart role slugs and interaction mode

**Specialized role files** (roles unique to one area):

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Same five fields. scope MUST read: `specialized — {area-slug}`.

Standard vs specialized distinction MUST be explicit in the `scope` field — not derivable
only from directory placement.

After each area's roles are written (not counting IA, which already exists):
`AREA-WRITTEN: [area-slug] — [n] std + [n] spec. Running total (incl IA): [n].`

FORBIDDEN: beginning Phase 5 before emitting the Phase 4 record block.

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-TOTAL-ROLE-FILES:  [n]
T4-IA-COUNT:          [n from T3-IA-FILES-WRITTEN]
T4-STANDARD-COUNT:    [n]
T4-SPECIALIZED-COUNT: [n]
T4-COUNT-IN-RANGE:    [YES — {range} / NO — {actual} vs {required}]
T4-DEPTH-FLAG:        [T1-DEPTH-FLAG value confirmed]
===
```

---

### PHASE 5 — WRITE ORG-CHART.MD

**Entry condition**: Phase 4 record block emitted. T2-PRESSURE, T2-VERDICT,
T2-ANTI-PATTERN-REQUIRED, T2-ANTI-PATTERN-FORBIDDEN, T4-TOTAL-ROLE-FILES are the binding
inputs. FORBIDDEN: executing Phase 5 before Phase 4 record block is emitted.

Write `org-chart.md`. Sections in this exact order:

**5a. ASCII Org Diagram**

Draw the full hierarchy. Minimum two org levels. Use box-drawing characters (`+--`, `|`).
Each area node shows headcount in parentheses. Names must match Phase 1 discovery exactly.

**5b. Headcount by Area**

```markdown
## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [n] | [role slugs] | [what this area decides autonomously] | [what goes up] |
| **Total** | **[n]** | | | |
```

Decides: the class of decisions this area owns without escalation.
Escalates: the class of decisions that go to the next level. MUST be populated for every row.
A row with empty Decides or Escalates columns fails.

**5c. Level Distribution**

```markdown
## Level Distribution

| Level | Count | % of Org |
|-------|-------|----------|
| [label] | [n] | [n]% |
| **Total** | **[n]** | 100% |
```

Infer levels from role names if not explicit. Total MUST match headcount table Total.

**5d. Inertia Assessment**

```markdown
## Inertia Assessment

FLAT-CASE-PRESSURE: [T2-PRESSURE]
VERDICT: [T2-VERDICT]
```

MUST include both `FLAT-CASE-PRESSURE:` and `VERDICT:` lines with closed-set values.
FORBIDDEN: generic prose verdict without the labeled lines.

**5e. Operating Rhythm**

```markdown
## Operating Rhythm

| Cadence | Meeting | Owner | Output | Standing Attendees |
|---------|---------|-------|--------|-------------------|
| Weekly  | Shiproom | [owner role] | [artifact] | [roles] |
| Weekly  | ROB | [owner role] | [artifact] | [roles] |
| Quarterly | [Governance meeting] | [owner role] | [artifact] | [roles] |
```

MUST have 3+ distinct rows. MUST include Shiproom, ROB, and at least one governance meeting.

For each governance meeting row, append a committee charter block:

```markdown
### Charter: [Meeting Name]
- Purpose: [one sentence]
- Owner: [role slug]
- Quorum: [N of M] (e.g., "3 of 5")
- Inputs: [what artifacts are required before the meeting can run]
- Outputs: [what decisions or artifacts are produced]
```

MUST include all five charter fields including Quorum as an "N of M" fraction.
A Quorum expressed as a percentage or headcount only (not a fraction) fails.

**5f. Org Evolution Roadmap**

```markdown
## Org Evolution Roadmap

| Trigger | Type | Action |
|---------|------|--------|
| [headcount threshold] | headcount | [structural change] |
| [cross-team dependency metric] | coordination-cost | [structural change] |
```

MUST have 2+ rows. Row 1 MUST be a headcount threshold. Row 2 MUST be a different trigger
category (coordination-cost, decision-latency, span-of-control — not another headcount).
Two headcount threshold rows fails.

**5g. Anti-Pattern Watch**

```markdown
## Anti-Pattern Watch

| Pattern | Category | Why It Applies Here | Mitigation |
|---------|----------|---------------------|------------|
| [name] | cat-N | [element name] (cat-N) — [reason specific to this org] | [remediation action] |
| [name] | cat-N | [element name] (cat-N) — [reason specific to this org] | [remediation action] |
```

MUST include 2+ rows. Every "Why It Applies Here" cell MUST open with
`[element name] (cat-N) —` syntax. Plain prose without cat-N citation fails.

Category selection MUST derive from T2-VERDICT:
- T2-VERDICT = CAN-OPERATE-FLAT     → MUST include cat-3, cat-2. FORBIDDEN: cat-1, cat-4.
- T2-VERDICT = STRUCTURE-WARRANTED  → MUST include cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: Mitigation cells that describe column format or provide descriptive guidance
instead of an action. A cell reading "describe the mitigation here" fails.

FORBIDDEN: beginning Phase 6 before emitting the Phase 5 record block.

```
=== RECORD: PHASE-5 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 6 begins before this block is emitted.
T5-CHART-WRITTEN:       YES
T5-HEADCOUNT-TOTAL:     [n]
T5-INERTIA-VERDICT:     [T2-VERDICT confirmed]
T5-RHYTHM-ROWS:         [n]
T5-CHARTERS-WRITTEN:    [list governance meeting names]
T5-ROADMAP-ROWS:        [n]
T5-ANTIPATTERN-ROWS:    [n]
T5-ANTIPATTERN-CATS:    [categories used]
===
```

---

### PHASE 6 — VERIFY

**Entry condition**: Phase 5 record block emitted.
FORBIDDEN: executing Phase 6 before Phase 5 record block is emitted.

Verify:

```
VERIFY:
  T1-ROLE-TARGET:        [from Phase 1]
  T4-TOTAL-ROLE-FILES:   [from Phase 4]
  count-in-range:        [YES / NO]
  IA-coverage:           [n of n areas — from T3]
  scope-template-check:  [all IA files contain verbatim T2-IA-TEMPLATE-KEY text: YES / NO]
  chart-sections:        [list: diagram, headcount-table, level-dist, inertia, rhythm, roadmap, antipattern]
  quorum-fractions:      [all charter Quorum fields as N of M: YES / NO]
  verdict-guard:         [single verdict, neither blank: YES / NO]
```

If any check fails: `VERIFY-FAIL: [list failures].`
If all pass: `VERIFY-PASS: build consistent with rubric.`

```
BUILD-COMPLETE — org-build — {date}
  depth:               [T1-DEPTH-FLAG]
  areas:               [T1-AREA-COUNT]
  role files:          [T4-TOTAL-ROLE-FILES] / target [T1-ROLE-TARGET]
  IA coverage:         [n of n areas]
  org-chart.md:        written (7 sections)
  inertia verdict:     [T2-VERDICT]
  verify:              [PASS / FAIL]
```

---

## V-02 — Output Format: Scan-Record-Driven Flat Structure

**Axis**: Output format
**Hypothesis**: Eliminating nested sub-steps and prose setup in favor of flat, labeled record
blocks as the primary structural unit makes every gate variable visible in the output stream
without cross-referencing. Each phase produces exactly one record block; the next phase's
input contract declares exactly which field names it consumes. This format is the most
mechanically auditable for C-20 (all gate outputs named, all consuming phases declare input
contracts) and C-21 (each named gate variable is imperatively constrained in its consumer).
Risk: the flat format may feel sparse; models may pad with prose that obscures the record block
boundaries, weakening C-26 (record block as unifying artifact).

---

You are running `org-build`. Inputs: repo path or `--scan {file}`. Flag: `--depth [standard|deep]`.

FORBIDDEN: beginning any phase before emitting the prior phase's `=== RECORD: PHASE-N ===` block.
FORBIDDEN: emitting a record block before all work in that phase is complete.

---

### PHASE 1 — SCAN AND PLAN

Scan the input source. Discover all areas (named domains, service groups, ownership clusters).
Determine the depth flag.

**Depth-flag role count binding (MUST be stated here, in this phase):**
- T1-DEPTH-FLAG = `standard` → MUST generate 20–30 role files total
- T1-DEPTH-FLAG = `deep`     → MUST generate 50+ role files total

FORBIDDEN: deferring this binding to a later phase. FORBIDDEN: stating a count range without
its flag condition.

Emit the scan findings as inline observations before the record block:

```
SCAN-FINDINGS:
  areas-found:        [list]
  tech-domains:       [list]
  scale-signals:      [observations suggesting team size]
  existing-roles:     [list or "none found"]
```

Then emit:

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:        [standard | deep]
T1-ROLE-TARGET:       [20-30 | 50+]
T1-AREA-LIST:         [{area-slug}, {area-slug}, ...]
T1-AREA-COUNT:        [n]
T1-SOURCE:            [repo | scan-results]
===
```

---

### PHASE 2 — INERTIA ASSESSMENT

Input contract: consumes T1-AREA-LIST, T1-AREA-COUNT from Phase 1 record block.
FORBIDDEN: executing Phase 2 before Phase 1 `=== RECORD: PHASE-1 ===` is emitted.

Score the org on four pressure dimensions. Each dimension: LOW / MODERATE / ELEVATED / HIGH.

```
PRESSURE-SCORING:
  coordination-surface:  [rating] — [one-sentence evidence from Phase 1 scan]
  decision-latency-risk: [rating] — [one-sentence evidence]
  span-of-control:       [rating] — [one-sentence evidence]
  scale-indicator:       [rating] — [one-sentence evidence]
```

Derive composite T2-PRESSURE as the max of the four dimension scores.
Derive T2-VERDICT:
- T2-PRESSURE = LOW or MODERATE     → T2-VERDICT = CAN-OPERATE-FLAT
- T2-PRESSURE = ELEVATED or HIGH    → T2-VERDICT = STRUCTURE-WARRANTED

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

IA scope template — select by T2-PRESSURE + T2-VERDICT key and copy verbatim:

| Key | Template text |
|-----|--------------|
| LOW/CAN | "The inertia-advocate operates as a velocity-preservation check — the org is structurally sound; this role monitors for premature complexity. Scope: challenge every proposed coordination layer before it ossifies into permanent structure." |
| MOD/CAN | "The inertia-advocate operates as a coordination-cost sentinel — flat structure is viable but strained at current scale; this role tracks the point at which coordination cost exceeds hierarchy cost. Scope: own the threshold number and surface it before each headcount decision." |
| ELE/STR | "The inertia-advocate operates as a structural-change auditor — hierarchy is indicated but the inertia cost of introducing it must be paid explicitly; this role documents what the flat org did well and ensures the new structure preserves it. Scope: produce a cost-of-transition ledger before any structural change is ratified." |
| HIGH/STR | "The inertia-advocate operates as a continuity guardian during structural transition — the org must add hierarchy and the risk is losing the coordination velocity of the flat phase; this role owns the handoff protocol between flat and structured operation. Scope: write the runbook that flat-era contributors will follow during the transition." |

Anti-pattern category rule (derived from T2-VERDICT):
- CAN-OPERATE-FLAT:    MUST use cat-3, cat-2. FORBIDDEN: cat-1, cat-4.
- STRUCTURE-WARRANTED: MUST use cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE:             [LOW | MODERATE | ELEVATED | HIGH]
T2-VERDICT:              [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-TEMPLATE-KEY:      [LOW/CAN | MOD/CAN | ELE/STR | HIGH/STR]
T2-REQUIRED-CAT:         [cat-3,cat-2 | cat-1,cat-4]
T2-FORBIDDEN-CAT:        [cat-1,cat-4 | cat-2,cat-3]
===
```

---

### PHASE 3 — WRITE ROLE FILES

Input contract: consumes T1-AREA-LIST, T1-DEPTH-FLAG, T1-ROLE-TARGET, T2-VERDICT,
T2-IA-TEMPLATE-KEY from prior record blocks.
FORBIDDEN: executing Phase 3 before Phase 2 `=== RECORD: PHASE-2 ===` is emitted.

For each area in T1-AREA-LIST, write role files in this sequence per area:
1. inertia-advocate
2. standard roles
3. specialized roles

**Inertia-advocate**: path `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields — all required:
- **orientation**: Rational defense position drawn from area's technical context.
- **lens**: Area-specific status quo. MUST reference a term from the area's discovery context.
  No generic "stability" language.
- **expertise**: Systems, code paths, or operational processes this advocate has run.
  MUST differ from every other area's IA expertise text.
- **scope**: Copy the T2-IA-TEMPLATE-KEY template text VERBATIM. No changes. No paraphrase.
- **collaborates_with**: Counterpart role slugs; forum and cadence.

**Standard roles**: path `.craft/roles/{area-slug}/{role-slug}.md`

Five fields — orientation, lens, expertise, scope: `standard`, collaborates_with.

**Specialized roles**: path `.craft/roles/{area-slug}/{role-slug}.md`

Same five fields. scope MUST read `specialized — {area-slug}`.

Total role files MUST comply with T1-ROLE-TARGET:
- T1-DEPTH-FLAG = standard → MUST be 20–30 total. FORBIDDEN: fewer than 20.
- T1-DEPTH-FLAG = deep     → MUST be 50+ total. FORBIDDEN: fewer than 50.

After all areas: `ROLES-COMPLETE: [n] files written. T1-ROLE-TARGET=[T1-ROLE-TARGET]. In range: [YES/NO]`

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-TOTAL-FILES:       [n]
T3-IA-COUNT:          [n]
T3-STANDARD-COUNT:    [n]
T3-SPECIALIZED-COUNT: [n]
T3-TARGET-MET:        [YES | NO — actual: {n}, required: {T1-ROLE-TARGET}]
T3-SCOPE-VERBATIM:    [YES — all IA files use exact T2-IA-TEMPLATE-KEY text]
T3-LENS-UNIQUE:       [YES — all IA lens fields are distinct | NO — collisions: {list}]
===
```

---

### PHASE 4 — WRITE ORG-CHART.MD

Input contract: consumes T1-AREA-LIST, T1-AREA-COUNT, T2-PRESSURE, T2-VERDICT,
T2-REQUIRED-CAT, T2-FORBIDDEN-CAT, T3-TOTAL-FILES, T3-IA-COUNT from prior record blocks.
FORBIDDEN: executing Phase 4 before Phase 3 `=== RECORD: PHASE-3 ===` is emitted.

Write `org-chart.md`. All seven sections MUST be present.

**Section 1 — ASCII Diagram**

Minimum two org levels. Box-drawing characters (`+--`, `|`). Each area shows headcount.

**Section 2 — Headcount by Area**

```markdown
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [n] | [slugs] | [autonomous decision class] | [escalation class] |
| **Total** | **[n]** | | | |
```

Decides and Escalates MUST be populated for every row. Empty cells fail.

**Section 3 — Level Distribution**

```markdown
| Level | Count | % of Org |
|-------|-------|----------|
| [label] | [n] | [n]% |
| **Total** | **[n]** | 100% |
```

Total MUST equal headcount table Total.

**Section 4 — Inertia Assessment**

```markdown
FLAT-CASE-PRESSURE: [T2-PRESSURE]
VERDICT: [T2-VERDICT]
```

**Section 5 — Operating Rhythm**

```markdown
| Cadence | Meeting | Owner | Output | Standing Attendees |
|---------|---------|-------|--------|-------------------|
| Weekly  | ROB     | [role] | [artifact] | [roles] |
| Weekly  | Shiproom | [role] | [artifact] | [roles] |
| Quarterly | [Governance] | [role] | [artifact] | [roles] |
```

3+ rows. MUST include ROB, Shiproom, and at least one governance meeting.

For each governance meeting, write a charter block with exactly five fields:
Purpose, Owner, Quorum (as "N of M"), Inputs, Outputs.
FORBIDDEN: Quorum as percentage or bare number without "of M" denominator.

**Section 6 — Org Evolution Roadmap**

```markdown
| Trigger | Type | Action |
|---------|------|--------|
| [headcount number] | headcount | [structural change] |
| [metric description] | [coordination-cost|decision-latency|span-of-control] | [structural change] |
```

Row 1 MUST be headcount type. Row 2 MUST be a different type. Minimum 2 rows.

**Section 7 — Anti-Pattern Watch**

```markdown
| Pattern | Category | Why It Applies Here | Mitigation |
|---------|----------|---------------------|------------|
| [name] | [T2-REQUIRED-CAT[0]] | [element] (cat-N) — [org-specific reason] | [remediation action] |
| [name] | [T2-REQUIRED-CAT[1]] | [element] (cat-N) — [org-specific reason] | [remediation action] |
```

MUST use categories from T2-REQUIRED-CAT. FORBIDDEN: using categories in T2-FORBIDDEN-CAT.
Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
Every Mitigation cell MUST contain a remediation action, not format guidance.

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-WRITTEN:     YES
T4-SECTIONS-PRESENT:  [list all 7 section names]
T4-HEADCOUNT-TOTAL:   [n, must match T3-TOTAL-FILES]
T4-VERDICT-CONFIRMED: [T2-VERDICT]
T4-QUORUM-VALID:      [all charters have N-of-M quorum: YES/NO]
T4-ANTIPATTERN-CATS:  [cats used — must match T2-REQUIRED-CAT]
===
```

---

### PHASE 5 — VERIFY

Input contract: consumes all T1–T4 record block values.
FORBIDDEN: executing Phase 5 before Phase 4 `=== RECORD: PHASE-4 ===` is emitted.

```
VERIFY-CHECKS:
  role-count-in-range:   T3-TOTAL-FILES=[n], T1-ROLE-TARGET=[range] → [PASS/FAIL]
  ia-coverage:           T3-IA-COUNT=[n], T1-AREA-COUNT=[n] → [PASS/FAIL]
  scope-verbatim:        T3-SCOPE-VERBATIM → [PASS/FAIL]
  lens-unique:           T3-LENS-UNIQUE → [PASS/FAIL]
  headcount-consistent:  T4-HEADCOUNT-TOTAL=[n] == T3-TOTAL-FILES=[n] → [PASS/FAIL]
  sections-complete:     T4-SECTIONS-PRESENT contains all 7 → [PASS/FAIL]
  quorum-valid:          T4-QUORUM-VALID → [PASS/FAIL]
  verdict-single:        T4-VERDICT-CONFIRMED is one value → [PASS/FAIL]
```

`VERIFY: [PASS — all checks pass | FAIL — [list failed checks]]`

---

## V-03 — Lifecycle Emphasis: Strict Sequential Gates with Double-Guard

**Axis**: Lifecycle emphasis
**Hypothesis**: Every phase transition carries both an outbound FORBIDDEN at the gate
("FORBIDDEN: beginning Phase N+1 before emitting this record block") and an inbound FORBIDDEN
at the consuming phase's entry ("FORBIDDEN: executing Phase N+1 before Phase N record block
is emitted") — satisfying C-25 (bidirectional redundancy). The double-guard means a model that
skips either the outbound gate or the inbound check still encounters the other. Combined with
`PHASE-ORDERING-GUARD` as the first field inside every record block (C-28), this variation
maximizes C-23/C-24/C-25/C-26 coverage. Pairs well with a pre-print skeleton (C-22) placed
immediately before each record block as a fill-template. Risk: the most verbose variation;
output pressure may cause abbreviation of Phase 5 chart sections.

---

You are running `org-build`. Input: repo path or `--scan {file}`. Flag: `--depth [standard|deep]`.

**Global execution rules** (apply to all phases):
- MUST work through phases in order: 1 → 2 → 3 → 4 → 5 → 6.
- FORBIDDEN: skipping any phase.
- Every phase has an outbound FORBIDDEN at its end and an inbound FORBIDDEN at the start of
  the next phase. Both MUST be observed. Skipping either is a build error.

---

### PHASE 1 — SCAN

**Outbound rule**: FORBIDDEN: beginning Phase 2 before Phase 1 record block is emitted.

Scan the repo or scan-results. Identify areas, tech domains, and scale signals.

**Depth-flag count floor (declare here, bound to flag value):**
- T1-DEPTH-FLAG = `standard` → MUST write 20–30 role files total
- T1-DEPTH-FLAG = `deep`     → MUST write 50+ role files total

FORBIDDEN: writing a flat count range without its T1-DEPTH-FLAG condition attached.

Pre-print skeleton for Phase 1 record block:
```
T1-DEPTH-FLAG:   ___________
T1-ROLE-TARGET:  ___________
T1-AREA-LIST:    ___________
T1-AREA-COUNT:   ___________
T1-SOURCE:       ___________
```

Fill the skeleton and emit the record block:

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:   [standard | deep]
T1-ROLE-TARGET:  [20-30 | 50+]
T1-AREA-LIST:    [comma-separated]
T1-AREA-COUNT:   [n]
T1-SOURCE:       [repo | scan-results]
===
```

---

### PHASE 2 — INERTIA ASSESSMENT

**Inbound rule**: FORBIDDEN: executing Phase 2 before Phase 1 `=== RECORD: PHASE-1 ===` is
emitted. Consume T1-AREA-LIST, T1-AREA-COUNT.

**Outbound rule**: FORBIDDEN: beginning Phase 3 before Phase 2 record block is emitted.

Score each pressure dimension (coordination-surface, decision-latency-risk, span-of-control,
scale-indicator) as LOW / MODERATE / ELEVATED / HIGH. Composite T2-PRESSURE = max of four.

Derive T2-VERDICT:
- T2-PRESSURE LOW or MODERATE → CAN-OPERATE-FLAT
- T2-PRESSURE ELEVATED or HIGH → STRUCTURE-WARRANTED

VERDICT GUARD: FORBIDDEN: writing both verdicts. FORBIDDEN: writing neither verdict.
One verdict. "Only one verdict. Both is an error. Neither is an error."

IA scope templates (copy one verbatim into every IA scope field):

| Key | Template |
|-----|---------|
| LOW/CAN | "The inertia-advocate operates as a velocity-preservation check — the org is structurally sound; this role monitors for premature complexity. Scope: challenge every proposed coordination layer before it ossifies into permanent structure." |
| MOD/CAN | "The inertia-advocate operates as a coordination-cost sentinel — flat structure is viable but strained at current scale; this role tracks the point at which coordination cost exceeds hierarchy cost. Scope: own the threshold number and surface it before each headcount decision." |
| ELE/STR | "The inertia-advocate operates as a structural-change auditor — hierarchy is indicated but the inertia cost of introducing it must be paid explicitly; this role documents what the flat org did well and ensures the new structure preserves it. Scope: produce a cost-of-transition ledger before any structural change is ratified." |
| HIGH/STR | "The inertia-advocate operates as a continuity guardian during structural transition — the org must add hierarchy and the risk is losing the coordination velocity of the flat phase; this role owns the handoff protocol between flat and structured operation. Scope: write the runbook that flat-era contributors will follow during the transition." |

Anti-pattern category derivation from T2-VERDICT:
- CAN-OPERATE-FLAT     → MUST use cat-3, cat-2. FORBIDDEN: cat-1, cat-4.
- STRUCTURE-WARRANTED  → MUST use cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

Pre-print skeleton for Phase 2 record block:
```
T2-PRESSURE:             ___________
T2-VERDICT:              ___________
T2-IA-TEMPLATE-KEY:      ___________
T2-REQUIRED-CAT:         ___________
T2-FORBIDDEN-CAT:        ___________
```

Fill and emit:

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE:             [LOW | MODERATE | ELEVATED | HIGH]
T2-VERDICT:              [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-IA-TEMPLATE-KEY:      [LOW/CAN | MOD/CAN | ELE/STR | HIGH/STR]
T2-REQUIRED-CAT:         [cat-3,cat-2 | cat-1,cat-4]
T2-FORBIDDEN-CAT:        [cat-1,cat-4 | cat-2,cat-3]
===
```

---

### PHASE 3 — WRITE ROLE FILES

**Inbound rule**: FORBIDDEN: executing Phase 3 before Phase 2 `=== RECORD: PHASE-2 ===` is
emitted. Consume T1-AREA-LIST, T1-DEPTH-FLAG, T1-ROLE-TARGET, T2-VERDICT, T2-IA-TEMPLATE-KEY.

**Outbound rule**: FORBIDDEN: beginning Phase 4 before Phase 3 record block is emitted.

For each area in T1-AREA-LIST, write: inertia-advocate → standard roles → specialized roles.

**Inertia-advocate** (every area, no exceptions):

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields — all MUST be present:
- **orientation**: Rational defense of the area's status quo. Area-specific; no boilerplate.
- **lens**: Area-specific domain focus referencing at least one term from scan context.
- **expertise**: Specific systems or decisions this person has run. MUST differ per area.
- **scope**: MUST be verbatim copy of T2-IA-TEMPLATE-KEY template. No paraphrase.
- **collaborates_with**: Named counterpart role slugs with forum and cadence.

FORBIDDEN: two IA files sharing identical lens text.
FORBIDDEN: two IA files sharing identical expertise text.
FORBIDDEN: paraphrasing the T2-IA-TEMPLATE-KEY scope template.

**Standard roles**: scope = `standard`. Five fields.
**Specialized roles**: scope = `specialized — {area-slug}`. Five fields.

Total file count MUST comply with T1-DEPTH-FLAG:
- standard → 20–30 total files. FORBIDDEN: fewer than 20.
- deep     → 50+ total files. FORBIDDEN: fewer than 50.

Pre-print skeleton for Phase 3 record block:
```
T3-TOTAL-FILES:       ___________
T3-IA-COUNT:          ___________
T3-STANDARD-COUNT:    ___________
T3-SPECIALIZED-COUNT: ___________
T3-TARGET-MET:        ___________
T3-SCOPE-VERBATIM:    ___________
T3-LENS-UNIQUE:       ___________
```

Fill and emit:

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-TOTAL-FILES:       [n]
T3-IA-COUNT:          [n]
T3-STANDARD-COUNT:    [n]
T3-SPECIALIZED-COUNT: [n]
T3-TARGET-MET:        [YES | NO — actual: {n}, required: {T1-ROLE-TARGET}]
T3-SCOPE-VERBATIM:    [YES | NO — explain if NO]
T3-LENS-UNIQUE:       [YES | NO — list collisions if NO]
===
```

---

### PHASE 4 — WRITE ORG-CHART.MD

**Inbound rule**: FORBIDDEN: executing Phase 4 before Phase 3 `=== RECORD: PHASE-3 ===` is
emitted. Consume T1-AREA-LIST, T2-PRESSURE, T2-VERDICT, T2-REQUIRED-CAT, T2-FORBIDDEN-CAT,
T2-IA-TEMPLATE-KEY, T3-TOTAL-FILES.

**Outbound rule**: FORBIDDEN: beginning Phase 5 before Phase 4 record block is emitted.

Write `org-chart.md` with these seven sections (all MUST be present):

1. **ASCII Org Diagram** — min 2 levels, box-drawing characters, headcount in parens per area
2. **Headcount by Area** — columns: Area, Headcount, Key Roles, Decides, Escalates
   - Decides and Escalates MUST be populated. Empty cells fail.
3. **Level Distribution** — Level, Count, % of Org. Total MUST match headcount Total.
4. **Inertia Assessment** — `FLAT-CASE-PRESSURE: {T2-PRESSURE}` and `VERDICT: {T2-VERDICT}`
5. **Operating Rhythm** — 3+ rows: ROB, Shiproom, 1+ governance meetings
   - Each governance meeting: charter block with Purpose, Owner, Quorum (N of M), Inputs, Outputs
   - FORBIDDEN: Quorum without "of M" denominator
6. **Org Evolution Roadmap** — 2+ rows; Row 1: headcount type; Row 2: different type
7. **Anti-Pattern Watch** — 2+ rows; cats from T2-REQUIRED-CAT; FORBIDDEN T2-FORBIDDEN-CAT
   - "Why It Applies Here" MUST open with `[element name] (cat-N) —`
   - Mitigation MUST be a remediation action, not format guidance

Pre-print skeleton for Phase 4 record block:
```
T4-CHART-WRITTEN:     ___________
T4-SECTIONS-PRESENT:  ___________
T4-HEADCOUNT-TOTAL:   ___________
T4-VERDICT-CONFIRMED: ___________
T4-QUORUM-VALID:      ___________
T4-ANTIPATTERN-CATS:  ___________
```

Fill and emit:

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-WRITTEN:     YES
T4-SECTIONS-PRESENT:  [list all 7 section names]
T4-HEADCOUNT-TOTAL:   [n]
T4-VERDICT-CONFIRMED: [T2-VERDICT]
T4-QUORUM-VALID:      [YES | NO]
T4-ANTIPATTERN-CATS:  [list cats used — must be T2-REQUIRED-CAT values]
===
```

---

### PHASE 5 — VERIFY

**Inbound rule**: FORBIDDEN: executing Phase 5 before Phase 4 `=== RECORD: PHASE-4 ===` is
emitted. Consume all T1–T4 record block fields.

Run each check. Emit PASS or FAIL per line:

```
VERIFY-CHECKS:
  V-1  role count in T1-ROLE-TARGET range
       actual=[T3-TOTAL-FILES], target=[T1-ROLE-TARGET] → [PASS/FAIL]

  V-2  every area in T1-AREA-LIST has an IA file
       areas=[T1-AREA-COUNT], IA files=[T3-IA-COUNT] → [PASS/FAIL]

  V-3  all IA scope fields verbatim from T2-IA-TEMPLATE-KEY
       T3-SCOPE-VERBATIM → [PASS/FAIL]

  V-4  all IA lens fields unique across areas
       T3-LENS-UNIQUE → [PASS/FAIL]

  V-5  T4-HEADCOUNT-TOTAL matches T3-TOTAL-FILES
       [T4-HEADCOUNT-TOTAL] == [T3-TOTAL-FILES] → [PASS/FAIL]

  V-6  all 7 org-chart.md sections present
       T4-SECTIONS-PRESENT contains all 7 → [PASS/FAIL]

  V-7  all governance charters have Quorum as N of M
       T4-QUORUM-VALID → [PASS/FAIL]

  V-8  T4-VERDICT-CONFIRMED is a single closed-set value
       [PASS/FAIL]
```

`FINAL: [PASS — all 8 checks pass | FAIL — checks failed: {list}]`

```
=== RECORD: PHASE-5 ===
PHASE-ORDERING-GUARD: FORBIDDEN: this is the final phase. No subsequent phase.
T5-VERIFY-RESULT:     [PASS | FAIL]
T5-FAILED-CHECKS:     [list or "none"]
T5-BUILD-STATUS:      [COMPLETE | INCOMPLETE]
===
```

---

## V-04 — Role Sequence + Inertia Framing (Combination)

**Axes**: Role sequence (IA files written across all areas before any other role) + Inertia
framing (IA scope templates pre-declared and named before any file writing begins, verdict
drives all subsequent anti-pattern and roadmap choices)
**Hypothesis**: Declaring the full IA scope template table and the verdict-to-anti-pattern
derivation rule as an explicit output artifact before any file is written creates an immutable
reference that all subsequent file-writing phases MUST cite. Combined with writing all IA files
in a single dedicated phase (before any standard or specialized roles), this variation produces
the strongest simultaneous coverage of C-03 (no IA omission), C-11 (scope keyed to verdict),
C-12 (anti-pattern categories from design choice), C-15 (bidirectional verdict guard), C-17
(verbatim scope), and C-18 (category exclusion). Risk: the declared-templates artifact adds
output before file writing; under token pressure Phase 4 (standard/specialized roles) may be
compressed.

---

You are running `org-build`. Input: repo path or `--scan {file}`. Flag: `--depth [standard|deep]`.

FORBIDDEN: beginning any phase before emitting the prior phase's `=== RECORD: PHASE-N ===` block.
FORBIDDEN: emitting a record block before completing all work in that phase.

---

### PHASE 1 — SCAN

Scan the repo or scan-results. Discover all areas, tech domains, and scale signals.

**Depth-flag count floor — bind here:**
- T1-DEPTH-FLAG = `standard` → MUST write 20–30 role files total
- T1-DEPTH-FLAG = `deep`     → MUST write 50+ role files total

FORBIDDEN: proceeding to Phase 2 before emitting:

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:   [standard | deep]
T1-ROLE-TARGET:  [20-30 | 50+]
T1-AREA-LIST:    [comma-separated]
T1-AREA-COUNT:   [n]
T1-SOURCE:       [repo | scan-results]
===
```

---

### PHASE 2 — INERTIA ASSESSMENT AND TEMPLATE DECLARATION

**Inbound rule**: FORBIDDEN: executing Phase 2 before Phase 1 record block is emitted.
Consume T1-AREA-LIST, T1-AREA-COUNT.

**Step 2a — Score pressure dimensions:**

```
PRESSURE-SCORING:
  coordination-surface:  [LOW|MOD|ELE|HIGH] — [evidence]
  decision-latency-risk: [LOW|MOD|ELE|HIGH] — [evidence]
  span-of-control:       [LOW|MOD|ELE|HIGH] — [evidence]
  scale-indicator:       [LOW|MOD|ELE|HIGH] — [evidence]
```

T2-PRESSURE = max of four dimensions.

T2-VERDICT derivation:
- LOW or MODERATE → CAN-OPERATE-FLAT
- ELEVATED or HIGH → STRUCTURE-WARRANTED

VERDICT GUARD: FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: omitting both and leaving verdict blank.
Only one verdict. Both is an error. Neither is an error.

**Step 2b — Declare IA scope templates as named artifact:**

```
IA-SCOPE-TEMPLATES:

LOW/CAN:
  "The inertia-advocate operates as a velocity-preservation check — the org is structurally
  sound; this role monitors for premature complexity. Scope: challenge every proposed
  coordination layer before it ossifies into permanent structure."

MOD/CAN:
  "The inertia-advocate operates as a coordination-cost sentinel — flat structure is viable
  but strained at current scale; this role tracks the point at which coordination cost exceeds
  hierarchy cost. Scope: own the threshold number and surface it before each headcount decision."

ELE/STR:
  "The inertia-advocate operates as a structural-change auditor — hierarchy is indicated but
  the inertia cost of introducing it must be paid explicitly; this role documents what the flat
  org did well and ensures the new structure preserves it. Scope: produce a cost-of-transition
  ledger before any structural change is ratified."

HIGH/STR:
  "The inertia-advocate operates as a continuity guardian during structural transition — the
  org must add hierarchy and the risk is losing the coordination velocity of the flat phase;
  this role owns the handoff protocol between flat and structured operation. Scope: write the
  runbook that flat-era contributors will follow during the transition."

ACTIVE-KEY: [LOW/CAN | MOD/CAN | ELE/STR | HIGH/STR]
ACTIVE-TEMPLATE: [copy the matching template text here]
```

Phase 3 MUST copy the ACTIVE-TEMPLATE text verbatim into every IA file's `scope` field.
FORBIDDEN: paraphrasing or adapting the ACTIVE-TEMPLATE text in any IA file.

**Step 2c — Declare anti-pattern category rule:**

```
ANTI-PATTERN-RULE:
  T2-VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
  REQUIRED-CATS: [cat-3, cat-2 | cat-1, cat-4]
  FORBIDDEN-CATS: [cat-1, cat-4 | cat-2, cat-3]
  DERIVATION: Categories are determined by the structural design choice encoded in T2-VERDICT.
    CAN-OPERATE-FLAT selects coordination and span pathologies (cat-2, cat-3) because a flat
    org's failure modes are excess coordination theater and span inflation — not authority
    vacuums (cat-1) or span collapse (cat-4), which arise only when hierarchy is attempted.
    STRUCTURE-WARRANTED selects authority and span-collapse pathologies (cat-1, cat-4) because
    introducing hierarchy without clear authority channels and controlled spans creates the
    opposite failure modes.
```

FORBIDDEN: beginning Phase 3 before emitting:

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE:         [LOW | MODERATE | ELEVATED | HIGH]
T2-VERDICT:          [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-ACTIVE-KEY:       [LOW/CAN | MOD/CAN | ELE/STR | HIGH/STR]
T2-REQUIRED-CAT:     [cat-3,cat-2 | cat-1,cat-4]
T2-FORBIDDEN-CAT:    [cat-1,cat-4 | cat-2,cat-3]
T2-TEMPLATES-DECLARED: YES
===
```

---

### PHASE 3 — WRITE ALL INERTIA-ADVOCATE FILES

**Inbound rule**: FORBIDDEN: executing Phase 3 before Phase 2 record block is emitted.
Consume T1-AREA-LIST, T2-ACTIVE-KEY, T2-TEMPLATES-DECLARED.

Write one inertia-advocate file for every area in T1-AREA-LIST before any other role is written.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

Five fields — MUST be present in every file:
- **orientation**: Rational defense of this area's status quo. Draw from area's technical
  context. Name the specific concern. No generic framing.
- **lens**: Domain-specific status quo protected. MUST reference a term from the area's
  discovery context. MUST differ from every other area's IA lens.
- **expertise**: Specific systems, code, or processes this advocate has run. MUST differ
  from every other area's IA expertise.
- **scope**: MUST be verbatim copy of ACTIVE-TEMPLATE text from Phase 2 T2-TEMPLATES-DECLARED.
  Verbatim. No edits. No paraphrase. Copy-paste only.
- **collaborates_with**: Counterpart role slugs; forum (design review, sprint planning,
  architecture board); cadence (every sprint, per-quarter, ad hoc).

After each file: `IA-WRITTEN: [area-slug] — lens-first-5-words: "[...]"`

FORBIDDEN: beginning Phase 4 before emitting:

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-IA-COUNT:          [n — must equal T1-AREA-COUNT]
T3-AREAS-WITH-IA:     [list all area slugs]
T3-AREAS-WITHOUT-IA:  [list or "none"]
T3-SCOPE-VERBATIM:    YES — every IA file scope field contains ACTIVE-TEMPLATE text verbatim
T3-LENS-COLLISIONS:   [list of any areas with identical lens text, or "none"]
===
```

---

### PHASE 4 — WRITE REMAINING ROLE FILES

**Inbound rule**: FORBIDDEN: executing Phase 4 before Phase 3 record block is emitted.
Consume T1-AREA-LIST, T1-DEPTH-FLAG, T1-ROLE-TARGET, T3-IA-COUNT.

For each area, write standard roles then specialized roles. IA files exist from Phase 3.

**Standard roles**: path `.craft/roles/{area-slug}/{role-slug}.md`
Five fields: orientation, lens, expertise, scope: `standard`, collaborates_with.

**Specialized roles**: path `.craft/roles/{area-slug}/{role-slug}.md`
Five fields: orientation, lens, expertise, scope: `specialized — {area-slug}`, collaborates_with.

MUST: scope field distinguishes standard from specialized explicitly — not derivable from
directory placement alone.

Total role files (including IA files from Phase 3) MUST comply with T1-DEPTH-FLAG:
- T1-DEPTH-FLAG = standard → total MUST be 20–30. FORBIDDEN: fewer than 20.
- T1-DEPTH-FLAG = deep     → total MUST be 50+. FORBIDDEN: fewer than 50.

After each area: `AREA-COMPLETE: [area-slug] — std=[n] spec=[n]. Running total: [n].`

FORBIDDEN: beginning Phase 5 before emitting:

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-STANDARD-COUNT:    [n]
T4-SPECIALIZED-COUNT: [n]
T4-TOTAL-FILES:       [n including T3-IA-COUNT]
T4-TARGET-MET:        [YES | NO — actual={n}, required={T1-ROLE-TARGET}]
===
```

---

### PHASE 5 — WRITE ORG-CHART.MD

**Inbound rule**: FORBIDDEN: executing Phase 5 before Phase 4 record block is emitted.
Consume T2-PRESSURE, T2-VERDICT, T2-REQUIRED-CAT, T2-FORBIDDEN-CAT, T4-TOTAL-FILES.

Write `org-chart.md`. All seven sections MUST be present:

**1. ASCII Org Diagram** — min 2 levels, box-drawing, headcount per area in parens.

**2. Headcount by Area**
```markdown
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
```
Decides and Escalates MUST be populated per row.

**3. Level Distribution**
```markdown
| Level | Count | % of Org |
```
Total MUST match Headcount Total.

**4. Inertia Assessment**
```
FLAT-CASE-PRESSURE: [T2-PRESSURE]
VERDICT: [T2-VERDICT]
```
Closed-set values only. No generic prose verdict.

**5. Operating Rhythm** — 3+ rows (ROB, Shiproom, 1+ governance). Charter for each governance
meeting: Purpose, Owner, Quorum (N of M), Inputs, Outputs. All 5 fields required.
FORBIDDEN: Quorum without N-of-M format.

**6. Org Evolution Roadmap** — 2+ rows. Row 1: headcount type. Row 2: different type.

**7. Anti-Pattern Watch** — 2+ rows. MUST use T2-REQUIRED-CAT. FORBIDDEN: T2-FORBIDDEN-CAT.
"Why It Applies Here" MUST open with `[element name] (cat-N) —`.
Mitigation MUST be a remediation action.

FORBIDDEN: beginning Phase 6 before emitting:

```
=== RECORD: PHASE-5 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 6 begins before this block is emitted.
T5-CHART-SECTIONS:    [list all 7]
T5-HEADCOUNT-TOTAL:   [n]
T5-VERDICT-IN-CHART:  [T2-VERDICT]
T5-QUORUM-VALID:      [YES/NO]
T5-ANTIPATTERN-CATS:  [cats used, must be T2-REQUIRED-CAT]
===
```

---

### PHASE 6 — VERIFY

**Inbound rule**: FORBIDDEN: executing Phase 6 before Phase 5 record block is emitted.

```
BUILD-VERIFY:
  role-count:     T4-TOTAL-FILES=[n], T1-ROLE-TARGET=[range] → [PASS/FAIL]
  ia-coverage:    T3-IA-COUNT=[n], T1-AREA-COUNT=[n] → [PASS/FAIL]
  scope-verbatim: T3-SCOPE-VERBATIM=YES → [PASS/FAIL]
  headcount-match: T5-HEADCOUNT-TOTAL=[n] == T4-TOTAL-FILES=[n] → [PASS/FAIL]
  sections:       T5-CHART-SECTIONS contains all 7 → [PASS/FAIL]
  quorum:         T5-QUORUM-VALID=YES → [PASS/FAIL]
  verdict:        T5-VERDICT-IN-CHART is single closed-set value → [PASS/FAIL]
  antipatterns:   T5-ANTIPATTERN-CATS == T2-REQUIRED-CAT → [PASS/FAIL]
```

`VERIFY: [PASS | FAIL — {list}]`

```
=== RECORD: PHASE-6 ===
PHASE-ORDERING-GUARD: FORBIDDEN: this is the final phase. No subsequent phase.
T6-BUILD-STATUS:  [COMPLETE | INCOMPLETE]
T6-VERIFY-RESULT: [PASS | FAIL]
===
```

---

## V-05 — Phrasing Register + Lifecycle Emphasis (Combination)

**Axes**: Phrasing register (full technical imperative: every constraint is MUST or FORBIDDEN,
zero advisory language anywhere) + Lifecycle emphasis (strict sequential phase gates with
double-guard at every boundary)
**Hypothesis**: Advisory language ("should", "prefer", "typically", "consider") is the primary
cause of C-19 failures in prior rounds. Eliminating it globally — not just in key sections but
in every constraint context throughout the entire prompt — combined with double-guard phase
boundaries produces the strongest joint coverage of C-19 (uniform imperative register),
C-20 (systematic gate coverage), C-21 (constraint-completeness), and C-25 (bidirectional
redundancy). Phrasing register is the single-biggest lever for C-19; lifecycle emphasis is
the biggest lever for C-25. Their combination targets the cluster of late-rubric criteria
(C-19 through C-28) most directly. Risk: rigid imperative framing may produce brittle output
that fails gracefully on edge cases; the skill has less room to handle unusual repo structures.

---

You are running `org-build`. Input: repo path or `--scan {file}`. Flag: `--depth [standard|deep]`.

**Global imperative register rule**: Every constraint in every phase MUST use MUST or FORBIDDEN.
FORBIDDEN: using "should", "prefer", "typically", "consider", "may", "might", "can", or any
advisory form in any constraint context throughout this execution. Constraints are MUST or
FORBIDDEN. No exceptions.

**Global phase-ordering rule**: Phases execute in order 1 → 2 → 3 → 4 → 5 → 6.
Every phase boundary carries two orthogonal FORBIDDENs:
- Outbound (at the emitting phase): FORBIDDEN: beginning Phase N+1 before emitting this block.
- Inbound (at the consuming phase): FORBIDDEN: executing Phase N+1 before Phase N record block
  is emitted.

Both FORBIDDENs MUST be observed. Observing only one direction is a build error.

---

### PHASE 1 — SCAN

**Outbound**: FORBIDDEN: beginning Phase 2 before Phase 1 record block is emitted.

Scan repo or scan-results. MUST identify: all areas, tech domains, scale signals.

**Depth-flag count floor — MUST be stated here with flag-conditioned bounds:**

```
DEPTH-FLOOR-DECLARATION:
  T1-DEPTH-FLAG = standard → MUST write 20–30 role files total
  T1-DEPTH-FLAG = deep     → MUST write 50+ role files total
```

FORBIDDEN: stating a flat count range without its T1-DEPTH-FLAG condition.
FORBIDDEN: deferring the count floor declaration to any later phase.

MUST emit:

```
=== RECORD: PHASE-1 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 2 begins before this block is emitted.
T1-DEPTH-FLAG:   [standard | deep]
T1-ROLE-TARGET:  [20-30 | 50+]
T1-AREA-LIST:    [comma-separated area slugs]
T1-AREA-COUNT:   [n]
T1-SOURCE:       [repo | scan-results]
===
```

---

### PHASE 2 — INERTIA ASSESSMENT

**Inbound**: FORBIDDEN: executing Phase 2 before Phase 1 `=== RECORD: PHASE-1 ===` is emitted.
MUST consume T1-AREA-LIST, T1-AREA-COUNT.
**Outbound**: FORBIDDEN: beginning Phase 3 before Phase 2 record block is emitted.

MUST score four pressure dimensions (coordination-surface, decision-latency-risk,
span-of-control, scale-indicator). Each MUST be rated: LOW | MODERATE | ELEVATED | HIGH.

T2-PRESSURE MUST be the maximum of the four dimension scores.

T2-VERDICT MUST be derived as:
- T2-PRESSURE = LOW or MODERATE     → MUST assign CAN-OPERATE-FLAT
- T2-PRESSURE = ELEVATED or HIGH    → MUST assign STRUCTURE-WARRANTED

VERDICT GUARD — apply both directions:
- FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
- FORBIDDEN: omitting both verdicts and leaving T2-VERDICT blank.
- Only one verdict. Both is an error. Neither is an error.

IA scope templates — MUST declare all four; MUST select one by T2-PRESSURE + T2-VERDICT key:

| Key | Template |
|-----|---------|
| LOW/CAN | "The inertia-advocate operates as a velocity-preservation check — the org is structurally sound; this role monitors for premature complexity. Scope: challenge every proposed coordination layer before it ossifies into permanent structure." |
| MOD/CAN | "The inertia-advocate operates as a coordination-cost sentinel — flat structure is viable but strained at current scale; this role tracks the point at which coordination cost exceeds hierarchy cost. Scope: own the threshold number and surface it before each headcount decision." |
| ELE/STR | "The inertia-advocate operates as a structural-change auditor — hierarchy is indicated but the inertia cost of introducing it must be paid explicitly; this role documents what the flat org did well and ensures the new structure preserves it. Scope: produce a cost-of-transition ledger before any structural change is ratified." |
| HIGH/STR | "The inertia-advocate operates as a continuity guardian during structural transition — the org must add hierarchy and the risk is losing the coordination velocity of the flat phase; this role owns the handoff protocol between flat and structured operation. Scope: write the runbook that flat-era contributors will follow during the transition." |

T2-IA-TEMPLATE MUST be the exact text of the selected row. FORBIDDEN: paraphrasing.
Phase 3 MUST copy T2-IA-TEMPLATE verbatim into every IA file scope field.

Anti-pattern category rule — MUST apply:
- T2-VERDICT = CAN-OPERATE-FLAT     → MUST use cat-3, cat-2. FORBIDDEN: cat-1, cat-4.
- T2-VERDICT = STRUCTURE-WARRANTED  → MUST use cat-1, cat-4. FORBIDDEN: cat-2, cat-3.

MUST emit:

```
=== RECORD: PHASE-2 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 3 begins before this block is emitted.
T2-PRESSURE:           [LOW | MODERATE | ELEVATED | HIGH]
T2-VERDICT:            [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T2-TEMPLATE-KEY:       [LOW/CAN | MOD/CAN | ELE/STR | HIGH/STR]
T2-IA-TEMPLATE:        [exact template text for T2-TEMPLATE-KEY]
T2-REQUIRED-CAT:       [cat-3,cat-2 | cat-1,cat-4]
T2-FORBIDDEN-CAT:      [cat-1,cat-4 | cat-2,cat-3]
===
```

---

### PHASE 3 — WRITE ROLE FILES

**Inbound**: FORBIDDEN: executing Phase 3 before Phase 2 `=== RECORD: PHASE-2 ===` is emitted.
MUST consume T1-AREA-LIST, T1-DEPTH-FLAG, T1-ROLE-TARGET, T2-VERDICT, T2-TEMPLATE-KEY,
T2-IA-TEMPLATE.
**Outbound**: FORBIDDEN: beginning Phase 4 before Phase 3 record block is emitted.

MUST write role files for every area in T1-AREA-LIST.
Sequence per area: inertia-advocate → standard roles → specialized roles.

**Inertia-advocate** — MUST write one per area. FORBIDDEN: skipping any area.

Path: `.craft/roles/{area-slug}/inertia-advocate.md`

MUST include all five fields:
- **orientation**: MUST name a specific concern from the area's technical context. FORBIDDEN:
  generic "this role values stability" framing.
- **lens**: MUST reference at least one term from the area's scan context. FORBIDDEN: two IA
  files sharing identical lens text.
- **expertise**: MUST name specific systems, processes, or decisions. FORBIDDEN: two IA files
  sharing identical expertise text.
- **scope**: MUST be T2-IA-TEMPLATE copied verbatim. FORBIDDEN: any paraphrase or adaptation.
- **collaborates_with**: MUST name counterpart role slugs, forum, and cadence.

**Standard roles** — path: `.craft/roles/{area-slug}/{role-slug}.md`
MUST include: orientation, lens, expertise, scope: `standard`, collaborates_with.

**Specialized roles** — path: `.craft/roles/{area-slug}/{role-slug}.md`
MUST include: orientation, lens, expertise, scope: `specialized — {area-slug}`, collaborates_with.
FORBIDDEN: scope field that is derivable only from directory placement.

Total file count MUST comply with T1-DEPTH-FLAG:
- T1-DEPTH-FLAG = standard → MUST be 20–30. FORBIDDEN: fewer than 20.
- T1-DEPTH-FLAG = deep     → MUST be 50+. FORBIDDEN: fewer than 50.

MUST emit:

```
=== RECORD: PHASE-3 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 4 begins before this block is emitted.
T3-TOTAL-FILES:       [n]
T3-IA-COUNT:          [n — MUST equal T1-AREA-COUNT]
T3-STANDARD-COUNT:    [n]
T3-SPECIALIZED-COUNT: [n]
T3-COUNT-IN-RANGE:    [YES | NO — actual: {n}, required: {T1-ROLE-TARGET}]
T3-SCOPE-VERBATIM:    [YES | NO]
T3-LENS-UNIQUE:       [YES | NO — collisions: {list if NO}]
===
```

---

### PHASE 4 — WRITE ORG-CHART.MD

**Inbound**: FORBIDDEN: executing Phase 4 before Phase 3 `=== RECORD: PHASE-3 ===` is emitted.
MUST consume T1-AREA-LIST, T2-PRESSURE, T2-VERDICT, T2-REQUIRED-CAT, T2-FORBIDDEN-CAT,
T3-TOTAL-FILES.
**Outbound**: FORBIDDEN: beginning Phase 5 before Phase 4 record block is emitted.

MUST write `org-chart.md` with all seven sections. FORBIDDEN: omitting any section.

**Section 1 — ASCII Org Diagram**
MUST use box-drawing characters (`+--`, `|`). MUST show min 2 org levels.
MUST show headcount per area in parentheses. FORBIDDEN: leaf nodes without headcount.

**Section 2 — Headcount by Area**
MUST include columns: Area, Headcount, Key Roles, Decides, Escalates.
MUST populate Decides and Escalates for every row. FORBIDDEN: empty Decides or Escalates cells.

**Section 3 — Level Distribution**
MUST include columns: Level, Count, % of Org.
MUST have Total row. Total MUST match Headcount by Area Total. FORBIDDEN: totals that differ.

**Section 4 — Inertia Assessment**
MUST include `FLAT-CASE-PRESSURE: {T2-PRESSURE}` line.
MUST include `VERDICT: {T2-VERDICT}` line.
FORBIDDEN: generic prose verdict without labeled lines.

**Section 5 — Operating Rhythm**
MUST include 3+ rows. MUST include ROB, Shiproom, and at least one governance meeting.
For every governance meeting MUST write a charter block with exactly five fields:
Purpose, Owner, Quorum, Inputs, Outputs. Quorum MUST be expressed as "N of M".
FORBIDDEN: Quorum as bare number or percentage.

**Section 6 — Org Evolution Roadmap**
MUST include 2+ rows. Row 1 MUST have type: headcount.
Row 2 MUST have a different type (coordination-cost, decision-latency, or span-of-control).
FORBIDDEN: two rows of the same type.

**Section 7 — Anti-Pattern Watch**
MUST include 2+ rows. Category MUST be drawn from T2-REQUIRED-CAT.
FORBIDDEN: using any category in T2-FORBIDDEN-CAT.
Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`.
FORBIDDEN: cells that do not open with this syntax.
Every Mitigation cell MUST contain a remediation action.
FORBIDDEN: Mitigation cells containing format guidance or descriptive column instructions.

MUST emit:

```
=== RECORD: PHASE-4 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 5 begins before this block is emitted.
T4-CHART-WRITTEN:      YES
T4-SECTIONS:           [list all 7 section names]
T4-HEADCOUNT-TOTAL:    [n]
T4-VERDICT-IN-CHART:   [T2-VERDICT]
T4-QUORUM-FORMAT:      [all N of M: YES | NO]
T4-ANTIPATTERN-CATS:   [cats used — must match T2-REQUIRED-CAT]
T4-DECIDES-POPULATED:  [YES | NO]
T4-ESCALATES-POPULATED:[YES | NO]
===
```

---

### PHASE 5 — AMEND SECTION

**Inbound**: FORBIDDEN: executing Phase 5 before Phase 4 `=== RECORD: PHASE-4 ===` is emitted.
MUST consume T1-AREA-LIST, T1-DEPTH-FLAG from Phase 1, and T4 values.
**Outbound**: FORBIDDEN: beginning Phase 6 before Phase 5 record block is emitted.

MUST append to org-chart.md:

```markdown
## AMEND

Run `org-build --amend` with one of these options:

1. **Regenerate area**: `--area "{area-slug}"` — rewrites all .craft/roles/ files for the
   named area (including its IA file) and updates the corresponding org-chart.md rows.
   Available areas in this build: [{list T1-AREA-LIST values}]

2. **Adjust depth**: `--depth [standard|deep]` — regenerates the role file count to the
   target range for the selected depth. Current depth: {T1-DEPTH-FLAG}. Changing to the other
   depth will add or remove roles across all areas proportionally.

3. **Change inertia verdict**: `--verdict [CAN-OPERATE-FLAT|STRUCTURE-WARRANTED]` — overrides
   the assessed verdict, regenerates IA scope fields using the new verdict's template, and
   rewrites the Anti-Pattern Watch using the new verdict's required categories.
   Current verdict: {T2-VERDICT}.
```

MUST substitute actual values for T1-AREA-LIST and T1-DEPTH-FLAG and T2-VERDICT in the AMEND
text above. FORBIDDEN: leaving placeholders unfilled.

MUST emit:

```
=== RECORD: PHASE-5 ===
PHASE-ORDERING-GUARD: FORBIDDEN: Phase 6 begins before this block is emitted.
T5-AMEND-WRITTEN:    YES
T5-AREAS-LISTED:     [confirmed: actual area slugs from T1-AREA-LIST in AMEND option 1]
T5-DEPTH-LISTED:     [confirmed: T1-DEPTH-FLAG in AMEND option 2]
T5-VERDICT-LISTED:   [confirmed: T2-VERDICT in AMEND option 3]
===
```

---

### PHASE 6 — VERIFY

**Inbound**: FORBIDDEN: executing Phase 6 before Phase 5 `=== RECORD: PHASE-5 ===` is emitted.
MUST consume all T1–T5 record block values.

MUST run each check and emit PASS or FAIL:

```
VERIFY-CHECKS:
  V-1  T3-COUNT-IN-RANGE = YES
       [T3-TOTAL-FILES] in [T1-ROLE-TARGET] → [PASS|FAIL]

  V-2  T3-IA-COUNT = T1-AREA-COUNT
       [T3-IA-COUNT] == [T1-AREA-COUNT] → [PASS|FAIL]

  V-3  T3-SCOPE-VERBATIM = YES
       → [PASS|FAIL]

  V-4  T3-LENS-UNIQUE = YES
       → [PASS|FAIL]

  V-5  T4-HEADCOUNT-TOTAL = T3-TOTAL-FILES
       [T4-HEADCOUNT-TOTAL] == [T3-TOTAL-FILES] → [PASS|FAIL]

  V-6  T4-SECTIONS contains all 7
       → [PASS|FAIL]

  V-7  T4-QUORUM-FORMAT = YES
       → [PASS|FAIL]

  V-8  T4-DECIDES-POPULATED = YES and T4-ESCALATES-POPULATED = YES
       → [PASS|FAIL]

  V-9  T4-ANTIPATTERN-CATS matches T2-REQUIRED-CAT
       [T4-ANTIPATTERN-CATS] == [T2-REQUIRED-CAT] → [PASS|FAIL]

  V-10 T5-AMEND-WRITTEN = YES with actual values
       → [PASS|FAIL]
```

`VERIFY: [PASS — all 10 checks pass | FAIL — checks failed: {list}]`

MUST emit:

```
=== RECORD: PHASE-6 ===
PHASE-ORDERING-GUARD: FORBIDDEN: this is the final phase. No subsequent phase.
T6-VERIFY-RESULT:  [PASS | FAIL]
T6-FAILED-CHECKS:  [list or "none"]
T6-BUILD-STATUS:   [COMPLETE | INCOMPLETE]
===

BUILD-COMPLETE — org-build — {date}
  depth:           [T1-DEPTH-FLAG]
  areas:           [T1-AREA-COUNT]
  role files:      [T3-TOTAL-FILES] / [T1-ROLE-TARGET]
  IA coverage:     [T3-IA-COUNT] of [T1-AREA-COUNT] areas
  org-chart.md:    7 sections written
  inertia verdict: [T2-VERDICT]
  amend section:   3 options with concrete values
  verify:          [PASS | FAIL]
```
