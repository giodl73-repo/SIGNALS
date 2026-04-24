Reading the R6 scorecard for new excellence signals before writing the rubric.

**Signal extraction:**

- **V-02 C-18 excellence**: V-02 upgrades C-18 from a single-branch verbatim block to a **two-branch conditional** — Branch A (all scout artifacts absent) and Branch B (requirements artifact absent while others are present). Each branch has its own demarcated `VERBATIM RESPONSE:` block with scenario-appropriate copy. A single-branch fallback satisfies C-18 but this differentiated-context pattern is strictly richer. → **C-25**

No other variation achieves C-23 or C-24 (both ✗ in V-01, both ✗ in V-02), so no new signals from those axes. The C-22 split pattern is already defined as C-22 in v6.

That adds one new aspirational criterion, raising aspirational from 16 to 17 and max composite from 170 to 175.

---

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v7
date: 2026-03-15
source_rounds: R1, R2, R3, R4, R5, R6
---

# Rubric — `draft-spec` — v7

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 17 | 85 |
| **Total** | **25** | **175** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 85.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/17 * 85)
```

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | Guided section structure preserved | essential | structure | All five guided sections (Purpose, Requirements, Design, Constraints, Open Questions) are present and appear in the prescribed order; reordering any section is a fail; appending extra sections after the prescribed set is allowed |
| C-02 | Scout artifact status table present | essential | structure | A status table with a row for each expected scout artifact appears in the SETUP block before any EXECUTE content; each row records LOADED or NOT FOUND; absence of the table is a fail even if the artifacts were used |
| C-03 | P0 requirement coverage | essential | coverage | Every P0 requirement from a loaded scout-requirements artifact maps to a named spec entry; coverage count is stated explicitly (e.g., "8/8 P0 requirements covered"); criterion is waived — not silently skipped — when no scout-requirements artifact exists, and the waiver is stated |
| C-04 | Self-review findings present | essential | behavior | A findings section explicitly addresses at least one of: contradictions, gaps, ambiguities, or hotspots; stating "none found" as a written claim is a pass; absence of the section, or producing an empty section without a written claim, is a fail |
| C-05 | Artifact frontmatter complete | essential | correctness | Output artifact follows `{topic}-spec-{date}.md` naming convention; frontmatter includes all required fields: skill, topic, item, date, skill_version, input |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | Secondary role validation | recommended | behavior | At least one secondary role (PM, Strategy, Compliance, or Design) is explicitly invoked to validate a named section and records PASS or a finding; listing role names without invoking them does not satisfy |
| C-07 | Contradiction detection and resolution | recommended | depth | Any conflicting requirements between loaded scout artifacts are identified by name (e.g., "R-06 vs R-10") and resolved or flagged with a proposed amendment; detection without resolution or flagging does not satisfy |
| C-08 | Actionable amendment list | recommended | depth | Phase 4 (Amend) produces a numbered list of at least 2 specific, actionable items that address gaps or ambiguities surfaced in the findings phase; vague items ("improve section 2") do not satisfy |

---

## Aspirational Criteria (85 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | No-scout-context fallback documented | aspirational | coverage | Spec explicitly documents behavior when no prior scout context is available (e.g., "ask 3–5 sentence description" or equivalent fallback prompt); fallback must appear as a named conditional in the spec, not implied by absence |
| C-10 | Cross-namespace coherence | aspirational | depth | At least one spec decision (constraint, design choice, or naming convention) is explicitly traced to a signal from a namespace other than scout-requirements (e.g., feasibility score, compliance posture, positioning differentiator), with the source artifact named |
| C-11 | Pre-printed cross-namespace column | aspirational | structure | The Purpose or Design section includes a pre-printed column or named row (e.g., "Cross-namespace signal") that requires the model to name a non-requirements artifact or leave the cell visibly blank; an instruction in prose to "name the artifact" does not satisfy — the column must be structurally present in the template so omission is immediately visible |
| C-12 | Role annotations inline with section content | aspirational | behavior | At least one secondary role annotation is embedded inline within its target section in the same content block, not deferred to a later phase or appended at document end; deferred-phase placement does not satisfy even if the annotation is complete; inline placement must be verifiable from the template itself — an axis declaration or role assignment at document top does not satisfy |
| C-13 | Per-row P0 status column in requirements table | aspirational | coverage | The requirements section includes a table with a per-row Status or Spec Entry column that maps each P0 requirement ID to its corresponding spec entry by name; a coverage count or summary statement without row-level traceability does not satisfy; requiring a specific entry name (e.g., "Design: retry-backoff component") rather than a pass/fail label satisfies at a higher level of specificity |
| C-14 | Active inspection guard for enumeration criteria | aspirational | depth | For each criterion requiring enumeration of named IDs or artifacts (contradiction R-ID pairs, cross-namespace artifact names), the spec includes at least one of: a named blank requiring a specific ID format (e.g., "R-XX vs R-YY"), an explicit scan instruction naming the data source to inspect before confirming absence, or a prohibition on confirming a default without review; a plain inertia default ("override if found") without a named inspection source does not satisfy; this criterion applies regardless of whether inertia framing is used elsewhere in the spec |
| C-15 | Cross-namespace signal instantiated in two independent locations | aspirational | structure | The cross-namespace signal field appears in at least two structurally independent locations in the template (e.g., both a SETUP/PM-step table and the Purpose section pre-printed row); if either location is filled, C-10 passes; if the Purpose row is empty, C-11's visibility criterion still fires from the Purpose location; two-location instantiation must be a deliberate design choice — accidental co-occurrence of mentions in prose does not satisfy |
| C-16 | PM-first coverage pre-assignment | aspirational | coverage | A named PM step or persona assigns each P0 requirement to a specific spec section before any prose writing begins; the assignment produces pre-filled rows or cells the Architect must complete, converting coverage from a voluntary post-hoc check to a structural pre-written contract; a PM coverage count or statement produced after prose writing does not satisfy — the assignment must precede writing and bind the Architect to pre-assigned rows |
| C-17 | Named progression gate token | aspirational | structure | The spec includes at least one named gate artifact (e.g., "PM SCAN GATE", "PM seal", "PM contract seal") that a phase must write to the document as proof of completion; a downstream phase names the gate artifact and states it is blocked until the artifact is present in the document; an ordering instruction ("complete X before Y") without a named writable gate artifact does not satisfy; the gate artifact must appear as a structural element in the template — a behavioral rule alone does not satisfy |
| C-18 | Scripted verbatim fallback response text | aspirational | coverage | The no-scout fallback conditional (C-09) includes pre-written, model-ready response text that the model emits verbatim or with minimal adaptation, demarcated with a write/respond prefix, blockquote, or quoted block; the scripted text must be complete enough that the model does not compose a response from scratch; a behavioral instruction ("ask for context", "request a description") without scripted copy does not satisfy; this criterion upgrades C-09 — C-09 can pass without C-18 |
| C-19 | Ordinal location markers for multi-instance required fields | aspirational | structure | Each required field that must appear in multiple structural locations is labeled with an explicit ordinal marker (e.g., "location 1 of 2 / 2 of 2", "location A of 2 / B of 2") so that completeness is verifiable by counting labeled instances rather than by searching prose; generic location names without a stated count denominator do not satisfy; unlabeled multi-location fields do not satisfy even if C-15 passes; this criterion is the structural mechanism by which C-15's "deliberate design choice" requirement is met at the highest level of specificity |
| C-20 | Unified role-and-source declaration | aspirational | structure | At least one template element combines role-invocation (as required by C-12) and data-source specification (as required by C-14) in a single structural declaration; the combined element names both who is responsible (role) and what they must inspect (named source artifact or data structure) in the same structural block; two co-located but separate elements — one naming the role and one naming the scan source — do not satisfy; the unified declaration must produce a single parseable instruction of the form "Role X inspects Source Y before confirming Z"; this criterion is independent of C-12 and C-14 — all three may pass via separate elements, but C-20 requires the unification; the axis-complementarity pattern (combining role-sequence ordering with field-level REQUIRES bindings) is the canonical implementation |
| C-21 | Gate token proof-of-work validity rule | aspirational | depth | The gate token required by C-17 includes an explicit structural invalidity rule: a gate token emitted without its prerequisite evidence in the same document block is declared structurally invalid; "prerequisite evidence" means a named scan result, coverage table, or artifact reference proving the gate-triggering work was done; the invalidity declaration must appear in the template as a structural rule, not a behavioral instruction; an ordering instruction ("complete the scan before emitting the token") without an explicit invalidity statement does not satisfy; a valid gate token is therefore a proof-of-work artifact — its presence certifies that the prerequisite block is present and non-empty; this criterion upgrades C-17 — C-17 can pass without C-21 |
| C-22 | IG-ID register split into parallel namespaces | aspirational | structure | The spec defines two structurally independent registers with distinct ID sequences: `[IG-REGISTER]` (IG-XX entries, one row per guard) and `[ID-REGISTER]` (ID-XX entries, one row per defeat); conflating guards and defeats into a single table with mixed IDs does not satisfy; the parallel structure must be a deliberate template design — incidental separation in prose does not satisfy; each register must use its own ID prefix so that an IG-XX reference unambiguously resolves to a guard row and an ID-XX reference unambiguously resolves to a defeat row |
| C-23 | IG guard entries bound to a named responsible role | aspirational | behavior | Each row in the `[IG-REGISTER]` (C-22) includes a Responsible Role column that names the role accountable for confirming the defeat of that guard; the Responsible Role column must be structurally present in the IG-REGISTER table — a role assignment in a separate section or in prose commentary does not satisfy; an IG guard entry without a named responsible role is a structural gap; this criterion requires C-22 — C-22 can pass without C-23 |
| C-24 | Cascade directive on unified declaration | aspirational | structure | The unified role-and-source declaration (C-20) includes an explicit `CASCADE TO:` annotation or equivalent structural directive that names the downstream location(s) where the unified declaration's output must propagate (e.g., a specific table column, a named register row, or a gate artifact slot); propagation implied by behavioral ordering or by convention does not satisfy; the cascade directive must be a structural element naming at least one target location by its template identifier; this criterion requires C-20 — C-20 can pass without C-24 |
| C-25 | Differentiated verbatim fallback branching | aspirational | coverage | The scripted verbatim fallback (C-18) includes at least two distinct branches differentiated by which scout artifacts are absent — at minimum: Branch A (all scout artifacts absent) and Branch B (requirements artifact absent while one or more other scout artifacts are present); each branch has its own demarcated `VERBATIM RESPONSE:` block with response copy appropriate to the specific missing-context scenario; a single-branch fallback satisfies C-18 but not C-25; the branch conditions must be named and structurally distinct — a single verbatim block with a conditional note or parenthetical appended does not satisfy; this criterion upgrades C-18 — C-18 can pass without C-25 |
```
