I have everything needed. Here are the 5 complete variations for Round 2, targeting rubric v2. The existing R2 session used: Inertia-Anchor-first, Signal-Synthesis-first, per-finding gates, combined anchor+synthesis, and augmented-golden. These 5 explore orthogonal axes.

---

# `/quest:variate` — `draft-spec` — Round 2

```
skill: quest:variate
target_skill: draft-spec
rubric_version: v2
date: 2026-03-14
round: R2
```

**Variation axes selected**:
- V-01 (single): Role sequence — PM-first coverage contract
- V-02 (single): Output format — full pre-printed document skeleton
- V-03 (single): Lifecycle emphasis — numbered checklist exit gates
- V-04 (combo): Phrasing register (conversational) + inertia framing per section
- V-05 (combo): Signal register pre-loading step + structural axis declaration block

---

## V-01 — PM-First Coverage Contract

**Axis**: Role sequence — PM maps P0 requirements to sections before Architect writes a word.
**Hypothesis**: When PM owns section-to-requirement assignment upfront, coverage is structural rather than voluntary — Architect fills a contract, not a blank page. Inline secondary role annotations in each section satisfy C-12 without requiring gate token machinery.

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.

Roles: PM (coverage step) | Architect (spec authoring) | Strategy, Compliance, Design (inline per section)
```

---

**SETUP**

Scan `simulations/scout/` for `{{topic}}` artifacts. Output this table before any other content:

| Row | Artifact type | Filename pattern | File found | Status |
|-----|--------------|-----------------|------------|--------|
| 1 | scout-requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | scout-feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | scout-market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | scout-compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | scout-stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | scout-naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | scout-positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

**No-scout-context conditional**: If Row 1 = NOT FOUND and all rows = NOT FOUND, stop here and respond: "No scout context for `{{topic}}`. Describe the feature in 3–5 sentences. I will derive requirements and proceed from your description." Do not write any EXECUTE content until Row 1 = LOADED or a user description is provided.

---

**PM COVERAGE STEP**

PM runs before Architect writes any prose. PM's task: review the loaded scout-requirements artifact and assign every requirement to one of the five prescribed sections.

Output this table:

| R-ID | Requirement (abbreviated) | Priority | Assigned section | Cross-namespace signal |
|------|--------------------------|----------|-----------------|----------------------|
| R-01 | | P0 | [Purpose / Requirements / Design / Constraints / Open Questions] | [name a signal from a non-requirements artifact — feasibility score, compliance posture, positioning differentiator — and the artifact filename; or: NOT FOUND] |
| R-02 | | P0 | | |
| ... | | | | |

Rules:
- Every P0 requirement gets a row. P1+ requirements: include or note "deferred."
- Assigned section: one of the five prescribed names only — no invented sections.
- Cross-namespace signal: if a non-requirements artifact provides relevant context for this requirement, name both the signal and the artifact. NOT FOUND is a valid, explicit value.
- If Row 1 = NOT FOUND: state "Waived — scout-requirements NOT FOUND. PM derives from loaded artifacts or user description." Use R-IE-01, R-IE-02, etc., Priority = INFERRED.

End the PM step with: `PM coverage statement: [N]/[P0 total] P0 requirements assigned to sections.`

---

**EXECUTE**

Architect writes the five sections in this exact order. Do not reorder, rename, or omit any section. Additional sections may be appended after Section 5 only.

---

**Section 1 — Purpose**

Write 2–4 sentences covering what this feature does, who it serves, and why it exists now.

Pre-printed table — Architect must complete or leave cells visibly blank:

| Field | Value |
|-------|-------|
| What it does | |
| Who it serves | |
| Why it exists now | |
| Cross-namespace signal | [name a signal from a non-requirements loaded artifact — feasibility score, compliance posture, positioning differentiator — with the artifact filename; or leave blank if none loaded] |
| Source artifact | |

> **[PM inline]** Does this purpose align with the problem identified in the coverage step? PASS, or name the misalignment:

---

**Section 2 — Requirements**

P0 requirements covered: ___/___ *(state this count before the table; or "Waived — scout-requirements NOT FOUND" if PM waived above)*

| R-ID | Requirement (abbreviated) | Priority | Spec entry | Status |
|------|--------------------------|----------|------------|--------|
| | | P0 | [name the design component, constraint, or section element this requirement maps to — not just "covered"] | COVERED / GAP |
| | | P0 | | COVERED / GAP |
| | | P1 | | |

Rules: Spec entry must be specific ("Design: retry-backoff component"). Conflicts: add a note in the Spec entry cell: "Conflict: R-XX vs R-YY — [description]."

> **[Strategy inline]** Are any requirements in tension with market, positioning, or feasibility signals from loaded artifacts? PASS, or name the conflict (R-IDs + source artifact):

---

**Section 3 — Design**

Describe the implementation approach: major components, key decisions, data flow. Reference R-IDs where design decisions respond to requirements. If the cross-namespace signal from Section 1 shapes a design choice, trace it explicitly (e.g., "feasibility score < 70 from [artifact] → constrain scope to Phase 1 only").

> **[Design inline]** Does this design satisfy any UX, interaction, or naming constraints from loaded scout artifacts? PASS, or name the gap and source artifact:

---

**Section 4 — Constraints**

List constraints with source artifact and type.

| Constraint | Type | Source artifact | Priority |
|-----------|------|----------------|----------|
| | technical / compliance / time / resource | | |

> **[Compliance inline]** Are compliance constraints accurately captured? Any missing from loaded scout-compliance artifact? PASS or finding:

---

**Section 5 — Open Questions**

List deferred decisions, unknowns, blocking dependencies.

| # | Question | Blocking dependency | Recommended next action |
|---|---------|--------------------|-----------------------|
| 1 | | | |
| 2 | | | |

---

**FINDINGS**

Architect self-review. For each category: write a specific finding or state "None found" explicitly. An empty category without a written claim is a fail.

- **Contradictions**: Name by R-ID pair. Propose a resolution or flag for amendment. (e.g., "R-06 vs R-10: [conflict]. Proposed: [resolution].")
- **Gaps**: Requirements or design areas not addressed.
- **Ambiguities**: Statements needing clarification before implementation.
- **Hotspots**: High-risk areas requiring close review.

---

**AMENDMENTS**

Numbered list, minimum 2 items. Each item must name the section, state the specific change, and reference the finding. Vague items ("improve the requirements section") do not satisfy.

Format: `N. Section [name] — [specific change] — Addresses: [finding category, element name or R-ID]`

---

**OUTPUT**

Write artifact to `simulations/draft/specs/{{topic}}-spec-{{date}}.md`.

Frontmatter (all fields required — missing any field is a hard fail):

```yaml
---
skill: draft-spec
topic: {{topic}}
item: spec
date: {{date}}
skill_version: 0.1.0
input: [comma-separated LOADED artifact filenames; or "freeform: [first 10 words of user description]"]
---
```

Document order: frontmatter → SETUP table → PM Coverage step → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Findings → Amendments

---

## V-02 — Full Pre-Printed Document Skeleton

**Axis**: Output format — the entire output is a pre-printed document skeleton; every required element is a named blank cell or pre-printed row. No phases, no gate tokens. Just fill in the structure.
**Hypothesis**: Pre-printing every required element as a named blank makes structural omission impossible without active effort — you cannot accidentally skip a cell that's waiting to be filled.

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.

Your task: fill in this complete spec skeleton. Every blank cell or [placeholder] must be completed.
A cell left empty when it is not marked optional is a structural failure.

Roles invoked inline: PM (Section 2), Strategy (Section 3), Compliance (Section 4).
```

---

**BLOCK 1 — Scout artifact status**

*(Complete before any other block. Every row required.)*

| Row | Artifact type | Filename pattern | File found | Status |
|-----|--------------|-----------------|------------|--------|
| 1 | scout-requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | scout-feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | scout-market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | scout-compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | scout-stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | scout-naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | scout-positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

**No-scout-context conditional**: If all 7 rows = NOT FOUND, write in BLOCK 1: "Fallback activated — no scout artifacts found. User description required: 'Describe the feature in 3–5 sentences.' Proceeding with freeform input." Then continue filling the skeleton using the user's description.

---

**BLOCK 2 — Section 1: Purpose**

| Field | Value |
|-------|-------|
| What this feature does | [2–3 sentences] |
| Who it serves | [user role or persona] |
| Why it exists now | [timing rationale] |
| **Cross-namespace signal** | **[name a signal from a non-requirements artifact — feasibility score / compliance posture / positioning differentiator / market insight — with the artifact filename. Leave blank if none loaded — the blank is a visible gap.]** |
| Signal source artifact | [filename or NOT FOUND] |

> **[PM inline — Purpose]**: Does the stated purpose reflect the core user problem? PASS, or state the misalignment:

---

**BLOCK 3 — Section 2: Requirements**

P0 requirements covered: ___/___ *(fill this count before the table)*

*(If scout-requirements NOT FOUND: write "Waived — scout-requirements NOT FOUND" here and derive requirements from loaded artifacts or user description, marking Priority as INFERRED.)*

| R-ID | Requirement text | Priority | Spec entry | Status |
|------|-----------------|----------|------------|--------|
| R-01 | | P0 | [specific design component, constraint, or open question name] | COVERED / GAP |
| R-02 | | P0 | | COVERED / GAP |
| R-03 | | P1 | | COVERED / GAP |
| *(add rows for all requirements)* | | | | |

Conflicts: for any pair of R-IDs in conflict, add a row:

| Conflict | R-ID A | R-ID B | Description | Resolution / Flag |
|---------|--------|--------|-------------|------------------|
| | | | | |

*(Write "No conflicts detected" if none.)*

> **[Strategy inline — Requirements]**: Does the requirement set form a coherent product story, or does it conflict with positioning or market signals? PASS, or name the tension (R-IDs + artifact):

---

**BLOCK 4 — Section 3: Design**

| Component | Responsibility | Key decision | R-IDs addressed | Cross-namespace constraint |
|-----------|---------------|-------------|----------------|--------------------------|
| | | | | [feasibility constraint / compliance constraint / NOT FOUND] |
| | | | | |
| | | | | |

Design narrative (2–4 sentences connecting the components to the purpose):

> [write here]

> **[Design inline — Design]**: Does this design satisfy UX, interaction, or naming constraints from loaded scout artifacts? PASS, or name the gap:

---

**BLOCK 5 — Section 4: Constraints**

| Constraint | Type | Source artifact | Impact |
|-----------|------|----------------|--------|
| | technical / compliance / time / resource | | |
| | | | |

> **[Compliance inline — Constraints]**: Are compliance constraints from scout-compliance accurately represented? PASS, or name the missing item:

---

**BLOCK 6 — Section 5: Open Questions**

| # | Question | Blocking dependency | Next action |
|---|---------|--------------------|-----------| 
| 1 | | | |
| 2 | | | |

---

**BLOCK 7 — Findings**

*(For each row: write a specific finding or write "None found" — do not leave the Finding column blank.)*

| Category | Finding | Severity |
|---------|---------|---------|
| Contradictions | | |
| Gaps | | |
| Ambiguities | | |
| Hotspots | | |

---

**BLOCK 8 — Amendments**

*(Minimum 2 rows. Cite the section and finding. Vague entries like "improve section 2" do not satisfy.)*

| # | Target section | Specific change | Finding addressed |
|---|--------------|----------------|-----------------|
| 1 | | | |
| 2 | | | |

---

**BLOCK 9 — Output artifact**

Write to `simulations/draft/specs/{{topic}}-spec-{{date}}.md`.

```yaml
---
skill: draft-spec
topic: {{topic}}
item: spec
date: {{date}}
skill_version: 0.1.0
input: [LOADED artifact filenames, comma-separated; or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → Block 1 → Block 2 → Block 3 → Block 4 → Block 5 → Block 6 → Block 7 → Block 8

---

## V-03 — Numbered Checklist Exit Gates

**Axis**: Lifecycle emphasis — every phase ends with a numbered checklist the model must confirm before proceeding. No BLOCKED tokens, no gate token machinery.
**Hypothesis**: Numbered checklist exits surface omissions at phase boundaries without requiring structured token emission — a model that resists gate tokens but completes checklists will produce more complete output.

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.
Roles: Architect (primary) | PM, Strategy, Compliance, Design (inline per section)

Protocol: Each phase ends with a numbered CONFIRM list. Check every item before proceeding.
A missing CONFIRM item means the phase is incomplete. Fix it, then confirm.
```

---

**PHASE 1 — Setup**

Scan `simulations/scout/` for `{{topic}}` artifacts. Output this table:

| Row | Artifact type | Filename pattern | File found | Status |
|-----|--------------|-----------------|------------|--------|
| 1 | scout-requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | scout-feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | scout-market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | scout-compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | scout-stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | scout-naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | scout-positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

**No-scout-context conditional**: If all 7 rows = NOT FOUND, write: "Fallback: no scout context found. Requesting 3–5 sentence feature description from user before proceeding." Do not advance to Phase 2 until Row 1 resolves.

**Phase 1 CONFIRM** (write each line before advancing):
```
[ ] 1. Status table written with one row per artifact type (7 rows total)
[ ] 2. Every row has an explicit LOADED or NOT FOUND value
[ ] 3. All LOADED files are read and loaded into context
[ ] 4. No-scout fallback: either not triggered, or conditional stated and user description received
```

---

**PHASE 2 — Spec authoring**

Write the five sections in this exact order. After completing each section, write its CONFIRM list.

---

**Section 1 — Purpose**

Write 2–4 sentences: what, who, why now. Include at least one signal from a non-requirements loaded artifact; if none are loaded, write: "Cross-namespace signal: NOT FOUND — no feasibility, compliance, positioning, or market artifact loaded."

Pre-printed signal row — complete or leave visibly blank:

| Cross-namespace signal | [feasibility score / compliance posture / positioning differentiator / market insight — name artifact; blank = visible gap] |
|------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Source artifact | |

> **[PM inline]** Does this purpose reflect the user's actual problem? PASS or finding:

**Section 1 CONFIRM**:
```
[ ] 1. Purpose written (2–4 sentences)
[ ] 2. Cross-namespace signal row completed or left visibly blank (not omitted)
[ ] 3. PM inline annotation written with PASS or a named finding
```

---

**Section 2 — Requirements**

P0 requirements covered: ___/___ *(before the table; or "Waived — scout-requirements NOT FOUND" with that statement explicitly written)*

| R-ID | Requirement (abbreviated) | Priority | Spec entry | Status |
|------|--------------------------|----------|------------|--------|
| | | P0 | [specific component, constraint, or question name — not generic] | COVERED / GAP |
| | | P0 | | COVERED / GAP |
| | | P1 | | |

Contradictions: name any conflicting pairs by R-ID with a resolution or flag. ("R-06 vs R-10: [conflict]. Flagged for Amendment 1.")

> **[Strategy inline]** Are requirements coherent with positioning or market signals? PASS or named conflict (R-IDs + artifact):

**Section 2 CONFIRM**:
```
[ ] 1. Coverage count stated (or waiver explicitly written)
[ ] 2. Every P0 requirement has a row with a named Spec entry
[ ] 3. Contradictions: either named pairs listed or "no contradictions detected" written
[ ] 4. Strategy annotation written with PASS or named finding
```

---

**Section 3 — Design**

Describe implementation: major components, decisions, data flow. Reference R-IDs. Trace any cross-namespace signal from Section 1 to a specific design choice if applicable.

> **[Design inline]** Does design satisfy UX/naming constraints from loaded artifacts? PASS or gap with source artifact:

**Section 3 CONFIRM**:
```
[ ] 1. Major components listed with responsibilities
[ ] 2. At least one R-ID referenced
[ ] 3. Design annotation written with PASS or named finding
```

---

**Section 4 — Constraints**

| Constraint | Type | Source artifact | Notes |
|-----------|------|----------------|-------|
| | technical / compliance / time / resource | | |

> **[Compliance inline]** Any compliance constraints missing? PASS or finding with source:

**Section 4 CONFIRM**:
```
[ ] 1. At least one constraint listed
[ ] 2. Source artifact named for each constraint (or "Architect judgment" if no artifact)
[ ] 3. Compliance annotation written with PASS or finding
```

---

**Section 5 — Open Questions**

| # | Question | Blocking dependency | Next action |
|---|---------|--------------------|-----------| 
| 1 | | | |

**Section 5 CONFIRM**:
```
[ ] 1. At least one open question listed
[ ] 2. Next action specified for each question
```

---

**Phase 2 CONFIRM** (after all 5 sections):
```
[ ] 1. All five sections present: Purpose, Requirements, Design, Constraints, Open Questions
[ ] 2. Sections appear in prescribed order — no reordering
[ ] 3. Cross-namespace signal row present in Section 1
[ ] 4. Per-row Spec entry and Status columns present in Section 2
[ ] 5. At least one inline role annotation in Sections 2, 3, and 4
```

---

**PHASE 3 — Findings**

Address each category. Write a specific finding or explicitly state "None found." An empty category without a written claim is incomplete.

- **Contradictions**: Name by R-ID pair. Resolution or amendment flag required.
- **Gaps**: Requirements or areas not addressed.
- **Ambiguities**: Statements needing clarification.
- **Hotspots**: High-risk areas.

**Phase 3 CONFIRM**:
```
[ ] 1. All four categories addressed (finding written or "None found" stated)
[ ] 2. Contradictions: if any, named by R-ID pair with resolution or flag
```

---

**PHASE 4 — Amendments**

Numbered list, minimum 2 items. Each must name the section, specify the exact change, and cite the finding. Generic items ("improve section 2") do not pass.

**Phase 4 CONFIRM**:
```
[ ] 1. At least 2 amendment items
[ ] 2. Each item names a section
[ ] 3. Each item cites a finding category and element
[ ] 4. No vague items ("improve...", "enhance...", "revise...")
```

---

**OUTPUT**

Write artifact to `simulations/draft/specs/{{topic}}-spec-{{date}}.md`.

```yaml
---
skill: draft-spec
topic: {{topic}}
item: spec
date: {{date}}
skill_version: 0.1.0
input: [LOADED artifact filenames; or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → Phase 1 table → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Findings → Amendments

---

## V-04 — Conversational Register + Per-Section Inertia Framing

**Axes**: Phrasing register (conversational) + inertia framing (what does the status quo miss here?) at each section boundary.
**Hypothesis**: Asking "what would teams do without this?" before writing each section produces more grounded, differentiated spec content than command-register prompts — because it forces the Architect to articulate value before describing implementation.

---

```
You're writing a spec for `{{topic}}` using the `draft-spec` skill.

You're the Architect. PM, Strategy, Compliance, and Design are available to give you quick checks
inline. Inertia framing is included — at each section, you'll consider what teams do today without
this feature, so your spec explicitly addresses real workflow gaps rather than just feature lists.
```

---

**Step 1 — What scout artifacts exist?**

Before writing anything else, check `simulations/scout/` for `{{topic}}` artifacts and fill in this table:

| Row | What you're looking for | Pattern | What you found | Status |
|-----|------------------------|---------|----------------|--------|
| 1 | Requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | Feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | Market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | Compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | Stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | Naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | Positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

**If nothing is loaded (all NOT FOUND)**: Let the user know — "I don't have any scout context for `{{topic}}` yet. Give me a 3–5 sentence description of what this feature should do and I'll spec it from that." Don't proceed with the spec sections until you have Row 1 content.

Read everything that's loaded before you start writing.

---

**Step 2 — Write the spec**

Work through these five sections in order. Don't skip, reorder, or rename any of them.

---

**Section 1 — Purpose**

*Before writing: think about what teams do today when this feature doesn't exist. What workaround do they use? What does that workaround cost them? Your purpose statement should make the value of this feature concrete against that baseline.*

Write 2–4 sentences: what `{{topic}}` does, who it helps, why it matters now.

Then fill in this table — the cross-namespace signal row is always here; leave it blank if you have nothing to fill in (that blank is itself a finding):

| Purpose field | Your answer |
|--------------|-------------|
| What it does | |
| Who it serves | |
| Why now, not later | |
| **Cross-namespace signal** | **[If you have a feasibility score, compliance posture, positioning signal, or market insight loaded — name it here and name the artifact it comes from. If not: leave blank.]** |
| Signal source | |

> *PM check: does this purpose statement address the real user problem you saw in requirements? Quick PASS or one-sentence finding:*

---

**Section 2 — Requirements**

*Before writing: without this feature, what do teams do? If the status quo is "build it manually each time" or "write a script," note that as context for why these requirements exist.*

State how many P0 requirements you're covering: **P0 requirements covered: ___/___** (or "Waived — scout-requirements NOT FOUND" if requirements weren't loaded)

Now list them:

| R-ID | What it says (brief) | Priority | Which part of the spec covers it | Covered? |
|------|---------------------|----------|----------------------------------|---------|
| | | P0 | [name the design component, constraint, or open question — be specific] | COVERED / GAP |
| | | P0 | | COVERED / GAP |
| | | P1 | | |

If two requirements conflict, note it in the "Which part covers it" cell: "Conflict with R-XX — [one-sentence description]."

> *Strategy check: do these requirements tell a coherent story, or does any of them cut against a positioning or market signal you loaded? PASS or one-sentence finding with the R-IDs involved:*

---

**Section 3 — Design**

*Before writing: the status quo approach is [what teams do today]. Your design should make it explicit how this feature replaces or improves that. Reference R-IDs where a design decision directly resolves a requirement. If a feasibility or compliance signal from Step 1 shapes this design, say so and name the artifact.*

Describe the implementation: key components, how they connect, what decisions you made and why.

> *Design check: does anything here conflict with UX, naming, or interaction constraints from loaded scout artifacts? PASS or finding with the artifact name:*

---

**Section 4 — Constraints**

*Before writing: inertia often hides compliance or technical constraints that teams discover late. Check your loaded compliance and feasibility artifacts — what do they tell you?*

List the constraints. Be specific about where each one comes from.

| What the constraint is | Type | Where it comes from | Why it matters |
|-----------------------|------|---------------------|---------------|
| | technical / compliance / time / resource | [artifact filename or "Architect judgment"] | |

> *Compliance check: any hard compliance constraints missing from this list? Check your loaded scout-compliance artifact. PASS or finding:*

---

**Section 5 — Open Questions**

*These are things you can't resolve from the current scout signals. Each should point to where the answer would come from.*

| Question | What's blocking it | What would resolve it |
|---------|---------------------|----------------------|
| | | |
| | | |

---

**Step 3 — Self-review**

Now step back and look at what you wrote. For each of these categories, write a specific finding or say "None found" — don't leave any category blank:

- **Contradictions** — any two requirements or constraints pulling in opposite directions? Name them by ID and propose a resolution or flag for amendment.
- **Gaps** — anything the spec doesn't address that it should?
- **Ambiguities** — any statement that could be interpreted multiple ways before implementation?
- **Hotspots** — anything that looks fragile or risky?

---

**Step 4 — Amendments**

Write at least 2 specific, actionable items based on what you found in Step 3. Each one should name the section it applies to and say exactly what needs to change. Generic items ("improve the design section") don't count.

Format: `N. [Section name] — [exactly what to change] — from: [which finding]`

---

**Output**

Save your spec to `simulations/draft/specs/{{topic}}-spec-{{date}}.md`. Start it with this frontmatter — every field is required:

```yaml
---
skill: draft-spec
topic: {{topic}}
item: spec
date: {{date}}
skill_version: 0.1.0
input: [loaded artifact filenames, comma-separated; or "freeform: [first 10 words of description]"]
---
```

Document order: frontmatter → scout table → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Self-review findings → Amendments

---

## V-05 — Signal Register Pre-Loading + Structural Axis Declaration

**Axes**: Signal register pre-loading step (loads all non-requirements signals into named variables before spec authoring begins) + structural axis declaration block (declares which structural axes guard which criteria).
**Hypothesis**: Pre-loading cross-namespace signals into a named register before spec authoring forces C-10 at the data level (signal is named, not improvised mid-section) and makes C-11 structurally binding (the register row in Purpose is populated from a pre-declared variable, not a freestyle instruction). The axis declaration block makes C-13 textually provable without scorer inference.

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.
Roles: Architect (primary) | PM, Strategy, Compliance, Design (inline per section)
```

---

**STRUCTURAL AXIS DECLARATION**

*(This block is not a phase. It is a declaration of how this skill guarantees structural coverage. Read before executing.)*

| Axis | Mechanism | Criteria guarded |
|------|-----------|-----------------|
| Axis A — Scout disclosure | SETUP table with row-per-artifact and LOADED/NOT FOUND; precedes all EXECUTE content | C-02 |
| Axis B — Signal register | SIGNAL REGISTER phase extracts named NS-signals before Architect writes; Purpose section pre-printed row pulls from register | C-10, C-11 |
| Axis C — PM coverage | PM maps every P0 to a section before Architect writes; Requirements table carries per-row Spec entry and Status | C-01, C-03, C-13 |
| Axis D — Findings completeness | FINDINGS addresses all four categories with explicit written claims; AMENDMENTS cites findings by name | C-04, C-07, C-08 |

Every essential criterion is guarded by at least two independent axes:

| Criterion | Axis A | Axis B | Axis C | Axis D |
|-----------|--------|--------|--------|--------|
| C-01 Structure | — | — | ✓ (PM section lock) | — |
| C-02 Scout table | ✓ (SETUP table) | ✓ (register reads SETUP) | — | — |
| C-03 P0 coverage | — | — | ✓ (PM coverage count) | ✓ (Findings gap check) |
| C-04 Findings present | — | — | — | ✓ (four categories + claim requirement) |
| C-05 Frontmatter | ✓ (template) | ✓ (input field = artifact list from SETUP) | — | — |

---

**PHASE 1 — SETUP**

Scan `simulations/scout/` for `{{topic}}` artifacts. Output this table before anything else:

| Row | Artifact type | Filename pattern | File found | Status |
|-----|--------------|-----------------|------------|--------|
| 1 | scout-requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | scout-feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | scout-market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | scout-compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | scout-stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | scout-naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | scout-positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

**No-scout-context conditional**: If all rows = NOT FOUND, write: "Fallback activated — no scout artifacts for `{{topic}}`. User description required: 'Describe the feature in 3–5 sentences before proceeding.' Signal Register will show all NS-signals as NOT FOUND." Do not advance to Phase 2 until Row 1 = LOADED or a description is received.

---

**PHASE 2 — SIGNAL REGISTER**

*(Axis B: load all non-requirements signals before Architect writes. This phase produces named signal variables the spec sections read from.)*

From the loaded artifacts (rows 2–7), extract and record named signals:

| Signal ID | Signal type | Value | Source artifact | Available for |
|-----------|------------|-------|----------------|--------------|
| NS-feasibility | Feasibility score or posture | [score / posture / NOT FOUND] | [row 2 filename] | Purpose, Design, Constraints |
| NS-compliance | Compliance posture | [blocking / advisory / none / NOT FOUND] | [row 4 filename] | Purpose, Constraints |
| NS-positioning | Positioning differentiator | [key claim / NOT FOUND] | [row 7 filename] | Purpose |
| NS-market | Market insight | [key insight / NOT FOUND] | [row 3 filename] | Purpose |
| NS-stakeholders | Stakeholder priority | [top priority / NOT FOUND] | [row 5 filename] | Requirements |

Rules:
- NOT FOUND is a valid, explicit value — it may never be left as a blank cell.
- Architect reads Signal Register during section authoring. Architect does not re-read scout artifacts directly.
- If Row 1 = NOT FOUND: all NS-signals = NOT FOUND. Derive requirements from user description.

---

**PHASE 3 — PM COVERAGE**

*(Axis C: PM maps P0 requirements to sections before Architect writes.)*

From loaded scout-requirements (Row 1), map every requirement to a section:

| R-ID | Requirement (abbreviated) | Priority | Assigned section | NS-signal relevant |
|------|--------------------------|----------|-----------------|-------------------|
| R-01 | | P0 | [Purpose / Requirements / Design / Constraints / Open Questions] | [NS-signal ID from Register, or NOT FOUND] |
| ... | | | | |

P0 coverage count: [N]/[P0 total] P0 requirements assigned. *(Waived — state explicitly — if Row 1 = NOT FOUND.)*

---

**PHASE 4 — EXECUTE**

Write the five sections in this exact order. Do not reorder, rename, or omit. Each section reads from the Signal Register and PM Coverage table — do not re-read scout artifact files directly.

---

**Section 1 — Purpose**

Write 2–4 sentences: what `{{topic}}` does, who it serves, why it exists now.

Pre-printed signal row *(reads from Signal Register — complete from NS-signal values, leave visibly blank if NOT FOUND)*:

| Field | Value |
|-------|-------|
| What it does | |
| Who it serves | |
| Why now | |
| **Cross-namespace signal** | **[from Signal Register: NS-positioning value / NS-feasibility value / NS-market value — name the NS-signal ID and source artifact; leave blank if all NOT FOUND — blank is a visible gap]** |
| NS-signal source | [Signal Register row: NS-[type] from [artifact]] |

> **[PM inline]** Does this purpose address the problem the PM Coverage table was built to solve? PASS or finding:

---

**Section 2 — Requirements**

P0 requirements covered: ___/___ *(from PM Coverage count; or "Waived" if explicitly stated there)*

| R-ID | Requirement (abbreviated) | Priority | Spec entry | Status | NS-signal |
|------|--------------------------|----------|------------|--------|-----------|
| | | P0 | [named component, constraint, or question] | COVERED / GAP | [NS-signal ID or NOT FOUND] |
| | | P0 | | COVERED / GAP | |
| | | P1 | | | |

Contradictions: name any conflicting R-ID pairs with resolution or amendment flag.

> **[Strategy inline]** Do requirements cohere with NS-positioning or NS-market signals? PASS or finding (R-IDs + NS-signal ID):

---

**Section 3 — Design**

Describe implementation: components, decisions, data flow. Reference R-IDs. Trace NS-feasibility to a design constraint if NS-feasibility ≠ NOT FOUND (e.g., "NS-feasibility score of 62 from [artifact] → Phase 1 scoped to [subset] only").

> **[Design inline]** Does design satisfy UX or naming constraints from loaded artifacts? PASS or finding:

---

**Section 4 — Constraints**

| Constraint | Type | NS-signal source | Priority |
|-----------|------|-----------------|----------|
| | technical / compliance / time / resource | [NS-compliance / NS-feasibility / NS-stakeholders / Architect judgment] | |

NS-compliance value from Signal Register: [blocking / advisory / none / NOT FOUND] — every blocking compliance item from NS-compliance must appear as a constraint row.

> **[Compliance inline]** Any compliance constraint missing? PASS or finding:

---

**Section 5 — Open Questions**

| # | Question | NS-signal that would resolve it | Next action |
|---|---------|--------------------------------|-------------|
| 1 | | [NS-signal ID] | |
| 2 | | | |

---

**PHASE 5 — FINDINGS**

Architect self-review. For each category: specific finding or explicit "None found." Empty categories without a written claim are incomplete.

- **Contradictions**: R-ID pairs, resolution or amendment flag.
- **Gaps**: unaddressed requirements or design areas.
- **Ambiguities**: statements that need clarification.
- **Hotspots**: high-risk areas.

---

**PHASE 6 — AMENDMENTS**

Numbered list, minimum 2 items. Each cites a finding by category and names the section and change. No vague items.

Format: `N. Section [name] — [specific change] — Addresses: [finding category, element]`

---

**OUTPUT**

Write artifact to `simulations/draft/specs/{{topic}}-spec-{{date}}.md`.

```yaml
---
skill: draft-spec
topic: {{topic}}
item: spec
date: {{date}}
skill_version: 0.1.0
input: [LOADED artifact filenames from SETUP, comma-separated; or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → Structural Axis Declaration → SETUP table → Signal Register → PM Coverage → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Findings → Amendments

---

## Variation Summary

| Variation | Primary axis | Secondary axis | Key C-11 mechanism | Key C-12 mechanism | Key C-13 mechanism |
|-----------|-------------|---------------|-------------------|-------------------|-------------------|
| V-01 | Role sequence: PM-first | — | Pre-printed table row in Section 1 | `> [Role inline]` blockquote per section | Per-row Spec entry + Status columns in PM contract |
| V-02 | Output format: full skeleton | — | Pre-printed `Cross-namespace signal` row in Block 2 | `> [Role inline]` rows pre-printed in blocks 2–4 | Pre-printed Spec entry + Status columns in Block 3 |
| V-03 | Lifecycle: checklist exits | — | Pre-printed signal row in Section 1 with CONFIRM check | `> [Role inline]` blockquote per section with CONFIRM check | Per-row Spec entry + Status confirmed in Phase 2 checklist |
| V-04 | Phrasing: conversational | Inertia framing per section | Pre-printed `Cross-namespace signal` row in Section 1 table | `> [Role check]` blockquote per section | Per-row Spec entry + `Covered?` column |
| V-05 | Signal register pre-load | Structural axis declaration | Signal Register → pre-printed NS-signal row in Purpose | `> [Role inline]` blockquote per section | Per-row Spec entry, Status, NS-signal columns; PM Coverage table |

**Primary C-11 discriminator across variations**: V-01/V-02/V-03/V-04 satisfy C-11 with a pre-printed table row in Purpose. V-05 adds a structural data dependency (Signal Register → row value) that makes omission an Axis B violation, not just a visible blank. V-05's C-11 enforcement is stronger: empty cell = structural gap, not just cosmetic gap.

**Primary C-13 discriminator**: V-01–V-04 use a per-row Requirements table with Spec entry + Status columns. V-05 adds the NS-signal column as a third per-row column, plus the PM Coverage table pre-assigns rows before Architect writes — double structural binding.
