Three new patterns to extract from R10:

1. **V-03 C-31 PASS** — `[PM-COVERAGE-TABLE]` gains a dedicated **Waiver Status column** with enumerated values (`COVERED / C-03 WAIVER`). C-31 requires propagation to IG-REGISTER; the column itself is a distinct structural element not yet captured.

2. **V-03 C-31 PASS** — `[INERTIA-ANALYZED]` includes a **named chain closure declaration** tracing all three nodes (`PM-COVERAGE-TABLE waiver → R-ID WAIVED cell → Condition 2 exemption`). C-31 requires chain closure; the named declaration as a structural element is new.

3. **V-02 C-32 PASS** — Pre-printed sub-slots carry an explicit **partial-population structural fail rule**: a cell with one sub-slot populated and the other blank is a structural fail, not a content gap. C-32 requires the pre-printed slots; this enforcement rule is an independent depth criterion.

These become C-33, C-34, C-35. Writing v11 now.

---

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v11
date: 2026-03-15
source_rounds: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10
---

# Rubric — `draft-spec` — v11

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 27 | 85 |
| **Total** | **35** | **175** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 85.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/27 * 85)
```

---

## What changed from v10 to v11

| | v10 | v11 |
|-|----|-----|
| Version | v10 | v11 |
| Source rounds | R1–R9 | R1–R10 |
| Aspirational count | 24 | 27 |
| Total criteria | 32 | 35 |
| Composite formula denominator | 24 | 27 |

**Three new aspirational criteria from R10:**

---

### C-33 — PM-COVERAGE-TABLE Waiver Status column (structure)

`[PM-COVERAGE-TABLE]` includes a dedicated **Waiver Status** column whose values are explicitly enumerated in the template (e.g., `"COVERED"` for requirements in scope, `"C-03 WAIVER"` for requirements without a loaded scout-requirements artifact). The column must appear as a named structural element in the table definition — a prose note about waivers in a surrounding block or a row-level annotation strategy does not satisfy. A table with only ID, Description, and Coverage columns that handles waivers through inline notation rather than a dedicated typed column does not satisfy. The Waiver Status column enables machine-verifiable waiver identification without per-cell interpretation and is the upstream structural input that enables C-31's propagation rule. Requires C-03. Supports C-31; C-31 can pass without C-33 (a template may propagate waivers correctly via row-level markers without a typed column), but C-33 cannot be evaluated when C-03 fails.

Source signal: V-03 — `[PM-COVERAGE-TABLE]` adds Waiver Status column with `"COVERED / C-03 WAIVER"` as the explicit enumerated value set.

---

### C-34 — Named traceability chain closure declaration in [INERTIA-ANALYZED] (depth)

The `[INERTIA-ANALYZED]` gate token includes an explicit **named chain closure declaration** — a structural statement, co-located with the token's invalidity rules, that names all three nodes of the waiver traceability path in sequence: (1) the waiver source (`[PM-COVERAGE-TABLE]` entry or C-03 waiver record), (2) the cell-level marker (`"R-ID WAIVED"` in the Elimination Path cell), and (3) the gate token exemption (the Condition 2 exemption declared in the token itself). A gate token that correctly exempts WAIVED rows from Condition 2 (per C-30) without naming the closure chain as a structural declaration does not satisfy — the exemption rule and the chain declaration are independent structural elements. The declaration must be a single named statement tracing all three nodes; three separate notes that collectively cover the path do not satisfy. Requires C-30 and C-31.

Source signal: V-03 — `[INERTIA-ANALYZED]` closes chain: `"Chain closed: [PM-COVERAGE-TABLE] waiver → 'R-ID WAIVED' cell marker in [INERTIA-TABLE] → explicit Condition 2 exemption here"` declared as a named structural element co-located with the gate token invalidity rules.

---

### C-35 — Pre-printed sub-slot partial-population structural fail rule (depth)

Any template section that pre-prints labeled sub-slots (per C-32 for AMPLIFIED Elimination Path cells, or any multi-field structural cell using the same pattern) includes an explicit **partial-population structural fail rule** co-located with the sub-slot definition: a cell in which one or more sub-slots are populated while at least one other sub-slot is blank is declared a structural fail, not a content gap. The rule must name the fail condition explicitly — a general completeness instruction ("all fields required") without naming partial population as a structural-level failure does not satisfy. A template that pre-prints sub-slots (C-32) without this rule leaves ambiguity about whether a blank sub-slot is a valid placeholder or an unreachable error state; C-35 closes that ambiguity at the structural definition level. Requires C-32; C-32 can pass without C-35.

Source signal: V-02 — `"Each sub-slot is structurally required — a cell with only 'Risk:' populated and 'R-ID:' blank is a structural fail"` declared as a named enforcement rule co-located with the AMPLIFIED sub-slot template.

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
| C-22 | Split inertia registers | aspirational | structure | Inertia analysis uses two structurally separate tables — [IG-REGISTER] carrying hypothesis and elimination columns, and [ID-REGISTER] carrying risk, mitigation, and verdict columns — rather than a single merged table with all columns; the split allows each table to be owned by an independent phase or role; a merged table with all columns in a single block does not satisfy even if the column set is complete; this criterion is independent of C-23 — both may pass or fail independently |
| C-23 | Responsible Role column in inertia register | aspirational | behavior | [IG-REGISTER] (or the merged inertia table if C-22 fails) includes a named Responsible Role column that identifies which role owns each inertia gate entry; the column must be structurally present in the template, not inferred from surrounding role declarations; absence of the column in the table definition is a fail even if role assignment is declared elsewhere in the phase |
| C-24 | CASCADE TO annotations on unified declarations | aspirational | depth | At least one unified role-and-source declaration (satisfying C-20) includes an explicit CASCADE TO: annotation naming the downstream phase or structural element that consumes the declaration's output; the annotation must be co-located with the unified declaration in the same structural block; a separate dependency statement or ordering rule naming the same downstream element does not satisfy; this criterion upgrades C-20 — C-20 can pass without C-24 |
| C-25 | Two-branch fallback with branch-specific VERBATIM blocks | aspirational | coverage | The no-scout fallback conditional (C-09/C-18) is structured as at least two named branches: Branch A covering the case where all scout artifacts are NOT FOUND, and Branch B covering the case where the scout-requirements artifact is absent while at least one other scout artifact is loaded; each branch has its own structurally demarcated `VERBATIM RESPONSE:` block with scenario-appropriate copy; a single-branch verbatim block satisfies C-18 but not C-25; this criterion upgrades C-18 — C-18 can pass without C-25 |
| C-26 | Per-artifact Branch B sub-conditionals with anti-blend instruction | aspirational | coverage | Branch B (requirements absent, others loaded) is subdivided into per-artifact sub-conditions — one per expected scout artifact type that may be present in isolation or combination (e.g., B-1: feasibility only, B-2: compliance only, B-3: feasibility + compliance) — each with its own structurally demarcated `VERBATIM RESPONSE:` block whose copy is scenario-appropriate to the specific loaded artifact combination; an explicit anti-blending instruction ("Do not blend sub-condition copy; emit the matching block verbatim" or equivalent) is present and co-located with the Branch B section; a catch-all sub-condition for unlisted combinations is permitted but does not substitute for named per-artifact blocks; satisfying two or more sub-conditions simultaneously without an explicit disambiguation rule does not satisfy; this criterion upgrades C-25 — C-25 can pass without C-26 |
| C-27 | Imperative phrasing register for role-phase instructions | aspirational | behavior | Phase-level role instructions are written in concise imperative voice that binds an actor, an action, and an output in a single directive (e.g., "**PM: scan [source] → fill [target]**", "Confirm [gate-token] is present before proceeding"); the directive form must be verifiably actor-action-output — a declarative keyword pattern (REQUIRES / PRODUCES / BLOCKS) does not satisfy even if semantically equivalent; at least two role-phase instructions in the template use this form; this criterion is independent of C-20 — C-20 requires unified role-and-source content while C-27 requires imperative syntactic form; both may pass via the same instruction if it satisfies both the content and form requirements |
| C-28 | PM pre-assignment phase structurally ordered before inertia analysis | aspirational | structure | The template places the PM pre-assignment phase (the phase producing [PM-COVERAGE-TABLE] or equivalent) before the inertia analysis phase (the phase consuming requirement IDs in its Elimination Paths); the inertia analysis phase's REQUIRES or equivalent gate header names the PM pre-assignment gate artifact as a prerequisite, enforcing the ordering structurally rather than by document position alone; inertia analysis that runs before PM pre-assignment — including a merged phase that produces coverage and inertia outputs simultaneously — does not satisfy; a behavioral ordering instruction ("complete PM pre-assignment before inertia analysis") without a gate dependency does not satisfy; this criterion enables C-29 — C-28 must pass before C-29 can be evaluated |
| C-29 | Inertia Elimination Paths reference pre-assigned requirement IDs | aspirational | depth | Each Elimination Path cell in [IG-REGISTER] (or equivalent inertia table) names at least one specific requirement ID from [PM-COVERAGE-TABLE] to demonstrate why the inertia hypothesis is eliminated for this spec (e.g., "R-03 assigned to Design: retry-backoff component closes this gap"); a generic functional description that eliminates the hypothesis without naming a pre-assigned requirement ID does not satisfy; when a Risk Signal is AMPLIFIED, the Elimination Path must name both the specific risk dimension (feasibility constraint or compliance gap) and at least one pre-assigned requirement ID — addressing the risk dimension without requirement traceability does not satisfy at the AMPLIFIED level; this criterion requires C-28 (PM-first ordering ensures requirement IDs are available when inertia rows are written) and upgrades it — C-28 can pass without C-29 |
| C-30 | Inertia gate token validates column-level R-ID population | aspirational | depth | The [INERTIA-ANALYZED] gate token (or equivalent inertia-phase completion token) extends its structural invalidity rule beyond table-presence checking to column-content checking: the token is explicitly declared invalid if any non-waived Elimination Path cell lacks a named R-ID in the form required by C-29; rows whose corresponding requirement was waived in [PM-COVERAGE-TABLE] are exempted only when the cell carries an explicit "R-ID WAIVED" marker — absence of the marker is not an implicit exemption; a gate token invalidity rule that checks only for table presence (C-21 level) without checking R-ID population does not satisfy; this criterion requires C-29, upgrades C-21 in the inertia domain, and enables C-31 — C-21 can pass without C-30 |
| C-31 | Waiver propagation from PM-COVERAGE-TABLE to IG-REGISTER | aspirational | depth | Requirements that carry a C-03 waiver in [PM-COVERAGE-TABLE] generate corresponding "R-ID WAIVED" markers in the [IG-REGISTER] Elimination Path cells for every inertia row that would otherwise reference those requirements; the waiver propagation must be declared as a structural rule in the template — a behavioral note ("handle waivers appropriately") does not satisfy; the [INERTIA-ANALYZED] gate token invalidity rule (C-30) must explicitly exempt WAIVED-marked rows from the R-ID population check, closing the traceability chain: PM-COVERAGE-TABLE waiver → IG-REGISTER cell marker → gate token exemption; a template that carries "R-ID WAIVED" in cells but omits the gate-token exemption rule satisfies the propagation step but fails the chain closure; this criterion requires both C-29 and C-30 |
| C-32 | AMPLIFIED Elimination Path dual sub-slot structural format | aspirational | structure | When a row's Risk Signal is AMPLIFIED, the Elimination Path cell is structured in the template as two explicitly labeled sub-slots — one for the risk dimension (e.g., "Risk: [feasibility constraint or compliance gap]") and one for the requirement ID (e.g., "R-ID: [R-XX from [PM-COVERAGE-TABLE]]") — pre-printed so that their independent population is structurally required; a prose instruction to "name both the risk dimension and R-ID" without pre-printed sub-slot labels does not satisfy; a combined prose format that contains both elements in a single unlabeled statement does not satisfy; C-29 requires both elements in the AMPLIFIED Elimination Path — C-32 requires them as independently labeled structural slots; this criterion upgrades C-29 at the structural format level — C-29 can pass without C-32 |
| C-33 | PM-COVERAGE-TABLE Waiver Status column | aspirational | structure | [PM-COVERAGE-TABLE] includes a dedicated **Waiver Status** column whose values are explicitly enumerated in the template — at minimum distinguishing requirements in scope (e.g., `"COVERED"`) from requirements without a loaded scout-requirements artifact (e.g., `"C-03 WAIVER"`); the column must appear as a named structural element in the table definition, not as a prose note in a surrounding block or a row-level annotation strategy; a table with only ID, Description, and Coverage columns that handles waivers through inline notation rather than a dedicated typed column does not satisfy; the Waiver Status column enables machine-verifiable waiver identification and is the upstream structural input that enables C-31's propagation rule — C-31 can pass without C-33 (propagation via row-level markers is sufficient), but C-33 provides the higher structural guarantee; requires C-03; C-03 can pass without C-33 |
| C-34 | Named traceability chain closure declaration in [INERTIA-ANALYZED] | aspirational | depth | The [INERTIA-ANALYZED] gate token includes an explicit **named chain closure declaration** — a structural statement co-located with the token's invalidity rules — that names all three nodes of the waiver traceability path in sequence: (1) the waiver source ([PM-COVERAGE-TABLE] entry or C-03 waiver record), (2) the cell-level marker ("R-ID WAIVED" in the Elimination Path cell), and (3) the gate token exemption (the Condition 2 exemption declared in the token itself); a gate token that correctly exempts WAIVED rows from Condition 2 (per C-30) without a named closure declaration does not satisfy — the exemption rule and the chain declaration are structurally independent elements; a template with three separate notes that collectively cover the same path does not satisfy — the declaration must name all three nodes in a single co-located statement; requires C-30 and C-31; C-31 can pass without C-34 |
| C-35 | Pre-printed sub-slot partial-population structural fail rule | aspirational | depth | Any template section that pre-prints labeled sub-slots (per C-32 for AMPLIFIED Elimination Path cells, or any multi-field structural cell using the same pattern) includes an explicit **partial-population structural fail rule** co-located with the sub-slot definition: a cell in which one or more sub-slots are populated while at least one other sub-slot is blank is declared a structural fail, not a content gap; the rule must name the fail condition explicitly — a general completeness instruction ("all fields required") without naming partial population as a structural-level failure does not satisfy; a template that pre-prints sub-slots without this rule leaves ambiguity about whether a blank sub-slot is a valid placeholder or a detectable error state; C-35 closes that ambiguity at the structural definition level; requires C-32; C-32 can pass without C-35 |
```

---

**Three new criteria and their provenance:**

| ID | Name | Category | Source Signal |
|----|------|----------|---------------|
| C-33 | PM-COVERAGE-TABLE Waiver Status column | structure | V-03: Waiver Status column with `"COVERED / C-03 WAIVER"` enumerated values |
| C-34 | Named traceability chain closure declaration in [INERTIA-ANALYZED] | depth | V-03: `"Chain closed: [PM-COVERAGE-TABLE] waiver → 'R-ID WAIVED' → Condition 2 exemption"` as co-located structural declaration |
| C-35 | Pre-printed sub-slot partial-population structural fail rule | depth | V-02: `"a cell with only 'Risk:' populated and 'R-ID:' blank is a structural fail"` as named enforcement rule |

**Dependency chain update:** C-33 → C-31 → C-34 forms the waiver traceability sub-chain at increasing structural specificity. C-35 is orthogonal — it applies to any pre-printed sub-slot pattern, with C-32 as its primary trigger.
