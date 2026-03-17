Now I have full context. The R1 scorecard already exists and shows the predicted scores. My job is to generate the 5 complete variation prompts. Let me produce them.

---

# `/quest:variate` — `draft-spec` — Round 1

**Rubric version**: v1 | **Golden threshold**: all 5 essential pass + composite ≥ 80

---

## V-01 — Role Sequence: Architect-First

**Variation axis**: Role sequence — Architect writes all sections in a single uninterrupted pass; PM and Strategy annotate afterward rather than interleaved.

**Hypothesis**: Deferring role annotations until after the full spec is written reduces role-switching overhead and produces more coherent section prose. Secondary roles annotating a complete document rather than a partial one catch more real issues.

---

You are running `/draft:spec`. Stock role: **Architect**. Secondary roles: **PM**, **Strategy**.

---

### SETUP

Scan `simulations/scout/` for artifacts matching the current topic. Produce the status table before writing any spec content:

```
| # | Artifact Type | File              | Items | Status             |
|---|---------------|-------------------|-------|--------------------|
| 1 | requirements  | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 2 | feasibility   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 3 | compliance    | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 4 | positioning   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
```

Missing artifacts: [list types, or "none"]

**No-scout-context conditional**: If row 1 = NOT FOUND, ask: "No requirements artifact found. Describe the feature in 3–5 sentences so I can extract requirements inline." Do not proceed to EXECUTE until row 1 is resolved.

---

### EXECUTE — Phase 1: Architect Writes

Architect writes all five spec sections in a single pass. Do not pause for role reviews during this phase — all role annotations follow in Phase 2.

**1. Purpose**

State what the feature is, what problem it solves, and who benefits. One paragraph.

Architect traces: [signal source(s) — name the artifact(s) that inform this statement, e.g., "per scout-positioning signal" or "from user intent"]

**2. Requirements**

If scout-requirements = LOADED: extract P0 requirements with R-IDs. State coverage: "Coverage: [N]/[P0 total] P0 requirements covered."
If scout-requirements = NOT FOUND: write exactly: "scout-requirements: NOT FOUND. Coverage criterion waived. Requirements extracted from user intent (IE-01..IE-NN)."

```
| R-ID | Priority | Requirement (abbreviated) | Status  |
|------|----------|---------------------------|---------|
| R-01 | P0       | [text]                    | PENDING |
```

**3. Design**

Describe the data model, key operations, and behavior contracts. Reference R-IDs per design element.

**4. Constraints**

List all constraints. State source for each.

```
| Constraint | Type                    | Source                          | Design Impact |
|------------|-------------------------|---------------------------------|---------------|
| [text]     | tech / biz / compliance | [scout-compliance / tech / biz] | [impact]      |
```

**5. Open Questions**

List open questions that cannot be resolved from available signals. Each references the R-ID or design element it blocks.

---

### EXECUTE — Phase 2: Role Annotations

After all five sections are written, apply the following annotations in order.

**PM annotates** (reviews Requirements section): Does every P0 from scout-requirements have a corresponding spec entry? Record one of:
`PM: PASS — [N]/[P0 total] P0 requirements covered.`
`PM: Finding — [R-ID] has no corresponding spec entry. [Action].`

**Strategy annotates** (reviews Purpose and Design): Does the design reflect competitive differentiation claims from scout-positioning (if loaded)?
`Strategy: PASS — differentiation claim reflected: [claim from scout-positioning].`
`Strategy: Finding — [claim] not reflected in Design. [Action].`

---

### FINDINGS

Self-review. Write each subsection even if the result is "none found."

**Contradictions**: Requirements that conflict with each other in the spec. Name by R-ID.
Write: "[R-XX vs R-YY: description. Resolution or flagging: ___.] " OR write: "Contradictions: none found."

**Gaps**: Requirements with no corresponding spec entry.
Write: "[R-XX: not addressed in spec. Action: ___.] " OR write: "Gaps: none found."

**Ambiguities**: Spec sections where intended behavior is unclear.
Write: "[Section N: ambiguous as written. Clarification: ___.] " OR write: "Ambiguities: none found."

**Hotspots**: Sections disproportionately complex relative to requirement priority.
Write: "[Section N: [N] R-IDs, [pct]%. Recommendation: split / defer / restructure.] " OR write: "Hotspots: none found."

---

### AMENDMENTS

Numbered list. Minimum 2 amendments. Each must trace to a finding above. Vague items ("improve section") do not satisfy.

1. [specific action] — Finding: [type], [R-ID or section]
2. [specific action] — Finding: [type], [R-ID or section]

---

### Output Artifact

Path: `simulations/draft/specs/{topic}-spec-{date}.md`

Frontmatter (all six fields required):
```yaml
---
skill: draft-spec
topic: [slug]
item: [kebab-case name]
date: [YYYY-MM-DD]
skill_version: 0.1.0
input: [file path or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → status table → spec sections 1–5 → role annotations (PM, Strategy) → FINDINGS → AMENDMENTS

---

## V-02 — Output Format: Table-Centric

**Variation axis**: Output format — every section uses a pre-printed table structure; no freeform prose for structured content.

**Hypothesis**: Pre-printed tables with required columns force completeness mechanically. The model cannot omit a field (e.g., cross-namespace source, P0 status) if the column is already named in the template.

---

You are running `/draft:spec`. Stock role: **Architect**. Secondary roles: **PM**, **Strategy**.

---

### SETUP

Scan `simulations/scout/` for artifacts matching the current topic. All four rows must appear in the status table before any spec content is written:

```
| # | Artifact Type | File              | Items | Status             |
|---|---------------|-------------------|-------|--------------------|
| 1 | requirements  | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 2 | feasibility   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 3 | compliance    | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 4 | positioning   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
```

Loaded: [N]. Missing: [list types, or "none"].

**No-scout-context conditional**: If row 1 = NOT FOUND, write: "requirements: NOT FOUND — waiting for user description." Ask for a 3–5 sentence feature description. Do not proceed to EXECUTE until row 1 is resolved.

---

### EXECUTE

Write the five spec sections using the table structures shown.

**1. Purpose**

```
| Field                  | Value                                                                             |
|------------------------|-----------------------------------------------------------------------------------|
| What is it             | [one-line definition]                                                             |
| Problem solved         | [problem statement]                                                               |
| Primary user           | [user/role]                                                                       |
| Cross-namespace signal | [which non-requirements signal informs this — feasibility score, compliance       |
|                        | posture, or positioning differentiator — name the artifact]                       |
```

PM role — does the stated purpose satisfy the user need in scout-requirements?
`PM: PASS — purpose covers stated user need.` OR `PM: Finding — [gap].`

**2. Requirements**

If requirements = LOADED: state coverage count before the table: "Coverage: [N]/[P0 total] P0 requirements covered."
If requirements = NOT FOUND: write: "scout-requirements: NOT FOUND. Coverage criterion waived. Requirements extracted from user intent."

```
| R-ID | Priority | Requirement (abbreviated) | Spec Entry | Status                  |
|------|----------|---------------------------|------------|-------------------------|
| R-01 | P0       | [text]                    | [§N]       | COVERED / UNCOVERED     |
```

**3. Design**

```
| Component | Behavior           | R-IDs Satisfied | Notes |
|-----------|--------------------|-----------------|-------|
| [name]    | [description]      | R-01, R-02      |       |
```

Strategy role — does the design reflect competitive differentiation from scout-positioning (if loaded)?
`Strategy: PASS — [differentiation claim reflected: claim].` OR `Strategy: Finding — [claim not reflected. Action].`

**4. Constraints**

```
| Constraint | Type                    | Source                          | Design Impact |
|------------|-------------------------|---------------------------------|---------------|
| [text]     | tech / biz / compliance | [scout-compliance / tech / biz] | [impact]      |
```

**5. Open Questions**

```
| Q-ID | Question | Blocks               | Severity         |
|------|----------|----------------------|------------------|
| Q-01 | [text]   | [R-ID or §N]         | HIGH / MED / LOW |
```

---

### FINDINGS

```
| Finding-ID | Type          | Description                           | R-IDs or §N | Severity | Action   |
|------------|---------------|---------------------------------------|-------------|----------|----------|
| F-01       | Contradiction | [R-XX vs R-YY: conflict description]  | R-XX, R-YY  | HIGH     | [action] |
| F-02       | Gap           | [requirement not covered in spec]     | R-XX        | MED      | [action] |
| F-03       | Ambiguity     | [unclear spec section]                | §N          | MED      | [action] |
| F-04       | Hotspot       | [§N: [N] R-IDs, [N]%]                 | §N          | LOW      | [action] |
```

If any finding type is absent: add a row with Type = [type] and Description = "[type]: none found."

Coverage (from Requirements table COVERED column): "[N]/[P0 total] P0 requirements covered."

---

### AMENDMENTS

Two or more specific amendments. Each traces to a Findings row above by Finding-ID. Vague items do not satisfy.

1. [specific action] — from F-NN ([type])
2. [specific action] — from F-NN ([type])

---

### Output Artifact

Path: `simulations/draft/specs/{topic}-spec-{date}.md`

Frontmatter (all six fields required):
```yaml
---
skill: draft-spec
topic: [slug]
item: [kebab-case name]
date: [YYYY-MM-DD]
skill_version: 0.1.0
input: [file path or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → status table → spec sections 1–5 → FINDINGS table → AMENDMENTS

---

## V-03 — Lifecycle Emphasis: Gated FINDINGS

**Variation axis**: Lifecycle emphasis — explicit BLOCKED gates between every phase; FINDINGS section uses pre-printed "none" claim text for each of the four required finding types.

**Hypothesis**: Pre-printed "none" claim text structurally prevents silent omission — the model must write either the finding entry or the exact pre-printed "none" text, making absence impossible without producing an explicit artifact.

---

You are running `/draft:spec`. Phases are sequential. A phase marked BLOCKED may not begin until its prerequisite is complete.

Stock role: **Architect**. Secondary roles: **PM**, **Strategy**.

---

### PHASE 1: Setup

Scan `simulations/scout/` for artifacts matching the current topic. Produce the status table:

```
| # | Artifact Type | File              | Items | Status             |
|---|---------------|-------------------|-------|--------------------|
| 1 | requirements  | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 2 | feasibility   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 3 | compliance    | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 4 | positioning   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
```

Missing artifacts: [list types, or "none"]

**No-scout-context conditional**: If row 1 = NOT FOUND, ask: "Describe the feature in 3–5 sentences. I will extract requirements from your description." Do not proceed to Phase 2 until row 1 is resolved.

**PHASE 1 COMPLETE.** Proceed to Phase 2.

---

### PHASE 2: Spec

BLOCKED until Phase 1 is complete.

Write the five spec sections in order. Do not skip or reorder.

**1. Purpose**

State what the feature is, what problem it solves, and who benefits. One paragraph.

Architect traces: [signal source(s) — name the artifact(s) that inform this: "per scout-positioning", "per scout-compliance", "from user intent"]

PM annotates: `PM: [PASS — purpose aligns with stated user need. / Finding: [gap].]`

**2. Requirements**

If requirements = LOADED: list P0 requirements with R-IDs. State: "Coverage: [N]/[P0 total] P0 requirements covered."
If requirements = NOT FOUND: state: "scout-requirements: NOT FOUND. Coverage criterion waived. Requirements extracted from user intent (IE-01..IE-NN)."

```
| R-ID | Priority | Requirement (abbreviated) | Spec Entry |
|------|----------|---------------------------|------------|
| R-01 | P0       | [text]                    | PENDING    |
```

**3. Design**

Describe the data model, operations, and behavior contracts. Reference R-IDs per design element.

Strategy annotates: `Strategy: [PASS — competitive differentiation reflected: [claim from scout-positioning]. / Finding: [claim not reflected. Action: ___].]`

**4. Constraints**

```
| Constraint | Type                    | Source                          | Design Impact |
|------------|-------------------------|---------------------------------|---------------|
| [text]     | tech / biz / compliance | [scout-compliance / tech / biz] | [impact]      |
```

All scout-compliance blocking constraints must appear here.

**5. Open Questions**

List open questions. Each references the R-ID or design element it blocks.

**PHASE 2 COMPLETE.** Proceed to Phase 3.

---

### PHASE 3: Findings

BLOCKED until Phase 2 is complete.

The following four finding types are required. For each type: write the finding entry using the template, OR write the pre-printed "none" claim. Absence of a finding type is a structural fail.

**3a. Contradictions**
`[R-XX vs R-YY: [description of conflict]. Resolution: [decision or "open — flagged for author"].]`
OR pre-print exactly:
`Contradictions: none found.`

**3b. Gaps**
`[R-XX: no corresponding spec entry. Action: [add to Design / defer to backlog / scope-out].]`
OR pre-print exactly:
`Gaps: none found.`

**3c. Ambiguities**
`[Section [N]: ambiguous as written. Clarification needed: [question or suggested rewrite].]`
OR pre-print exactly:
`Ambiguities: none found.`

**3d. Hotspots**
`[Section [N] ([name]): [N] R-IDs ([pct]% of total). Recommendation: [split / defer lower-priority R-IDs / restructure].]`
OR pre-print exactly:
`Hotspots: none found.`

Coverage summary: "[N]/[P0 total] P0 requirements covered." (or waiver statement if NOT FOUND)

**PHASE 3 COMPLETE.** Proceed to Phase 4.

---

### PHASE 4: Amend

BLOCKED until Phase 3 is complete.

Numbered list. Minimum 2 amendments. Each traces to a specific Phase 3 finding by type and source (R-ID or section). Vague items ("improve section 2") do not satisfy.

1. [specific action] — Finding type: [contradiction / gap / ambiguity / hotspot], source: [R-ID or §N]
2. [specific action] — Finding type: [type], source: [R-ID or §N]

If all Phase 3 checks returned "none found": write `Amendments: none required. All Phase 3 checks passed.`

---

### Output Artifact

Path: `simulations/draft/specs/{topic}-spec-{date}.md`

Frontmatter (all six fields required):
```yaml
---
skill: draft-spec
topic: [slug]
item: [kebab-case name]
date: [YYYY-MM-DD]
skill_version: 0.1.0
input: [file path or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → status table → spec sections 1–5 (with role annotations) → Findings 3a–3d + coverage → Amendments

---

## V-04 — Phrasing Register: Conversational

**Variation axis**: Phrasing register — conversational, first-person imperative throughout; plain-language section names; minimal formal structure.

**Hypothesis**: A conversational register reduces cognitive overhead and produces more natural model output. The tradeoff is weaker structural guarantees — instructions replace pre-printed templates.

---

You're running `/draft:spec`. Your role is **Architect**. You'll also get brief input from **PM** and **Strategy** as you go.

---

### Step 1: Find what already exists

Start by scanning `simulations/scout/` for anything related to this topic. You're looking for requirements, feasibility, compliance, and positioning artifacts.

Write down what you found — and what's missing:

```
What I found:
- requirements: [filename] — LOADED / NOT FOUND
- feasibility:  [filename] — LOADED / NOT FOUND
- compliance:   [filename] — LOADED / NOT FOUND
- positioning:  [filename] — LOADED / NOT FOUND

Missing: [list them, or "nothing — all present"]
```

**If requirements is NOT FOUND**: Don't guess. Ask the user: "I didn't find a requirements artifact. Tell me what this feature is supposed to do in 3–5 sentences and I'll work from that." Wait for the answer before continuing.

---

### Step 2: Write the spec

Write the five sections in order. Don't skip or swap them.

**Purpose**: What is this feature? What problem does it solve? Who uses it? One paragraph. Reference your sources by name if you have them.

**Requirements**: If you loaded a requirements artifact, list the P0 requirements with their R-IDs. Write: "[N] out of [P0 total] P0 requirements are covered in this spec." If you didn't load one, write: "No requirements artifact loaded — working from user description. Coverage criterion not applicable."

PM says: [PASS — every P0 is accounted for. / Finding: [which one is missing and why it matters].]

**Design**: Describe the main design — data model, key operations, how the pieces fit together. Point back to the R-IDs that each design element serves.

Strategy says: [PASS — the design reflects what makes this different from the competition. / Finding: [what's missing and what to do about it].]

**Constraints**: List what can't change, can't be assumed, or has external requirements. For each one, say where it came from — is it a compliance finding? a technical limitation? a business rule?

**Open Questions**: What's still unclear? For each question, say what it blocks — which requirement or design decision can't proceed until it's answered.

---

### Step 3: Review your work

Go through your spec and look for four things. This step is required. Do not skip a category — write something for each one, even if the answer is "none."

**Contradictions**: Do any requirements conflict with each other in your spec? Name them by ID. Say how you resolved it, or flag it as open.
[Your findings here. If none: write "No contradictions found."]

**Gaps**: Are there requirements that don't have a home in the spec?
[Your findings here. If none: write "No gaps found."]

**Unclear parts**: Are there sections where someone reading the spec wouldn't know what to build?
[Your findings here. If none: write "No ambiguities found."]

**Heavy sections**: Are there sections trying to do too much — covering too many requirements for their importance level?
[Your findings here. If none: write "No hotspots found."]

---

### Step 4: Fix list

Based on what you found in Step 3, write at least 2 specific things to fix. Don't write vague items like "improve section 2" — write what specifically needs to change and why, pointing back to the finding that surfaced it.

1. [specific fix] — because [finding from Step 3]
2. [specific fix] — because [finding from Step 3]

---

### Output file

Save to: `simulations/draft/specs/{topic}-spec-{date}.md`

Start the file with:
```yaml
---
skill: draft-spec
topic: [slug]
item: [kebab-case name]
date: [YYYY-MM-DD]
skill_version: 0.1.0
input: [file path or "freeform: [first 10 words of description]"]
---
```

Order in the file: frontmatter → what you found (Step 1) → spec (Step 2) → review (Step 3) → fix list (Step 4)

---

## V-05 — Combined: Architect-First + Gated FINDINGS

**Variation axes**: Role sequence (Architect-first, Phase 2) + Lifecycle emphasis (BLOCKED gates + pre-printed "none" paths in Phase 3).

**Hypothesis**: These axes guard complementary rubric surface. Architect-first (V-01 axis) secures section presence and role annotation visibility. Gated FINDINGS (V-03 axis) secures finding completeness. Together they leave no essential criterion unguarded by structure.

---

You are running `/draft:spec`. Phases are sequential. A phase marked BLOCKED may not begin until its prerequisite is complete. Absence of any required output element is a structural fail.

Stock role: **Architect**. Secondary roles: **PM**, **Strategy**.

---

### PHASE 1: Setup

Scan `simulations/scout/` for artifacts matching the current topic. All five rows must appear before any spec content is written:

```
| # | Artifact Type | File              | Items | Status             |
|---|---------------|-------------------|-------|--------------------|
| 1 | requirements  | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 2 | feasibility   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 3 | compliance    | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 4 | positioning   | [filename or "—"] | [N]   | LOADED / NOT FOUND |
| 5 | [other]       | [filename or "—"] | [N]   | LOADED / NOT FOUND |
```

Missing artifacts: [list types, or "none"]

**No-scout-context conditional**: If row 1 = NOT FOUND, write: "requirements: NOT FOUND — waiting for user intent." Ask: "Describe the feature in 3–5 sentences. Strategy will extract requirements from your description." Do not proceed to Phase 2 until row 1 is resolved.

BLOCKED: Spec may not begin until this table is complete and row 1 is LOADED or user intent is recorded.

---

### PHASE 2: Execute — Architect Writes

BLOCKED until Phase 1 is complete.

Architect writes all five spec sections in a single uninterrupted pass. Role annotations follow in Phase 2b — do not pause to annotate during Phase 2.

**1. Purpose**

State what the feature is, what problem it solves, and who benefits. One paragraph.

Architect traces: [signal source(s) — name the artifact(s): "per scout-positioning signal", "per scout-compliance", "from user intent", etc.]

**2. Requirements**

If requirements = LOADED: list P0 requirements with R-IDs. Pre-print: "Coverage: [N]/[P0 total] P0 requirements covered."
If requirements = NOT FOUND: write exactly: "scout-requirements: NOT FOUND. Coverage criterion waived. Requirements extracted from user intent (IE-01..IE-NN). Run /scout:requirements before implementation."

```
| R-ID | Priority | Requirement (abbreviated) | §     | Status  |
|------|----------|---------------------------|-------|---------|
| R-01 | P0       | [text]                    | [§N]  | PENDING |
```

**3. Design**

Describe the data model, operations, and behavior contracts. Each element references the R-IDs it satisfies.

**4. Constraints**

```
| Constraint | Type                    | Source                          | Design Impact |
|------------|-------------------------|---------------------------------|---------------|
| [text]     | tech / biz / compliance | [scout-compliance / tech / biz] | [impact]      |
```

All scout-compliance blocking constraints must appear. Source column must name the artifact.

**5. Open Questions**

List open questions. Each references the R-ID or design element it blocks.

---

### PHASE 2b: Role Annotations

After all five sections are written, apply annotations in order. Do not annotate during Phase 2 — annotations are separate from authoring.

**PM annotates** (reviews Requirements):
`PM: [PASS — [N]/[P0 total] P0 requirements covered. / Finding: [R-ID] not covered. Action: ___.]`

**Strategy annotates** (reviews Purpose and Design for competitive differentiation):
`Strategy: [PASS — differentiation reflected: [claim from scout-positioning]. / Finding: [claim not reflected. Action: ___].]`

---

### PHASE 3: Findings

BLOCKED until Phase 2b is complete.

The following four finding types are required. For each: write the finding entry using the pre-printed template, OR write the pre-printed "none" claim. Absence of any finding type is a structural fail.

**Contradictions**:
`[R-XX vs R-YY: [conflict]. Resolution: [decision or "open — flagged"].]`
OR pre-print exactly:
`Contradictions: NONE.`

**Gaps**:
`[R-XX: no spec entry. Action: [add to Design / defer / scope-out].]`
OR pre-print exactly:
`Gaps: NONE.`

**Ambiguities**:
`[Section [N]: ambiguous as written. Clarification: [question or rewrite].]`
OR pre-print exactly:
`Ambiguities: NONE.`

**Hotspots**:
`[Section [N] ([name]): [N] R-IDs ([pct]%). Recommendation: [split / defer / restructure].]`
OR pre-print exactly:
`Hotspots: NONE.`

Coverage: "Coverage: [N]/[P0 total] P0 requirements covered." (or waiver if NOT FOUND)

BLOCKED: Amendments may not be written until all four finding types above are resolved — entry or "NONE" claim present for each.

---

### PHASE 4: Amend

BLOCKED until Phase 3 is complete.

Numbered list. Minimum 2 specific amendments. Each traces to a Phase 3 finding by type and source. Vague items do not satisfy.

1. [specific action] — [finding type]: [R-ID or §N]
2. [specific action] — [finding type]: [R-ID or §N]

If all Phase 3 finding types returned "NONE": write `Amendments: none required. All Phase 3 checks returned NONE.`

---

### Output Artifact

Path: `simulations/draft/specs/{topic}-spec-{date}.md`

Frontmatter (all six fields, hard fail if any missing):
```yaml
---
skill: draft-spec
topic: [slug]
item: [kebab-case name]
date: [YYYY-MM-DD]
skill_version: 0.1.0
input: [file path or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → status table → spec sections 1–5 → role annotations (PM, Strategy) → Findings (contradictions, gaps, ambiguities, hotspots, coverage) → Amendments

---

## Predicted Scores

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 Structure | 12 | 12 | 12 | 12 | 12 | 12 |
| C-02 Scout status table | 12 | 12 | 12 | 12 | 12 | 12 |
| C-03 P0 coverage | 12 | 12 | 12 | 12 | **6** | 12 |
| C-04 Self-review findings | 12 | **6** | **6** | 12 | **6** | 12 |
| C-05 Frontmatter | 12 | 12 | 12 | 12 | 12 | 12 |
| C-06 Secondary role | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 Contradiction detection | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 Amendment list | 10 | 10 | 10 | 10 | **6** | 10 |
| C-09 No-scout fallback | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 Cross-namespace coherence | 5 | 5 | 5 | **2.5** | **2.5** | 5 |
| **Total** | **100** | **94** | **94** | **97.5** | **81.5** | **100** |

**Predicted ranking**: V-05 > V-03 > V-01 = V-02 > V-04

**Key differentiation**:

- **C-04 split** (V-01/V-02/V-04 PARTIAL vs V-03/V-05 PASS): V-01 and V-02 instruct the model to write "none found" — V-03 and V-05 pre-print the exact claim text, making absence structurally impossible.
- **V-04 weakness**: Conversational register trades structural enforcement for naturalness. C-03 is instruction-only (no template), C-08 has no hotspot table, and C-10 has no dedicated cross-namespace field — three partial-point risks vs one in V-01/V-02.
- **V-05 advantage over V-03**: The Architect-first pass (Phase 2 / Phase 2b split) makes role annotation visibility explicit in the document. V-03 has role annotations inline during authoring, which allows the model to compress or skip them during a dense authoring pass.
