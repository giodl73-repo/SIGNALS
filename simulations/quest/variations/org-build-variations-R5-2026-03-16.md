# org-build Skill Variations — Round 5

---

## V-01: Role Sequence — Inertia-First

**Axis:** Role sequence  
**Hypothesis:** Generating the inertia-advocate role before any other role forces the model to commit to a FLAT-CASE-PRESSURE rating and CAN-OPERATE-FLAT/STRUCTURE-WARRANTED verdict before populating the org. All subsequent roles are then scoped against the locked verdict, preventing drift between the assessment and the org structure.

---

```markdown
Generate a complete org from scan results or a repo path.

Inputs:
- Source: scan results file OR repo path (required)
- Depth: --depth deep → 50+ roles; default → 20-30 roles
- Date: use today's date for artifact filenames

---

## PHASE 0 — INERTIA ASSESSMENT FIRST

Before generating any role, run the inertia assessment and lock its verdict. All subsequent phases consume the verdict as an input contract.

### Step 0.1 — Scan for structural signals

Read the source material and extract:
- Team size and headcount distribution
- Decision bottlenecks (approvals that require escalation)
- Repeated cross-team coordination patterns
- Domain boundaries (distinct expertise clusters)
- Existing hierarchy signals (manager/IC ratios, reporting chains)

### Step 0.2 — Rate FLAT-CASE-PRESSURE

Rate the org on this closed set. One rating. No range.

| Rating | Meaning |
|--------|---------|
| LOW | Clear flat path. No coordination overhead detected. |
| MEDIUM | Mixed signals. Some coordination cost but not structural. |
| HIGH | Strong structural pressure. Repeated bottlenecks. Domain sprawl. |
| CRITICAL | Flat would create unacceptable coordination cost. |

**FLAT-CASE-PRESSURE: [RATING]**

### Step 0.3 — Issue single verdict

Issue exactly one verdict from this closed set:

```
VERDICT: CAN-OPERATE-FLAT
```
or
```
VERDICT: STRUCTURE-WARRANTED
```

**FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Only one verdict is valid. Writing both is an error. Writing neither is an error.**

### Step 0.4 — Lock typed output variables

Record these variables. All downstream phases MUST reference them by name.

```
T0-VERDICT = [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
T0-PRESSURE = [LOW | MEDIUM | HIGH | CRITICAL]
```

---

## PHASE 1 — INERTIA-ADVOCATE ROLE FILE

Before generating any other role, generate the inertia-advocate role file. Its `scope` field MUST be taken verbatim from the template keyed to T0-PRESSURE. Do not paraphrase. Do not adapt. Copy the template text exactly.

**Input contract:** T0-VERDICT, T0-PRESSURE (from Phase 0)

Scope templates (copy verbatim, no modification):

| T0-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| LOW | "Audit all proposed structural additions for necessity. Reject any role whose function can be absorbed by an existing flat collaborator. Recommend flat operation." |
| MEDIUM | "Flag every coordination mechanism proposed as optional. Require a reversibility plan for any structural addition. Default to flat; document structural exceptions." |
| HIGH | "Accept structural additions only with explicit coordination cost evidence. For each structural layer, require a headcount trigger and a removal condition." |
| CRITICAL | "Challenge the need for each proposed role against the baseline flat team. For unavoidable structure, require a sunset clause and owner accountability." |

Generate the inertia-advocate role file at `.roles/governance/inertia-advocate.md`:

```
---
role: inertia-advocate
area: governance
orientation: [challenge | steward | auditor]
lens: organizational-inertia
expertise: status-quo-defense, structural-cost-analysis, reversibility-planning
scope: [VERBATIM TEXT FROM TABLE ABOVE keyed to T0-PRESSURE]
collaborates_with: [all area leads, org-chart owner]
---
```

**MUST: scope field contains exact verbatim template text. Paraphrase fails.**

---

## PHASE 2 — AREA IDENTIFICATION

**Input contract:** T0-VERDICT (from Phase 0)

Identify primary expertise areas from the source material. Each area becomes a subdirectory under `.roles/`.

- If T0-VERDICT = CAN-OPERATE-FLAT: MUST produce 3-5 flat areas with no hierarchy within areas
- If T0-VERDICT = STRUCTURE-WARRANTED: MUST produce 4-7 areas with explicit parent-child relationships where needed

Record typed output:

```
T2-AREAS = [comma-separated list of area names]
T2-AREA-COUNT = [integer]
```

---

## PHASE 3 — ROLE GENERATION

**Input contract:** T0-VERDICT, T0-PRESSURE, T2-AREAS (from Phases 0 and 2)

Generate all roles. The inertia-advocate (Phase 1) counts toward the total.

Role count targets:
- Standard (default): 20-30 roles total
- Deep (--depth deep): 50+ roles total

For every role file, ALL FIVE fields are REQUIRED:

```markdown
---
role: [role-name]
area: [area-name matching T2-AREAS]
orientation: [one word: builder | steward | connector | challenger | synthesizer]
lens: [primary analytical perspective]
expertise: [3-5 comma-separated skills]
scope: [2-3 sentences: what this role owns and decides]
collaborates_with: [2-4 other roles]
---
```

**MUST: every file contains all five fields. Any missing field fails.**  
**MUST: area values match T2-AREAS exactly.**

Record typed output:

```
T3-ROLE-COUNT = [integer]
T3-ROLE-LIST = [list of role paths]
```

---

## PHASE 4 — ORG-CHART.MD

**Input contract:** T0-VERDICT, T0-PRESSURE, T2-AREAS, T3-ROLE-COUNT (from Phases 0–3)

Generate `org-chart.md` with all sections below. MUST appear in this order.

### Section 1 — ASCII Hierarchy Diagram

Draw an ASCII box diagram showing reporting relationships. MUST have at minimum 2 org levels. Flat name lists fail.

Example shape (content will differ):
```
┌─────────────────┐
│   [Top Level]   │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐  ┌───────┐
│[Area] │  │[Area] │
└───────┘  └───────┘
```

### Section 2 — Headcount by Area Table

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| ... | ... | ... | ... | ... |

**MUST include Decides and Escalates columns. Table without these columns fails.**

### Section 3 — Inertia Assessment

```
FLAT-CASE-PRESSURE: {{T0-PRESSURE}}
VERDICT: {{T0-VERDICT}}
```

**FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.**

Anti-pattern derivation: category selection MUST be tied to T0-VERDICT:
- If T0-VERDICT = CAN-OPERATE-FLAT: MUST cite cat-3 (unnecessary hierarchy) and cat-2 (coordination bloat). FORBIDDEN: citing cat-1 or cat-4.
- If T0-VERDICT = STRUCTURE-WARRANTED: MUST cite cat-1 (missing structure) and cat-4 (accountability gaps). FORBIDDEN: citing cat-2 or cat-3.

### Section 4 — Anti-Pattern Watch Table

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|-------------|----------|---------------------|------------|
| ...         | cat-N    | [element] (cat-N) — [reason] | [specific remediation action] |

**MUST: every "Why It Applies Here" cell opens with `[element name] (cat-N) —` syntax.**  
**MUST: Mitigation cells contain specific remediation actions. Format guidance or descriptive instructions fail.**  
**MUST: use imperative language throughout. MUST/FORBIDDEN. Advisory language ("should", "prefer", "consider") in any constraint context fails.**

### Section 5 — Operating Rhythm

| Meeting | Cadence | Owner | Attendees | Quorum |
|---------|---------|-------|-----------|--------|
| ROB     | ...     | ...   | ...       | N of M |
| Shiproom | ...   | ...   | ...       | N of M |
| [Governance] | ... | ... | ...     | N of M |

**MUST have 3+ distinct rows with different meeting types.**

For each governance meeting, provide a charter with all 5 fields: Purpose, Owner, Attendees, Decisions, Quorum (as `N of M` fraction).

### Section 6 — Org Evolution Roadmap

| Trigger | Type | Action | Owner |
|---------|------|--------|-------|
| Headcount reaches [N] | headcount-threshold | [specific action] | [role] |
| [Non-headcount condition] | [different category] | [specific action] | [role] |

**MUST have 2+ rows. Row 1 MUST be headcount-threshold type. Row 2 MUST be a different trigger category.**

---

## PHASE 5 — VERIFICATION

**Input contract:** T0-VERDICT, T0-PRESSURE, T2-AREAS, T3-ROLE-COUNT, T3-ROLE-LIST (all prior phases)

Before completing, verify:

1. T0-VERDICT appears in org-chart.md Section 3 exactly once
2. T0-PRESSURE appears in org-chart.md Section 3 exactly once
3. inertia-advocate scope matches the verbatim template for T0-PRESSURE
4. Anti-pattern categories match the verdict path and exclusion sets are explicit
5. Role count is within depth-appropriate range
6. All five role fields present in every file
7. All phase gate variables (T0-VERDICT, T0-PRESSURE, T2-AREAS, T3-ROLE-COUNT) were consumed by name in downstream phases

**MUST: complete verification before finalizing output. Any failed check MUST be corrected before output is complete.**
```

---

## V-02: Output Format — Pre-Print Skeleton

**Axis:** Output format  
**Hypothesis:** Presenting filled template skeletons with named placeholder slots keyed to gate variables before asking for generation forces the model to commit to output shape first. A reader who knows only the gate outputs can fill every slot. This directly targets C-22 and prevents shape drift between the phase gate declarations and the final artifacts.

---

```markdown
Generate a complete org from scan results or a repo path.

Inputs:
- Source: scan results file OR repo path (required)
- Depth: --depth deep → 50+ roles; default → 20-30 roles

---

## OUTPUT SKELETONS

The following templates define the exact shape of every output artifact. Named placeholder slots in `{{DOUBLE-BRACES}}` correspond to typed gate variables computed during generation. Fill every slot. A slot left as `{{VARIABLE-NAME}}` in the final output fails. An unnamed slot (e.g., `[VALUE]` or `___`) fails.

---

### Skeleton A — org-chart.md

```markdown
# Org Chart — {{REPO-NAME}}

## Structure

{{ASCII-DIAGRAM}}

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
{{HEADCOUNT-TABLE-ROWS}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}

## Anti-Pattern Watch

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|-------------|----------|---------------------|------------|
{{ANTI-PATTERN-TABLE-ROWS}}

## Operating Rhythm

| Meeting | Cadence | Owner | Attendees | Quorum |
|---------|---------|-------|-----------|--------|
{{RHYTHM-TABLE-ROWS}}

### Committee Charters

{{CHARTER-BLOCKS}}

## Org Evolution Roadmap

| Trigger | Type | Action | Owner |
|---------|------|--------|-------|
{{ROADMAP-TABLE-ROWS}}
```

---

### Skeleton B — Role File (.roles/{area}/{role}.md)

```markdown
---
role: {{ROLE-NAME}}
area: {{AREA-NAME}}
orientation: {{ORIENTATION}}
lens: {{LENS}}
expertise: {{EXPERTISE-LIST}}
scope: {{SCOPE-TEXT}}
collaborates_with: {{COLLABORATES-LIST}}
---
```

**MUST: every role file matches Skeleton B exactly. Every slot filled. No extra fields. No missing fields.**

---

### Skeleton C — inertia-advocate role file

```markdown
---
role: inertia-advocate
area: governance
orientation: challenger
lens: organizational-inertia
expertise: status-quo-defense, structural-cost-analysis, reversibility-planning
scope: {{IA-SCOPE-TEXT}}
collaborates_with: {{IA-COLLABORATES-LIST}}
---
```

**MUST: `{{IA-SCOPE-TEXT}}` is populated with the verbatim text from the scope template table keyed to `{{T1-PRESSURE}}`. Paraphrase fails. Adaptation fails. Verbatim copy required.**

---

### Skeleton D — Phase Gate Record (one per phase)

```markdown
## Gate: Phase {{PHASE-NUMBER}} Output

| Variable | Type | Value |
|----------|------|-------|
| {{GATE-VAR-1}} | {{GATE-TYPE-1}} | {{GATE-VALUE-1}} |
| {{GATE-VAR-2}} | {{GATE-TYPE-2}} | {{GATE-VALUE-2}} |
```

---

## PHASE 1 — INERTIA ASSESSMENT

Compute `{{T1-PRESSURE}}` and `{{T1-VERDICT}}`. These are the primary gate variables. All downstream skeletons reference them.

**Compute T1-PRESSURE** from source material signals:

| Rating | Signal Pattern |
|--------|---------------|
| LOW | Small team, clear ownership, no escalation chains detected |
| MEDIUM | Mixed signals, some coordination cost, bounded domain |
| HIGH | Repeated cross-team bottlenecks, domain sprawl, approval chains |
| CRITICAL | Coordination failure risk, accountability gaps, domain overlap conflicts |

**Compute T1-VERDICT** from T1-PRESSURE:

| T1-PRESSURE | Permitted Verdict |
|-------------|------------------|
| LOW | CAN-OPERATE-FLAT only |
| MEDIUM | Either; justify the choice |
| HIGH | STRUCTURE-WARRANTED only |
| CRITICAL | STRUCTURE-WARRANTED only |

**FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Only one verdict is valid. Both is an error. Neither is an error.**

Emit Phase 1 gate record using Skeleton D:

```
Gate: Phase 1 Output
T1-PRESSURE = [LOW | MEDIUM | HIGH | CRITICAL]
T1-VERDICT  = [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
```

---

## PHASE 2 — AREA SCAN

**Input contract:** MUST consume T1-VERDICT (from Phase 1 gate record)

Identify expertise areas from source material.

- If T1-VERDICT = CAN-OPERATE-FLAT: MUST identify 3-5 areas, no sub-hierarchy within areas
- If T1-VERDICT = STRUCTURE-WARRANTED: MUST identify 4-7 areas, hierarchy permitted within areas

Emit Phase 2 gate record using Skeleton D:

```
Gate: Phase 2 Output
T2-AREAS      = [comma-separated area names]
T2-AREA-COUNT = [integer]
```

---

## PHASE 3 — ROLE GENERATION

**Input contract:** MUST consume T1-VERDICT (Phase 1), T2-AREAS (Phase 2)

Generate all role files using Skeleton B. The inertia-advocate file MUST use Skeleton C with `{{IA-SCOPE-TEXT}}` filled verbatim from the pressure-keyed template.

**Scope templates for inertia-advocate — copy verbatim into `{{IA-SCOPE-TEXT}}`:**

| T1-PRESSURE | Verbatim text for {{IA-SCOPE-TEXT}} |
|-------------|--------------------------------------|
| LOW | "Audit all proposed structural additions for necessity. Reject any role whose function can be absorbed by an existing flat collaborator. Recommend flat operation." |
| MEDIUM | "Flag every coordination mechanism proposed as optional. Require a reversibility plan for any structural addition. Default to flat; document structural exceptions." |
| HIGH | "Accept structural additions only with explicit coordination cost evidence. For each structural layer, require a headcount trigger and a removal condition." |
| CRITICAL | "Challenge the need for each proposed role against the baseline flat team. For unavoidable structure, require a sunset clause and owner accountability." |

Role count targets:
- Standard: 20-30 files total
- Deep (--depth deep): 50+ files total

**MUST: all roles under `.roles/{{AREA-NAME}}/{{ROLE-NAME}}.md` paths.**  
**MUST: minimum 2 area subdirectories.**

Emit Phase 3 gate record using Skeleton D:

```
Gate: Phase 3 Output
T3-ROLE-COUNT = [integer]
T3-ROLE-LIST  = [list of generated role paths]
T3-IA-PATH    = [path to inertia-advocate file]
```

---

## PHASE 4 — FILL ORG-CHART.MD

**Input contract:** MUST consume T1-PRESSURE (Phase 1), T1-VERDICT (Phase 1), T2-AREAS (Phase 2), T3-ROLE-COUNT (Phase 3)

Fill Skeleton A completely. Every `{{PLACEHOLDER}}` MUST be replaced with computed content.

**Filling `{{ASCII-DIAGRAM}}`:** MUST produce a diagram with minimum 2 levels using box-drawing characters. Flat name list fails.

**Filling `{{HEADCOUNT-TABLE-ROWS}}`:** One row per area. MUST include Decides and Escalates columns.

**Filling `{{ANTI-PATTERN-TABLE-ROWS}}`:**

Anti-pattern categories are derived from T1-VERDICT:

| T1-VERDICT | Required categories | FORBIDDEN categories |
|------------|--------------------|-----------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax.  
Every Mitigation cell MUST contain a specific remediation action. Format guidance fails.

**Filling `{{RHYTHM-TABLE-ROWS}}`:** MUST include ROB, shiproom, and at minimum one governance meeting. Quorum column as `N of M` fraction.

**Filling `{{CHARTER-BLOCKS}}`:** One charter per governance meeting. MUST contain all 5 fields: Purpose, Owner, Attendees, Decisions, Quorum.

**Filling `{{ROADMAP-TABLE-ROWS}}`:** MUST include at minimum 2 rows. First row trigger type MUST be `headcount-threshold`. Second row MUST be a different trigger category.

---

## PHASE 5 — CONSTRAINT-COMPLETENESS CHECK

**Input contract:** MUST consume T1-PRESSURE, T1-VERDICT, T2-AREAS, T3-ROLE-COUNT, T3-ROLE-LIST, T3-IA-PATH (all prior gate records)

For every named typed variable declared at a phase gate, verify its consuming input contract uses MUST or FORBIDDEN — not advisory language.

| Variable | Consumed in Phase | Governing constraint | Status |
|----------|-------------------|---------------------|--------|
| T1-VERDICT | Phase 2 | MUST consume T1-VERDICT | verify |
| T1-VERDICT | Phase 3 | MUST consume T1-VERDICT | verify |
| T1-VERDICT | Phase 4 | MUST consume T1-VERDICT | verify |
| T1-PRESSURE | Phase 3 (IA scope) | MUST use verbatim template | verify |
| T1-PRESSURE | Phase 4 (inertia section) | MUST appear in Section 3 | verify |
| T2-AREAS | Phase 3 | MUST match area names | verify |
| T3-ROLE-COUNT | Phase 4 | MUST reference count | verify |

**MUST: all rows show verified. Any advisory consumption fails. Correct before finalizing.**
```

---

## V-03: Lifecycle Emphasis — Explicit Phase Gates

**Axis:** Lifecycle emphasis  
**Hypothesis:** Dedicating a full section to each phase boundary — with explicit input contract declarations and typed output variable blocks — produces systematic gate coverage (C-20) and constraint-completeness seals (C-21) because the model cannot skip declaring an output at a gate or leave an input contract implicit.

---

```markdown
Generate a complete org from scan results or a repo path.

Inputs:
- Source: scan results file OR repo path (required)
- Depth: --depth deep → 50+ roles; default → 20-30 roles

Every phase below follows this structure:
1. INPUT CONTRACT — variables this phase consumes (by name, from a prior gate)
2. WORK — what this phase computes
3. OUTPUT GATE — typed variables this phase produces for downstream consumption

Every variable declared at a gate MUST be governed by MUST or FORBIDDEN in every downstream input contract that references it. Advisory language in any input contract fails.

---

## GATE 0 — ENTRY

No inputs. Begins the phase chain.

**Gate 0 outputs:**
```
G0-SOURCE    : string  = [source file path or repo path]
G0-DEPTH     : enum    = [standard | deep]
G0-DATE      : string  = [today's date YYYY-MM-DD]
```

---

## PHASE 1 — INERTIA ASSESSMENT

### Input Contract

MUST consume: G0-SOURCE (Gate 0)

### Work

Read G0-SOURCE. Extract structural signals:
- Team size and headcount distribution
- Decision escalation patterns
- Cross-team coordination overhead
- Domain boundary clarity
- Reporting chain depth

Rate FLAT-CASE-PRESSURE from this closed set (one value, no range):

| Rating | Trigger condition |
|--------|------------------|
| LOW | Headcount < 12, clear ownership, no escalation chains |
| MEDIUM | Headcount 12-25 OR mixed ownership signals |
| HIGH | Headcount > 25 OR repeated cross-team bottlenecks |
| CRITICAL | Domain overlap conflicts OR accountability gaps |

Issue exactly one verdict:

- `CAN-OPERATE-FLAT` — if FLAT-CASE-PRESSURE is LOW or MEDIUM with clear ownership
- `STRUCTURE-WARRANTED` — if FLAT-CASE-PRESSURE is HIGH or CRITICAL

**FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Both is an error. Neither is an error.**

### Gate 1 Outputs

```
G1-PRESSURE : enum   = [LOW | MEDIUM | HIGH | CRITICAL]
G1-VERDICT  : enum   = [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
```

---

## PHASE 2 — AREA DECOMPOSITION

### Input Contract

MUST consume: G1-VERDICT (Gate 1)

- If G1-VERDICT = CAN-OPERATE-FLAT: MUST produce 3-5 areas, flat structure, no sub-hierarchy
- If G1-VERDICT = STRUCTURE-WARRANTED: MUST produce 4-7 areas, hierarchy permitted

### Work

Extract expertise clusters from G0-SOURCE. Name each area. Map role domains to areas.

### Gate 2 Outputs

```
G2-AREAS      : list[string]  = [area name list]
G2-AREA-COUNT : integer       = [count of areas]
```

---

## PHASE 3 — INERTIA-ADVOCATE GENERATION

### Input Contract

MUST consume: G1-PRESSURE (Gate 1), G1-VERDICT (Gate 1), G2-AREAS (Gate 2)

MUST apply verbatim scope template keyed to G1-PRESSURE. Paraphrase fails. The template text is the scope field. Copy it. Do not adapt it.

### Work

Select scope text verbatim from this table:

| G1-PRESSURE | Verbatim scope (copy exactly) |
|-------------|-------------------------------|
| LOW | "Audit all proposed structural additions for necessity. Reject any role whose function can be absorbed by an existing flat collaborator. Recommend flat operation." |
| MEDIUM | "Flag every coordination mechanism proposed as optional. Require a reversibility plan for any structural addition. Default to flat; document structural exceptions." |
| HIGH | "Accept structural additions only with explicit coordination cost evidence. For each structural layer, require a headcount trigger and a removal condition." |
| CRITICAL | "Challenge the need for each proposed role against the baseline flat team. For unavoidable structure, require a sunset clause and owner accountability." |

Generate `.roles/governance/inertia-advocate.md`:

```
---
role: inertia-advocate
area: governance
orientation: challenger
lens: organizational-inertia
expertise: status-quo-defense, structural-cost-analysis, reversibility-planning
scope: [VERBATIM TEXT FROM TABLE ABOVE]
collaborates_with: [all area leads]
---
```

### Gate 3 Outputs

```
G3-IA-PATH       : string  = [path to inertia-advocate.md]
G3-IA-SCOPE-TEXT : string  = [verbatim scope text used]
G3-IA-PRESSURE   : enum    = [value of G1-PRESSURE used for template selection]
```

---

## PHASE 4 — ROLE GENERATION

### Input Contract

MUST consume: G1-VERDICT (Gate 1), G2-AREAS (Gate 2), G3-IA-PATH (Gate 3)

MUST generate roles into area subdirectories matching G2-AREAS.  
MUST include G3-IA-PATH in the total role count.  
MUST ensure role count meets depth target:
- G0-DEPTH = standard: MUST produce 20-30 roles total
- G0-DEPTH = deep: MUST produce 50+ roles total

### Work

For every role, generate `.roles/{area}/{role}.md` with all five required fields:

```
---
role:             [role name]
area:             [must match a value in G2-AREAS]
orientation:      [one of: builder | steward | connector | challenger | synthesizer]
lens:             [primary analytical perspective]
expertise:        [3-5 comma-separated skills]
scope:            [2-3 sentences describing ownership and decisions]
collaborates_with:[2-4 other roles by name]
---
```

**MUST: every file contains all five fields. Any missing field fails.**

### Gate 4 Outputs

```
G4-ROLE-COUNT   : integer      = [total role files including IA]
G4-ROLE-PATHS   : list[string] = [all role file paths]
G4-AREA-DIRS    : list[string] = [area subdirectories created]
```

---

## PHASE 5 — ORG-CHART.MD GENERATION

### Input Contract

MUST consume: G1-PRESSURE (Gate 1), G1-VERDICT (Gate 1), G2-AREAS (Gate 2), G4-ROLE-COUNT (Gate 4), G4-AREA-DIRS (Gate 4)

### Work — Section 1: ASCII Hierarchy

Draw box diagram. MUST have minimum 2 org levels. Flat name list fails. Use `┌┐└┘─│├┤┬┴┼` characters.

### Work — Section 2: Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|

**MUST: include Decides and Escalates columns.**

### Work — Section 3: Inertia Assessment

Emit:
```
FLAT-CASE-PRESSURE: [G1-PRESSURE]
VERDICT: [G1-VERDICT]
```

MUST derive anti-pattern categories from G1-VERDICT per this table:

| G1-VERDICT | MUST cite | FORBIDDEN to cite |
|------------|-----------|-------------------|
| CAN-OPERATE-FLAT | cat-3, cat-2 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

### Work — Section 4: Anti-Pattern Watch

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|-------------|----------|---------------------|------------|

**MUST: every "Why It Applies Here" cell opens with `[element name] (cat-N) —` syntax.**  
**MUST: every Mitigation cell contains a specific remediation action. Format guidance fails.**

### Work — Section 5: Operating Rhythm

| Meeting | Cadence | Owner | Attendees | Quorum |
|---------|---------|-------|-----------|--------|

**MUST: minimum 3 rows (ROB + shiproom + 1 governance). Quorum as `N of M` fraction.**

For each governance meeting, charter with 5 fields: Purpose, Owner, Attendees, Decisions, Quorum.

### Work — Section 6: Org Evolution Roadmap

| Trigger | Type | Action | Owner |
|---------|------|--------|-------|

**MUST: Row 1 type = headcount-threshold. Row 2 type = different category.**

### Gate 5 Outputs

```
G5-ORGCHART-PATH : string  = [path to org-chart.md]
G5-SECTIONS      : integer = [count of sections generated, must be 6]
```

---

## PHASE 6 — CONSTRAINT-COMPLETENESS VERIFICATION

### Input Contract

MUST consume: ALL prior gate outputs (G1 through G5)

### Work

For every typed variable declared at a gate, verify it was consumed by name in a downstream input contract governed by MUST or FORBIDDEN.

| Variable | Declared at | Consumed in | Governing language | Pass? |
|----------|------------|-------------|-------------------|-------|
| G1-PRESSURE | Gate 1 | Phase 3 | MUST consume | — |
| G1-PRESSURE | Gate 1 | Phase 5 | MUST consume | — |
| G1-VERDICT | Gate 1 | Phase 2 | MUST consume | — |
| G1-VERDICT | Gate 1 | Phase 4 | MUST consume | — |
| G1-VERDICT | Gate 1 | Phase 5 | MUST consume | — |
| G2-AREAS | Gate 2 | Phase 3 | MUST consume | — |
| G2-AREAS | Gate 2 | Phase 4 | MUST consume | — |
| G3-IA-PATH | Gate 3 | Phase 4 | MUST include | — |
| G4-ROLE-COUNT | Gate 4 | Phase 5 | MUST consume | — |

**MUST: all rows pass before output is finalized. Any advisory consumption in a named-variable contract fails. Correct failures before completing.**

### Gate 6 Outputs

```
G6-VERIFIED : boolean = true
G6-FAILURES : list    = [any failed rows, empty if all pass]
```

**FORBIDDEN: finalizing output if G6-VERIFIED = false.**
```

---

## V-04: Phrasing Register — Full Imperative

**Axis:** Phrasing register  
**Hypothesis:** Replacing every advisory word ("should", "prefer", "typically", "consider", "recommend") with MUST or FORBIDDEN throughout all sections eliminates C-19 failures entirely, because the model cannot produce advisory constraint language if the prompt itself only demonstrates imperative register.

---

```markdown
Generate a complete org from scan results or a repo path.

Inputs:
- Source: scan results file OR repo path (required)
- Depth: --depth deep → 50+ roles; default → 20-30 roles

REGISTER CONTRACT: Every constraint in every section of your output MUST use MUST or FORBIDDEN. Advisory language — "should", "prefer", "typically", "consider", "recommend", "may want to" — is FORBIDDEN in any constraint context throughout the entire output.

---

## STEP 1 — ASSESS INERTIA

Read the source material. Extract structural signals. Compute FLAT-CASE-PRESSURE.

**MUST select exactly one rating:**

| Rating | Condition |
|--------|-----------|
| LOW | Small team, clear ownership, no escalation chains |
| MEDIUM | Mixed signals, moderate coordination overhead |
| HIGH | Bottlenecks, domain sprawl, multi-party approvals |
| CRITICAL | Coordination failure risk, accountability overlap |

**MUST issue exactly one verdict:**

```
FLAT-CASE-PRESSURE: [LOW | MEDIUM | HIGH | CRITICAL]
VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
```

**FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.**  
**FORBIDDEN: writing "either" or "either/or". One verdict. Both is an error. Neither is an error.**

---

## STEP 2 — GENERATE INERTIA-ADVOCATE ROLE

**MUST generate `.roles/governance/inertia-advocate.md` before generating any other role file.**

**MUST populate the `scope` field with the verbatim text from the table below, keyed to FLAT-CASE-PRESSURE. FORBIDDEN: paraphrasing the template. FORBIDDEN: adapting the template. FORBIDDEN: omitting any words from the template.**

| FLAT-CASE-PRESSURE | scope (copy verbatim) |
|--------------------|----------------------|
| LOW | "Audit all proposed structural additions for necessity. Reject any role whose function can be absorbed by an existing flat collaborator. Recommend flat operation." |
| MEDIUM | "Flag every coordination mechanism proposed as optional. Require a reversibility plan for any structural addition. Default to flat; document structural exceptions." |
| HIGH | "Accept structural additions only with explicit coordination cost evidence. For each structural layer, require a headcount trigger and a removal condition." |
| CRITICAL | "Challenge the need for each proposed role against the baseline flat team. For unavoidable structure, require a sunset clause and owner accountability." |

**MUST include all five fields:**

```
---
role: inertia-advocate
area: governance
orientation: challenger
lens: organizational-inertia
expertise: status-quo-defense, structural-cost-analysis, reversibility-planning
scope: [VERBATIM TEXT FROM TABLE]
collaborates_with: [all area leads, program-lead, org-chart-owner]
---
```

---

## STEP 3 — IDENTIFY AREAS

**MUST identify expertise areas before generating remaining roles.**

- If VERDICT = CAN-OPERATE-FLAT: MUST produce 3-5 areas. FORBIDDEN: creating sub-hierarchy within any area.
- If VERDICT = STRUCTURE-WARRANTED: MUST produce 4-7 areas. FORBIDDEN: creating fewer than 4 areas.

---

## STEP 4 — GENERATE REMAINING ROLE FILES

**MUST generate all role files at `.roles/{area}/{role}.md`.**

**MUST include all five fields in every file:**

| Field | MUST contain |
|-------|-------------|
| orientation | MUST be one of: builder, steward, connector, challenger, synthesizer |
| lens | MUST be a single primary analytical perspective |
| expertise | MUST list 3-5 comma-separated skills |
| scope | MUST contain 2-3 sentences describing ownership and decisions |
| collaborates_with | MUST name 2-4 other roles |

**FORBIDDEN: generating a role file with any field missing.**  
**FORBIDDEN: adding fields beyond the five required.**

Role count:
- Standard: MUST produce 20-30 total role files (including inertia-advocate). FORBIDDEN: producing fewer than 20 or more than 36.
- Deep (--depth deep): MUST produce 50+ total role files. FORBIDDEN: producing fewer than 50.

**MUST create minimum 2 area subdirectories under `.roles/`.**

---

## STEP 5 — GENERATE ORG-CHART.MD

**MUST include all six sections in order.**

### Section 1 — ASCII Diagram

**MUST draw a box diagram using box-drawing characters with minimum 2 org levels.**  
**FORBIDDEN: flat name lists. FORBIDDEN: single-level diagrams.**

### Section 2 — Headcount by Area Table

**MUST include columns: Area, Headcount, Key Roles, Decides, Escalates.**  
**FORBIDDEN: tables missing Decides or Escalates columns.**

### Section 3 — Inertia Assessment

**MUST emit:**
```
FLAT-CASE-PRESSURE: [rating]
VERDICT: [verdict]
```

**MUST derive anti-pattern categories from VERDICT per this table:**

| VERDICT | MUST cite | FORBIDDEN to cite |
|---------|-----------|-------------------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1 or cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2 or cat-3 |

**FORBIDDEN: citing categories from the wrong verdict path.**

### Section 4 — Anti-Pattern Watch Table

**MUST format every "Why It Applies Here" cell as: `[element name] (cat-N) — [reason]`.**  
**FORBIDDEN: plain prose in Why cells. FORBIDDEN: cells that do not open with the `[element] (cat-N) —` pattern.**

**MUST fill every Mitigation cell with a specific remediation action.**  
**FORBIDDEN: Mitigation cells containing format guidance, column descriptions, or procedural instructions.**

**MUST use MUST or FORBIDDEN in every constraint statement in this section.**  
**FORBIDDEN: "should", "prefer", "typically", "consider", or "recommend" in any constraint row.**

### Section 5 — Operating Rhythm

**MUST include minimum 3 distinct meeting rows: ROB, shiproom, and at minimum one governance meeting.**  
**MUST express every Quorum value as `N of M` fraction.**  
**FORBIDDEN: Quorum expressed as a percentage or as a plain number without denominator.**

**MUST provide a charter for every governance meeting with all 5 fields: Purpose, Owner, Attendees, Decisions, Quorum.**  
**FORBIDDEN: governance meetings without charters. FORBIDDEN: charters missing any of the 5 fields.**

### Section 6 — Org Evolution Roadmap

**MUST include minimum 2 rows.**  
**MUST make Row 1 trigger type `headcount-threshold`.**  
**MUST make Row 2 a different trigger category from Row 1.**  
**FORBIDDEN: two headcount-threshold rows. FORBIDDEN: rows with identical trigger types.**

---

## STEP 6 — FINAL VERIFICATION

**MUST verify before completing:**

1. VERDICT appears exactly once in org-chart.md Section 3. FORBIDDEN: VERDICT appearing in more than one location.
2. inertia-advocate scope matches verbatim template. FORBIDDEN: any deviation from template text.
3. Anti-pattern categories match verdict path. FORBIDDEN: categories from the excluded set.
4. Every role file contains all five fields. FORBIDDEN: incomplete role files.
5. Role count is within the depth-appropriate range. FORBIDDEN: counts outside the specified range.
6. Every phase gate variable was consumed by name using MUST or FORBIDDEN. FORBIDDEN: advisory language in any named-variable input contract.

**FORBIDDEN: finalizing output before all verification items pass.**
```

---

## V-05: Combination — Inertia-First + Pre-Print Skeleton + Imperative Register

**Axis:** Combination of V-01 (inertia-first sequencing) + V-02 (pre-print skeleton) + V-04 (imperative register)  
**Hypothesis:** The three axes are mutually reinforcing: inertia-first locks the verdict early so all skeletons can reference `{{T1-VERDICT}}` with a known value; the pre-print skeleton ensures every downstream artifact has explicitly named slots for gate variables; imperative register ensures every slot consumption is governed by MUST/FORBIDDEN. Together they close all three gap families (shape, sequence, register) simultaneously.

---

```markdown
Generate a complete org from scan results or a repo path.

Inputs:
- Source: scan results file OR repo path (required)
- Depth: --depth deep → 50+ roles; default → 20-30 roles

REGISTER CONTRACT: Every constraint statement in this prompt and in your output MUST use MUST or FORBIDDEN. FORBIDDEN: "should", "prefer", "typically", "consider", "recommend" in any constraint context anywhere in the output.

SKELETON CONTRACT: Every output artifact MUST match a named skeleton below. Every `{{SLOT}}` MUST be filled with computed content. FORBIDDEN: leaving any slot as its placeholder name. FORBIDDEN: unnamed slots (`[VALUE]`, `___`).

SEQUENCE CONTRACT: MUST generate inertia-advocate role before any other role file. MUST lock T1-VERDICT before generating any role content. FORBIDDEN: generating role files before Phase 1 gate is complete.

---

## OUTPUT SKELETONS

### Skeleton A — Phase Gate Record

```
## Gate {{PHASE-NUMBER}} — {{PHASE-NAME}}

| Variable | Type | Value |
|----------|------|-------|
| {{VAR-NAME-1}} | {{TYPE-1}} | {{VALUE-1}} |
| {{VAR-NAME-2}} | {{TYPE-2}} | {{VALUE-2}} |
```

### Skeleton B — inertia-advocate.md

```markdown
---
role: inertia-advocate
area: governance
orientation: challenger
lens: organizational-inertia
expertise: status-quo-defense, structural-cost-analysis, reversibility-planning
scope: {{IA-SCOPE-VERBATIM}}
collaborates_with: {{IA-COLLABORATES}}
---
```

### Skeleton C — Role file (all roles except inertia-advocate)

```markdown
---
role: {{ROLE-NAME}}
area: {{AREA-NAME}}
orientation: {{ORIENTATION}}
lens: {{LENS}}
expertise: {{EXPERTISE-LIST}}
scope: {{SCOPE-TEXT}}
collaborates_with: {{COLLABORATES-LIST}}
---
```

### Skeleton D — org-chart.md

```markdown
# Org Chart — {{REPO-NAME}}

## Structure

{{ASCII-DIAGRAM}}

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
{{HEADCOUNT-ROWS}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}

Inertia-Advocate Scope Applied: {{IA-SCOPE-VERBATIM}}

## Anti-Pattern Watch

| Anti-Pattern | Category | Why It Applies Here | Mitigation |
|-------------|----------|---------------------|------------|
{{ANTI-PATTERN-ROWS}}

## Operating Rhythm

| Meeting | Cadence | Owner | Attendees | Quorum |
|---------|---------|-------|-----------|--------|
{{RHYTHM-ROWS}}

### Committee Charters

{{CHARTER-BLOCKS}}

## Org Evolution Roadmap

| Trigger | Type | Action | Owner |
|---------|------|--------|-------|
{{ROADMAP-ROWS}}
```

### Skeleton E — Committee Charter

```markdown
#### {{MEETING-NAME}} Charter

- **Purpose:** {{CHARTER-PURPOSE}}
- **Owner:** {{CHARTER-OWNER}}
- **Attendees:** {{CHARTER-ATTENDEES}}
- **Decisions:** {{CHARTER-DECISIONS}}
- **Quorum:** {{CHARTER-QUORUM}} (N of M)
```

---

## PHASE 1 — INERTIA ASSESSMENT (RUNS FIRST, LOCKS VERDICT)

MUST complete this phase and emit Gate 1 before proceeding to any other phase.

Read source material. Extract:
- Headcount and distribution
- Escalation chains
- Cross-team coordination patterns
- Domain boundary clarity
- Approval bottlenecks

**MUST select exactly one T1-PRESSURE value:**

| T1-PRESSURE | Conditions |
|-------------|-----------|
| LOW | Headcount ≤ 12, clear ownership, no escalation |
| MEDIUM | Headcount 12-25 OR mixed ownership signals |
| HIGH | Headcount > 25 OR bottlenecks OR domain sprawl |
| CRITICAL | Accountability overlap OR coordination failure risk |

**MUST issue exactly one T1-VERDICT:**

| T1-PRESSURE | MUST issue |
|-------------|-----------|
| LOW | CAN-OPERATE-FLAT |
| MEDIUM | CAN-OPERATE-FLAT or STRUCTURE-WARRANTED (MUST justify choice) |
| HIGH | STRUCTURE-WARRANTED |
| CRITICAL | STRUCTURE-WARRANTED |

**FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts. Both is an error. Neither is an error.**

Emit Gate 1 using Skeleton A:

```
Gate 1 — Inertia Assessment
T1-PRESSURE : enum = [LOW | MEDIUM | HIGH | CRITICAL]
T1-VERDICT  : enum = [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]
```

---

## PHASE 2 — INERTIA-ADVOCATE ROLE FILE (RUNS SECOND)

**Input contract:** MUST consume T1-PRESSURE (Gate 1). FORBIDDEN: proceeding without T1-PRESSURE value.

MUST select `{{IA-SCOPE-VERBATIM}}` from this table. FORBIDDEN: paraphrase. FORBIDDEN: adaptation. FORBIDDEN: omitting any word from the selected template.

| T1-PRESSURE | {{IA-SCOPE-VERBATIM}} |
|-------------|----------------------|
| LOW | "Audit all proposed structural additions for necessity. Reject any role whose function can be absorbed by an existing flat collaborator. Recommend flat operation." |
| MEDIUM | "Flag every coordination mechanism proposed as optional. Require a reversibility plan for any structural addition. Default to flat; document structural exceptions." |
| HIGH | "Accept structural additions only with explicit coordination cost evidence. For each structural layer, require a headcount trigger and a removal condition." |
| CRITICAL | "Challenge the need for each proposed role against the baseline flat team. For unavoidable structure, require a sunset clause and owner accountability." |

Generate `.roles/governance/inertia-advocate.md` using Skeleton B. MUST fill `{{IA-SCOPE-VERBATIM}}` with verbatim template text. MUST fill `{{IA-COLLABORATES}}` with at minimum 2 area lead roles.

Emit Gate 2 using Skeleton A:

```
Gate 2 — IA Role
T2-IA-PATH         : string = [path to inertia-advocate.md]
T2-IA-SCOPE-HASH   : string = [first 8 words of scope text, for downstream verification]
T2-IA-PRESSURE-KEY : enum   = [T1-PRESSURE value used for template selection]
```

---

## PHASE 3 — AREA DECOMPOSITION

**Input contract:** MUST consume T1-VERDICT (Gate 1). FORBIDDEN: area count violating verdict-area rule.

- If T1-VERDICT = CAN-OPERATE-FLAT: MUST produce 3-5 areas. FORBIDDEN: sub-hierarchy within areas.
- If T1-VERDICT = STRUCTURE-WARRANTED: MUST produce 4-7 areas. FORBIDDEN: fewer than 4 areas.

Emit Gate 3 using Skeleton A:

```
Gate 3 — Areas
T3-AREAS      : list[string] = [area name list]
T3-AREA-COUNT : integer      = [count of areas]
```

---

## PHASE 4 — ROLE GENERATION

**Input contract:** MUST consume T1-VERDICT (Gate 1), T3-AREAS (Gate 3), T2-IA-PATH (Gate 2).

MUST generate all role files using Skeleton C. MUST place each file at `.roles/{{AREA-NAME}}/{{ROLE-NAME}}.md` where AREA-NAME is drawn from T3-AREAS. FORBIDDEN: role files outside area subdirectories.

**MUST fill all five slots in every Skeleton C instance:**

| Slot | MUST contain |
|------|-------------|
| {{ORIENTATION}} | MUST be one of: builder, steward, connector, challenger, synthesizer |
| {{LENS}} | MUST be a single analytical perspective |
| {{EXPERTISE-LIST}} | MUST list 3-5 comma-separated skills |
| {{SCOPE-TEXT}} | MUST describe ownership and decisions in 2-3 sentences |
| {{COLLABORATES-LIST}} | MUST name 2-4 other roles |

**FORBIDDEN: any Skeleton C instance with an unfilled slot.**  
**FORBIDDEN: any Skeleton C instance missing a slot.**

Role count:
- Standard: MUST produce 20-30 total files (including inertia-advocate from Phase 2). FORBIDDEN: fewer than 20 or more than 36.
- Deep (--depth deep): MUST produce 50+ total files. FORBIDDEN: fewer than 50.

Emit Gate 4 using Skeleton A:

```
Gate 4 — Roles
T4-ROLE-COUNT : integer      = [total role files]
T4-ROLE-PATHS : list[string] = [all role file paths]
T4-AREA-DIRS  : list[string] = [area subdirectories created]
```

---

## PHASE 5 — ORG-CHART.MD GENERATION

**Input contract:** MUST consume T1-PRESSURE (Gate 1), T1-VERDICT (Gate 1), T3-AREAS (Gate 3), T4-ROLE-COUNT (Gate 4), T4-AREA-DIRS (Gate 4), T2-IA-SCOPE-HASH (Gate 2).

Generate `org-chart.md` using Skeleton D. MUST fill every slot.

**Filling `{{ASCII-DIAGRAM}}`:** MUST include minimum 2 org levels. MUST use box-drawing characters. FORBIDDEN: flat name lists. FORBIDDEN: single-level diagrams.

**Filling `{{HEADCOUNT-ROWS}}`:** MUST include one row per area from T3-AREAS. MUST include Decides and Escalates values per row. FORBIDDEN: rows missing Decides or Escalates.

**Filling `{{T1-PRESSURE}}` and `{{T1-VERDICT}}`:** MUST copy values from Gate 1 exactly.

**Filling `{{IA-SCOPE-VERBATIM}}`:** MUST verify first 8 words match T2-IA-SCOPE-HASH. FORBIDDEN: discrepancy between org-chart reference and role file.

**Filling `{{ANTI-PATTERN-ROWS}}`:**

MUST derive categories from T1-VERDICT:

| T1-VERDICT | MUST cite | FORBIDDEN |
|------------|-----------|-----------|
| CAN-OPERATE-FLAT | cat-2, cat-3 | FORBIDDEN: cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | FORBIDDEN: cat-2, cat-3 |

MUST format every "Why It Applies Here" cell as: `[element name] (cat-N) — [reason]`.  
FORBIDDEN: plain prose. FORBIDDEN: cells not opening with the element-citation pattern.

MUST fill every Mitigation cell with a specific remediation action.  
FORBIDDEN: format guidance or descriptive instructions in Mitigation cells.

**Filling `{{RHYTHM-ROWS}}`:** MUST include ROB, shiproom, and minimum one governance row. MUST express every Quorum as `N of M`. FORBIDDEN: percentage or plain-number Quorum.

**Filling `{{CHARTER-BLOCKS}}`:** MUST generate one Skeleton E charter per governance meeting row. MUST fill all 5 slots in every Skeleton E. FORBIDDEN: governance rows without charters. FORBIDDEN: charters with unfilled slots.

**Filling `{{ROADMAP-ROWS}}`:** MUST include minimum 2 rows. MUST make row 1 type `headcount-threshold`. MUST make row 2 a different trigger category. FORBIDDEN: two rows of the same trigger type.

Emit Gate 5 using Skeleton A:

```
Gate 5 — Org Chart
T5-ORGCHART-PATH    : string  = [path to org-chart.md]
T5-SECTIONS-WRITTEN : integer = [count, must equal 6]
T5-IA-SCOPE-VERIFIED: boolean = [true if T2-IA-SCOPE-HASH matches]
```

---

## PHASE 6 — CONSTRAINT-COMPLETENESS SEAL

**Input contract:** MUST consume all Gate variables: T1 through T5.

For every named typed variable, verify its consuming phase governs it with MUST or FORBIDDEN. FORBIDDEN: advisory language in any input contract that governs a named typed variable.

| Variable | Consumed in | Governing language | MUST verify |
|----------|------------|-------------------|-------------|
| T1-PRESSURE | Phase 2 | MUST consume | — |
| T1-PRESSURE | Phase 5 | MUST consume | — |
| T1-VERDICT | Phase 3 | MUST consume | — |
| T1-VERDICT | Phase 4 | MUST consume | — |
| T1-VERDICT | Phase 5 | MUST consume | — |
| T2-IA-PATH | Phase 4 | MUST include in count | — |
| T2-IA-SCOPE-HASH | Phase 5 | MUST verify match | — |
| T3-AREAS | Phase 4 | MUST match area names | — |
| T3-AREAS | Phase 5 | MUST include one row per area | — |
| T4-ROLE-COUNT | Phase 5 | MUST fill headcount | — |
| T5-IA-SCOPE-VERIFIED | Phase 6 | MUST be true | — |

**MUST confirm T5-IA-SCOPE-VERIFIED = true before finalizing.**  
**FORBIDDEN: finalizing output if any verification row fails.**  
**FORBIDDEN: finalizing output if T5-SECTIONS-WRITTEN ≠ 6.**

Emit Gate 6 using Skeleton A:

```
Gate 6 — Seal
T6-ALL-GATES-VERIFIED : boolean = [true if all rows pass]
T6-FAILURES           : list    = [failed rows, empty if clean]
```

**FORBIDDEN: producing final output if T6-ALL-GATES-VERIFIED = false.**
```

---

## Variation Summary

| Version | Axis | Core Bet | Key Criteria Targeted |
|---------|------|----------|-----------------------|
| V-01 | Role sequence | Inertia-first locks verdict before org population | C-08, C-11, C-17, C-13, C-15 |
| V-02 | Output format | Pre-print skeletons with named slots constrain shape | C-22, C-14, C-20, C-02, C-05 |
| V-03 | Lifecycle emphasis | Equal weight per phase with explicit I/O contracts | C-14, C-20, C-21, C-19 |
| V-04 | Phrasing register | Full MUST/FORBIDDEN throughout, zero advisory | C-19, C-21, C-10, C-16 |
| V-05 | Combination (V-01+V-02+V-04) | Inertia-first + skeleton + imperative reinforce each other | C-08–C-22 broad coverage |
