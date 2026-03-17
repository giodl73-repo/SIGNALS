Here are the 5 complete variations for `draft-spec` Round 3, targeting rubric v3. Written to `simulations/quest/variations/draft-spec-variations-R3-2026-03-14.md`.

---

## Round 3 Variation Summary

Each variation targets the three new rubric v3 criteria with a distinct primary mechanism:

| # | Axis | C-14 (inspection guard) | C-15 (two locations) | C-16 (PM-first lock) |
|---|------|------------------------|---------------------|----------------------|
| **V-01** | Role sequence: Temporal Lock | Pre-printed `R-__ vs R-__` rows + required scan completion statement | Labeled "location 1 of 2" / "location 2 of 2" in PM table and Purpose | `PM SCAN GATE` token blocks Architect |
| **V-02** | Output format: Enumeration Skeletons | Pre-printed blank rows force ID-format entry; "no conflicts" requires scan statement | Block 0 CNS-A + Block 2 CNS-B, labeled in headers | Block 0 is structurally first; PM coverage seal required |
| **V-03** | Lifecycle: Scan-Then-Confirm | Protocol-level rule: "CONFIRM without SCAN = violation" | Phase 2B scan (location 1) + Section 1 row (location 2) | Phase 2 PM → Phase 3 Architect; temporal lock explicit |
| **V-04** | Conversational + Inspection Override | `[SCAN REQUIRED]` markers with named source and required ID format | Step 2 PM table (loc 1) + Section 1 table (loc 2), both labeled | "Before you write a word" + PM seal required |
| **V-05** | Signal Register + Scan Gate Tokens | Gate token validity rule: PM CONTRACT invalid without scan block | Structural Axis Declaration names two-location CNS contract explicitly | PM = Phase 3, Architect = Phase 4, BLOCKED declared in axis table |

**Key design choices vs R2:**
- V-04 is the direct fix for R2-V-04's C-07/C-14 failure — same conversational axis, same inertia framing, but `[SCAN REQUIRED]` markers replace passive inertia defaults on enumeration fields
- V-05 inherits R2-V-05's signal register and axis declaration but adds scan gate token validity rules and explicitly declares the two-location CNS contract as a deliberate design choice, not accidental co-occurrence
- All five preserve the R2-V-01 excellence patterns: PM-first role sequence, inline role annotations per section, per-row Requirements table
ontract. Gate token emitted by PM scan gate blocks Architect from writing prose. Contradiction scan is integrated into PM step using pre-printed "R-__ vs R-__" rows.
**Hypothesis**: The R2-V-01 PM step was structural but not temporally locked — Architect could have written first. Adding a named PM SCAN GATE token that Architect may not proceed without converts C-16 from behavioral to contractual. The contradiction scan inside the PM step satisfies C-14 (named blank with required ID format) before any prose begins.

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.

Roles: PM (scan + contract) | Architect (spec sections) | Strategy, Compliance, Design (inline per section)

Temporal contract:
  PM SCAN GATE token is required before Architect writes any prose.
  Architect may not begin Section 1 until PM SCAN GATE token exists in output.
  Missing token = structural failure.
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

**No-scout-context conditional**: If Row 1 = NOT FOUND and all rows = NOT FOUND, stop here and respond: "No scout context for `{{topic}}`. Describe the feature in 3–5 sentences. PM will derive requirements from your description." Do not write EXECUTE content until Row 1 = LOADED or a user description is received.

---

**PM SCAN GATE**

Architect may not write any spec section until this gate completes and the PM SCAN GATE token is emitted.

**Substep A — Requirements scan:**

Read Row 1 (scout-requirements). List every R-ID and its text. This is the authority for all subsequent steps.

```
Scanning requirements from [filename]:
  R-01: [text]
  R-02: [text]
  ...
Total P0 requirements found: [N]
```

*(If Row 1 = NOT FOUND: write "Requirements scan waived — Row 1 NOT FOUND. Using user description. Derived IDs: R-IE-01, R-IE-02, etc., Priority = INFERRED.")*

**Substep B — Contradiction scan:**

For each pair of R-IDs from substep A where requirements could conflict (incompatible scope, competing priorities, contradictory behaviors), complete one pre-printed row. Add rows as needed. If no conflicts after scanning all pairs: write the scan completion statement.

Pre-printed contradiction rows (complete or add rows):

| R-ID A | R-ID B | Conflict description | Resolution / Flag |
|--------|--------|---------------------|------------------|
| R-__ | R-__ | [describe the conflict] | [proposed resolution, or "Flag for amendment"] |

Scan completion statement (required before gate token — do not skip):
`"Contradiction scan complete: read [N] R-IDs from [filename]. Found [N] conflict pair(s) as listed above."` or `"Contradiction scan complete: read [N] R-IDs from [filename] — no conflicts found."`

**Substep C — CNS pre-load (CNS location 1 of 2):**

Read rows 2–7 from SETUP. Record the primary signal from each loaded artifact:

| NS-type | Value | Source artifact |
|---------|-------|----------------|
| NS-feasibility | [score / posture / NOT FOUND] | [row 2 filename] |
| NS-compliance | [posture / NOT FOUND] | [row 4 filename] |
| NS-positioning | [differentiator / NOT FOUND] | [row 7 filename] |
| NS-market | [insight / NOT FOUND] | [row 3 filename] |

Every cell: NOT FOUND is valid. Blank is not.

**Substep D — P0 section assignment:**

Map each P0 requirement to one prescribed section. Section names are binding.

| R-ID | Requirement (abbreviated) | Priority | Assigned section | NS-signal relevant |
|------|--------------------------|----------|-----------------|-------------------|
| R-01 | | P0 | [Purpose / Requirements / Design / Constraints / Open Questions] | [NS-type from substep C, or NOT FOUND] |
| R-02 | | P0 | | |
| ... | | | | |

*(P1+ requirements: include with priority noted or mark "deferred.")*

PM SCAN GATE token (emit after substeps A–D complete):
`[PM SCAN GATE: [N] P0 requirements scanned from [filename], assigned to [M] sections. [N] conflict pairs found. CNS pre-load complete ([N] of 4 NS-signals loaded). Architect may not write spec sections until this token exists. Architect proceeds.]`

PM coverage statement: `[N]/[P0 total] P0 requirements assigned to sections.`

---

**EXECUTE**

BLOCKED until: PM SCAN GATE token exists.

Write the five sections in this exact order. Do not reorder, rename, or omit any section. Additional sections may be appended after Section 5 only. Section assignments from PM SCAN GATE substep D are binding — Architect does not reassign requirements.

---

**Section 1 — Purpose**

Write 2–4 sentences: what this feature does, who it serves, and why it exists now.

Pre-printed table — complete or leave cells visibly blank (CNS location 2 of 2):

| Field | Value |
|-------|-------|
| What it does | |
| Who it serves | |
| Why it exists now | |
| **CNS signal (location 2 of 2)** | **[read from PM SCAN GATE substep C — name NS-type, value, and source artifact; or write NOT FOUND if all NS-signals = NOT FOUND. Do not leave blank.]** |
| NS-signal source | [artifact filename] |

> **[PM inline]** Does this purpose align with the assignments in the PM SCAN GATE contract? PASS, or name the misalignment:

---

**Section 2 — Requirements**

P0 requirements covered: ___/___ *(state count before table; or "Waived — scout-requirements NOT FOUND" if PM waived above)*

| R-ID | Requirement (abbreviated) | Priority | Spec entry | Status |
|------|--------------------------|----------|------------|--------|
| | | P0 | [name the design component, constraint, or section element — not just "covered"] | COVERED / GAP |
| | | P1 | | |

Rules: Spec entry must be specific ("Design: retry-backoff component"). Conflict pairs from PM SCAN GATE substep B: copy into Notes cell — "Conflict: R-XX vs R-YY — see PM scan."

> **[Strategy inline]** Are any requirements in tension with positioning or feasibility signals? PASS, or name the conflict (R-IDs + source artifact):

---

**Section 3 — Design**

Describe implementation: major components, key decisions, data flow. Reference R-IDs. If the CNS signal from Section 1 shapes a design decision, trace it explicitly (e.g., "NS-feasibility score of 65 from [artifact] → constrain scope to Phase 1 only").

> **[Design inline]** Does this design satisfy UX, interaction, or naming constraints from loaded scout artifacts? PASS, or name the gap and source artifact:

---

**Section 4 — Constraints**

| Constraint | Type | Source artifact | Priority |
|-----------|------|----------------|----------|
| | technical / compliance / time / resource | | |

> **[Compliance inline]** Are compliance constraints accurately captured? Any missing from loaded scout-compliance? PASS or finding:

---

**Section 5 — Open Questions**

| # | Question | Blocking dependency | Recommended next action |
|---|---------|--------------------|-----------------------|
| 1 | | | |
| 2 | | | |

---

**FINDINGS**

Architect self-review. For each category: write a specific finding or state "None found" explicitly. Empty category without a written claim is a fail.

- **Contradictions**: Reference PM SCAN GATE substep B. For any conflict pairs found: "R-XX vs R-YY: [conflict]. Proposed: [resolution or amendment flag]." Or: "None found — confirmed in PM SCAN GATE contradiction scan."
- **Gaps**: Requirements or design areas not addressed.
- **Ambiguities**: Statements needing clarification before implementation.
- **Hotspots**: High-risk areas requiring close review.

---

**AMENDMENTS**

Numbered list, minimum 2 items. Each must name the section, state the specific change, and reference the finding. Vague items ("improve requirements") do not satisfy.

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

Document order: frontmatter → SETUP table → PM SCAN GATE (substeps A–D + token) → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Findings → Amendments

---

## V-02 — Pre-Printed Enumeration Skeletons

**Axis**: Output format — every enumeration criterion has a pre-printed skeleton with ID-format blanks that require specific values. Contradiction rows pre-print "R-__ vs R-__" format. Cross-namespace appears in two explicitly labeled structural blocks. PM pre-assignment is Block 0, temporally first.
**Hypothesis**: Pre-printing named blanks with required ID formats makes passive confirmation impossible — to satisfy a "R-__ vs R-__" cell you must provide IDs, not a prose confirmation. Two explicitly labeled CNS blocks (Block 0 = location A, Block 2 = location B) make the two-location design a verifiable structural choice, not accidental co-occurrence. Block 0 ordering makes C-16 temporal order structurally enforced.

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.

Your task: fill in this complete spec skeleton. Every cell or [placeholder] must be completed.
A cell left empty when not explicitly marked optional is a structural failure.
Block 0 (PM Pre-Assignment) must be completed before any spec section block.

Roles invoked inline: PM (Block 0, Block 2), Strategy (Block 3), Compliance (Block 5).
```

---

**BLOCK 0 — PM Pre-Assignment Contract** *(complete before any other block)*

Scan Row 1 (scout-requirements). Assign each requirement to a prescribed section. This block is temporally prior to all spec content.

| R-ID | Requirement (abbreviated) | Priority | Pre-assigned section | CNS-signal (location A) |
|------|--------------------------|----------|---------------------|------------------------|
| R-01 | | P0 | [Purpose / Requirements / Design / Constraints / Open Questions] | [NS-type: value, source: filename — from rows 2–7; or NOT FOUND] |
| R-02 | | P0 | | |
| *(add rows for all requirements)* | | | | |

CNS-signal column (location A) rules:
- Read rows 2–7 from Block 1 SETUP. For each requirement, name the most relevant non-requirements signal.
- "NS-[type]: [value], source: [filename]" or "NOT FOUND" — never blank.
- This is cross-namespace location A of 2. Location B appears in Block 2.

Contradiction scan — pre-printed rows (complete one per conflicting R-ID pair; add rows as needed):

| Conflict # | R-ID A | R-ID B | Conflict description | Resolution / Flag |
|-----------|--------|--------|---------------------|------------------|
| C-01 | R-__ | R-__ | [describe the conflict in one sentence] | [proposed resolution or "Flag: Amendment [N]"] |
| C-02 | R-__ | R-__ | | |

*(If no conflicts after scanning all R-ID pairs, write: "Scanned [N] R-ID pairs — no conflicts found." Do not leave the contradiction section blank or uncompleted.)*

PM coverage seal: `"[N]/[N] P0 requirements pre-assigned to sections. Contradiction scan complete. Architect proceeds to Block 1."`

*(If Row 1 = NOT FOUND: write "Block 0 waived — scout-requirements NOT FOUND. Derived requirements labeled R-IE-01, R-IE-02, etc. Priority = INFERRED.")*

---

**BLOCK 1 — Scout artifact status**

*(Complete after Block 0. Every row required.)*

| Row | Artifact type | Filename pattern | File found | Status |
|-----|--------------|-----------------|------------|--------|
| 1 | scout-requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | scout-feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | scout-market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | scout-compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | scout-stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | scout-naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | scout-positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

**No-scout-context conditional**: If all 7 rows = NOT FOUND, write: "Fallback activated. User description required: 'Describe the feature in 3–5 sentences.'" Continue with user description.

---

**BLOCK 2 — Section 1: Purpose**

| Field | Value |
|-------|-------|
| What this feature does | [2–3 sentences] |
| Who it serves | [user role or persona] |
| Why it exists now | [timing rationale] |
| **CNS-signal (location B of 2)** | **[NS-type: value, source: filename — read from rows 2–7 of Block 1. Must contain a named NS-type, value, and source filename. If all rows 2–7 = NOT FOUND, write "NOT FOUND" — blank is a structural failure.]** |
| NS-signal source artifact | [filename or "NOT FOUND"] |

> **[PM inline — Purpose]**: Does stated purpose reflect the problem in Block 0 pre-assignment? PASS, or state the misalignment:

---

**BLOCK 3 — Section 2: Requirements**

P0 requirements covered: ___/___ *(from Block 0 seal; or "Waived — scout-requirements NOT FOUND")*

| R-ID | Requirement text | Priority | Spec entry | Status |
|------|-----------------|----------|------------|--------|
| R-01 | | P0 | [specific design component or constraint name — e.g., "Design: retry-backoff component"] | COVERED / GAP |
| R-02 | | P0 | | COVERED / GAP |
| *(rows from Block 0 pre-assignment)* | | | | |

Conflict reference — copy conflict pairs from Block 0 contradiction scan:

| Conflict # | R-ID A | R-ID B | Spec entry status | Amendment? |
|-----------|--------|--------|------------------|-----------|
| *(from Block 0)* | | | [COVERED / GAP] | [Yes / No] |

> **[Strategy inline — Requirements]**: Requirements coherent with NS-positioning or NS-market signals from Block 1? PASS, or name the tension (R-IDs + artifact):

---

**BLOCK 4 — Section 3: Design**

| Component | Responsibility | Key decision | R-IDs addressed | CNS constraint |
|-----------|---------------|-------------|----------------|---------------|
| [name] | | | | [NS-type: value from Block 0 CNS location A or Block 2 location B — or NOT FOUND] |
| | | | | |

Design narrative (2–4 sentences connecting components to purpose; trace any CNS-signal to a specific design choice):

> [write here]

> **[Design inline]**: Design satisfies UX or naming constraints from loaded artifacts? PASS, or name the gap and source artifact:

---

**BLOCK 5 — Section 4: Constraints**

| Constraint | Type | Source artifact | Impact |
|-----------|------|----------------|--------|
| | technical / compliance / time / resource | [filename or "Architect judgment"] | |

> **[Compliance inline]**: Compliance constraints from scout-compliance accurately captured? PASS, or name the missing item:

---

**BLOCK 6 — Section 5: Open Questions**

| # | Question | Blocking dependency | Next action |
|---|---------|--------------------|-----------|
| 1 | | | |
| 2 | | | |

---

**BLOCK 7 — Findings**

*(For each row: write a specific finding or "None found" — empty cells are structural failures.)*

| Category | Finding | Severity |
|---------|---------|---------|
| Contradictions | [reference Block 0 conflict table. Or: "None found — see Block 0 scan."] | |
| Gaps | | |
| Ambiguities | | |
| Hotspots | | |

---

**BLOCK 8 — Amendments**

*(Minimum 2 rows. Each row names the section and finding. Vague entries don't satisfy.)*

| # | Target section | Specific change | Finding addressed |
|---|--------------|----------------|-----------------|
| 1 | | [section + exact change] | [Block N, finding category] |
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

Document order: frontmatter → Block 0 → Block 1 → Block 2 → Block 3 → Block 4 → Block 5 → Block 6 → Block 7 → Block 8

---

## V-03 — Scan-Then-Confirm Lifecycle

**Axis**: Lifecycle emphasis — every enumeration phase has two mandatory sub-steps: SCAN (active inspection of named data source, listing items found) then CONFIRM (conclusion stated only after citing the scan output). Confirmation without a preceding named scan is prohibited.
**Hypothesis**: Splitting enumeration phases into scan + confirm makes the inspection step a documented artifact the confirmation must reference. A model that would otherwise write "no contradictions found" must instead write "scanned [N] R-ID pairs from [filename] — none found." The temporal split also satisfies C-16 (PM scan precedes Architect) and C-15 (CNS scan appears in Phase 2 PM register and Phase 3.1 Purpose row).

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.

Roles: PM (phases 2A–2C) | Architect (phase 3) | Strategy, Compliance, Design (inline per section)

Scan-then-confirm protocol:
  Every enumeration step has two sub-steps:
    SCAN:    Read the named data source. List what you find, using the required format.
    CONFIRM: State your conclusion, citing the SCAN output by reference.
  You may not CONFIRM an enumeration result without a preceding SCAN.
  Writing "none found" or "no conflicts" without a SCAN is a protocol violation.
```

---

**PHASE 1 — Setup**

Scan `simulations/scout/` for `{{topic}}` artifacts:

| Row | Artifact type | Filename pattern | File found | Status |
|-----|--------------|-----------------|------------|--------|
| 1 | scout-requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | scout-feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | scout-market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | scout-compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | scout-stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | scout-naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | scout-positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

**No-scout-context conditional**: If Row 1 = NOT FOUND, write: "Fallback — no requirements artifact loaded. User description required before Phase 2 begins." Do not advance until Row 1 resolves or description received.

---

**PHASE 2 — PM Contract** *(temporal lock — Architect may not write spec sections until Phases 2A–2C complete)*

---

**Phase 2A — SCAN: P0 Requirements**

Read Row 1 (scout-requirements). List every R-ID and its text.

```
SCAN source: [filename]
  R-01: [text]
  R-02: [text]
  ...
SCAN complete: [N] total requirements found ([M] P0, [K] P1+)
```

*(If Row 1 = NOT FOUND: write "SCAN waived — Row 1 NOT FOUND. User description will be scanned instead. Derived IDs: R-IE-01, etc.")*

---

**Phase 2B — SCAN: Cross-namespace signals (CNS location 1 of 2)**

Read rows 2–7 from Phase 1. List each loaded artifact's primary signal.

```
SCAN source: rows 2–7 of Phase 1 SETUP table
  Row 2 (feasibility): [signal value and filename / NOT FOUND]
  Row 3 (market): [signal value and filename / NOT FOUND]
  Row 4 (compliance): [posture and filename / NOT FOUND]
  Row 5 (stakeholders): [priority and filename / NOT FOUND]
  Row 6 (naming): [constraint and filename / NOT FOUND]
  Row 7 (positioning): [differentiator and filename / NOT FOUND]
SCAN complete: [N] of 6 non-requirements rows loaded
```

---

**Phase 2C — CONFIRM: Pre-assignment table + Contradiction scan**

Based on Phase 2A scan, assign each P0 to a prescribed section:

| R-ID | Requirement (abbreviated) | Priority | Assigned section | NS-signal (from Phase 2B) |
|------|--------------------------|----------|-----------------|--------------------------|
| R-01 | | P0 | [Purpose / Requirements / Design / Constraints / Open Questions] | [NS-type: value, source: filename — from 2B scan; or NOT FOUND] |
| ... | | | | |

CONFIRM coverage: `"[N]/[N] P0 requirements assigned to [M] sections. Source: Phase 2A SCAN."`

**Phase 2C — Contradiction SCAN:**

Read the R-IDs from Phase 2A. For any two requirements that conflict:

```
Contradiction SCAN source: [filename from Phase 2A]
Scanning [N] R-ID pairs:
  R-__ vs R-__: [conflict description] — [resolution or "Flag for amendment"]
  ...
SCAN complete: [N] conflict pair(s) found.
```

*(This SCAN step is required. Do not write "no contradictions" without the above scan statement.)*

PM contract seal: `"Phase 2 complete: [N] P0 requirements scanned and assigned, [N] contradiction pairs found, CNS pre-load complete. Architect may proceed to Phase 3."`

---

**PHASE 3 — Execute**

BLOCKED until: PM contract seal from Phase 2C exists.

Write the five sections in this exact order. Do not reorder, rename, or omit. Section assignments from Phase 2C are binding.

---

**Section 1 — Purpose**

Write 2–4 sentences: what the feature does, who it serves, why it exists now.

Pre-printed CNS row *(CNS location 2 of 2 — reads from Phase 2B scan; leave visibly blank if all NOT FOUND)*:

| Field | Value |
|-------|-------|
| What it does | |
| Who it serves | |
| Why now | |
| **CNS signal (location 2 of 2)** | **[from Phase 2B SCAN — name NS-type, value, and source artifact. Blank if all rows 2–7 = NOT FOUND — a visible blank fires the gap; an absent row is a structural failure.]** |
| NS-signal source | [artifact filename or "NOT FOUND"] |

> **[PM inline]** Does this purpose address the problem the Phase 2C pre-assignment was built to solve? PASS or finding:

---

**Section 2 — Requirements**

P0 requirements covered: ___/___ *(from Phase 2C CONFIRM, or "Waived")*

| R-ID | Requirement (abbreviated) | Priority | Spec entry | Status |
|------|--------------------------|----------|------------|--------|
| | | P0 | [named component, constraint, or question — specific, not generic] | COVERED / GAP |
| | | P1 | | |

Contradictions: copy conflict pairs from Phase 2C contradiction SCAN into table. If none:
`"Contradiction reference: Phase 2C SCAN — [N] R-ID pairs scanned, no conflicts found."`

> **[Strategy inline]** Do requirements cohere with NS-positioning or NS-market signals from Phase 2B? PASS or finding (R-IDs + NS-type + source):

---

**Section 3 — Design**

Describe implementation: major components, decisions, data flow. Reference R-IDs. Trace any CNS signal from Section 1 to a specific design constraint if applicable (e.g., "NS-feasibility score of 62 from [artifact] → Phase 1 scope only").

> **[Design inline]** Design satisfies UX or naming constraints from loaded artifacts? PASS or gap with source artifact:

---

**Section 4 — Constraints**

| Constraint | Type | Source artifact | Notes |
|-----------|------|----------------|-------|
| | technical / compliance / time / resource | [filename or "Architect judgment"] | |

> **[Compliance inline]** Any compliance constraint missing? PASS or finding with source:

---

**Section 5 — Open Questions**

| # | Question | Blocking dependency | Next action |
|---|---------|--------------------|-----------|
| 1 | | | |
| 2 | | | |

---

**PHASE 4 — Findings**

For each category: specific finding or explicit "None found." Empty without written claim is a fail.

- **Contradictions**: Reference Phase 2C contradiction SCAN. For any pairs found: "R-XX vs R-YY: [conflict]. Proposed: [resolution]." Or: "None found — confirmed in Phase 2C SCAN (N R-ID pairs examined)."
- **Gaps**: Requirements or design areas not addressed.
- **Ambiguities**: Statements needing clarification.
- **Hotspots**: High-risk areas.

---

**PHASE 5 — Amendments**

Numbered list, minimum 2 items. Each names the section, states the specific change, references the finding. No vague items.

Format: `N. Section [name] — [specific change] — Addresses: [finding category, element or R-ID]`

---

**OUTPUT**

Write to `simulations/draft/specs/{{topic}}-spec-{{date}}.md`.

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

Document order: frontmatter → Phase 1 → Phase 2A (SCAN) → Phase 2B (SCAN) → Phase 2C (CONFIRM + contradiction SCAN) → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Findings → Amendments

---

## V-04 — Conversational Register + Active Inspection Override

**Axes**: Phrasing register (conversational) + active inspection override for all enumeration fields.
**Hypothesis**: R2-V-04's C-07 failure was caused by "No contradictions assumed — override if found" allowing passive confirmation without R-ID inspection. This variation preserves conversational tone but adds explicit "inspection required" markers wherever an inertia default could produce false confirmation: the model is told to scan first, name what it finds in the required ID format, and only confirm absence after that scan. Two CNS locations are labeled (Step 2 = location 1, Section 1 = location 2). PM pre-assignment step runs before spec writing begins.

---

```
You're writing a spec for `{{topic}}` using the `draft-spec` skill.

You're the Architect. PM runs upfront coverage and contradiction checks before you write a word.
Strategy, Compliance, and Design give inline checks per section.

Two types of fields in this prompt:
  Standard fields: describe or confirm; inertia defaults show you what's typical.
  Inspection-required fields: you must read the named source and list what you find before
    confirming anything. These are marked [SCAN REQUIRED]. You cannot confirm absence on an
    [SCAN REQUIRED] field without first naming what you read and what you found.
```

---

**Step 1 — What's loaded?**

Check `simulations/scout/` for `{{topic}}` artifacts:

| Row | What you're looking for | Pattern | File found | Status |
|-----|------------------------|---------|------------|--------|
| 1 | Requirements | {{topic}}-requirements-*.md | | LOADED / NOT FOUND |
| 2 | Feasibility | {{topic}}-feasibility-*.md | | LOADED / NOT FOUND |
| 3 | Market | {{topic}}-market-*.md | | LOADED / NOT FOUND |
| 4 | Compliance | {{topic}}-compliance-*.md | | LOADED / NOT FOUND |
| 5 | Stakeholders | {{topic}}-stakeholders-*.md | | LOADED / NOT FOUND |
| 6 | Naming | {{topic}}-naming-*.md | | LOADED / NOT FOUND |
| 7 | Positioning | {{topic}}-positioning-*.md | | LOADED / NOT FOUND |

If all 7 = NOT FOUND: "I don't have scout context for `{{topic}}` yet. Give me 3–5 sentences on what this should do. I'll derive requirements and proceed." Don't start the spec until Row 1 resolves.

---

**Step 2 — PM covers requirements before you write a word**

*[SCAN REQUIRED]* Read the loaded scout-requirements file (Row 1). Don't assume the list — scan it and report.

```
Scanning requirements from [filename]:
  R-01: [text]
  R-02: [text]
  ...
```

Map each P0 to a section:

| R-ID | What it says (brief) | Priority | Which section covers it | CNS-signal (location 1 of 2) |
|------|---------------------|----------|------------------------|------------------------------|
| R-01 | | P0 | [Purpose / Requirements / Design / Constraints / Open Questions] | *[SCAN REQUIRED: check rows 2–7. Name one relevant signal: "NS-[type]: [value], source: [filename]". Write NOT FOUND if all rows 2–7 are NOT FOUND — not blank.]* |
| R-02 | | P0 | | |
| ... | | | | |

*[SCAN REQUIRED — Contradictions]* Before moving on, scan your R-IDs for conflicts. For any pair pulling in opposite directions: "R-__ vs R-__: [one sentence on the conflict]. [Proposed resolution or 'Flag for amendment']." Then: "Scanned [N] R-ID pairs from [filename] — [N] conflict(s) found." You cannot skip this scan or write any inertia default in its place.

PM seal: "P0 requirements covered: ___/___. Contradiction scan complete. Writing begins now."

*(If Row 1 = NOT FOUND: "Waived — requirements not loaded. Using user description. PM labels derived requirements R-IE-01...")*

---

**Step 3 — Write the spec**

Work through these five sections in order. Don't skip, reorder, or rename any.

---

**Section 1 — Purpose**

*Standard field: purpose is roughly "let teams signal feature readiness from evidence" — confirm or be more specific to `{{topic}}`.*

Write 2–4 sentences: what `{{topic}}` does, who it helps, why now.

Then fill in this table. The CNS-signal row is always here (location 2 of 2). If you have a loaded non-requirements artifact, name the signal and where it came from. If you don't, write NOT FOUND — don't leave it blank:

| Purpose field | Value |
|--------------|-------|
| What it does | |
| Who it serves | |
| Why now, not later | |
| **CNS-signal (location 2 of 2)** | ***[SCAN REQUIRED: check rows 2–7 from Step 1. Name the most relevant signal: "NS-[type]: [value], source: [filename]". If all rows 2–7 = NOT FOUND, write NOT FOUND. Do not leave this cell blank.]*** |
| Signal source | [artifact filename or "NOT FOUND"] |

> *PM check: does this purpose address the real problem from Step 2? PASS or one-sentence finding:*

---

**Section 2 — Requirements**

*Standard field: P0 count starts at 0 — fill in from Step 2 PM scan.*

P0 requirements covered: ___/___ *(from Step 2 PM seal, or "Waived" if NOT FOUND)*

| R-ID | What it says (brief) | Priority | Which part covers it | Covered? |
|------|---------------------|----------|---------------------|---------|
| | | P0 | [specific name — "Design: [component]" or "Constraint: [name]" — not generic] | COVERED / GAP |
| | | P1 | | |

Contradictions: copy conflict pairs from Step 2 scan. For each: "R-__ vs R-__: [conflict]. [Resolution or amendment flag]." If none found in Step 2 scan: "No contradictions — confirmed in Step 2 scan ([N] R-ID pairs examined)."

> *Strategy check: requirements coherent with market or positioning signals? PASS or one-sentence finding (R-IDs + artifact):*

---

**Section 3 — Design**

*Standard field: the design should improve on what teams do today without this feature. Briefly note the workflow gap before describing your approach.*

Describe implementation: key components, how they connect, decisions and why. Reference R-IDs. If the CNS-signal from Section 1 shapes a design decision, say so and name the artifact.

> *Design check: any UX, naming, or interaction constraints from loaded artifacts not addressed? PASS or name the artifact:*

---

**Section 4 — Constraints**

*Standard field: constraints are typically technical or compliance-derived. Confirm the loaded compliance artifact's posture or add constraints from Architect judgment.*

| What the constraint is | Type | Where it comes from | Why it matters |
|-----------------------|------|---------------------|---------------|
| | technical / compliance / time / resource | [filename or "Architect judgment"] | |

> *Compliance check: any hard compliance constraint missing? Check Row 4. PASS or finding:*

---

**Section 5 — Open Questions**

| Question | What's blocking it | What would resolve it |
|---------|---------------------|----------------------|
| | | |
| | | |

---

**Step 4 — Self-review**

For each category, write a specific finding or "None found" — don't leave any blank.

- **Contradictions** — *[SCAN REQUIRED]: reference your Step 2 R-ID scan. For any conflict pairs found, state: "R-XX vs R-YY: [conflict]. [Resolution or flag]." If none: "None found — Step 2 scan examined [N] R-ID pairs from [filename], no conflicts found." You may not write "no contradictions" without citing the Step 2 scan.*
- **Gaps** — anything not addressed that should be?
- **Ambiguities** — any statement interpretable multiple ways before implementation?
- **Hotspots** — anything fragile or risky?

---

**Step 5 — Amendments**

At least 2 specific, actionable items. Each names the section and says exactly what to change. Generic items ("improve the design section") don't count.

Format: `N. [Section name] — [exactly what to change] — from: [which finding]`

---

**Output**

Save to `simulations/draft/specs/{{topic}}-spec-{{date}}.md`. Every field required:

```yaml
---
skill: draft-spec
topic: {{topic}}
item: spec
date: {{date}}
skill_version: 0.1.0
input: [loaded artifacts, comma-separated; or "freeform: [first 10 words]"]
---
```

Document order: frontmatter → scout table → Step 2 PM contract (scan + contradiction SCAN) → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Findings → Amendments

---

## V-05 — Signal Register + Scan Gate Tokens + Two-Location CNS Contract

**Axes**: Signal register pre-load (from R2-V-05) + scan gate tokens that require a named scan output before emission + explicit two-location CNS contract.
**Hypothesis**: R2-V-05 nearly reached perfect score but failed C-12 (inline role annotations declared at top, not embedded in sections). This variation: (1) preserves the signal register as CNS-location 1; (2) declares Purpose section pre-printed row as CNS-location 2 in an explicit axis declaration; (3) adds scan-gate token rules requiring a named scan output before enumeration gate tokens can be emitted — preventing passive confirmation on contradiction and CNS fields even with gate token machinery; (4) fixes R2-V-05 C-12 by embedding role annotations inline within sections, not at document top.

---

```
You are running `/draft:spec` for Signal. Topic: {{topic}}.

Roles: Strategy | PM | Architect

Gate token contract: Every role transition emits a token.
Two gate token validity rules govern enumeration steps:
  CNS rule:  Signal Register gate token is invalid unless the CNS pre-load scan lists
             each of rows 2–7 by NS-type with an explicit value or "NOT FOUND."
  SCAN rule: PM CONTRACT gate token is invalid unless the contradiction scan names
             the source artifact and states a completion count before confirming absence.
Missing token or invalid token = incomplete step. Role that follows may not proceed.
```

---

**STRUCTURAL AXIS DECLARATION**

*(Not a phase. Declaration of how this skill guarantees structural coverage. Read before executing.)*

| Axis | Mechanism | Criteria guarded |
|------|-----------|-----------------|
| Axis A — Role-sequential gates | BLOCKED tokens prevent roles from acting out of order | C-01, C-02, C-03, C-04 |
| Axis B — Signal Register (CNS location 1) | Signal Register phase extracts named NS-signals before Architect writes; Purpose section pre-printed row reads from register (CNS location 2) | C-10, C-11, C-15 |
| Axis C — PM pre-assignment contract | PM maps every P0 to a section before Architect writes; Requirements table carries per-row Spec entry and Status | C-03, C-13, C-16 |
| Axis D — Scan gate tokens | Enumeration gate tokens invalid without named scan output; prevents passive confirmation on contradictions and CNS fields | C-07, C-14 |

| Criterion | Axis A | Axis B | Axis C | Axis D |
|-----------|--------|--------|--------|--------|
| C-01 Structure | ✓ (PM section lock) | — | ✓ (PM section names bound) | — |
| C-02 Scout table | ✓ (SETUP precedes gates) | ✓ (register reads SETUP rows) | — | — |
| C-03 P0 coverage | ✓ (BLOCKED until contract) | — | ✓ (PM count + per-row assignment) | — |
| C-04 Self-review | ✓ (BLOCKED until ARCHITECT SEAL) | — | — | ✓ (scan gate on contradictions) |
| C-05 Frontmatter | ✓ (template) | ✓ (input field = artifact list from SETUP) | — | — |

Every essential criterion guarded by ≥2 independent axes.

**Two-location CNS contract (C-15 explicit design):**
- CNS location 1: Signal Register table — extracted before any spec writing (Phase 2)
- CNS location 2: Purpose section pre-printed "Cross-namespace signal" row — reads from register (Phase 4, Section 1)
- These two locations are structurally independent: location 1 is a data-extraction phase; location 2 is a template row in spec content. If location 1 is filled, C-10 passes. If location 2 is empty, C-11's visibility criterion fires from location 2.

---

**PHASE 1 — SETUP**

Scan `simulations/scout/` for `{{topic}}` artifacts. Output table before any other content:

| Row | Artifact type | Filename pattern | File found | Status |
|-----|--------------|-----------------|------------|--------|
| 1 | scout-requirements | {{topic}}-requirements-*.md | | loaded/not found |
| 2 | scout-feasibility | {{topic}}-feasibility-*.md | | loaded/not found |
| 3 | scout-market | {{topic}}-market-*.md | | loaded/not found |
| 4 | scout-compliance | {{topic}}-compliance-*.md | | loaded/not found |
| 5 | scout-stakeholders | {{topic}}-stakeholders-*.md | | loaded/not found |
| 6 | scout-naming | {{topic}}-naming-*.md | | loaded/not found |
| 7 | scout-positioning | {{topic}}-positioning-*.md | | loaded/not found |

**No-scout-context conditional**: If row 1 = "not found" and all rows = "not found": add row 8 (user intent, BLOCKED). Ask: "Describe `{{topic}}` in 3–5 sentences. Signal Register will show all NS-signals as NOT FOUND." STOP until row 1 resolved.

---

**PHASE 2 — SIGNAL REGISTER** *(CNS location 1 of 2)*

*(Axis B: load all non-requirements signals before Architect writes. This phase produces named signal variables the spec sections read from.)*

Read rows 2–7 from Phase 1. Extract and record:

```
Signal Register SCAN source: SETUP rows 2–7
  NS-feasibility: [score / posture / NOT FOUND] — source: [row 2 filename]
  NS-market: [key insight / NOT FOUND] — source: [row 3 filename]
  NS-compliance: [blocking / advisory / none / NOT FOUND] — source: [row 4 filename]
  NS-stakeholders: [top priority / NOT FOUND] — source: [row 5 filename]
  NS-naming: [constraint / NOT FOUND] — source: [row 6 filename]
  NS-positioning: [differentiator / NOT FOUND] — source: [row 7 filename]
SCAN complete: [N] of 6 rows loaded.
```

Rules: NOT FOUND is a valid explicit value — never blank. Architect reads Signal Register during section authoring, not the scout artifacts directly.

Signal Register gate token (emit after scan complete):
`[SIGNAL REGISTER: [N] of 6 NS-signals loaded. CNS pre-load scan complete (rows 2–7 named above). PM may not map requirements until signal register is complete. PM proceeds.]`

*Gate token validity rule: token is invalid if the SCAN block above is absent or if any row shows a blank instead of a value or "NOT FOUND."*

---

**PHASE 3 — PM COVERAGE CONTRACT**

BLOCKED until: SIGNAL REGISTER token exists.

*(Axis C: PM maps P0 requirements to sections before Architect writes. Axis D: contradiction scan required before gate token emission.)*

From loaded scout-requirements (row 1), map every P0 to a section:

| R-ID | Requirement (abbreviated) | Priority | Assigned section | NS-signal |
|------|--------------------------|----------|-----------------|----------|
| R-01 | | P0 | [Purpose / Requirements / Design / Constraints / Open Questions] | [NS-type from Register, or NOT FOUND] |
| ... | | | | |

P0 coverage count: [N]/[P0 total] P0 requirements assigned. *(State "Waived" explicitly if row 1 = NOT FOUND.)*

**Contradiction SCAN** *(Axis D — required before gate token):*

```
Contradiction SCAN source: [scout-requirements filename, row 1]
Scanning [N] R-ID pairs:
  R-__ vs R-__: [conflict description] — [resolution or "Flag for amendment"]
  ...
SCAN complete: [N] conflict pair(s) found.
```

*(This scan must appear before the PM CONTRACT gate token. A gate token emitted without this scan block is invalid per the SCAN rule.)*

PM CONTRACT gate token:
`[PM CONTRACT: [N] P0 requirements mapped to [M] sections. Contradiction SCAN complete ([N] conflict pairs found, source: [filename]). NS-signal column populated from Signal Register. Architect may not write spec content until matrix is built from this contract. Architect proceeds.]`

*Gate token validity rule: token is invalid if contradiction SCAN block is absent.*

---

**PHASE 4 — EXECUTE**

BLOCKED until: SIGNAL REGISTER and PM CONTRACT tokens exist.

Write the five sections in this exact order. Do not reorder, rename, or omit. Each section reads from the Signal Register and PM Coverage table — do not re-read scout artifact files directly. Section assignments from Phase 3 are binding.

---

**Section 1 — Purpose**

Write 2–4 sentences: what `{{topic}}` does, who it serves, why it exists now.

Pre-printed signal row *(CNS location 2 of 2 — reads from Signal Register — complete from NS-signal values, leave visibly blank if all NOT FOUND)*:

| Field | Value |
|-------|-------|
| What it does | |
| Who it serves | |
| Why now | |
| **Cross-namespace signal (location 2 of 2)** | **[from Signal Register: NS-positioning / NS-feasibility / NS-market — name the NS-type, value, and source artifact. Leave blank if all NOT FOUND — blank is a visible gap that fires C-11; an absent row is a structural failure.]** |
| NS-signal source | [Signal Register entry: NS-[type] from [artifact]] |

> **[PM inline]** Does this purpose address the problem the Phase 3 PM Coverage contract was built to solve? PASS or finding:

---

**Section 2 — Requirements**

P0 requirements covered: ___/___ *(from Phase 3 PM CONTRACT count; or "Waived" if explicitly stated)*

| R-ID | Requirement (abbreviated) | Priority | Spec entry | Status | NS-signal |
|------|--------------------------|----------|------------|--------|-----------|
| | | P0 | [named component, constraint, or question — specific] | COVERED / GAP | [NS-type or NOT FOUND] |
| | | P1 | | | |

Contradiction reference: copy pairs from Phase 3 contradiction SCAN. If none: "No contradictions — Phase 3 SCAN examined [N] R-ID pairs from [filename]."

> **[Strategy inline]** Do requirements cohere with NS-positioning or NS-market signals? PASS or finding (R-IDs + NS-type + source):

---

**Section 3 — Design**

Describe implementation: components, decisions, data flow. Reference R-IDs. Trace NS-feasibility to a design constraint if NS-feasibility ≠ NOT FOUND (e.g., "NS-feasibility score of 62 from [artifact] → Phase 1 scope only").

> **[Design inline]** Design satisfies UX or naming constraints from loaded artifacts? PASS or finding with source:

---

**Section 4 — Constraints**

| Constraint | Type | NS-signal source | Priority |
|-----------|------|-----------------|----------|
| | technical / compliance / time / resource | [NS-compliance / NS-feasibility / Architect judgment] | |

NS-compliance from Signal Register: [value] — every blocking compliance item must appear as a constraint row.

> **[Compliance inline]** Any compliance constraint missing? PASS or finding:

---

**Section 5 — Open Questions**

| # | Question | NS-signal that would resolve it | Next action |
|---|---------|--------------------------------|-------------|
| 1 | | [NS-type or "none"] | |
| 2 | | | |

---

**PHASE 5 — FINDINGS**

BLOCKED until: ARCHITECT SEAL token exists.

*(Emit ARCHITECT SEAL after completing all five sections: `[ARCHITECT SEAL: [M] sections written. Phase 5 reads matrix and signal register only. Phase 5 proceeds.]`)*

Read Signal Register and Phase 3 contract only. Do not re-read prose or scout artifacts.

- **Contradictions**: Reference Phase 3 contradiction SCAN. Name pairs: "R-XX vs R-YY: [conflict]. [Resolution]." Or: "None found — Phase 3 SCAN confirmed ([N] pairs examined)."
- **Gaps**: Unaddressed requirements or design areas.
- **Ambiguities**: Statements needing clarification.
- **Hotspots**: High-risk areas.

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

Document order: frontmatter → Structural Axis Declaration → Phase 1 → Phase 2 (Signal Register) → Phase 3 (PM Contract + contradiction SCAN) → Section 1 → Section 2 → Section 3 → Section 4 → Section 5 → Findings → Amendments

---

## Variation Summary

| Variation | Primary axis | Secondary axis | C-14 mechanism | C-15 mechanism | C-16 mechanism |
|-----------|-------------|---------------|---------------|---------------|---------------|
| V-01 | Role sequence: temporal lock | — | Pre-printed "R-__ vs R-__" rows in PM step + scan completion statement required | "CNS location 1 of 2" label in PM table + "CNS location 2 of 2" label in Purpose | PM SCAN GATE token; Architect BLOCKED until token exists |
| V-02 | Output format: pre-printed enumeration skeletons | — | Pre-printed "R-__ vs R-__" blank rows with "no conflicts" only after scan statement | Block 0 CNS-A column + Block 2 CNS-B row, both labeled and structurally mandatory | Block 0 is temporally first; PM coverage seal required before any spec block |
| V-03 | Lifecycle emphasis: scan-then-confirm protocol | — | SCAN sub-step mandatory before CONFIRM on every enumeration field; "You may not CONFIRM without a preceding SCAN" stated in protocol | Phase 2B CNS scan (location 1) + Section 1 pre-printed row (location 2) | Phase 2 PM contract precedes Phase 3 Architect; "temporal lock" explicit |
| V-04 | Phrasing: conversational | Active inspection override | "[SCAN REQUIRED]" markers on contradiction and CNS fields; "You cannot confirm absence without naming what you read" | Step 2 PM table (location 1) + Section 1 table (location 2), both labeled | Step 2 runs "before you write a word"; PM seal required before writing begins |
| V-05 | Signal register pre-load | Scan gate tokens | Gate token validity rule: "PM CONTRACT token invalid if contradiction SCAN block absent" | Signal Register (location 1, Axis B) + Purpose pre-printed row (location 2); two-location contract declared in Structural Axis Declaration | PM Coverage Contract is Phase 3; Architect is Phase 4; BLOCKED until PM CONTRACT token; explicit in Structural Axis Declaration C-16 row |

**Primary C-14 discriminator across variations**: V-01/V-02/V-03 use structural pre-printing (blank rows with required ID format); V-04 uses an inline "[SCAN REQUIRED]" marker as an instruction-level prohibition; V-05 uses gate token validity rules as a mechanical constraint (no token = no proceed regardless of content). V-05's C-14 enforcement is strongest: the gate token itself is declared invalid if the scan is absent.

**Primary C-15 discriminator**: V-01 labels "location 1 of 2" and "location 2 of 2" inline. V-02 labels "location A" and "location B" in block headers. V-03 assigns locations to named phases (Phase 2B = location 1, Section 1 = location 2). V-04 labels inline in step-level prose. V-05 declares two-location contract explicitly in Structural Axis Declaration table before execution begins — making it self-documenting proof rather than a verifiable structural claim.

**Primary C-16 discriminator**: V-01 uses a named gate token (PM SCAN GATE). V-02 uses block ordering (Block 0 first) and PM coverage seal. V-03 uses phase ordering (Phase 2 PM before Phase 3 Architect) with explicit temporal lock language. V-04 uses conversational phrasing ("before you write a word"). V-05 uses both BLOCKED gates and explicit Structural Axis Declaration row for C-16.
