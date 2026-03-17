Reading the four excellence signals from the Round 4 scorecard, I'll extract the new structural patterns, then produce the complete v5 rubric.

**Signals → criteria mapping:**

- Signal 1 (axis complementarity unlock) + Signal 3 (REQUIRES doubles as field guard) both describe the same underlying property: a single declaration satisfying two distinct criteria simultaneously. → **C-20**
- Signal 2 (token validity rule / proof-of-work) → **C-21**
- Signal 4 (IG-ID parallel finding surface) → **C-22**

That gives three new aspirational criteria (C-20, C-21, C-22), raising aspirational from 11 to 14 and max composite from 145 to 160.

---

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v5
date: 2026-03-15
source_rounds: R1, R2, R3, R4
---

# Rubric — `draft-spec` — v5

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 14 | 70 |
| **Total** | **22** | **160** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/14 * 70)
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

## Aspirational Criteria (70 pts total)

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
| C-22 | Named enumerable risk class with parallel finding surface | aspirational | depth | The spec defines at least one named enumerable risk class beyond P0 requirements (examples: inertia-guard IDs (IG-NN), compliance-flag IDs, type-E findings) as first-class template entities receiving the full finding-surface treatment: numbered IDs per instance, an elimination-path field per ID, a named risk-amplification signal when a threshold condition is crossed, and a dedicated gate token for the class; partial treatment — IDs without elimination paths, elimination paths without a gate token, or an amplification signal without a named threshold condition — does not satisfy; the risk class must be structurally parallel to the R-ID treatment, enforced by pre-printed template fields rather than prose commentary |

---

## Scoring

Composite score formula (restated):
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/14 * 70)
```

Maximum composite: **160**. Golden threshold: all 5 essential pass AND composite >= 80.
```

---

**Three new criteria added:**

- **C-20** (unified role-and-source declaration): The V-04 axis-complementarity signal and the "REQUIRES doubles as field guard" signal both point to the same structural property — a single template element that satisfies both C-12 (inline role) and C-14 (named scan source). They're two angles on one criterion.
- **C-21** (gate token proof-of-work validity rule): The V-04 token-validity-rule signal. Transforms C-17 from structural presence to proof-of-work certification. Explicitly upgrades C-17.
- **C-22** (named enumerable risk class with parallel finding surface): The V-05 IG-ID signal. The inertia-guard pattern is the first instance; the criterion is written to generalize to any named risk class — compliance flags, type-E findings, etc.

**Totals shift:** 11 → 14 aspirational criteria, 55 → 70 aspirational points, max composite 145 → 160.
