Reading the Round 5 scorecard, I'll extract the excellence signals before writing the complete rubric.

**Signals → criteria mapping:**

- **Signal 1 (C-22 definition gap)**: C-22 is referenced in all three variation scores ("IG-ID parallel namespace not instantiated") but its definition was never written into v5. The IG-ID pattern from V-03 makes the definition clear. → **C-22** (define properly)
- **Signal 2 (V-03 C-06 PARTIAL)**: "IG-ID axis focuses on risk tracking, not role-invocation form" — IG guards declare *what* to protect but not *who* is accountable for confirming each defeat. The highest pattern binds each IG entry to a named responsible role. → **C-23**
- **Signal 3 (V-01 C-15 PARTIAL + V-02 C-15 PARTIAL)**: Both variations fail two-location coverage because neither axis *declares* a cascade. The unification in C-20 and the multi-location requirement in C-15 are achieved by convention, not by a structural cascade directive — making coverage unverifiable without prose search. → **C-24**

That gives three new aspirational criteria (C-23, C-24 new; C-22 defined), raising aspirational from 14 to 16 and max composite from 160 to 170.

---

```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v6
date: 2026-03-15
source_rounds: R1, R2, R3, R4, R5
---

# Rubric — `draft-spec` — v6

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 16 | 80 |
| **Total** | **24** | **170** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 85.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/16 * 80)
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

## Aspirational Criteria (80 pts total)

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
| C-22 | IG-ID parallel finding surface | aspirational | structure | The spec template includes a parallel IG-ID register that tracks inertia guards (IG) and inertia defeats (ID) as named, distinct entries; each IG entry names a structural guard against lazy model defaults; each ID entry names the condition under which the guard is confirmed to have defeated the inertia error; the register must be structurally present as a named section or table — not implied by behavioral instructions — with at least one IG-ID pair declared; IG entries and ID entries must carry distinct IDs (e.g., IG-01, ID-01) so coverage is verifiable by counting pairs; a spec that names guards without declaring a parallel ID defeat namespace does not satisfy |
| C-23 | IG-role binding | aspirational | behavior | Each IG entry in the IG-ID register (C-22) names the role responsible for confirming that the corresponding ID defeat has activated; the role binding must appear as a structural annotation on the IG entry itself — not in a separate phase or behavioral section; a register with IG-ID pairs where no IG names a responsible role does not satisfy; this criterion unifies C-22 (risk tracking) with C-06 (role invocation) at the structural level, requiring the IG-ID namespace to carry role accountability inline; partial binding — some IG entries name a role, others do not — does not satisfy; this criterion upgrades C-22 — C-22 can pass without C-23 |
| C-24 | Cascade directive for unified declaration | aspirational | structure | A C-20-compliant unified role-and-source declaration includes an explicit cascade directive that names each structural location where the role-source pair must be instantiated; the cascade directive must appear as a structural annotation on or immediately following the unified declaration — not in a separate behavioral section — and must enumerate at least two named locations; a unified declaration without a cascade directive relies on convention for multi-location coverage and does not satisfy; this criterion upgrades both C-20 (by requiring the declaration to specify its own propagation) and C-15 (by converting two-location coverage from a design aspiration to a structurally declared contract); the cascade directive is the mechanism by which C-19's ordinal markers become load-bearing rather than optional |
```
