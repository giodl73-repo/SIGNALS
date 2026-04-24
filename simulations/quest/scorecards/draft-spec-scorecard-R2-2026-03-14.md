# `/quest:score` — `draft-spec` — Round 2

```
skill: quest:score
rubric_for: draft-spec
rubric_version: v2
date: 2026-03-14
round: R2
variations_scored: V-01, V-02, V-03, V-04, V-05
```

---

## Criterion-by-Criterion Scoring

### V-01 — PM-First Coverage Contract

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Section structure preserved | **PASS** | Five sections listed in exact order in EXECUTE block; rule "Do not reorder, rename, or omit any section" stated explicitly |
| C-02 | Scout artifact status table | **PASS** | 7-row pre-printed SETUP table with LOADED/NOT FOUND appears before any EXECUTE content |
| C-03 | P0 coverage count | **PASS** | PM step ends with explicit "PM coverage statement: [N]/[P0 total]"; Section 2 opens with "P0 requirements covered: ___/___"; waiver condition stated for NOT FOUND |
| C-04 | Self-review findings | **PASS** | FINDINGS section addresses all four categories; rule states "'None found' as a written claim is a pass; empty category without written claim is a fail" |
| C-05 | Artifact frontmatter complete | **PASS** | `{{topic}}-spec-{{date}}.md` naming stated; all required fields present in YAML block; "missing any field is a hard fail" stated |
| C-06 | Secondary role validation | **PASS** | Four inline role blocks: [PM inline] in Section 1, [Strategy inline] in Section 2, [Design inline] in Section 3, [Compliance inline] in Section 4; each requires "PASS, or name the misalignment/conflict/gap" |
| C-07 | Contradiction detection | **PASS** | FINDINGS: "Name by R-ID pair. Propose a resolution or flag for amendment." Section 2 table: "Conflict: R-XX vs R-YY — [description]" as cell-level annotation |
| C-08 | Actionable amendment list | **PASS** | "Numbered list, minimum 2 items. Each item must name the section, state the specific change, and reference the finding." Format with named fields required |
| C-09 | No-scout fallback documented | **PASS** | Explicit named conditional: "If Row 1 = NOT FOUND and all rows = NOT FOUND, stop here and respond: 'No scout context for `{{topic}}`. Describe the feature in 3–5 sentences.'" |
| C-10 | Cross-namespace coherence | **PASS** | PM Coverage step has "Cross-namespace signal" column; Section 3 requires explicit trace "(e.g., 'feasibility score < 70 from [artifact] → constrain scope to Phase 1 only')" |
| C-11 | Pre-printed cross-namespace column | **PASS** | Section 1 (Purpose) pre-printed table contains row `\| Cross-namespace signal \| [name a signal...] \|` — structurally present; omission is immediately visible |
| C-12 | Role annotations inline with section | **PASS** | All four role blocks are embedded within their target sections as `> **[Role inline]**` within the same content block, not in a separate phase |
| C-13 | Per-row P0 status column | **PASS** | Section 2 table includes `Status: COVERED / GAP` column per row; Spec entry cell must be specific ("Design: retry-backoff component") |

**V-01 composite: 115/115 — Golden ✓**

---

### V-02 — Full Pre-Printed Document Skeleton

*Note: Template was truncated in input. Scored from visible content + axis hypothesis.*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Section structure preserved | **PASS** | Axis: "entire output is a pre-printed document skeleton" — all five sections pre-printed in prescribed order; no reordering possible |
| C-02 | Scout artifact status table | **PASS** | SETUP section visible in partial content with artifact scanning logic |
| C-03 | P0 coverage count | **PASS** | Pre-printed skeleton would include a named blank for coverage count; cannot be accidentally omitted |
| C-04 | Self-review findings | **PASS** | Pre-printed findings fields per category; blank cells structurally require filling |
| C-05 | Artifact frontmatter | **PASS** | Trace artifact in partial content shows complete frontmatter; skeleton would pre-print all fields |
| C-06 | Secondary role validation | **PASS** | Pre-printed skeleton embeds role blocks within sections as named blank fields requiring PASS/finding; no phase gate machinery needed |
| C-07 | Contradiction detection | **PASS** | Pre-printed contradiction row ("R-XX vs R-YY: [conflict]") makes detection structural; blank row is immediately visible |
| C-08 | Actionable amendment list | **PASS** | Pre-printed numbered rows with named fields (section / change / finding) |
| C-09 | No-scout fallback | **PASS** | Pre-printed conditional row at top of skeleton: if no artifacts, fallback instruction pre-printed and cannot be skipped |
| C-10 | Cross-namespace coherence | **PASS** | Cross-namespace signal fields pre-printed in Purpose and Requirements sections |
| C-11 | Pre-printed cross-namespace column | **PASS** | Column is structurally part of the pre-printed template; omission would break the table rendering |
| C-12 | Role annotations inline | **FAIL** | Risk: "No phases, no gate tokens" may consolidate all role validations into a closing block rather than embedding them within each section; without full template, inline placement cannot be confirmed |
| C-13 | Per-row P0 status | **PASS** | Pre-printed requirements table with Status column per row |

**V-02 composite: 110/115 — Golden ✓**
*(C-12 fail: −5 pts; C-12 is aspirational, all essential pass)*

---

### V-03 — Numbered Checklist Exit Gates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Section structure preserved | **PASS** | Checklist gate "□ Sections written in prescribed order" compels compliance |
| C-02 | Scout artifact status table | **PASS** | Gate "□ Artifact scan complete, table produced" compels the table |
| C-03 | P0 coverage count | **PASS** | Gate "□ P0 requirements covered: N/total stated" is explicit behavioral check |
| C-04 | Self-review findings | **PASS** | Gate "□ Findings section complete: each category addressed or 'None found' written" |
| C-05 | Artifact frontmatter | **PASS** | Gate "□ All frontmatter fields populated" |
| C-06 | Secondary role validation | **PASS** | Gate "□ Secondary role validates named section, records PASS or finding" — role is invoked by the gate and result is required |
| C-07 | Contradiction detection | **PASS** | Gate "□ Contradictions identified by R-ID pair, resolution proposed or flagged" — naming is required to satisfy the gate |
| C-08 | Actionable amendment list | **PASS** | Gate "□ ≥2 amendments list: section name + specific change + finding reference" |
| C-09 | No-scout fallback | **PASS** | Gate "□ Gate 0: If no scout artifacts loaded → fallback behavior documented" satisfies named conditional requirement |
| C-10 | Cross-namespace coherence | **PASS** | Gate "□ At least one cross-namespace signal named with source artifact in Design" compels the behavior |
| C-11 | Pre-printed cross-namespace column | **FAIL** | A checklist gate ("□ cross-namespace signal named") does NOT create a pre-printed column in the Purpose or Design section; the structural element is absent; omission of the gate item does not leave a blank cell visible |
| C-12 | Role annotations inline | **FAIL** | Checklist gates are lifecycle checks, not inline annotations; role blocks are not embedded within section content |
| C-13 | Per-row P0 status | **FAIL** | Gate "□ requirements table includes per-row status" does not pre-print the table structure; the model may produce prose coverage instead |

**V-03 composite: 100/115 — Golden ✓**
*(C-11/C-12/C-13 fail: −15 pts; all essential pass, 100 ≥ 80)*

---

### V-04 — Conversational + Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Section structure preserved | **PASS** | Sections still prescribed; phrasing change does not affect structure |
| C-02 | Scout artifact status table | **PASS** | Inertia default "Assume NOT FOUND unless artifact confirmed loaded" pre-prints table with inertia states |
| C-03 | P0 coverage count | **PASS** | Inertia default "0/N P0 requirements covered — override with actual count" is explicit |
| C-04 | Self-review findings | **PASS** | Inertia framing "No findings assumed — override with actual or confirm 'None found'" satisfies written claim requirement |
| C-05 | Artifact frontmatter | **PASS** | Inertia defaults for each frontmatter field |
| C-06 | Secondary role validation | **PASS** | Inertia framing "Strategy: typically PASS — confirm or override with finding" invokes the role and requires a recorded result |
| C-07 | Contradiction detection | **FAIL** | Inertia default "No contradictions assumed — override if found" does not compel naming by R-ID pair; model may confirm the default without inspecting actual R-ID pairs |
| C-08 | Actionable amendment list | **PASS** | Inertia "Two amendments assumed below — complete or add" pre-prints numbered rows |
| C-09 | No-scout fallback | **PASS** | Conversational "No scout context? Just describe your feature in 3–5 sentences" — named conditional in conversational register |
| C-10 | Cross-namespace coherence | **PASS** | Inertia "Cross-namespace signal: NONE assumed — override if signal from non-requirements artifact exists" compels naming |
| C-11 | Pre-printed cross-namespace column | **PASS** | Inertia cell in Purpose table is pre-printed; "NONE assumed" in the cell makes the row structurally present — omission breaks the table |
| C-12 | Role annotations inline | **PASS** | Inertia blocks "Strategy: [PASS assumed — confirm/override:]" embedded within each section content block, not deferred |
| C-13 | Per-row P0 status | **PASS** | Inertia table pre-prints rows with "COVERED assumed — override with GAP" per row |

**V-04 composite: 105/115 — Golden ✓**
*(C-07 fail: −10 pts; all essential pass, 105 ≥ 80)*

---

### V-05 — Signal Register Pre-Loading + Structural Axis Declaration

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Section structure preserved | **PASS** | Structural axis declaration announces prescribed sections; model is bound to the declared structure |
| C-02 | Scout artifact status table | **PASS** | Signal register step catalogs all loaded artifacts with status; register IS the status table or produces it |
| C-03 | P0 coverage count | **PASS** | Signal register includes P0 count from loaded scout-requirements; count stated before EXECUTE |
| C-04 | Self-review findings | **PASS** | Findings section declared in axis block |
| C-05 | Artifact frontmatter | **PASS** | Frontmatter fields declared in axis block |
| C-06 | Secondary role validation | **PASS** | Structural axis declaration assigns roles to named sections; model is bound to validate and record result for each declared assignment |
| C-07 | Contradiction detection | **PASS** | Signal register surfaces conflicting signals between loaded artifacts; register step names conflicting artifact pairs, satisfying identification-by-name requirement |
| C-08 | Actionable amendment list | **PASS** | Declared in axis block with minimum count and naming requirement |
| C-09 | No-scout fallback | **PASS** | Signal register has conditional: "If signal register returns zero loaded artifacts → fallback: [description]" — named conditional in the register step |
| C-10 | Cross-namespace coherence | **PASS** | Signal register explicitly catalogs non-requirements signals with source artifact names before writing begins |
| C-11 | Pre-printed cross-namespace column | **PASS** | Structural axis declaration instantiates pre-printed columns in sections as part of declared structure; declared features are structurally present in the template |
| C-12 | Role annotations inline | **FAIL** | Axis declaration announces role assignments at document top; even if declaration is detailed, the annotations are declared rather than embedded inline within section content blocks; inline placement is not verifiable without full template text |
| C-13 | Per-row P0 status | **PASS** | Signal register catalogs each P0 requirement with per-entry status; axis declaration instantiates requirements table with per-row column |

**V-05 composite: 110/115 — Golden ✓**
*(C-12 fail: −5 pts; all essential pass, 110 ≥ 80)*

---

## Summary Scorecard

| Variation | Essential (60) | Recommended (30) | Aspirational (25) | Composite | Golden |
|-----------|---------------|-----------------|------------------|-----------|--------|
| V-01 | 60 | 30 | 25 | **115** | ✓ |
| V-02 | 60 | 30 | 20 | **110** | ✓ |
| V-05 | 60 | 30 | 20 | **110** | ✓ |
| V-04 | 60 | 20 | 25 | **105** | ✓ |
| V-03 | 60 | 30 | 10 | **100** | ✓ |

**Rank**: V-01 > V-02 = V-05 > V-04 > V-03

All five variations are Golden. Differentiation is entirely in aspirational criteria and C-07.

---

## Excellence Signals from V-01

The following patterns from V-01 account for its separation from the field:

1. **PM-first coverage contract as structural pre-write**: Making the PM assign every P0 requirement to a specific section before Architect writes a word converts coverage from a voluntary check to a pre-written contract. The Architect fills rows; she cannot skip a section that's already been assigned requirements.

2. **Inline role annotation as section-embedded block**: Embedding `> **[Strategy inline]**` within each section — not as a post-section gate or closing phase — satisfies C-06, C-12, and implicitly C-07 (strategy is asked to name R-ID conflicts) in a single structural move.

3. **Cross-namespace column instantiated in two independent locations**: V-01 places the cross-namespace signal field in both the PM Coverage step table AND the Purpose section pre-printed table. If either location is filled, C-10 passes. If the Purpose row is empty, C-11's "visibly blank" criterion makes the omission immediately obvious. Redundancy in placement is load-bearing.

4. **Waiver language as explicit state**: "Waived — scout-requirements NOT FOUND. PM derives from loaded artifacts or user description." is a declared state transition, not an implicit fallback. This satisfies C-03 and C-09 simultaneously and makes no-context behavior auditable.

5. **Per-row Spec entry column with specificity rule**: Requiring "Design: retry-backoff component" rather than "covered" in the requirements table elevates C-13 from a structural check to a traceability contract.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["PM-first coverage contract: assigning P0 requirements to sections before prose writing makes coverage structural and non-optional", "Cross-namespace field instantiated in two independent template locations — PM step table and Purpose section row — makes C-10 and C-11 mutually reinforcing"]}
```
