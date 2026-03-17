---
skill: quest:variate
rubric_for: draft-spec
rubric_version: v4
round: R4
date: 2026-03-15
axes_explored: role-sequence, output-format, phrasing-register, lifecycle-emphasis, inertia-framing
---

# Quest Variate — `draft-spec` — Round 4 (Rubric v4)

## Axis Map

| Variation | Primary Axis | Secondary Axes | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Role Sequence | — | PM→Strategy→Architect strict ordering creates C-17 gate tokens organically; scripted fallback in PM-first position satisfies C-18; ordinal markers follow from two-step CNS placement |
| V-02 | Output Format (REQUIRES/PRODUCES) | — | Full REQUIRES/PRODUCES chain creates C-17 mechanically; NOT FOUND branch PRODUCES verbatim text satisfies C-18; A-of-2/B-of-2 slot labels satisfy C-19 |
| V-03 | Phrasing Register | — | Conversational tone with `respond:` quoted blocks satisfies C-18; `[SCAN REQUIRED]` markers create active inspection guards (C-14); "entry 1/2" natural language satisfies C-19 |
| V-04 | Role Sequence + Output Format + Lifecycle Emphasis | all three | Combining role ordering, REQUIRES/PRODUCES tokens, and explicit phase gates achieves all 19 criteria with maximum structural rigor |
| V-05 | Role Sequence + Output Format + Lifecycle + Inertia Framing | all four | Adds inertia competitor analysis (IG-IDs, risk amplification) on top of V-04 — surfaces depth patterns not yet captured by v4 rubric |

---

## V-01 — Role Sequence: PM → Strategy → Architect Lock

**Axis**: Role sequence
**Hypothesis**: Strict PM → Strategy → Architect ordering with named gate tokens between each role
naturally satisfies C-17 (tokens are role-completion proofs, not ordering instructions). The
no-scout fallback is written as scripted model-ready copy in the PM-first block (C-18).
Ordinal markers follow from two structurally independent CNS slots (C-19).

---

You are executing `/draft:spec` for topic: `{topic}`. Follow all phases in order. Do not
skip or reorder phases. Each phase is gated by the previous phase's token.

---

### PHASE 1 — SETUP: Scout Discovery

Scan the following locations. Write this table as the **first output block** — before any other content.

| # | Artifact | Expected Path | Status | Key Finding |
|---|----------|--------------|--------|-------------|
| 1 | scout-requirements | simulations/scout/requirements/{topic}-requirements-*.md | LOADED / NOT FOUND | R-count, P0-count |
| 2 | scout-feasibility | simulations/scout/feasibility/{topic}-feasibility-*.md | LOADED / NOT FOUND | Score /100 |
| 3 | scout-compliance | simulations/scout/compliance/{topic}-compliance-*.md | LOADED / NOT FOUND | Blocking count |
| 4 | scout-positioning | simulations/scout/positioning/{topic}-positioning-*.md | LOADED / NOT FOUND | Differentiator count |
| 5 | scout-market | simulations/scout/market/{topic}-market-*.md | LOADED / NOT FOUND | SOM estimate |

Status: LOADED if the file exists and is readable. NOT FOUND if no matching file exists.
**Do not leave any cell blank — NOT FOUND is explicit content. An empty cell is a structural failure.**

**NO-SCOUT FALLBACK** — named conditional: `INLINE-REQUIREMENTS-MODE`

If Row 1 (scout-requirements) is NOT FOUND, stop and emit the following verbatim:

> write: "I don't have a prior requirements brief for `{topic}`. To write a specification I
> need a short description. Please describe what you're building in 3–5 sentences: what it
> does, who it's for, and what problem it solves. I'll extract inline requirements and proceed."

Wait for user response. Extract 5–10 requirements from the response, assign R-IDs (R-01 onward),
mark all P0. Continue from Phase 2 with these inline requirements as the loaded artifact.

After writing the scout table, emit: **[PM-SCAN-GATE]**
Phase 2 may not begin until `[PM-SCAN-GATE]` appears in this document.

---

### PHASE 2 — PM: Coverage Pre-Assignment

**Requires: [PM-SCAN-GATE]**

PM role activates. **Before Architect writes any prose**, assign every P0 requirement to a
named spec section and register the cross-namespace signal.

| R-ID | Priority | Requirement | Assigned Section | CNS Signal (location 1 of 2) |
|------|----------|-------------|-----------------|------------------------------|
| R-01 | P0 | [text from loaded requirements] | Purpose / Requirements / Design / Constraints / Open Questions | [artifact-name: key-value] or NOT FOUND |
| ... | | | | |

**CNS Signal (location 1 of 2)**: if a non-requirements artifact is LOADED and its finding
bears on this requirement, name the artifact and value (e.g., `scout-feasibility: 42/100`).
If no non-requirements artifact is LOADED for this row, write NOT FOUND. Empty is a structural
failure — NOT FOUND is always valid.

**Contradiction scan**: before sealing the contract, scan every R-ID pair for conflicts.
Pre-print the contradiction template below. For each real conflict, fill in R-IDs and description.
For no conflicts, write the scan completion statement — you may not skip the template.

| Contradiction # | R-ID pair | Description | Proposed resolution |
|-----------------|-----------|-------------|---------------------|
| 1 | R-__ vs R-__ | [conflict or "none — pair clean"] | [resolution or NOT APPLICABLE] |

Scan completion statement (required): "Scanned [N] requirement pairs; [K] contradictions found."
This statement must precede the gate token. A contradiction result without a preceding scan
statement is a protocol violation.

Coverage count: "PM pre-assignment: [N]/[total-P0] P0 requirements assigned."

Emit: **[PM-CONTRACT-COMPLETE: N/total-P0 assigned, K contradictions]**
Phase 3 may not begin until `[PM-CONTRACT-COMPLETE]` appears in this document.

---

### PHASE 3 — STRATEGY: Positioning Charter

**Requires: [PM-CONTRACT-COMPLETE]**

Strategy role activates. Review PM assignments. For each section that touches a
competitive differentiator, name it:

| Section | Differentiator (from scout-positioning) | Validation |
|---------|----------------------------------------|------------|
| [section] | [differentiator name] or NOT APPLICABLE | VALIDATED / NOT LOADED |

If scout-positioning is NOT FOUND, write in every Validation cell: NOT LOADED — differentiator
validation skipped.

Emit: **[STRATEGY-CHARTER-COMPLETE]**
Phase 4 may not begin until `[STRATEGY-CHARTER-COMPLETE]` appears in this document.

---

### PHASE 4 — ARCHITECT: Specification Writing

**Requires: [STRATEGY-CHARTER-COMPLETE]**

Write the five sections below **in the prescribed order**. Do not reorder. Additional sections
may appear after Section 5 only.

#### Section 1: Purpose

| Attribute | Value |
|-----------|-------|
| Feature | [name] |
| Audience | [who uses it] |
| Problem | [what it solves] |
| Key differentiator | [from Strategy charter, or NOT APPLICABLE] |
| **CNS Signal (location 2 of 2)** | [artifact-name: key-value] or NOT FOUND |

**CNS Signal (location 2 of 2)**: read from the loaded scout artifacts — feasibility score,
compliance posture, market segment, or positioning. Name the source artifact and value.
If no non-requirements artifact is LOADED, write NOT FOUND. This cell may not be left blank.

> *[PM annotation: purpose maps to R-[XX] from pre-assignment — PASS / MISMATCH with finding]*
> *[STRATEGY annotation: differentiator reflected in purpose — PASS / ABSENT]*

#### Section 2: Requirements

| R-ID | Priority | Requirement | Spec Entry | Status |
|------|----------|-------------|------------|--------|
| R-01 | P0 | [text] | [specific named component, e.g., "Design: retry-backoff module"] | COVERED / UNCOVERED |
| ... | | | | |

Coverage: [N]/[total-P0] P0 requirements covered.

> *[PM annotation: [N]/[total-P0] P0 requirements covered — PASS / VIOLATION — uncovered: R-XX, ...]*

**Spec Entry column**: must name a specific component in a specific section (e.g., "Design:
auth-token-store"), not a generic label (e.g., "covered in design"). Generic labels are
structural failures.

#### Section 3: Design

For each component or subsystem:

| Component | Responsibility | Traces to | CNS Signal |
|-----------|---------------|-----------|------------|
| [name] | [what it does] | [R-ID list] | [artifact: value] or NOT FOUND |

> *[ARCHITECT inline: key design decisions and rationale for choices made]*
> *[STRATEGY annotation: competitive differentiation present in design — PASS / ABSENT — finding: ...]*

#### Section 4: Constraints

| Constraint | Type | Source | Spec Impact |
|------------|------|--------|-------------|
| [text] | compliance / performance / platform / compatibility | [R-ID or scout-compliance artifact] | [how design accommodates it] |

> *[PM annotation: all blocking compliance requirements present — PASS / VIOLATION — missing: ...]*

#### Section 5: Open Questions

| # | Question | Blocks | Owner | Resolution |
|---|----------|--------|-------|------------|
| 1 | [unresolved question] | [section or R-ID it blocks] | [role or person] | OPEN / [resolution] |

Emit: **[ARCHITECT-COMPLETE]**
Phase 5 may not begin until `[ARCHITECT-COMPLETE]` appears in this document.

---

### PHASE 5 — FINDINGS: Self-Review

**Requires: [ARCHITECT-COMPLETE]**

Run all four finding types in order. Each must produce a written result before the next begins.

**TYPE A — Coverage Gaps**
Scan Section 2 Status column. List every UNCOVERED P0 requirement.
Result: `[N gaps: R-XX, R-YY, ...]` or `[NONE: all [N] P0 requirements covered — verified by Section 2 Status scan]`

**TYPE B — Contradictions**
Review the Phase 2 contradiction scan. Add any new conflicts surfaced during spec writing.
Inspection rule: before writing NONE, cite the Phase 2 scan count.
Result: `[N contradictions: R-XX vs R-YY, ...]` or `[NONE: Phase 2 scan confirmed [N] pairs clean, 0 new conflicts in spec]`

**TYPE C — Complexity Hotspots**
Identify sections disproportionately complex relative to their requirement priority.
Result: `[N hotspots: section-name (N R-IDs, complexity level), ...]` or `[NONE: no section exceeds 8 R-IDs — verified by Design table row count]`

**TYPE D — Cross-NS Coherence**
Confirm CNS Signal is present in both independent locations.
Inspection rule: before confirming coherence, scan each LOADED row in the Phase 1 table and name the artifacts inspected.
Result: `[location 1 of 2: [artifact] value populated; location 2 of 2: [artifact] value populated]` or `[MISSING from location [N] of 2]`

Emit: **[FINDINGS-COMPLETE]**
Phase 6 may not begin until `[FINDINGS-COMPLETE]` appears in this document.

---

### PHASE 6 — AMENDMENTS

**Requires: [FINDINGS-COMPLETE]**

Produce a numbered list of amendments addressing Phase 5 findings. Minimum 2 items.

| # | Finding type | Scope | Action |
|---|-------------|-------|--------|
| 1 | TYPE [A/B/C/D] | [R-ID or section name] | [specific, concrete action — names the change, not just the area] |
| 2 | ... | ... | ... |

Each action must name the R-ID or section and specify the concrete change. "Improve section" or
"review coverage" are not acceptable.

---

### OUTPUT ARTIFACT

Write to: `simulations/draft/specs/{topic}-spec-{date}.md`

```yaml
---
skill: draft-spec
topic: {topic}
item: {feature-slug}
date: {YYYY-MM-DD}
skill_version: v1
input: scout-requirements={LOADED|NOT FOUND}, scout-feasibility={LOADED|NOT FOUND}, scout-compliance={LOADED|NOT FOUND}, scout-positioning={LOADED|NOT FOUND}
---
```

All six fields (skill, topic, item, date, skill_version, input) are required.
**If any field is absent, the artifact is invalid — do not write it.**

---

---

## V-02 — Output Format: Full REQUIRES/PRODUCES Chain

**Axis**: Output format (REQUIRES/PRODUCES declarations)
**Hypothesis**: Making every step declare its inputs (REQUIRES) and outputs (PRODUCES) with
exact token names creates C-17 mechanically — the PRODUCES token is the gate artifact, not
a separate instruction. The NOT FOUND branch PRODUCES verbatim scripted text (C-18). Slot
labels A-of-2 and B-of-2 on the CNS field satisfy C-19 without requiring ordinal prose.

---

You are executing `/draft:spec` for topic: `{topic}`. Every step below declares what it
REQUIRES (the predecessor's token) and PRODUCES (its own token). No step may begin until
its REQUIRES token is present in the document.

---

### STEP 1 — Scout Discovery

REQUIRES: none (first step)
PRODUCES: [DISCOVERY-TABLE]

Write the scout artifact table below. This table is [DISCOVERY-TABLE].

| # | Artifact | Path | Status | Key Finding |
|---|----------|------|--------|-------------|
| 1 | scout-requirements | simulations/scout/requirements/{topic}-requirements-*.md | LOADED / NOT FOUND | R-count, P0-count |
| 2 | scout-feasibility | simulations/scout/feasibility/{topic}-feasibility-*.md | LOADED / NOT FOUND | Score /100 |
| 3 | scout-compliance | simulations/scout/compliance/{topic}-compliance-*.md | LOADED / NOT FOUND | Blocking count |
| 4 | scout-positioning | simulations/scout/positioning/{topic}-positioning-*.md | LOADED / NOT FOUND | Differentiator count |
| 5 | scout-market | simulations/scout/market/{topic}-market-*.md | LOADED / NOT FOUND | SOM estimate |

Status: LOADED if the file exists and is readable; NOT FOUND if absent.
All cells required. NOT FOUND is valid. Empty is a structural failure.

**NOT FOUND BRANCH** — named conditional: `INLINE-REQUIREMENTS-MODE`

If Row 1 status = NOT FOUND:
PRODUCES: [INLINE-REQUEST] — emit the following verbatim:

> respond: "I don't have a prior requirements brief for `{topic}`. Please describe what
> you're building in 3–5 sentences — what it does, who uses it, and what problem it solves.
> I'll extract requirements inline and continue from there."

Wait for response. Extract R-IDs, mark all P0. Continue from Step 2 with inline requirements.
[INLINE-REQUEST] satisfies the REQUIRES for Step 2 in this branch.

After writing the complete table: `[DISCOVERY-TABLE: N artifacts scanned, M LOADED]`

---

### STEP 2 — PM Coverage Contract

REQUIRES: [DISCOVERY-TABLE]
PRODUCES: [PM-CONTRACT: N/total-P0 assigned, K contradictions]

PM role activates. Build two sub-tables before writing any spec prose.

**Sub-table 2a — P0 Pre-Assignment:**

| R-ID | Priority | Requirement | Assigned Section | CNS Signal [slot A-of-2] |
|------|----------|-------------|-----------------|--------------------------|
| R-01 | P0 | [text] | Purpose / Requirements / Design / Constraints / Open Questions | [artifact-name: key-value] or NOT FOUND |
| ... | | | | |

CNS Signal [slot A-of-2]: name a non-requirements loaded artifact and its key finding. If none
loaded for this row, write NOT FOUND. Empty is a structural failure.

**Sub-table 2b — Contradiction Scan:**

| # | R-ID pair | Description | Resolution |
|---|-----------|-------------|------------|
| 1 | R-__ vs R-__ | [conflict description] | [resolution] or [FLAG: needs scope decision] |

Required scan statement: "Scanned [N] R-ID pairs; [K] contradictions identified."
This statement must appear before PRODUCES is declared.
**Writing [PM-CONTRACT] without a scan statement is a PRODUCES violation — the token is invalid.**

Coverage summary: "PM pre-assignment: [N]/[total-P0] P0 requirements assigned to sections."

`[PM-CONTRACT: N/total-P0 assigned, K contradictions confirmed]`

---

### STEP 3 — Strategy Charter

REQUIRES: [PM-CONTRACT]
PRODUCES: [STRATEGY-CHARTER]

Strategy role activates. Validate positioning for each assigned section.

| Section | Differentiator (scout-positioning) | Validation |
|---------|-----------------------------------|------------|
| [section] | [differentiator] or NOT APPLICABLE | VALIDATED / NOT LOADED |

If scout-positioning NOT FOUND: write "NOT LOADED" in all Validation cells.

`[STRATEGY-CHARTER: M differentiators validated]`

---

### STEP 4 — Architect: Five-Section Specification

REQUIRES: [STRATEGY-CHARTER]
PRODUCES: [SPEC-COMPLETE]

Write the five sections in prescribed order. Reordering is a structural failure.
Extra sections may follow Section 5 only.

#### Section 1: Purpose

| Attribute | Value |
|-----------|-------|
| Feature | [name] |
| Audience | [who] |
| Problem | [what it solves] |
| Differentiator | [from Strategy charter or NOT APPLICABLE] |
| **CNS Signal [slot B-of-2]** | [artifact-name: key-value] or NOT FOUND |

CNS Signal [slot B-of-2]: slot A-of-2 appeared in the PM pre-assignment table (Step 2).
This is the second of two structurally independent instantiations. Name the source artifact
and value. NOT FOUND is valid. Empty is a structural failure.

> *[PM annotation: purpose matches pre-assigned section for R-[XX] — PASS / MISMATCH]*
> *[STRATEGY annotation: differentiator reflected — PASS / ABSENT]*

#### Section 2: Requirements

| R-ID | Priority | Requirement | Spec Entry | Status |
|------|----------|-------------|------------|--------|
| R-01 | P0 | [text] | [named component: "Design: component-name"] | COVERED / UNCOVERED |
| ... | | | | |

Coverage: [N]/[total-P0] P0 requirements covered.

> *[PM annotation: [N]/[total-P0] P0 covered — PASS / VIOLATION: R-XX uncovered]*

Spec Entry must name a specific component. Generic entries ("covered in design") are structural
failures.

#### Section 3: Design

| Component | Responsibility | Traces to | CNS Signal |
|-----------|---------------|-----------|------------|
| [name] | [function] | [R-IDs] | [artifact: value] or NOT FOUND |

> *[ARCHITECT inline: design rationale — choices made and why]*
> *[STRATEGY annotation: competitive differentiation present — PASS / ABSENT]*

#### Section 4: Constraints

| Constraint | Type | Source | Spec Impact |
|------------|------|--------|-------------|
| [text] | compliance / performance / platform | [R-ID or scout-compliance artifact] | [how design handles it] |

> *[PM annotation: blocking compliance requirements present — PASS / VIOLATION]*

#### Section 5: Open Questions

| # | Question | Blocks | Owner | Resolution |
|---|----------|--------|-------|------------|
| 1 | [question] | [what it blocks] | [owner] | OPEN / [resolution] |

`[SPEC-COMPLETE]`

---

### STEP 5 — Findings

REQUIRES: [SPEC-COMPLETE]
PRODUCES: [FINDINGS-COMPLETE]

**TYPE A — Coverage Gaps**
Inspect Section 2 Status column row by row.
PRODUCES (per finding): `[GAP: R-XX — recommended section: ...]`
PRODUCES (no gaps): `[CLEAN: all [N] P0 covered — Section 2 scan complete]`

**TYPE B — Contradictions**
Review Step 2 sub-table 2b and inspect spec for new conflicts.
Inspection guard: cite Step 2 scan count before confirming absence.
PRODUCES (per conflict): `[CONTRADICTION: R-XX vs R-YY — resolution: ...]`
PRODUCES (none): `[CLEAN: Step 2 scan confirmed [N] pairs; 0 new conflicts in spec]`

**TYPE C — Complexity Hotspots**
Inspect Section 3 component table row count.
PRODUCES (per hotspot): `[HOTSPOT: section-name — [N] R-IDs, complexity: HIGH/MEDIUM]`
PRODUCES (none): `[CLEAN: no section exceeds 8 R-IDs — Design table count: N]`

**TYPE D — CNS Coherence**
Verify both CNS Signal slots are populated.
Inspection guard: scan each LOADED row in [DISCOVERY-TABLE]; name artifacts inspected.
PRODUCES: `[CNS-COHERENT: slot A-of-2 from [artifact]; slot B-of-2 from [artifact]]`
or `[CNS-GAP: slot [A/B]-of-2 unpopulated]`

`[FINDINGS-COMPLETE: A=[result], B=[result], C=[result], D=[result]]`

---

### STEP 6 — Amendments

REQUIRES: [FINDINGS-COMPLETE]
PRODUCES: [AMENDMENTS-COMPLETE]

| # | PRODUCES token from Findings | Scope | Action |
|---|------------------------------|-------|--------|
| 1 | [e.g., GAP: R-XX] | [R-ID or section] | [specific, concrete action] |
| 2 | ... | ... | ... |

Minimum 2 rows. Vague actions ("review coverage") are structural failures.

`[AMENDMENTS-COMPLETE]`

---

### OUTPUT ARTIFACT

REQUIRES: [AMENDMENTS-COMPLETE]
PRODUCES: artifact file at `simulations/draft/specs/{topic}-spec-{date}.md`

Frontmatter:
```yaml
---
skill: draft-spec
topic: {topic}
item: {feature-slug}
date: {YYYY-MM-DD}
skill_version: v1
input: scout-requirements={LOADED|NOT FOUND}, scout-feasibility={LOADED|NOT FOUND}, scout-compliance={LOADED|NOT FOUND}, scout-positioning={LOADED|NOT FOUND}
---
```

PRODUCES hard-fail contract: if any of [skill, topic, item, date, skill_version, input] is
absent from frontmatter, the artifact is invalid — do not write it. This is a PRODUCES
violation equivalent to an absent gate token.

---

---

## V-03 — Phrasing Register: Conversational + [SCAN REQUIRED] Markers

**Axis**: Phrasing register (conversational, imperative-second-person)
**Hypothesis**: A conversational register with `[SCAN REQUIRED]` markers as inline cues creates
active inspection guards (C-14) more naturally than formal protocol rules. `respond: "..."` quoted
blocks provide scripted fallback text (C-18) in a readable format. "Entry 1/2" and "Entry 2/2"
natural-language markers satisfy C-19 without bureaucratic slot notation.

---

You're running `/draft:spec` for `{topic}`. Here's how to work through it — follow the steps
in order, don't skip ahead.

---

### Step 1 — Find Your Scout Context

Start by checking what scout work already exists for this topic. Write this table first,
before anything else:

| Artifact | Where to look | Did you find it? | What it says |
|----------|--------------|-----------------|--------------|
| scout-requirements | simulations/scout/requirements/{topic}-requirements-*.md | yes (LOADED) / no (NOT FOUND) | requirements count, P0 count |
| scout-feasibility | simulations/scout/feasibility/{topic}-feasibility-*.md | yes (LOADED) / no (NOT FOUND) | feasibility score /100 |
| scout-compliance | simulations/scout/compliance/{topic}-compliance-*.md | yes (LOADED) / no (NOT FOUND) | blocking requirement count |
| scout-positioning | simulations/scout/positioning/{topic}-positioning-*.md | yes (LOADED) / no (NOT FOUND) | differentiator count |
| scout-market | simulations/scout/market/{topic}-market-*.md | yes (LOADED) / no (NOT FOUND) | SOM estimate |

Don't leave the "Did you find it?" column blank — if nothing is there, write NOT FOUND.
A blank cell is wrong even if there's nothing to put in it.

**If you didn't find scout-requirements** (named conditional: `NO-PRIOR-BRIEF`):

Stop here and respond with this text exactly:

> respond: "I don't see a prior requirements brief for `{topic}`. Before I can write a spec,
> I need to understand what you're building. Can you give me 3–5 sentences describing it?
> Cover what it does, who it's for, and what problem it solves — I'll pull out requirements
> from your description and keep going."

Once you have the description, extract 5–10 requirements (call them R-01, R-02, etc., all P0)
and proceed.

After you've written the complete table, mark it: **✓ SCOUT SCAN SEALED**
Don't move to Step 2 until you've written ✓ SCOUT SCAN SEALED.

---

### Step 2 — PM Covers the Requirements First

Before you write a word of the spec, PM needs to assign every P0 requirement to a section.
This happens first — it's what keeps coverage from being an afterthought.

Build this table:

| R-ID | Priority | Requirement | Which section covers it | Cross-namespace signal (entry 1/2) |
|------|----------|-------------|------------------------|-------------------------------------|
| R-01 | P0 | [requirement text] | Purpose / Requirements / Design / Constraints / Open Questions | [artifact-name: value] or NOT FOUND |
| ... | | | | |

**Cross-namespace signal (entry 1/2)**: if one of your other loaded scout artifacts (feasibility,
compliance, positioning) says something relevant to this requirement, name the artifact and its
key value here. If not, write NOT FOUND. Don't leave it blank — a blank cell means you skipped
the check, which is different from checking and finding nothing.

`[SCAN REQUIRED — Contradictions]`
Before you seal this step, scan the requirements list for conflicts. Use this format for each
pair you check:

| Pair # | R-ID pair | Do they conflict? | If yes, what's the resolution? |
|--------|-----------|-------------------|-------------------------------|
| 1 | R-__ vs R-__ | yes — [conflict] / no | [resolution] or NOT APPLICABLE |

You can't confirm "no contradictions" without actually scanning the pairs.
Write: "Scanned [N] pairs; [K] conflicts found." before sealing.

Coverage: "PM pre-assignment done: [N]/[total-P0] P0 requirements assigned."

Mark: **✓ PM CONTRACT SEALED: [N]/[total-P0] requirements assigned, [K] conflicts found**
Don't start Step 3 until ✓ PM CONTRACT SEALED is written.

---

### Step 3 — Strategy Checks Positioning

Strategy looks at the PM assignments and checks which sections surface competitive differentiators.

| Section | Differentiator from scout-positioning | Does it show up in spec? |
|---------|--------------------------------------|-------------------------|
| [section] | [differentiator name] or NOT IN SCOPE | yes (VALIDATED) / no artifact (NOT LOADED) |

If scout-positioning wasn't found: note "NOT LOADED — differentiator check skipped" in every row.

Mark: **✓ STRATEGY CHARTER SEALED**
Don't start Step 4 until ✓ STRATEGY CHARTER SEALED is written.

---

### Step 4 — Write the Spec

Five sections, in this order. If you want to add more, put them after Section 5.

#### Section 1: Purpose

What is this, who is it for, what does it solve?

| | |
|---|---|
| Feature | [name] |
| Audience | [who uses it] |
| Problem it solves | [what problem] |
| Competitive angle | [from Strategy charter, or: not applicable — no positioning loaded] |
| **Cross-namespace signal (entry 2/2)** | [artifact-name: value] or NOT FOUND |

`[SCAN REQUIRED — Cross-namespace signal (entry 2/2)]`
Look at the loaded scout artifacts before filling this in. Name the artifact and value (e.g.,
`scout-feasibility: 42/100` or `scout-compliance: 3 blocking requirements`). If none loaded,
write NOT FOUND. This is the second of two entries — entry 1/2 appeared in the PM table above.
Two independent entries are required for this field to count.

> *PM check: purpose section corresponds to assigned sections for P0 requirements — PASS / note finding*
> *Strategy check: competitive differentiator reflected in purpose — PASS / absent*

#### Section 2: Requirements

List every requirement with a clear answer to "where does the spec cover it?"

| R-ID | Priority | Requirement | Which part of the spec covers it | Covered? |
|------|----------|-------------|----------------------------------|----------|
| R-01 | P0 | [text] | [specific entry, e.g., "Design: token-refresh component"] | yes (COVERED) / no (UNCOVERED) |
| ... | | | | |

Coverage total: [N]/[total-P0] P0 requirements covered.

> *PM check: [N]/[total-P0] P0 requirements covered — PASS / these R-IDs are uncovered: ...*

"Which part covers it" needs a specific name — not "covered in design" but "Design: the-specific-component".

#### Section 3: Design

What are we building, component by component?

| Component | What it does | Satisfies | Cross-namespace signal |
|-----------|-------------|-----------|------------------------|
| [name] | [function] | [R-ID list] | [artifact: value] or NOT FOUND |

> *Architect note: key design choices and the reasoning behind them*
> *Strategy check: competitive differentiation present in design — PASS / finding: ...*

#### Section 4: Constraints

What can't change — compliance, platform, performance, compatibility.

| Constraint | Kind | Comes from | How spec handles it |
|------------|------|-----------|---------------------|
| [text] | compliance / performance / platform | [R-ID or scout-compliance artifact] | [how design accommodates it] |

> *PM check: all blocking compliance requirements appear here — PASS / missing: ...*

#### Section 5: Open Questions

What needs a decision before implementation can start?

| # | Question | What it blocks | Who decides | Status |
|---|----------|---------------|-------------|--------|
| 1 | [question] | [what it blocks] | [owner] | OPEN / [resolution] |

Mark: **✓ SPEC DRAFT SEALED**
Don't start Step 5 until ✓ SPEC DRAFT SEALED is written.

---

### Step 5 — Self-Review

Four checks. Do them in order and write the result of each before moving to the next.

**Check A — Coverage gaps**
Scan the "Covered?" column in Section 2. List every UNCOVERED row.
Write: `[N gaps: R-XX, ...]` or `[none — all [N] P0 requirements covered, verified by Section 2 scan]`

**Check B — Contradictions**
`[SCAN REQUIRED — Contradictions]`
Review Step 2 contradiction table. Check if spec writing revealed any new conflicts.
You must cite the Step 2 scan count before writing "none."
Write: `[N contradictions: R-XX vs R-YY, ...]` or `[none — Step 2 scan: [N] pairs, 0 new conflicts in spec]`

**Check C — Complexity hotspots**
Count R-IDs per section. Flag anything disproportionate.
Write: `[N hotspots: section-name ([N] R-IDs), ...]` or `[none — no section exceeds 8 R-IDs, verified by Design table]`

**Check D — Cross-namespace coverage**
`[SCAN REQUIRED — Cross-namespace signal]`
Confirm the cross-namespace signal appears in both entries:
- Entry 1/2: PM pre-assignment table (Step 2)
- Entry 2/2: Section 1 Purpose table (Step 4)

Before confirming both populated, scan the LOADED artifacts from Step 1 and name what you checked.
Write: `[both entries populated: entry 1/2 from [artifact], entry 2/2 from [artifact]]` or `[missing entry [1/2 or 2/2]]`

Mark: **✓ FINDINGS SEALED**
Don't start Step 6 until ✓ FINDINGS SEALED is written.

---

### Step 6 — Amendments

At least 2 specific, concrete amendments. Vague ones don't count ("review section 3" is not an amendment).

| # | Refers to Check | What exactly | What to do |
|---|----------------|-------------|------------|
| 1 | A / B / C / D | [R-ID or section name] | [concrete change, e.g., "Add Design entry for R-14: define versioning component"] |
| 2 | ... | ... | ... |

---

### Save the Spec

Write to `simulations/draft/specs/{topic}-spec-{date}.md` with this frontmatter:

```yaml
---
skill: draft-spec
topic: {topic}
item: {feature-slug}
date: {YYYY-MM-DD}
skill_version: v1
input: scout-requirements={LOADED|NOT FOUND}, scout-feasibility={LOADED|NOT FOUND}, scout-compliance={LOADED|NOT FOUND}, scout-positioning={LOADED|NOT FOUND}
---
```

All six fields are required. Don't write the file if any are missing.

---

---

## V-04 — Combined: Role Sequence + REQUIRES/PRODUCES + Lifecycle Emphasis

**Axes**: Role sequence, output format, lifecycle emphasis
**Hypothesis**: Combining PM-first role ordering, full REQUIRES/PRODUCES token chain, and
explicit lifecycle phase gates with hard-stops achieves all 19 criteria simultaneously.
Role sequence provides C-16 (PM-first pre-assignment) and C-06 (secondary role validation).
REQUIRES/PRODUCES provides C-17 (gate token is a PRODUCES declaration) and C-18 (NOT FOUND
branch PRODUCES verbatim text). Lifecycle emphasis provides explicit ordinal location markers
(C-19) through phase-level structural design. C-14 is met by the token validity rule: a gate
token PRODUCES declaration is invalid without its named predecessor's scan evidence.

---

You are executing `/draft:spec` for topic: `{topic}`. Every phase declares its REQUIRES and
PRODUCES. No phase may execute until its REQUIRES token is present. Gate tokens are structural
proof artifacts — a token declared without its prerequisite evidence is invalid.

---

### PHASE 1 — Scout Discovery

REQUIRES: none
PRODUCES: [DISCOVERY-TABLE]

Write the scout table **as the first content block**. This is [DISCOVERY-TABLE].

| # | Artifact | Path | Status | Key Finding |
|---|----------|------|--------|-------------|
| 1 | scout-requirements | simulations/scout/requirements/{topic}-requirements-*.md | LOADED / NOT FOUND | R-count, P0-count |
| 2 | scout-feasibility | simulations/scout/feasibility/{topic}-feasibility-*.md | LOADED / NOT FOUND | Score /100 |
| 3 | scout-compliance | simulations/scout/compliance/{topic}-compliance-*.md | LOADED / NOT FOUND | Blocking count |
| 4 | scout-positioning | simulations/scout/positioning/{topic}-positioning-*.md | LOADED / NOT FOUND | Differentiator count |
| 5 | scout-market | simulations/scout/market/{topic}-market-*.md | LOADED / NOT FOUND | SOM estimate |

Status: LOADED if readable, NOT FOUND if absent. Empty cells are structural failures.

**NOT FOUND BRANCH** — named conditional: `INLINE-REQUIREMENTS-MODE`
PRODUCES: [INLINE-REQUEST] — if Row 1 = NOT FOUND, emit verbatim:

> write: "I don't have a requirements brief for `{topic}`. To write a spec, I need a product
> description. Please describe what you're building in 3–5 sentences: what it does, who uses it,
> and what problem it solves. I'll extract requirements inline and continue."

Wait for response; extract R-IDs, mark all P0; [INLINE-REQUEST] satisfies REQUIRES for Phase 2.

`[DISCOVERY-TABLE: N artifacts scanned, M LOADED]`

---

### PHASE 2 — PM: Coverage Contract

REQUIRES: [DISCOVERY-TABLE]
PRODUCES: [PM-CONTRACT: N/total-P0 assigned, K contradictions]

PM role activates. Build the pre-assignment matrix and contradiction scan before Architect writes.

**2a. P0 Pre-Assignment Matrix:**

| R-ID | Priority | Requirement | Assigned Section | CNS Signal [location 1 of 2] |
|------|----------|-------------|-----------------|------------------------------|
| R-01 | P0 | [requirement text] | Purpose / Requirements / Design / Constraints / Open Questions | [artifact-name: key-value] or NOT FOUND |
| ... | | | | |

CNS Signal [location 1 of 2]: name a non-requirements loaded artifact and key value. If none
applies, write NOT FOUND. Empty is a structural failure; NOT FOUND is always valid.

**2b. Contradiction Scan:**

Scan every R-ID pair. Pre-print the scan template; complete every row.

| Pair | R-ID pair | Conflict | Resolution |
|------|-----------|---------|------------|
| 1 | R-__ vs R-__ | [conflict or "pair clean"] | [resolution] or NOT APPLICABLE |

Scan completion statement (required): "Scanned [N] pairs; [K] contradictions identified."

**Token validity rule**: [PM-CONTRACT] is invalid if the contradiction scan block and scan
completion statement are absent from this phase. An invalid token does not satisfy REQUIRES
for Phase 3.

Coverage: "PM pre-assignment: [N]/[total-P0] P0 requirements assigned."

`[PM-CONTRACT: N/total-P0 assigned, K contradictions confirmed]`

---

### PHASE 3 — Strategy: Positioning Charter

REQUIRES: [PM-CONTRACT]
PRODUCES: [STRATEGY-CHARTER]

Strategy role activates. Validate competitive positioning for each assigned section.

| Section | Differentiator (scout-positioning) | Validation |
|---------|-----------------------------------|------------|
| [section] | [differentiator] or NOT APPLICABLE | VALIDATED / NOT LOADED |

If scout-positioning NOT FOUND: all Validation cells = "NOT LOADED — skipped."

`[STRATEGY-CHARTER: M differentiators validated]`

---

### PHASE 4 — Architect: Five-Section Specification

REQUIRES: [STRATEGY-CHARTER]
PRODUCES: [SPEC-COMPLETE]

Write the five sections in prescribed order. No reordering. Additions after Section 5 only.

#### Section 1: Purpose

| Attribute | Value |
|-----------|-------|
| Feature | [name] |
| Audience | [who] |
| Problem | [what it solves] |
| Differentiator | [from Strategy charter, or NOT APPLICABLE] |
| **CNS Signal [location 2 of 2]** | [artifact-name: key-value] or NOT FOUND |

CNS Signal [location 2 of 2]: location 1 of 2 appeared in Phase 2 PM pre-assignment matrix.
This is the second structurally independent instantiation. Name the source artifact and value.
Inspect each LOADED row in [DISCOVERY-TABLE] before filling this field.
NOT FOUND is valid. Empty is a structural failure.

> *[PM annotation: purpose maps to pre-assigned section for R-[XX] — PASS / MISMATCH: finding]*
> *[STRATEGY annotation: differentiator reflected in purpose — PASS / ABSENT: finding]*

#### Section 2: Requirements

| R-ID | Priority | Requirement | Spec Entry | Status |
|------|----------|-------------|------------|--------|
| R-01 | P0 | [text] | [named entry: "Design: component-name"] | COVERED / UNCOVERED |
| ... | | | | |

Coverage: [N]/[total-P0] P0 requirements covered.

> *[PM annotation: [N]/[total-P0] P0 covered — PASS / VIOLATION — uncovered: R-XX, ...]*

Spec Entry must name a specific component (e.g., "Design: retry-backoff module").
Generic entries ("covered in design") are structural failures.

#### Section 3: Design

| Component | Responsibility | Traces to | CNS Signal |
|-----------|---------------|-----------|------------|
| [name] | [what it does] | [R-IDs] | [artifact: value] or NOT FOUND |

> *[ARCHITECT inline: design decisions — choices made and rationale]*
> *[STRATEGY annotation: competitive differentiation in design — PASS / ABSENT: finding]*

#### Section 4: Constraints

| Constraint | Type | Source | Spec Impact |
|------------|------|--------|-------------|
| [text] | compliance / performance / platform | [R-ID or scout-compliance artifact] | [how design handles it] |

> *[PM annotation: blocking compliance requirements present — PASS / VIOLATION: missing ...]*

#### Section 5: Open Questions

| # | Question | Blocks | Owner | Resolution |
|---|----------|--------|-------|------------|
| 1 | [question] | [what it blocks] | [owner] | OPEN / [resolution] |

`[SPEC-COMPLETE]`

---

### PHASE 5 — Findings: Self-Review

REQUIRES: [SPEC-COMPLETE]
PRODUCES: [FINDINGS-COMPLETE: A=result, B=result, C=result, D=result]

Run four finding types in sequence. Each PRODUCES its result before the next begins.

**TYPE A — Coverage Gaps**
Inspect Section 2 Status column row by row.
PRODUCES: `[GAP: R-XX, ...]` or `[CLEAN: all [N] P0 covered — Section 2 scan complete]`

**TYPE B — Contradictions**
Review Phase 2 contradiction scan. Inspect spec for new conflicts.
Inspection guard: cite Phase 2 scan count before confirming absence.
PRODUCES: `[CONTRADICTION: R-XX vs R-YY, ...]` or `[CLEAN: Phase 2 scan: [N] pairs; 0 new in spec]`

**TYPE C — Complexity Hotspots**
Count R-IDs per component in Section 3 Design table.
PRODUCES: `[HOTSPOT: section-name, [N] R-IDs]` or `[CLEAN: no section exceeds 8 R-IDs — Design count: N]`

**TYPE D — CNS Coherence**
Verify both CNS Signal locations are populated.
Inspection guard: scan each LOADED row in [DISCOVERY-TABLE]; name artifacts inspected.
PRODUCES: `[CNS-COHERENT: location 1 of 2 from [artifact]; location 2 of 2 from [artifact]]`
or `[CNS-GAP: location [1/2 or 2/2] unpopulated]`

`[FINDINGS-COMPLETE: A=[CLEAN/GAP], B=[CLEAN/CONTRADICTION], C=[CLEAN/HOTSPOT], D=[CNS-COHERENT/CNS-GAP]]`

---

### PHASE 6 — Amendments

REQUIRES: [FINDINGS-COMPLETE]
PRODUCES: [AMENDMENTS-COMPLETE]

| # | Finding PRODUCES token | Scope | Action |
|---|------------------------|-------|--------|
| 1 | [e.g., GAP: R-XX] | [R-ID or section] | [specific, concrete action] |
| 2 | ... | ... | ... |

Minimum 2 rows. Actions must name the R-ID or section and specify the change.
Vague actions are structural failures.

`[AMENDMENTS-COMPLETE]`

---

### OUTPUT ARTIFACT

REQUIRES: [AMENDMENTS-COMPLETE]
PRODUCES: `simulations/draft/specs/{topic}-spec-{date}.md`

```yaml
---
skill: draft-spec
topic: {topic}
item: {feature-slug}
date: {YYYY-MM-DD}
skill_version: v1
input: scout-requirements={LOADED|NOT FOUND}, scout-feasibility={LOADED|NOT FOUND}, scout-compliance={LOADED|NOT FOUND}, scout-positioning={LOADED|NOT FOUND}
---
```

PRODUCES hard-fail contract: all six fields (skill, topic, item, date, skill_version, input)
required. Absent field = artifact invalid, do not write.

---

---

## V-05 — Combined + Inertia Framing: V-04 with IG-ID Gap Analysis

**Axes**: Role sequence, output format, lifecycle emphasis, inertia framing
**Hypothesis**: Adding explicit inertia competitor analysis to V-04 — naming the status-quo
alternative, mapping each R-ID against whether the inertia option satisfies it, assigning IG-IDs
to gaps, and amplifying risk signals from the NS column — surfaces depth patterns not yet scored
by the v4 rubric. Specifically: IG-IDs create a parallel finding surface alongside R-IDs; risk
amplification via NS signal (feasibility < 70 → AMPLIFIED) connects compliance and feasibility
posture to inertia risk. Candidate for C-20 in v5: "Per-IG-ID elimination-path analysis with
risk amplification signal."

---

You are executing `/draft:spec` for topic: `{topic}`. This variation includes inertia gap
analysis — you will name the status-quo alternative to this feature, evaluate which requirements
it fails to satisfy, and assign IG-IDs to each inertia gap. Every phase declares REQUIRES and
PRODUCES.

---

### PHASE 1 — Scout Discovery

REQUIRES: none
PRODUCES: [DISCOVERY-TABLE]

Write the scout table as the **first content block**.

| # | Artifact | Path | Status | Key Finding | Inertia Exposure |
|---|----------|------|--------|-------------|------------------|
| 1 | scout-requirements | simulations/scout/requirements/{topic}-requirements-*.md | LOADED / NOT FOUND | R-count, P0-count | — |
| 2 | scout-feasibility | simulations/scout/feasibility/{topic}-feasibility-*.md | LOADED / NOT FOUND | Score /100 | HIGH if score < 70 / LOW if >= 70 / NOT LOADED |
| 3 | scout-compliance | simulations/scout/compliance/{topic}-compliance-*.md | LOADED / NOT FOUND | Blocking count | HIGH if any blocking / LOW if none / NOT LOADED |
| 4 | scout-positioning | simulations/scout/positioning/{topic}-positioning-*.md | LOADED / NOT FOUND | Differentiator count | — |
| 5 | scout-market | simulations/scout/market/{topic}-market-*.md | LOADED / NOT FOUND | SOM estimate | — |

Inertia Exposure column: rates the inertia risk contribution from each artifact. Empty is structural failure.

**NOT FOUND BRANCH** — named conditional: `INLINE-REQUIREMENTS-MODE`
PRODUCES: [INLINE-REQUEST] — if Row 1 = NOT FOUND, emit verbatim:

> write: "I don't have a requirements brief for `{topic}`. Please describe what you're building
> in 3–5 sentences — what it does, who uses it, and what problem it solves. I'll extract
> requirements inline and continue."

Wait for response; extract R-IDs, mark all P0; [INLINE-REQUEST] satisfies REQUIRES for Phase 2.

`[DISCOVERY-TABLE: N artifacts scanned, M LOADED]`

---

### PHASE 2 — PM: Coverage Contract + Inertia Register

REQUIRES: [DISCOVERY-TABLE]
PRODUCES: [PM-CONTRACT: N/total-P0 assigned, K contradictions, J inertia gaps (IG-01..IG-JJ)]

PM role activates. Build three sub-tables.

**2a. P0 Pre-Assignment Matrix:**

| R-ID | Priority | Requirement | Assigned Section | CNS Signal [location 1 of 2] | Inertia Match? |
|------|----------|-------------|-----------------|------------------------------|----------------|
| R-01 | P0 | [requirement text] | Purpose / Requirements / Design / Constraints / Open Questions | [artifact-name: key-value] or NOT FOUND | YES — inertia satisfies this / NO — inertia gap |

CNS Signal [location 1 of 2]: name a non-requirements loaded artifact and key finding. NOT FOUND
is valid. Empty is a structural failure.

Inertia Match: "YES" means the status-quo alternative already satisfies this requirement and
building this feature provides no additional value for it. "NO" means this is a gap — the feature
is needed to satisfy this requirement.

**2b. Inertia Gap Register (IG-IDs):**

For every row where Inertia Match = NO, assign an IG-ID and analyze the elimination path.

| IG-ID | R-ID | Gap Description | Elimination Path | Risk Signal |
|-------|------|-----------------|-----------------|-------------|
| IG-01 | R-XX | [why inertia fails this requirement] | [what specifically in the spec closes this gap] | AMPLIFIED if CNS signal shows feasibility < 70 or any blocking compliance / STANDARD otherwise |
| IG-02 | ... | ... | ... | ... |

Risk Signal: scan the CNS Signal column from sub-table 2a. If the CNS signal for this R-ID
shows feasibility < 70 or a blocking compliance requirement, mark AMPLIFIED — this gap is
harder to close than it appears. Otherwise STANDARD.

Inertia name: state the status-quo alternative being compared: "[name of existing approach or tool]."

**2c. Contradiction Scan:**

| Pair | R-ID pair | Conflict | Resolution |
|------|-----------|---------|------------|
| 1 | R-__ vs R-__ | [conflict or "pair clean"] | [resolution] or NOT APPLICABLE |

Scan completion statement (required): "Scanned [N] pairs; [K] contradictions identified."

**Token validity rule**: [PM-CONTRACT] is invalid if the contradiction scan block and scan
completion statement are absent. An invalid token does not satisfy REQUIRES for Phase 3.

Coverage: "PM pre-assignment: [N]/[total-P0] P0 assigned. Inertia gaps: [J] IG-IDs registered."

`[PM-CONTRACT: N/total-P0 assigned, K contradictions, J inertia gaps registered]`

---

### PHASE 3 — Strategy: Positioning Charter

REQUIRES: [PM-CONTRACT]
PRODUCES: [STRATEGY-CHARTER]

Strategy role activates. Validate positioning and note where IG-IDs with AMPLIFIED risk touch
competitive differentiators.

| Section | Differentiator (scout-positioning) | IG-IDs at risk | Validation |
|---------|-----------------------------------|----------------|------------|
| [section] | [differentiator] or NOT APPLICABLE | [IG-XX, ...] or NONE | VALIDATED / NOT LOADED |

If scout-positioning NOT FOUND: all Validation cells = "NOT LOADED — skipped."

`[STRATEGY-CHARTER: M differentiators validated]`

---

### PHASE 4 — Architect: Five-Section Specification

REQUIRES: [STRATEGY-CHARTER]
PRODUCES: [SPEC-COMPLETE]

Write the five sections in prescribed order. No reordering. Additions after Section 5 only.

#### Section 1: Purpose

| Attribute | Value |
|-----------|-------|
| Feature | [name] |
| Audience | [who] |
| Problem | [what it solves] |
| Differentiator | [from Strategy charter, or NOT APPLICABLE] |
| **CNS Signal [location 2 of 2]** | [artifact-name: key-value] or NOT FOUND |
| Inertia alternative | [name of status-quo alternative this feature replaces or improves on] |

CNS Signal [location 2 of 2]: location 1 of 2 appeared in Phase 2 pre-assignment matrix.
Inspect each LOADED row in [DISCOVERY-TABLE] before filling this field. NOT FOUND is valid.
Empty is a structural failure.

> *[PM annotation: purpose maps to R-[XX] pre-assigned section — PASS / MISMATCH]*
> *[STRATEGY annotation: differentiator reflected in purpose — PASS / ABSENT: finding]*

#### Section 2: Requirements

| R-ID | Priority | Requirement | Spec Entry | Status | IG-ID |
|------|----------|-------------|------------|--------|-------|
| R-01 | P0 | [text] | [named entry: "Design: component-name"] | COVERED / UNCOVERED | IG-XX / — |
| ... | | | | | |

Coverage: [N]/[total-P0] P0 requirements covered. Inertia gaps with spec entries: [J] IG-IDs addressed.

> *[PM annotation: [N]/[total-P0] P0 covered — PASS / VIOLATION — uncovered: R-XX]*

IG-ID column: link each requirement to its IG-ID from the Phase 2 register if it was an inertia
gap. "—" if Inertia Match was YES.

#### Section 3: Design

| Component | Responsibility | Traces to | CNS Signal | Closes IG-IDs |
|-----------|---------------|-----------|------------|---------------|
| [name] | [what it does] | [R-IDs] | [artifact: value] or NOT FOUND | [IG-XX, ...] or — |

> *[ARCHITECT inline: design decisions — choices made and rationale, esp. for AMPLIFIED gaps]*
> *[STRATEGY annotation: competitive differentiation in design — PASS / ABSENT: finding]*

#### Section 4: Constraints

| Constraint | Type | Source | Spec Impact |
|------------|------|--------|-------------|
| [text] | compliance / performance / platform | [R-ID or artifact] | [how design handles it] |

> *[PM annotation: blocking compliance requirements present — PASS / VIOLATION]*

#### Section 5: Open Questions

| # | Question | Blocks | Owner | Resolution |
|---|----------|--------|-------|------------|
| 1 | [question] | [section or R-ID] | [owner] | OPEN / [resolution] |

`[SPEC-COMPLETE]`

---

### PHASE 5 — Findings: Self-Review

REQUIRES: [SPEC-COMPLETE]
PRODUCES: [FINDINGS-COMPLETE: A=result, B=result, C=result, D=result, E=result]

**TYPE A — Coverage Gaps**
Inspect Section 2 Status column.
PRODUCES: `[GAP: R-XX, ...]` or `[CLEAN: all [N] P0 covered]`

**TYPE B — Contradictions**
Review Phase 2 contradiction scan. Check spec for new conflicts.
Inspection guard: cite Phase 2 scan count before confirming CLEAN.
PRODUCES: `[CONTRADICTION: R-XX vs R-YY, ...]` or `[CLEAN: Phase 2 scan: [N] pairs; 0 new]`

**TYPE C — Complexity Hotspots**
Count R-IDs per Section 3 component.
PRODUCES: `[HOTSPOT: component-name, [N] R-IDs]` or `[CLEAN: no component exceeds 8 R-IDs]`

**TYPE D — CNS Coherence**
Verify both CNS Signal locations populated. Inspect [DISCOVERY-TABLE] LOADED rows.
PRODUCES: `[CNS-COHERENT: location 1 of 2 from [artifact]; location 2 of 2 from [artifact]]`
or `[CNS-GAP: location [N] of 2 unpopulated]`

**TYPE E — Inertia Gap Analysis**
For each IG-ID from the Phase 2 register, confirm the spec closes the gap.

| IG-ID | Gap closed by | Closing component | Risk signal | Assessment |
|-------|--------------|------------------|-------------|------------|
| IG-01 | [Section: component] | [component name] | AMPLIFIED / STANDARD | CLOSED / OPEN — spec entry missing |

PRODUCES: `[INERTIA-ANALYZED: [J] gaps, [K] closed, [L] open; AMPLIFIED: [M]]`
or `[INERTIA-ABSENT: no inertia register in Phase 2]`

`[FINDINGS-COMPLETE: A=[result], B=[result], C=[result], D=[result], E=[result]]`

---

### PHASE 6 — Amendments

REQUIRES: [FINDINGS-COMPLETE]
PRODUCES: [AMENDMENTS-COMPLETE]

| # | Finding PRODUCES token | Scope | Action |
|---|------------------------|-------|--------|
| 1 | [e.g., GAP: R-XX] | [R-ID or section] | [specific, concrete action] |
| 2 | ... | ... | ... |

For AMPLIFIED IG-IDs that are OPEN: amendments must name the IG-ID and the elimination path.
Minimum 2 rows. Vague actions are structural failures.

`[AMENDMENTS-COMPLETE]`

---

### OUTPUT ARTIFACT

REQUIRES: [AMENDMENTS-COMPLETE]
PRODUCES: `simulations/draft/specs/{topic}-spec-{date}.md`

```yaml
---
skill: draft-spec
topic: {topic}
item: {feature-slug}
date: {YYYY-MM-DD}
skill_version: v1
input: scout-requirements={LOADED|NOT FOUND}, scout-feasibility={LOADED|NOT FOUND}, scout-compliance={LOADED|NOT FOUND}, scout-positioning={LOADED|NOT FOUND}, inertia-gaps={J}
---
```

PRODUCES hard-fail contract: all six fields required. Absent field = artifact invalid.

---

---

## Variation Axis Summary

| ID | Criterion | V-01 mechanism | V-02 mechanism | V-03 mechanism | V-04 mechanism | V-05 mechanism |
|----|-----------|---------------|---------------|---------------|---------------|---------------|
| C-17 | Named gate token | `[PM-SCAN-GATE]` role-completion token | `[DISCOVERY-TABLE]` PRODUCES declaration | `✓ SCOUT SCAN SEALED` natural-language seal | `[DISCOVERY-TABLE]` PRODUCES + token validity rule | Same as V-04 + `[INERTIA-ANALYZED]` for TYPE E |
| C-18 | Scripted verbatim fallback | `write: "..."` block in Phase 1 | `respond: "..."` block as PRODUCES of NOT FOUND branch | `respond: "..."` quoted block in Step 1 conditional | `write: "..."` block as PRODUCES of NOT FOUND branch | Same as V-04 |
| C-19 | Ordinal location markers | "location 1 of 2" / "location 2 of 2" labels on CNS Signal field | "[slot A-of-2]" / "[slot B-of-2]" labels | "entry 1/2" / "entry 2/2" natural-language labels | "location 1 of 2" / "location 2 of 2" labels | Same as V-04, extended to IG-ID column |
| C-15 | Two independent locations | Phase 2 PM table + Section 1 Purpose table | Step 2 sub-table 2a + Section 1 Purpose table | Step 2 PM table + Section 1 Purpose table | Phase 2 PM matrix + Section 1 Purpose table | Same as V-04 |
| C-16 | PM-first pre-assignment | Phase 2 before Phase 4; [STRATEGY-CHARTER] required | Step 2 REQUIRES [DISCOVERY-TABLE]; Step 4 REQUIRES [STRATEGY-CHARTER] | Step 2 "before you write a word"; ✓ PM CONTRACT SEALED gate | Phase 2 REQUIRES [DISCOVERY-TABLE]; Phase 4 REQUIRES [STRATEGY-CHARTER] | Same as V-04 + IG register before spec |

## New Pattern Candidates for v5

**V-05 only — IG-IDs as parallel finding surface**: assigning sequential IG-IDs to every
inertia-gap row creates a named finding namespace alongside R-IDs. Each IG-ID gets: an
elimination-path analysis, a risk signal amplified by the NS column (feasibility < 70 or
blocking compliance → AMPLIFIED), and a TYPE E finding type. The spec can be evaluated for
"AMPLIFIED + OPEN" coverage independently of R-ID gap analysis. Candidate C-20: "Per-IG-ID
elimination-path analysis with AMPLIFIED risk signal when NS column shows feasibility < 70
or any blocking compliance requirement."

**All variations — Token validity rule (V-04/V-05 explicit)**: a gate token declared without
its prerequisite evidence (contradiction scan block, scan completion statement) is invalid.
This upgrades C-17 from "a gate artifact must appear" to "a gate artifact must prove its
prerequisites." The V-04/V-05 explicit rule ("token is invalid without scan statement") is
the highest-specificity form; V-01 achieves it via the required scan completion statement
before gate emission.

**V-03 conversational — [SCAN REQUIRED] as inline field-level cue**: placing `[SCAN REQUIRED]`
as a marker directly before the field requiring inspection (not as a phase-level rule) creates
field-level active inspection guards. This is more granular than phase-level protocol rules and
more readable than per-step REQUIRES declarations. Combined with `respond:` scripted blocks,
the conversational register achieves structural rigor without formal protocol syntax.
