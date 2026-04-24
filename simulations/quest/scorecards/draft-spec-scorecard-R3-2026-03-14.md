# Quest Score — `draft-spec` Round 3

## Per-Variation Scoring

### V-01 — Role Sequence: Temporal Lock

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Section structure | **PASS** | Five sections in prescribed order; FINDINGS and AMENDMENTS appended after Section 5 |
| C-02 | Scout artifact table | **PASS** | SETUP table (7 rows, LOADED/NOT FOUND) is the first block, before PM SCAN GATE and EXECUTE |
| C-03 | P0 requirement coverage | **PASS** | PM substep D assigns every P0 to a named section; PM SCAN GATE token states explicit count; Section 2 states ___/___ before table |
| C-04 | Self-review findings | **PASS** | FINDINGS section has four named categories; "None found" must be written explicitly; empty = fail |
| C-05 | Frontmatter complete | **PASS** | OUTPUT block specifies `{{topic}}-spec-{{date}}.md`; all required fields listed |
| C-06 | Secondary role validation | **PASS** | PM inline (Section 1), Strategy inline (Section 2), Design inline (Section 3), Compliance inline (Section 4) — each records PASS or finding |
| C-07 | Contradiction detection | **PASS** | Substep B pre-prints `R-__ vs R-__` rows and requires scan completion statement before gate token can be emitted |
| C-08 | Actionable amendment list | **PASS** | AMENDMENTS: minimum 2, names section + specific change + finding reference; vague items explicitly excluded |
| C-09 | No-scout fallback | **PASS** | Named conditional: "If Row 1 = NOT FOUND and all rows = NOT FOUND, stop here and respond…" |
| C-10 | Cross-namespace coherence | **PASS** | CNS substep C pre-loads signal values; Section 3 Design traces NS-feasibility to design constraint with source artifact named |
| C-11 | Pre-printed CNS column | **PASS** | Section 1 Purpose table has `**CNS signal (location 2 of 2)**` row; blank is not valid; absent row is structural failure |
| C-12 | Inline role annotations | **PASS** | Role annotations embedded as blockquotes within their target sections, not deferred to later phase |
| C-13 | Per-row P0 status column | **PASS** | Section 2 table: R-ID + Spec entry (named component required, e.g. "Design: retry-backoff") + Status per row |
| C-14 | Active inspection guard | **PASS** | `R-__ vs R-__` named blanks in substep B rows; scan completion statement required before gate token emission; blank CNS cells prohibited |
| C-15 | CNS two independent locations | **PASS** | Substep C labeled "CNS location 1 of 2" (data-extraction phase) + Section 1 labeled "CNS location 2 of 2" (spec content) — structurally independent, deliberately labeled |
| C-16 | PM-first coverage pre-assignment | **PASS** | PM substep D assigns every P0 to a section; gate token blocks Architect; Section 2 assignments from substep D are "binding — Architect does not reassign" |

**Essential**: 5/5 = 60 pts | **Recommended**: 3/3 = 30 pts | **Aspirational**: 8/8 = 40 pts  
**Composite**: 130/130 | **Golden**: YES

---

### V-02 — Pre-Printed Enumeration Skeletons

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Section structure | **PASS** | Five sections in prescribed order (Blocks 2–6) |
| **C-02** | **Scout artifact table** | **FAIL** | Block 0 (PM Pre-Assignment) is explicitly ordered first — "complete before any other block" — producing document content before Block 1 (scout table). Scout table appears *after* PM execution output, not before any EXECUTE content |
| C-03 | P0 requirement coverage | **PASS** | Block 0 PM coverage seal: "[N]/[N] P0 requirements pre-assigned to sections"; Block 3 states count from seal |
| C-04 | Self-review findings | **PASS** | Block 7 Findings table; empty cells are structural failures; "None found" must be written |
| C-05 | Frontmatter complete | **PASS** | Block 9 OUTPUT with all required fields |
| C-06 | Secondary role validation | **PASS** | PM inline (Block 2), Strategy inline (Block 3), Design inline (Block 4), Compliance inline (Block 5) |
| C-07 | Contradiction detection | **PASS** | Block 0 pre-prints `R-__ | R-__` rows; "no conflicts" requires scan statement citing N R-ID pairs |
| C-08 | Actionable amendment list | **PASS** | Block 8: minimum 2 rows, each naming section + specific change + finding; vague entries excluded |
| C-09 | No-scout fallback | **PASS** | Named conditional in Block 1: "If all 7 rows = NOT FOUND, write: 'Fallback activated...'" |
| C-10 | Cross-namespace coherence | **PASS** | CNS-signal column (location A) in Block 0; CNS-signal row (location B) in Block 2; Block 4 Design traces signal to design choice |
| C-11 | Pre-printed CNS column | **PASS** | Block 2 Purpose has `**CNS-signal (location B of 2)**` row; blank is structural failure |
| C-12 | Inline role annotations | **PASS** | Role annotations embedded within each section block (Blocks 2–5) |
| C-13 | Per-row P0 status column | **PASS** | Block 3 table: R-ID + Spec entry (specific component name required) + Status per row |
| C-14 | Active inspection guard | **PASS** | `R-__ | R-__` named blanks in Block 0 contradiction rows; scan statement required before PM seal |
| C-15 | CNS two independent locations | **PASS** | Block 0 "location A" column (PM assignment table) + Block 2 "location B of 2" row (Purpose section) — both labeled |
| C-16 | PM-first coverage pre-assignment | **PASS** | Block 0 is temporally first; PM seal required before "Architect proceeds to Block 1"; section assignments binding |

**Essential**: 4/5 = 48 pts | **Recommended**: 3/3 = 30 pts | **Aspirational**: 8/8 = 40 pts  
**Composite**: 118/130 | **Golden**: NO (C-02 essential fail)

---

### V-03 — Scan-Then-Confirm Lifecycle

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Section structure | **PASS** | Five sections in prescribed order in Phase 3; FINDINGS and AMENDMENTS appended after |
| C-02 | Scout artifact table | **PASS** | Phase 1 SETUP is the first phase; scout table with 7 rows precedes Phases 2–5 |
| C-03 | P0 requirement coverage | **PASS** | Phase 2A SCAN lists all R-IDs; Phase 2C CONFIRM table maps P0s to sections; coverage count stated |
| C-04 | Self-review findings | **PASS** | Phase 4 Findings: four categories; "None found" must be written; empty = fail |
| C-05 | Frontmatter complete | **PASS** | OUTPUT block with all required fields |
| C-06 | Secondary role validation | **PASS** | PM inline (Section 1), Strategy inline (Section 2), Design inline (Section 3), Compliance inline (Section 4) |
| C-07 | Contradiction detection | **PASS** | Phase 2C Contradiction SCAN: template with `R-__ vs R-__` format; SCAN complete statement required; protocol rule: CONFIRM without SCAN = violation |
| C-08 | Actionable amendment list | **PASS** | Phase 5: minimum 2, names section + specific change + finding reference |
| C-09 | No-scout fallback | **PASS** | Named conditional in Phase 1: "If Row 1 = NOT FOUND, write: 'Fallback — no requirements artifact loaded…'" |
| C-10 | Cross-namespace coherence | **PASS** | Phase 2B SCAN records CNS signals; Section 1 CNS row names signal + source; Section 3 traces NS-feasibility to design constraint |
| C-11 | Pre-printed CNS column | **PASS** | Section 1 Purpose: `**CNS signal (location 2 of 2)**` row; absent row = structural failure |
| C-12 | Inline role annotations | **PASS** | Role annotations embedded as blockquotes within their target sections in Phase 3 |
| C-13 | Per-row P0 status column | **PASS** | Section 2 table: R-ID + Spec entry (specific, not generic) + Status per row |
| C-14 | Active inspection guard | **PASS** | Protocol-level rule: "You may not CONFIRM an enumeration result without a preceding SCAN"; template `R-__ vs R-__`; Phase 2B scan names each row source explicitly |
| C-15 | CNS two independent locations | **PASS** | Phase 2B labeled "CNS location 1 of 2" (scan phase) + Section 1 labeled "CNS location 2 of 2" (spec content) — structurally independent |
| C-16 | PM-first coverage pre-assignment | **PASS** | Phase 2C pre-assignment table (PM) before Phase 3 (Architect); "temporal lock" explicit; "BLOCKED until: PM contract seal from Phase 2C exists" |

**Essential**: 5/5 = 60 pts | **Recommended**: 3/3 = 30 pts | **Aspirational**: 8/8 = 40 pts  
**Composite**: 130/130 | **Golden**: YES

---

### V-04 — Conversational Register + Active Inspection Override

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Section structure | **PASS** | Five sections in prescribed order in Step 3 |
| C-02 | Scout artifact table | **PASS** | Step 1 scout table (7 rows) is the first step; precedes Step 2 PM and Step 3 spec writing |
| C-03 | P0 requirement coverage | **PASS** | Step 2 [SCAN REQUIRED] reads requirements; PM seal states count; Section 2 count "from Step 2 PM seal" |
| C-04 | Self-review findings | **PASS** | Step 4 Self-review: four categories; "don't leave any blank" |
| C-05 | Frontmatter complete | **PASS** | Output block with all required fields |
| C-06 | Secondary role validation | **PASS** | PM check (Section 1), Strategy check (Section 2), Design check (Section 3), Compliance check (Section 4) — all inline |
| C-07 | Contradiction detection | **PASS** | `[SCAN REQUIRED — Contradictions]` marker; `R-__ vs R-__` format required; "You cannot skip this scan or write any inertia default in its place" |
| C-08 | Actionable amendment list | **PASS** | Step 5: minimum 2, names section + exact change; "generic items don't count" |
| C-09 | No-scout fallback | **PASS** | Step 1 conditional: "If all 7 = NOT FOUND: 'I don't have scout context... Give me 3–5 sentences…'" |
| C-10 | Cross-namespace coherence | **PASS** | CNS-signal row in Section 1 Purpose (location 2) + CNS column in Step 2 PM table (location 1); Section 3 traces signal to design decision |
| C-11 | Pre-printed CNS column | **PASS** | Section 1 Purpose table: `**CNS-signal (location 2 of 2)**` row with `[SCAN REQUIRED]` marker; blank prohibited |
| C-12 | Inline role annotations | **PASS** | Role annotations embedded as inline prose checks within each section's content block |
| C-13 | Per-row P0 status column | **PASS** | Section 2 table: R-ID + "Which part covers it" (specific name required) + Covered? per row |
| C-14 | Active inspection guard | **PASS** | `[SCAN REQUIRED]` markers on contradiction field AND CNS field, each naming the data source; explicit prohibition on confirming absence without naming what was read |
| C-15 | CNS two independent locations | **PASS** | Step 2 PM table column labeled "location 1 of 2" + Section 1 Purpose table labeled "location 2 of 2" — structurally independent, both labeled |
| C-16 | PM-first coverage pre-assignment | **PASS** | "PM covers requirements before you write a word"; PM seal required before writing begins; document order: scout table → Step 2 PM contract → Section 1 |

**Essential**: 5/5 = 60 pts | **Recommended**: 3/3 = 30 pts | **Aspirational**: 8/8 = 40 pts  
**Composite**: 130/130 | **Golden**: YES

---

### V-05 — Signal Register + Scan Gate Tokens

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Section structure | **PASS** | Five sections in prescribed order in Phase 4; additional phases (Findings, Amendments) after |
| C-02 | Scout artifact table | **PASS** | Phase 1 SETUP (scout table) is the first phase; Structural Axis Declaration is pre-execution metadata, not execute content |
| C-03 | P0 requirement coverage | **PASS** | Phase 3 PM CONTRACT maps every P0 to a section; coverage count stated in gate token; Section 2 count "from Phase 3 PM CONTRACT count" |
| C-04 | Self-review findings | **PASS** | Phase 5 Findings: four categories; BLOCKED until ARCHITECT SEAL; each finding requires specific text |
| C-05 | Frontmatter complete | **PASS** | OUTPUT block with all required fields; input field = artifact list from SETUP |
| C-06 | Secondary role validation | **PASS** | PM inline (Section 1), Strategy inline (Section 2), Design inline (Section 3), Compliance inline (Section 4) — all inline in sections, not in Axis Declaration |
| C-07 | Contradiction detection | **PASS** | Phase 3 Contradiction SCAN template with `R-__ vs R-__`; SCAN complete count required; gate token validity rule: "PM CONTRACT invalid if contradiction SCAN block absent" |
| C-08 | Actionable amendment list | **PASS** | Phase 6: minimum 2, cites finding by category, names section + specific change |
| C-09 | No-scout fallback | **PASS** | Named conditional in Phase 1: "If row 1 = 'not found' and all rows = 'not found': add row 8 (user intent, BLOCKED). Ask: 'Describe `{{topic}}` in 3–5 sentences.'" |
| C-10 | Cross-namespace coherence | **PASS** | Phase 2 Signal Register loads CNS signals with source artifacts; Section 1 Purpose CNS row reads from register; Section 3 traces NS-feasibility to design constraint |
| C-11 | Pre-printed CNS column | **PASS** | Section 1 Purpose: `**Cross-namespace signal (location 2 of 2)**` row; "absent row is a structural failure" |
| C-12 | Inline role annotations | **PASS** | Inline annotations embedded within sections (not replaced by Structural Axis Declaration at top) |
| C-13 | Per-row P0 status column | **PASS** | Section 2: R-ID + Spec entry (named, specific) + Status + NS-signal per row — richest requirements table of all five |
| C-14 | Active inspection guard | **PASS** | Gate token validity rule: "PM CONTRACT gate token is invalid if contradiction SCAN block is absent" — strongest enforcement mechanism; Signal Register gate requires explicit per-row values or NOT FOUND |
| C-15 | CNS two independent locations | **PASS** | Structural Axis Declaration explicitly names two-location CNS contract: "Phase 2 Signal Register = location 1; Phase 4 Section 1 pre-printed row = location 2. Two-location instantiation must be a deliberate design choice." — only variation making this a self-documenting verifiable claim |
| C-16 | PM-first coverage pre-assignment | **PASS** | PM = Phase 3, Architect = Phase 4; BLOCKED until PM CONTRACT token; Structural Axis Declaration row for C-16: "PM Coverage Contract: PM maps every P0 to section before Architect writes; per-row assignment; C-16" |

**Essential**: 5/5 = 60 pts | **Recommended**: 3/3 = 30 pts | **Aspirational**: 8/8 = 40 pts  
**Composite**: 130/130 | **Golden**: YES

---

## Ranking

| Rank | Variation | Composite | Golden | Distinguishing strength |
|------|-----------|-----------|--------|------------------------|
| T-1 | **V-01** | **130** | YES | Cleanest PM SCAN GATE token; scan completion statement as gate prerequisite |
| T-1 | **V-03** | **130** | YES | Protocol-level CONFIRM-without-SCAN rule elevates constraint to definitional |
| T-1 | **V-04** | **130** | YES | `[SCAN REQUIRED]` markers with field-level prohibition; best readability |
| T-1 | **V-05** | **130** | YES | Gate token validity rule (strongest C-14); Structural Axis Declaration (only self-documenting C-15 proof) |
| 5 | **V-02** | **118** | NO | C-02 essential fail: Block 0 PM Pre-Assignment precedes scout table in document order |

**V-02 failure note**: The "Block 0 first" design creates an architectural contradiction with C-02 — the PM scans requirements and produces document content before the scout artifact table is output. Block 0 explicitly says "*(complete before any other block)*," which includes Block 1 (scout table). The scout table must be the first substantive output. This is the same trap as V-04's R2 C-07 failure: an ordering choice that looks clever but breaks a structural requirement.

---

## Excellence Signals

**V-05 gate token validity rule**: Rather than instructing the model to scan before confirming, the gate token itself is declared invalid without a scan block. This converts C-14 enforcement from a behavioral instruction ("you must scan") to a mechanical proof requirement ("your token has no effect without this evidence"). The distinction matters: a gate token rule is enforceable by inspection of the output; an instruction requires inferring compliance from content.

**V-05 Structural Axis Declaration**: The only variation that makes the two-location CNS contract a verifiable top-level design claim before execution. Other variations label locations inline; V-05 names the contract in a pre-execution table with explicit rationale. An evaluator can verify C-15 from the declaration alone, without tracing inline labels across phases. This is a new structural pattern: *a declarations block that makes design intent auditable without reading the full output.*

**V-03 protocol-level CONFIRM prohibition**: "You may not CONFIRM an enumeration result without a preceding SCAN. Writing 'none found' without a SCAN is a protocol violation." This makes the scan-before-confirm a definitional rule, not an instruction. It's the weakest of the three patterns mechanically (no token, no gate), but has the cleanest conceptual separation: SCAN is always an artifact; CONFIRM is always evidence-based.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Gate token validity rule — declaring a gate token invalid without a named scan block converts C-14 from a behavioral instruction to a mechanical proof requirement; the token itself is evidence of compliance, not a claim of it", "Structural Axis Declaration — a pre-execution table mapping axes to criteria makes the two-location CNS contract a self-documenting verifiable design claim rather than an observable pattern; enables criterion verification without full output traversal"]}
```
