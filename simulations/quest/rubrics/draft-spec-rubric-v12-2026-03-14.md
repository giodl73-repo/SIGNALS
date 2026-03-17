```markdown
---
skill: quest:score
rubric_for: draft-spec
version: v12
date: 2026-03-15
source_rounds: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12
---

# Rubric — `draft-spec` — v12

## Summary

| Tier | Count | Points |
|------|-------|--------|
| Essential | 5 | 60 |
| Recommended | 3 | 30 |
| Aspirational | 29 | 85 |
| **Total** | **37** | **175** |

**Golden threshold**: all 5 essential criteria pass AND composite >= 85.

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/29 * 85)
```

---

## What changed from v11 to v12

| | v11 | v12 |
|-|----|-----|
| Version | v11 | v12 |
| Source rounds | R1–R10 | R1–R12 |
| Aspirational count | 27 | 29 |
| Total criteria | 35 | 37 |
| Composite formula denominator | 27 | 29 |

**Two new aspirational criteria from R12:**

---

### C-36 — [INERTIA-ANALYZED] Condition 1 extended to [STATUS-QUO-SNAPSHOT] presence (depth)

The [INERTIA-ANALYZED] gate token's Condition 1 invalidity rule explicitly names [STATUS-QUO-SNAPSHOT] as a required presence check alongside [IG-REGISTER] and [ID-REGISTER]: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated." A gate token whose Condition 1 names only [IG-REGISTER] and [ID-REGISTER] without [STATUS-QUO-SNAPSHOT] does not satisfy, even if the template elsewhere defines [STATUS-QUO-SNAPSHOT] as required. The extension must appear as a named structural element in the token's invalidity rules — a surrounding prose note that the snapshot must be present does not satisfy. Without C-36, a gate token designed for the two-register model (C-21, C-30) can pass Condition 1 while silently ignoring [STATUS-QUO-SNAPSHOT] absence; C-36 closes that gap at the token definition level. Applicable only to template variants that introduce the status-quo-first inertia pattern; a template without [STATUS-QUO-SNAPSHOT] cannot be evaluated against this criterion. Requires C-30.

Source signal: V-02 — [INERTIA-ANALYZED] Condition 1 extended to: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated."

---

### C-37 — [STATUS-QUO-SNAPSHOT] row structural fail rule (depth)

The [STATUS-QUO-SNAPSHOT] block includes an explicit **structural fail rule** co-located with the row definition: a row with a named status-quo alternative but a blank gap statement is declared a structural fail, not a content gap. The rule must name the fail condition explicitly — a general completeness instruction ("all fields required") without naming the named-alternative-plus-blank-gap-statement pattern as a structural-level failure does not satisfy. This is the status-quo-snapshot application of the C-35 partial-population enforcement pattern: the failure mode is a row that appears partially populated (alternative named, gap unstated) but is structurally invalid because the gap statement is the load-bearing element for downstream inertia analysis. A template that defines [STATUS-QUO-SNAPSHOT] rows without this rule leaves ambiguity about whether a blank gap statement is a valid placeholder or an unreachable error state; C-37 closes that ambiguity at the structural definition level. A template without [STATUS-QUO-SNAPSHOT] cannot be evaluated against this criterion. C-36 can pass without C-37.

Source signal: V-02 note — "A row with a named alternative but a blank gap statement is a structural fail" declared co-located with the [STATUS-QUO-SNAPSHOT] row definition.

---

## Essential Criteria (60 pts total)

### C-01 — Five guided sections in prescribed order (12 pts)

The spec template contains all five guided sections — Phase 1 (PM PRE-ASSIGNMENT), Phase 2 (INERTIA ANALYSIS), Phase 3 (REQUIREMENTS), Phase 4 (AMENDMENTS), and FINDINGS — present in that prescribed order. A template with missing sections, merged phases, or reordered phases does not satisfy. This is the foundational structural requirement; all other criteria presuppose this scaffold is in place.

---

### C-02 — [SCOUT-STATUS-TABLE] with artifact rows before EXECUTE (12 pts)

A [SCOUT-STATUS-TABLE] block appears before the EXECUTE section and contains at minimum 7 rows covering the expected scout artifact types. Each row names the artifact type and a status field. A table with fewer rows, with catch-all rows substituting for individual artifact entries, or placed after EXECUTE does not satisfy.

---

### C-03 — [PM-COVERAGE-TABLE] with P0 coverage and C-03 waiver protocol (12 pts)

A [PM-COVERAGE-TABLE] block is present and contains rows for all P0 requirements. For requirements where the `scout-requirements` artifact was NOT FOUND, the table includes an explicit C-03 waiver statement acknowledging the gap. A table without waiver rows or with a general "N/A" notation in place of a named waiver does not satisfy. This criterion is the upstream dependency for C-33 (Waiver Status column) and C-31 (waiver propagation).

---

### C-04 — FINDINGS section with scan list and structured table (12 pts)

A FINDINGS section is present containing: (1) a scan list enumerating what was inspected, and (2) a structured findings table. A FINDINGS section with prose only, a table only, or a bulleted list without the structural table does not satisfy.

---

### C-05 — Frontmatter with naming convention and all required fields (12 pts)

The spec's frontmatter follows the prescribed naming convention and includes all six required fields. Missing fields or a naming convention deviation do not satisfy.

---

## Recommended Criteria (30 pts total)

### C-06 — PM explicitly invoked as secondary role in Phase 3 (10 pts)

The PM role is explicitly named in the Phase 3 Requirements section as a secondary validation role performing inline validation against [PM-COVERAGE-TABLE] — not only as the primary Phase 1 author. A Phase 3 section that references only Architect tasks without naming the PM role does not satisfy. The PM reference must appear as a named instruction in the section body, not only in a preamble or surrounding block.

---

### C-07 — Contradiction detection with named scan range requirement (10 pts)

Phase 3 includes a contradiction detection instruction that: (1) names a scan instruction for conflicting requirements, and (2) requires naming conflicting R-ID pairs before confirming absence of conflicts. "Do not confirm absent without naming scan range" or equivalent anti-passive-confirmation constraint must be present as a named rule. A general "check for contradictions" instruction without the named-scan-range guard does not satisfy.

---

### C-08 — Amendment list with minimum 2 specific actionable items (10 pts)

Phase 4 contains an amendment list with at minimum 2 specific, actionable items. Vague placeholders, a single combined item, or a structural template with no enumerated example items do not satisfy.

---

## Aspirational Criteria (85 pts total)

### C-09 — No-scout fallback Branch A with HALT (structure)

The spec includes a named fallback branch (Branch A) for the condition when ALL scout artifacts are NOT FOUND, containing an explicit HALT instruction. A fallback that covers only partial-missing cases without a distinct ALL-NOT-FOUND branch with HALT does not satisfy. Branch A must be named and the HALT must be explicit, not implied by surrounding prose.

---

### C-10 — Cross-namespace signal traced to named non-requirements artifact (traceability)

Phase 1 includes a cross-namespace signal — a row tracing to a named artifact from a namespace other than `scout-requirements`. The artifact must be named explicitly; a generic cross-namespace reference or "see other signals" placeholder does not satisfy.

---

### C-11 — Pre-printed cross-namespace row in both template locations (structure)

The cross-namespace signal row is pre-printed (not fill-in-blank) in both the Phase 1 PM table and the Purpose section. A template that requires the PM to manually locate and add the cross-namespace row at either location does not satisfy.

---

### C-12 — Inline role annotation in Phase 3 Requirements section (role)

Phase 3 Requirements contains an inline annotation naming the PM role with a specific action — "The PM should scan [PM-COVERAGE-TABLE]..." or the imperative equivalent ("PM: scan [PM-COVERAGE-TABLE] → fill..."). The annotation must appear inline in the section body, not only in a preamble, header, or surrounding block.

---

### C-13 — Per-row P0 status column in Phase 3 Requirements table (structure)

The Phase 3 Requirements table includes at minimum two columns — Spec Entry and Status — applied per row. A table with only a Spec Entry column, or with a single aggregate status field covering all rows, does not satisfy.

---

### C-14 — Active inspection guard requiring named scan source (depth)

The spec includes an explicit active inspection guard in at least one phase: an instruction prohibiting confirmation of "none found" without naming the scan range or source. "Do not confirm 'none found' without naming the scan range" or equivalent must appear as a named constraint. A general completeness instruction without this anti-passive-confirmation guard does not satisfy.

---

### C-15 — Cross-namespace signal in two named locations with ordinal markers (traceability)

The cross-namespace signal appears in two named locations, each marked with an ordinal label — "(location 1 of 2)" and "(location 2 of 2)". The ordinal markers must appear on the signal field itself, not only in surrounding prose or section-level headers.

---

### C-16 — PM pre-assignment of all P0 rows before Architect prose (ordering)

All P0 rows in [PM-COVERAGE-TABLE] are assigned by the PM in Phase 1, before any Architect prose in Phase 2 or later. A template in which PM assignment and Architect drafting are interleaved or co-located in the same phase does not satisfy.

---

### C-17 — Named gate token [PM-CONTRACT-SEAL] with Phase 2 dependency (governance)

The template defines a named gate token [PM-CONTRACT-SEAL] and Phase 2 declares REQUIRES [PM-CONTRACT-SEAL] in its header or preamble. The token must be named (not anonymous) and the REQUIRES dependency must be explicitly declared. A template with a gate concept but without a named token or without the explicit REQUIRES declaration does not satisfy.

---

### C-18 — Scripted VERBATIM RESPONSE in Branch A fallback (resilience)

Branch A (ALL NOT FOUND fallback) contains a blockquoted VERBATIM RESPONSE with complete scripted text — text the PM should emit verbatim without modification. A fallback with paraphrase instructions, fill-in-blank templates, or summarized response guidance does not satisfy.

---

### C-19 — Ordinal location markers on cross-namespace signal field (precision)

The cross-namespace signal field carries ordinal markers "(location 1 of 2)" and "(location 2 of 2)" directly on the field definition — not only in surrounding prose or section-level headers. A template where ordinals appear in prose description but not on the field itself does not satisfy. C-19 is the field-level precision requirement where C-15 is the location-level requirement; both must pass independently.

---

### C-20 — Unified role-and-source declaration (role)

A single declaration names both the PM role and the source artifact (`scout-requirements`) in one statement: "PM: scan `scout-requirements` → assign each P0 row → emit [PM-CONTRACT-SEAL]" or the descriptive equivalent. A template where role and source are named in separate sentences or separate blocks does not satisfy. REQUIRES/PRODUCES axis-complementarity pattern preserved.

---

### C-21 — Gate token proof-of-work rule ([PM-CONTRACT-SEAL] INVALID IF) (governance)

[PM-CONTRACT-SEAL] includes an explicit "INVALID IF" invalidity rule naming [PM-COVERAGE-TABLE] as a required presence condition: "INVALID IF emitted without [PM-COVERAGE-TABLE] present" or equivalent. A token with a description but no invalidity rule, or an invalidity rule that does not name [PM-COVERAGE-TABLE], does not satisfy.

---

### C-22 — [IG-REGISTER] and [ID-REGISTER] as structurally independent tables (structure)

[IG-REGISTER] (inertia gaps) and [ID-REGISTER] (inertia decisions) are structurally independent tables — separate named blocks with distinct headers and column definitions. A single combined table or a table with a type column distinguishing gaps from decisions does not satisfy.

---

### C-23 — Responsible Role column in [IG-REGISTER] (accountability)

[IG-REGISTER] includes a Responsible Role column naming the accountable role for each inertia gap row. A register without this column does not satisfy. A register that names roles only in prose notes adjacent to the table does not satisfy.

---

### C-24 — CASCADE TO annotation co-located with unified declaration (traceability)

A "CASCADE TO" annotation appears co-located with the unified role-and-source declaration (C-20), naming the downstream blocks that receive the PM's pre-assignments: [IG-REGISTER] in Phase 2 and the Purpose section cross-namespace signal row. A CASCADE TO annotation placed in a different section or block from the unified declaration does not satisfy.

---

### C-25 — Two-branch fallback with independent VERBATIM blocks (resilience)

The fallback structure contains two distinct named branches: Branch A (ALL NOT FOUND — `scout-requirements` absent and all other artifacts absent) and Branch B (`scout-requirements` absent but at least one other artifact loaded), each with its own independent VERBATIM response block. A single unified fallback branch or two branches sharing a single VERBATIM block does not satisfy.

---

### C-26 — Per-artifact Branch B sub-conditionals with anti-blend instruction (resilience)

Branch B contains per-artifact sub-conditionals — B-1, B-2, B-3, B-catch — each with a distinct VERBATIM block, and includes an explicit anti-blend instruction prohibiting the PM from combining responses across sub-conditionals. A Branch B with a single block covering all sub-conditions, or without the anti-blend instruction, does not satisfy.

---

### C-27 — Imperative phrasing in role-phase instructions (clarity)

Role-phase instructions use the concise actor→action→output directive form with `→` binding: "PM: scan `scout-requirements` → assign each P0 row → emit [PM-CONTRACT-SEAL]". Instructions using the descriptive "The PM should..." form or passive constructions do not satisfy. Gate tokens and REQUIRES/PRODUCES headers are not subject to this criterion.

---

### C-28 — PM pre-assignment phase before inertia phase with gate enforcement (ordering)

Phase 1 (PM PRE-ASSIGNMENT) appears before Phase 2 (INERTIA ANALYSIS) in the template structure, and the [PM-CONTRACT-SEAL] dependency in Phase 2's REQUIRES header enforces this ordering computationally. Template ordering alone without the gate token dependency does not satisfy. Requires C-17.

---

### C-29 — Elimination paths require named R-ID reference (traceability)

The Elimination Path field in [IG-REGISTER] rows requires an explicit R-ID reference in a defined format: "R-ID: [R-XX from [PM-COVERAGE-TABLE]]" or equivalent named format. A template that accepts free-text elimination paths without requiring a named R-ID does not satisfy.

---

### C-30 — [INERTIA-ANALYZED] Condition 2 validates per-cell R-ID presence (governance)

The [INERTIA-ANALYZED] gate token's Condition 2 explicitly checks that each [IG-REGISTER] Elimination Path cell contains a populated R-ID field — a per-cell check, not a table-level completeness check. A gate token whose Condition 2 validates table-level completeness without naming per-cell R-ID population as the check condition does not satisfy.

---

### C-31 — Waiver propagation rule with [INERTIA-ANALYZED] Condition 2 exemption (traceability)

A waiver propagation rule is declared in Phase 1: rows marked as waived in [PM-COVERAGE-TABLE] must propagate their waived status (as "R-ID WAIVED" or equivalent marker) to corresponding [IG-REGISTER] Elimination Path cells. [INERTIA-ANALYZED] Condition 2 includes an explicit exemption: cells marked "R-ID WAIVED" are exempt from the per-cell R-ID population check. A template with waiver notation in Phase 1 that does not propagate to [INERTIA-ANALYZED] Condition 2 does not satisfy. C-31 can pass without C-33; a template may propagate waivers correctly via row-level markers without a typed Waiver Status column.

---

### C-32 — AMPLIFIED dual sub-slot format for Elimination Path (depth)

Elimination Path cells in [IG-REGISTER] AMPLIFIED rows use a pre-printed dual sub-slot template with named sub-slots — `Risk:` and `R-ID:` — each on its own line within the cell. A free-text Elimination Path field, a field with a single combined label, or a field that requires the PM to manually format the sub-slots does not satisfy. Requires the AMPLIFIED row type to be defined in the template.

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

### C-36 — [INERTIA-ANALYZED] Condition 1 extended to [STATUS-QUO-SNAPSHOT] presence (depth)

The [INERTIA-ANALYZED] gate token's Condition 1 invalidity rule explicitly names [STATUS-QUO-SNAPSHOT] as a required presence check alongside [IG-REGISTER] and [ID-REGISTER]: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated." A gate token whose Condition 1 names only [IG-REGISTER] and [ID-REGISTER] without [STATUS-QUO-SNAPSHOT] does not satisfy, even if the template elsewhere defines [STATUS-QUO-SNAPSHOT] as required. The extension must appear as a named structural element in the token's invalidity rules — a surrounding prose note that the snapshot must be present does not satisfy. Without C-36, a gate token designed for the two-register model (C-21, C-30) can pass Condition 1 while silently ignoring [STATUS-QUO-SNAPSHOT] absence; C-36 closes that gap at the token definition level. Applicable only to template variants that introduce the status-quo-first inertia pattern; a template without [STATUS-QUO-SNAPSHOT] cannot be evaluated against this criterion. Requires C-30.

Source signal: V-02 — [INERTIA-ANALYZED] Condition 1 extended to: "INVALID IF [STATUS-QUO-SNAPSHOT], [IG-REGISTER], or [ID-REGISTER] is absent or any required row is unpopulated."

---

### C-37 — [STATUS-QUO-SNAPSHOT] row structural fail rule (depth)

The [STATUS-QUO-SNAPSHOT] block includes an explicit **structural fail rule** co-located with the row definition: a row with a named status-quo alternative but a blank gap statement is declared a structural fail, not a content gap. The rule must name the fail condition explicitly — a general completeness instruction ("all fields required") without naming the named-alternative-plus-blank-gap-statement pattern as a structural-level failure does not satisfy. This is the status-quo-snapshot application of the C-35 partial-population enforcement pattern: the failure mode is a row that appears partially populated (alternative named, gap unstated) but is structurally invalid because the gap statement is the load-bearing element for downstream inertia analysis. A template that defines [STATUS-QUO-SNAPSHOT] rows without this rule leaves ambiguity about whether a blank gap statement is a valid placeholder or an unreachable error state; C-37 closes that ambiguity at the structural definition level. A template without [STATUS-QUO-SNAPSHOT] cannot be evaluated against this criterion. C-36 can pass without C-37.

Source signal: V-02 note — "A row with a named alternative but a blank gap statement is a structural fail" declared co-located with the [STATUS-QUO-SNAPSHOT] row definition.
```
